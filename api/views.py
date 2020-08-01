from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from sqlalchemy_filters import apply_filters, apply_pagination, apply_sort

from .models import Base, Transactions
from .db import ConnectionDB
from django.conf import settings
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .serializers import TransactionsSerializer

import io
import sqlalchemy, sqlalchemy.orm
import pandas as pd
import requests
import json

from .thread import save_db
from threading import Thread


class TransactionsViewSet(viewsets.ViewSet):


    def list(self, request):
        """
        [List transactions objects by queryparams and paginate this.]

        Args:
            request ([HttpRequest]): [Http request]

        Returns:
            [Response | JSON]: [Response with results of data searched]
        Authors:
            [dcorquir]
        """
        try:
            connection = ConnectionDB()
            session = connection.get_session()
            args = request.query_params
            query = session.query(Transactions)

            # Verify filters by the fields specified
            if 'transaction_id' in args:
                query = query.filter(Transactions.transaction_id == args["transaction_id"])
            if 'client_id' in args:
                query = query.filter(Transactions.client_id == args["client_id"])
            if 'transaction_date' in args:
                query = query.filter(Transactions.transaction_date == args["transaction_date"])

            # Descending sort by the field specified
            if "sort" in args and args["sort"].startswith("-"):
                field = args["sort"].replace("-", "")
                sort_by = getattr(Transactions, field).desc()
            else:
                sort_by = getattr(Transactions, args["sort"]).asc()
            query = query.order_by(sort_by)
            query, pagination = apply_pagination(query, page_number=int(args['page']), page_size=int(args['per_page']))
            data = query.all()
            session.close()
            serializer = TransactionsSerializer(data, many=True)
            return Response({
                'status': 'OK', 
                'data': serializer.data,
                'pagination': {
                    'page_number': pagination[0],
                    'page_size': pagination[1],
                    'num_pages': pagination[2],
                    'total_results': pagination[3]
                }}, status=200)
        except Exception as e:
            print('vws49: An error has been occurred -- '.format(e))
            return Response({'status': 'FAILED', 'data': [], 'error_message': '{}'.format(e)}, status=400)

    def create(self, request):
        """
        [Create transfers data by csv read form specify url.]

        Args:
            request ([HttpRequest]): [Http request]

        Returns:
            [Response | JSON]: [Response with results]

        Authors:
            [dcorquir]
        """
        try:
            url = settings.URL_FILE
            file_content = requests.get(url).content
            csv_reader = pd.read_csv(io.StringIO(file_content.decode('utf-8')))
            df2 = pd.DataFrame(csv_reader, columns=['transaction_id', 'transaction_date', 'transaction_amount', 'client_id', 'client_name'])
            process = Thread(target=save_db, args=(df2.iterrows(),))
            process.start()
            return Response({'status': 'OK', 'message': 'Se ha iniciado el proceso de carga de archivo.'}, status=200)
        except Exception as e:
            print("api.vws56: An error has been ocurred while create data - - ".format(e))
            return Response({'error': 'File Error Upload'}, status=400)

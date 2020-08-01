from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Base, Transactions
from .db import ConnectionDB
from django.conf import settings

import sqlalchemy, sqlalchemy.orm
import pandas as pd
import io
import requests


class TransactionsViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            connection = ConnectionDB()
            session = connection.get_session()
            trs = connection.get_by_fields(session, Transactions, client_id='20')
            if trs is not None:
                return Response({'status': 'OK', 'data': trs.client_id}, status=200)
            return Response({'status': 'OK', 'data': []}, status=404)
        except Exception as e:
            return Response({'status': 'FAILED', 'data': [], 'error_message': '{}'.format(e)}, status=400)

    def create(self, request):
        # try:
        url = settings.URL_FILE
        file_content = requests.get(url).content
        csv_reader = pd.read_csv(io.StringIO(file_content.decode('utf-8')))
        df2 = pd.DataFrame(csv_reader, columns=['transaction_id', 'transaction_date', 'transaction_amount', 'client_id', 'client_name'])
        connection = ConnectionDB()
        session = connection.get_session()
        for index, row in df2.iterrows():
            trs_aux = connection.get_by_fields(session, Transactions, transaction_id=row['transaction_id'])
            if trs_aux is None:
                print(row['transaction_id'])
                connection.create(
                    session,
                    Transactions,
                    transaction_id=row['transaction_id'],
                    transaction_date=row['transaction_date'],
                    transaction_amount=row['transaction_amount'],
                    client_id=row['client_id'],
                    client_name=row['client_name']
                )
            else:
                print('....................')

        return Response({'mdj': 'read'}, status=200)
        # except Exception as e:
            # print(e)
            # return Response({'error': 'File Error Upload'}, status=404)

    def __is_empty(self, session):
        return len(session.query(Transactions).all()) <= 0

    def __populate(self, session):
        ConnectionDB().create(
            session,
            Transactions,
            transaction_id='101010101',
            transaction_date='2020/02/20',
            transaction_amount='20000',
            client_id='20',
            client_name='cxa'
        )

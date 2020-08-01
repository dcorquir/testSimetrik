from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Base, Transactions
from .db import get_or_create, get_session
from django.conf import settings

import sqlalchemy, sqlalchemy.orm
import pandas as pd
import io
import requests


class TransactionsViewSet(viewsets.ViewSet):

    def list(self, request):
        session = get_session()
        trs = get_or_create(
            session,
            Transactions,
            client_id='20'
        )
        return Response({'msj': 'ok', 'cos': trs.client_id}, status=200)

    def create(self, request):
        # try:
        url = settings.URL_FILE
        file_content = requests.get(url).content
        csv_reader = pd.read_csv(io.StringIO(file_content.decode('utf-8')))
        df2 = pd.DataFrame(csv_reader, columns=['transaction_id', 'transaction_date', 'transaction_amount', 'client_id', 'client_name'])
        print('¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿')
        print(df2)
        print('¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿')
        return Response({'mdj': 'read'}, status=200)
        # except Exception as e:
            # print(e)
            # return Response({'error': 'File Error Upload'}, status=404)

    def __is_empty(self, session):
        return len(session.query(Transactions).all()) <= 0

    def __populate(self, session):
        get_or_create(
            session,
            Transactions,
            transaction_id='101010101',
            transaction_date='2020/02/20',
            transaction_amount='20000',
            client_id='20',
            client_name='cxa'
        )

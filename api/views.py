from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Base, Transactions
from .db import get_or_create, get_session
from io import StringIO

import sqlalchemy, sqlalchemy.orm
import pandas as pd


class TransactionsViewSet(viewsets.ViewSet):

    def list(self, request):
        session = get_session()
        if self.__is_empty(session):
            self.__populate(session)
        trs = get_or_create(
            session,
            Transactions,
            client_id='20'
        )
        return Response({'msj': 'ok', 'cos': trs.client_id}, status=200)

    def create(self, request):
        # try:
        print('-----------------------------')
        print(request.FILES)
        print('-----------------------------')
        if request.FILES:
            print("data===",request.FILES.get('fileToUpload').read().decode("utf-8"))
            test_file = request.FILES.get('fileToUpload')
            df = pd.read_csv(test_file, delimiter="\t")
            print('+++++++++++++++++++++++++++')
            print(df)
            print('+++++++++++++++++++++++++++')
            return Response(df, status=200)
        # except Exception as e:
            # print(e)
            # return Response({'error': 'File Error Upload'}, status=404)

    def __is_empty(self, session):
        return len(session.query(Transactions).all()) <= 0

    def __populate(self, session):
        get_or_create(
            session,
            Transactions,
            transaction_date='2020/02/20',
            transaction_amount='20000',
            client_id='20',
            client_name='cxa'
        )

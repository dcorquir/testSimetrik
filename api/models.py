from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transactions(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True)
    transaction_date = Column(String)
    transaction_amount = Column(String)
    client_id = Column(String)
    client_name = Column(String)

    def __init__(self, transaction_date, transaction_amount, client_id, client_name):
        self.transaction_date = transaction_date
        self.transaction_amount = transaction_amount
        self.client_id = client_id
        self.client_name = client_name

    def __repr__(self):
        return u"Transaction(%s, %s)" % (self.transaction_date, self.client_name)

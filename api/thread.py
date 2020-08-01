from .db import ConnectionDB
from .models import Transactions

def save_db(data):
    """
    [Thread to save all data readed in database.]

    Args:
        data ([DataFrame | iterrows]): [data read for csv]

    Authors:
        [dcorquir]
    """
    connection = ConnectionDB()
    session = connection.get_session()
    for index, row in data:
        trs_aux = connection.get_by_fields(session, Transactions, transaction_id=row['transaction_id'])
        if trs_aux is None:
            connection.create(
                session,
                Transactions,
                transaction_id=row['transaction_id'],
                transaction_date=row['transaction_date'],
                transaction_amount=row['transaction_amount'],
                client_id=row['client_id'],
                client_name=row['client_name']
            )
    session.close()


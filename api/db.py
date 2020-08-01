import sqlalchemy, sqlalchemy.orm
from sqlalchemy_filters import apply_filters, apply_pagination, apply_sort

from django.conf import settings
from .models import Base

# Class to connect and manage data base
class ConnectionDB():

    def get_session(self):
        """
        Get session from database connection
        @author: dcorquir
        """
        try:
            engine = sqlalchemy.create_engine(settings.DATABASE_ENGINE)
            Session = sqlalchemy.orm.sessionmaker(bind=engine)
            session = Session()
            Base.metadata.create_all(engine)
            return session
        except Exception as e:
            print("db21: An error has been ocurred whit database engine -- {}".format(e))
            return None

    def create(self, session, model, **kwargs):
        """
        Insert a model instace on database
        @author: dcorquir
        """
        try:
            instance = model(**kwargs)
            session.add(instance)
            session.commit()
            return instance
        except Exception as e:
            print("db35: An error has been ocurred while insert into database -- {}".format(e))
            return None

    def get_by_fields(self, session, model, **kwargs):
        """
        Find fields in model by fields
        @return: First object obtain in the query
        @author: dcorquir
        """
        try:
            data = session.query(model).filter_by(**kwargs).first()
            session.close()
            return data
        except  Exception as e:
            print("db47: An error has been occurred while query execute by fields -- {}".format(e))
            return None

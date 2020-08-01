import sqlalchemy, sqlalchemy.orm

from django.conf import settings
from .models import Base

# Class to connect and manage data base
class ConnectionDB():

    """
    Get session from database connection
    @author: dcorquir
    """
    def get_session(self):
        try:
            engine = sqlalchemy.create_engine(settings.DATABASE_ENGINE, echo=True)
            Session = sqlalchemy.orm.sessionmaker(bind=engine)
            session = Session()
            Base.metadata.create_all(engine)
            return session
        except Exception as e:
            print("db21: An error has been ocurred whit database engine")
            return None

    """
    Insert a model instace on database
    @author: dcorquir
    """
    def create(self, session, model, **kwargs):
        try:
            instance = model(**kwargs)
            session.add(instance)
            session.commit()
            return instance
        except Exception as e:
            print("db35: An error has been ocurred while insert into database")
            return None

    """
    Find fields in model by fields
    @return: First object obtain in the query
    @author: dcorquir
    """
    def get_by_fields(self, session, model, **kwargs):
        try:
            return session.query(model).filter_by(**kwargs).first()
        except  Exception as e:
            print("db47: An error has been occurred while query execute by fields")
            return None

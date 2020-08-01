import sqlalchemy, sqlalchemy.orm

from sqlalchemy.ext.declarative import declarative_base
from django.conf import settings

def get_session():
    Base = declarative_base()
    engine = sqlalchemy.create_engine(settings.DATABASE_ENGINE)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    return session

def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance
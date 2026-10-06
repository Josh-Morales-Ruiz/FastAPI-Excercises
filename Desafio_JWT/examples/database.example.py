from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
POSTGRES_SERVER = ''
POSTGRES_PORT = ''
POSTGRES_DB = ''

SQLALCHEMY_DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

#Motor de sqlalchemy
engine = create_engine(SQLALCHEMY_DB_URL)

#Sesion local para las peticiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base para los modelos de la base de datos
Base = declarative_base()

#Funcion para iniciar la conexion a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
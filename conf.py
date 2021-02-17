


# LOGGING
#==========
import logging
log_principal = "rodam/rodam.log"
formato_log = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(level=logging.DEBUG,filename=log_principal, filemode='w',format=formato_log )

# BD 
#=========


BD_URL = '/Users/jaumaf/.devs/rodam/prueba_laboratorio.db'
BD_PRUEBA = '/Users/jaumaf/.devs/rodam/esto_es_una_prueba.db'
BD_PRUEBA2 = '/Users/jaumaf/.devs/rodam/esto_es_una_prueba2.db'
BD_PRUEBA3 = '/Users/jaumaf/.devs/rodam/esto_es_una_prueba3.db'
DESARROLLO = '/Users/jaumaf/.devs/rodam/desarollo.db'

CURRENT_BD = DESARROLLO



#SQlALCHEMY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,DateTime, Boolean, Float, Table
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()
eng = create_engine(f"sqlite:///{CURRENT_BD}", echo=False)

## El session factory se deja aquí.
# Además, el bind se hace con el motor definido aquí
Session = sessionmaker(bind= eng)



# BD para pruebas
#========
eng_TEST = create_engine("sqlite:///:memory:",echo=False)
Session_TEST = sessionmaker(bind= eng_TEST)
ACEPTACION_ENG = create_engine(f"sqlite:////Users/jaumaf/.devs/rodam/aceptacion.db", echo=False)
PG_ENG = create_engine("postgresql+psycopg2://postgres:1234@localhost/laboratorio_rodam")

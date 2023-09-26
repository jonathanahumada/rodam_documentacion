##############################
Ejecución de pruebas
##############################

:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  primera version 2023-06-06, último build el |date|
	  

Resumen
##############################
Este documento resume el proceso de ejecución de
pruebas unitarias.

Algunas elementos preliminales son:

1. Las pruebas se escriben con base en `unittest`
2. Las pruebas se corren con `managment.py test`, porque tienen que pasar por el registry de Django


Ubicación de pruebas
##############################

Las pruebas están concentradas en un solo directorio `PROJECT_DIRECTORY/tests`.

Así que si quieren revisar todas las pruebas es solo inspeccionar este directorio.
Esto es diferente a la 'sugerencia' tradicional de juntar las pruebas dentro de cada
app de django. 

.. code-block:: shell


	   mysite/tests/
	├── emision
	│   ├── __init__.py
	│   ├── test_baseBuilder.py
	│   └── test_emisorDeCertificado.py
	├── formularios
	│   ├── __init__.py
	│   ├── test_especificar_un_analisis.py
	│   ├── test_lecturaDeMuestra.py
	│   └── test_lectura_individual.py
	├── __init__.py
	├── procesos
	│   ├── base
	│   ├── calidad
	│   ├── catalogo
	│   ├── ingreso
	│   ├── __init__.py
	│   ├── inventario
	│   ├── login
	│   ├── no_funcionales
	│   ├── __pycache__
	│   ├── recoleccion
	│   └── test_copiado_especificaciones.py~
	├── __pycache__
	│   └── __init__.cpython-39.pyc
	├── reporter
	│   ├── __init__.py
	│   ├── test_certificado_de_emision.py
	│   ├── test_lote_de_medio_reporter.py
	│   └── test_muestra_reporter.py
	├── services
	│   ├── __init__.py
	│   ├── __pycache__
	│   ├── test_dashboard_dinamico.py
	│   ├── test_EspecificacionDeAnalisisEnCuadroAdaptor.py
	│   ├── test_LoteDeMedioAdaptor.py
	│   ├── test_loteDeMedioParaCertificadoDeEmision.py
	│   ├── test_MuestraAdaptorGestionaLotes.py
	│   ├── test_MuestraAdaptor.py
	│   ├── test_PdfAdaptor.py
	│   ├── test_SalaDeControlAdaptor.py
	│   └── test_SalaDeLecturasParaMuestra.py
	├── teoremas
	│   ├── __init__.py
	│   ├── test_email.py
	│   ├── test_factories.py
	│   ├── test_LogEntry.py
	│   ├── test_named_tuple_es_hashable.py
	│   └── test_organizar_fechas.py
	├── validaciones
	│   ├── __init__.py
	│   └── lote_de_medio
	└── vistas
	    ├── calidad
	    ├── catalogo
	    ├── emision
	    ├── ingreso
	    └── __init__.py
	
	25 directories, 33 files


Agrupación de pruebas
##############################

Cada directorio de `tests/` agrupa pruebas según algun criterio. Este puede ser:

1. corresponde a un área funcional del negocio

2. correponde a un nivel de abstracción del desarrollo. Por ejemplo, 'formularios'



Tips
##############################

- correr primero las prubas en `/procesos`. Estas dan una mirada transversal del flujo de datos.
- concentrar la lógica de negocio en  `/servicios` para probarla toda en un solo directorio

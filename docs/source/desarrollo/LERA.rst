##########################
LERA (Guía de desarrollo)
##########################

.. |date| date::
	  
:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  primera versión 2023-05-26, último build el |date|

.. contents::

Mantenimiento de los comportamientos
######################################

Los comportamientos son objetos de *runtime* y no pueden seguirse
directamente con *version control*. La solución a esto es usar el
mecanismo de *fixtures* de Django.

El flujo de trabajo es el siguiente:

1. En desarrollo se llena la base de datos con los comportamientos
2. Una vez se quiere hacer un 'commit' de los comportamientos, se hace un fixture (siempre todos a la vez)
3. El fixture se agrega al repo (no se borran los fixtures anteriores
   por trazabilidad. Ver :ref:`Nomenclatura`)
4. En producción se limpian todos los comportamientos anteriores de la
   base de datos (a través del admin es fácil)
5. En producción, se carga el fixture con ``loaddata``


¿Cómo generar un fixture?
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

   manage.py  dumpdata LERA --indent 1  -o `date +%d%m%y`.json"


¿Dónde guardo el fixture?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Deben ir en el directorio ``/fixtures`` del app ``LERA``.


¿Cómo cargo el fixture en produccion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

   manage.py loaddata mydata


Nomenclatura
~~~~~~~~~~~~~~~~

La nomenclatura debe seguir el ISO 'YYYY-MM-DD' seguido por un
comentario descriptivo

Los fixtures son acumulativos, bajo el entendido de que en cada
actualización se borra la configuración de LERA y se vuelve a subir.

Ejemplo
^^^^^^^^^^^^^

.. code:: sh

     /home/jaumaf/dev/django-project/mysite/LERA/fixtures:
    total used in directory 28 available 12.8 GiB
    drwxr-xr-x 2 jaumaf jaumaf 4096 may 23 14:30 .
    drwxr-xr-x 6 jaumaf jaumaf 4096 may 23 14:26 ..
    -rw-r--r-- 1 jaumaf jaumaf 6494 may 23 14:26 2023-05-17-fix-corregir-unidades.json
    -rw-r--r-- 1 jaumaf jaumaf 7121 may 23 14:22 2023-05-23-unidad-presencia-ausencia.json

Comprobación de los datos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La diferencia entre cada incremento cada modificación al set de
comportamientos se puede establecer con ``diff``.



Ejemplo
^^^^^^^^^^^^^

.. code:: sh

      (venv) (base) [jaumaf@Sypha django-project]$ diff mysite/LERA/fixtures/2023-05-17-fix-corregir-unidades.json  mysite/LERA/fixtures/2023-05-23-unidad-presencia-ausencia.json 
    204a205,222
    >  "model": "LERA.transformacion",
    >  "pk": 6,
    >  "fields": {
    >   "nombre": "unidad_presencia_ausencia",
    >   "data": {
    >    "operacion": "'/{espec[valor_numerico][magnitud]}{espec[valor_numerico][unidad][cadena]}'",
    >    "accionable": "True",
    >    "precondiciones": [
    >     "espec['valor_numerico'] is not None"
    >    ],
    >    "transformacion": "{lectura[presencia_o_ausencia]} {unidad_presencia_ausencia}",
    >    "campo_accionable": "resultado_lectura_transformado",
    >    "variable_operacion": "unidad_presencia_ausencia"
    >   },
    >   "activo": true
    >  }
    > },
    > {
    316a335,342
    >  }
    > },
    > {
    >  "model": "LERA.casotransformacion",
    >  "pk": 9,
    >  "fields": {
    >   "caso": 3,
    >   "transformacion": 6

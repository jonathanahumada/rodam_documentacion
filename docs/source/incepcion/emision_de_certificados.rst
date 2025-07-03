=============================================
Emisión de certificados 
=============================================

:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date: <2021-01-15 Fri>

Introducción
============

Este documento estipula los requermientos de la *Emisión de certificados*


Información del cliente
------------------------
.. code-block:: sql

		select nom_empresa as empresa, nit_empresa as nit,
		direccion, pagina, correo from empresa, ciudad where
		empresa.id_ciudad = ciudad.id_ciudad;


Tabla resumen
-------------


.. code-block:: sql

		select nom_grupo as grupo, nom_analisis as
		analisis,nom_metodo as metodo, valor_lectura as
		lectura, especificacion.descripcion as especificacion,
		concepto from grupo, analisis,metodo,
		lectura,especificacion where grupo.id_grupo =
		lectura.id_grupo and analisis.id_analisis =
		lectura.id_analisis and metodo.id_metodo =
		lectura.id_metodo and lectura.id_producto =
		especificacion.id_producto and lectura.id_analisis =
		especificacion.id_analisis and lectura.id_metodo =
		especificacion.id_metodo and lectura.id_grupo =
		especificacion.id_grupo;



Equipos
-------

sqlite no tiene cursores. Tocaría en pg o a través del ORM. Pero en general un comando así funcionaria. 



.. code-block:: sql
		
   select nom_equipo, ref_documental from equipo, metodo_equipos where
   equipo.id_equipo = metodo_equipos.id_equipo;

		

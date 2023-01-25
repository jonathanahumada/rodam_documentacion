=======
Scripts
=======

Este documento registra algunas operaciones comunes.

Sincronización entre desarrollo y produccion
============================================

Los ambientes de desarrollo y producción son distintos.  Esto algunas
veces puede conllevar a que las ramas de desarollo y producción se
bifurquen.

Las migraciónes de django guardan una referencia a su antecesor, por
lo que el orden de las migraciones es un factor relevante a la hora de
correr comandos como `manage.py migrate`

La única forma de garantizar consistencia entre las dos ramas
bifurcadas es revisar el schema de la base de datos como tal. Algunos
comandos útiles son:

.. code-block::

    pg_dump -W -p 3333 -h localhost -U postgres   -d rodam -s > schema_prod_rodam_`date +%m%d%y_%H%M`.sql

    copia el schema de la bd de producción

similarmente, para crear un tunnel ssh

.. code-block::
      
   ssh -L 3333:127.0.0.1:5432 -M -S /tmp/db-backup-socket -fNT dev@$RODAM_IP


Recuperar una base de datos 
------------------------------
La documentación de postgres propone este commando
.. code-block:: bash
		psql --set ON_ERROR_STOP=on dbname < dumpfile

En la practica, esto genera que psql interprete `dbname` como el rol.
Por eso se usa

.. code-block:: bash
		psql -d dbname < dumpfile 

Gestionar de estados
------------------------------

Varias entidades de la base datos tienen diferentes estados que determinaran
su aparición en ciertas vistas, así como también serán usados para hacer
ciertas validaciones.

Es importante poder garantizar que en todo momento se pueda realizar programaticamente
un chequeo de los estados.

check_ciclo_de_vida.py
++++++++++++++++++++++++++++++
Este script lee los ciclos de vida descritos en los protocolos para cada entidad y
reporta si se encuentran en la base de datos. La salida se ve algo así:

.. code-block:: python
		>>> from scripts import check_ciclo_de_vida
		>>> check_ciclo_de_vida.main()
		-.*****************EstadoCuadroAnalitico*****************.
		|              Sin remitir               |  Encontrado   |
		|                Remitido                |  Encontrado   |
		|                Aprobado                |  Encontrado   |
		|               Archivado                |   Faltante    |
		-.*********************EstadoCalidad*********************.
		|              Sin remitir               |  Encontrado   |
		|    Solicita aprobación de lecturas     |  Encontrado   |
		|          con aprobación final          |  Encontrado   |
		|               Archivado                |  Encontrado   |
		|              Re-análisis               |  Encontrado   |
		|               facturada                |  Encontrado   |
		-.*********************EstadoDeLote**********************.
		|              Sin remitir               |  Encontrado   |
		|                Remitido                |  Encontrado   |
		|          Solicita aprobación           |  Encontrado   |
		|           Aprobado para uso            |  Encontrado   |
		|              Desaprobado               |  Encontrado   |
		|                Agotado                 |  Encontrado   |
		-.*****************EstadoCuadroDeControl*****************.
		|           Proceso de ingreso           |  Encontrado   |
		|                 En uso                 |  Encontrado   |


llenar_estado.py
++++++++++++++++++++++++++++++
Este script itera por el ciclo de vida de cada objeto registrado en el
script y crea el estado *solo si este no existe previamente*. La salida se ve algo
así 
.. code-block:: python
	>>> from scripts import llenar_estado
	>>> llenar_estado.main()
	creando estado Sin remitir
	creando estado Remitido
	creando estado Aprobado
	creando estado Archivado
	terminó script
	creando estado Sin remitir
	creando estado Remitido
	creando estado Solicita aprobación
	creando estado Aprobado para uso
	creando estado Desaprobado
	creando estado Agotado
	terminó script
	creando estado Sin remitir
	creando estado Solicita aprobación de lecturas
	creando estado con aprobación final
	creando estado Archivado
	creando estado Re-análisis
	creando estado facturada
	terminó script
	creando estado En edición
	creando estado Disponible
	terminó script

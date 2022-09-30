=======
Scripts
=======

Este documento registra algunas operaciones comunes.

Sincronización entre desarrollo y produccion
============================================

Los ambientes de desarrollo y producción son distintos.
Esto algunas veces puede conllevar a que las ramas
de desarollo y producción se bifurqyen. Algunos
cambios, denominados "en caliente", se hicieron
directamente sobre la aplicación en el servidor de producción.
Alguno de estos cambios luego se replicaron en desarrollo, pero algunos
otros no.

Más aun, lo que se replicaron fueron hechos en diferente
orden, lo que puede o no plantear un problema para las migraciones de
Django. Recordemos que las migraciónes de django guardan
una referencia a su antecesor, por lo que el orden de las migraciones
es un factor relevante a la hora de correr comandos como `manage.py migrate`

La única forma de garantizar consistencia entre las dos ramas bifurcadas
es revisar el schema de la base de datos como tal. Algunos comandos útiles
son:

.. code-block::

    pg_dump -W -p 3333 -h localhost -U postgres   -d rodam -s > schema_prod_rodam_`date +%m%d%y_%H%M`.sql

    copia el schema de la bd de producción

similarmente, para crear un tunnel ssh

.. code-block::
      
   ssh -L 3333:127.0.0.1:5432 -M -S /tmp/db-backup-socket -fNT dev@$RODAM_IP

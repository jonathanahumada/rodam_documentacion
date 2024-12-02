##############################
Modo realtime
##############################
:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  primera version 2024-12-02, último build el |date|

Resumen
##############################

Este documento describe las motivaciones y el uso correcto del *modo
realtime* dentro del Weblab.

¿Qué es el modo realtime?
##############################

El modo realtime es una variable configuración dentro de `SETTINGS` de tipo booleano.

Si el valor es verdadero se dice que modo realtime está activo, de lo
contrario está desactivado.

Cuando el modo realtime está activo, los usuarios del WebLab serán incapaces de modificar:

1. la fecha de ingreso de la muestra
2. la fecha del resultado de la lectura

 Cuando el modo realtime está desactivado estos valores están habilitados para edición en las
 distintas vistas que lo utilicen. Esto *no* quiere decir se salten los respectivos permisos
 para estas acciones. Simplemente quiere decir que, teniendo los permisos, es posible hacerlo.

Motivación
###############################
El WebLab está diseñado para usarse en modo realtime, de tal modo que los datos queden
fechados automáticamente al momento de ser ingresados por los usuarios.

Sin embargo, la experiencia ha demostrado de que algunas veces se presentan imprevistos y
el laboratorio realiza procesos físicamente que luego deben ser trasladados al sistema de
información WebLab.

En estos casos, las muestras y las lecturas quedarían con fechas que
no corresponderían con el procedimiento físico que se hizo. Además,
estas fechas estarán expuestas al cliente, lo que acarrearía más
problemas.

Para solucionar estos casos, se estableció el switch `MODO_REALTIME`, que puede
activarse y desactivarse dependiendo de los imprevistos que se presenten.

Uso correcto
##############################

Si bien el modo realtime funciona tan solo asignando un booleano. Es
un procedimiento que solo puede hacer un desarrollador con
credenciales suficientes para hacer un *despliegue a producción*. Por
lo tanto, su uso es de estricta necesidad y previamente acordado con
el responsable del laboratorio.



Estos son usos correctos:

.. code-block:: python

   MODO_REALTIME = True
   MODO_REALTIME = False

Estos son usos incorrectos:

.. code-block:: python

   MODO_REALTIME = "true"
   MODO_REALTIME = None
   

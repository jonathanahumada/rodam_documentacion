##########################
API: Comportamientos
##########################

.. |date| date::
	  
:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  primera versión 2023-05-26, último build el |date|


.. contents::

Estructura básica de un comportamiento
#######################################

Un comportamiento es un 'miniprograma' que corre con un *contexto*
especifico. Concretamente, el 'miniprograma' se expresa en el atributo
``operacion`` de la API (ver :ref:`Ejemplos`). El formato de la API es
JSON y en el Weblab se guardan como modelos Django.

¿Exactamente cómo se ejecuta este programa? Los comportamientos hacen
una llamada al `eval()` de python
(https://docs.python.org/3/library/functions.html#eval) pasándole un
contexto restringido para evitar fallas de seguridad.

Sin embargo, escribir de antemano la cadena que debe ser ejecutada es
difícil (¿cómo obtener los valores, si dependen de la entrada del
usuario?) por lo que hay un paso previo en el que se suele formatear
la cadena. Este formateo se hace a través de la sintaxis ``format()``
de python.

.. graphviz::

   digraph {
      "reemplazo en string" -> "evaluación en contexto";
   }

Sintaxis de un comportamiento
##############################                            

Como la ``operacion`` es una string almacenada en un JSON que será
interpetada por Python en un algún punto, adquiere la siguiente
sintaxis de:

.. code:: python

	 "{entrada_del_usuario.valor1} +  { entrada_del_usuario.valor2 }"


Adicionalmente, la API de Casos maneja una sintaxis basada en el
accesso de diccionarios, que puede sobrecargar más la sintaxis:

.. code:: python

	  "{entrada_del_usuario[valor1]} +  { entrada_del_usuario[valor2] }"

.. note::

   Por alguna razón, Python omite el uso de comillas para el acceso de diccionarios
   dentro de una  ``format()`` string

Ejemplos
##############################

Validación
------------------------------

.. code:: json
	  
   {
   "operacion": "{adicional[resultado_lectura_transformado][magnitud]} {espec[sentido]} {espec[magnitud]}",
   "accionable": true,
   "precondiciones": [
   "'resultado_lectura_transformado' in adicional"
   ],
   "valor_esperado": true,
   "campo_accionable": "cumple_especificacion",
   "valor_accionable": "paso_validacion",
   "ocultar_por_precondiciones": true
   }

  
Transformación
------------------------------


.. code:: json

	  {
	  "operacion": "{espec[unidad][lista_sugerencias][exactas]}",
	  "accionable": "True",
	  "precondiciones": [
	  "'resultado_lectura_transformado' in adicional.keys()"
	  ],
	  "transformacion": "{adicional[resultado_lectura_transformado][magnitud]} {unidades_sugeridas}",
	  "campo_accionable": "resultado_lectura_transformado",
	  "variable_operacion": "unidades_sugeridas",
	  "ocultar_por_precondiciones": true
	  } 

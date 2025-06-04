##############################
Certificado de emision
##############################
:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  primera version 2023-07-31, último build el |date|
	  

¿Cómo se renderizan las imágenes?
#################################


El objeto `FirmaMiembroRodam` tiene un atributo `imagen`. Cuando el `Builder` renderiza una firma,
toma `imagen` y lo carga a traves de  `reportlab.platypus.Image`. Para que esto funcione, `image`
debe ser un path-like válido.

Sucede algo así:

.. code: python

          # Image es una clase de ReportLab que gestiona los detalles. Recibe un path como argumento
	  imagen = Image(firma.imagen, width=ANCHO_FIRMA, height=ALTURA_FIRMA, hAlign='LEFT')


.. warning:

   Django guarda una imagen asociada a un objeto a través de su ImageField. El proceso de
   generar un certificado *no* utiliza directamente ese ImageField de Django, sino que toma
   el path del recurso.

¿Qué sucede si el path a la imagen no es válido?
####################################################

El `Builder` gestiona cualquier error que haga que la imagen no pueda cargarse.
Esto puede suceder por diferentes motivos (usuario no la subió, o se cambió
el sistema de archivos y ahora no coincide el path, se corrompió el archivo, etc).

La solución a esto es que se reemplaza la imagen por una mensaje indicando que no se
encontró la imagen, pero se sigue renderizando el pdf.


¿Qué chequeos existen?
##############################

El modelo `MiembroRodam` arroja una excepción cuando no existe la firma y se intenta
y se llama `MiembroRodam.firmar()`.

Sin embargo, *no* se hace doble-chequeo para asegurar que el archivo sí se encuentre en el
path que queda asociado al campo. Esto es problemático si se cambia de ambiente (de desarrollo
a producción, o entre dos servidores de produccion).



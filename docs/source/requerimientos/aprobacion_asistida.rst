##############################
La aprobación asistida
##############################

.. |date| date::
	  
:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  primera version 2023-09-25, último build el |date|


.. contents::

Objetivos de este documento
##############################
Este documento busca describir a rasgos generales una nueva
funcionalidad que se implementará en el sistema: la 'aprobación
asistida'. Al terminar de leer este documento se espera que el
lector comprenda:

1. por qué es necesario la aprobación asistida
2. qué dificultades se deben sobrepasar para implementarla
3. cuáles son los posibles riesgos que conlleva esta funcionalidad
4. cuáles son algunas ideas que guiarán su implementación inicial

*No* se presentarán descripciónes detalladas de la API o de otras
definiciones ni se presentarán ejemplos. En caso de necesitarse más
adelante, los documentos relacionados deberán vincularse a este documento. 

Descripción general
##############################
La aprobación asistida le brindará al sistema la capacidad 
para decidir si una muestra ingresada y leída cumpla o no especificaciones,
sin necesidad de que un humano manualmente lo decida.

Las muestras que cumplan los *criterios* para ser aprobadas, cambiarán su
estado a "Con aprobación final" y el sistema pasará a generar su Certificado
de Emisión, tal como si el Director las hubiera inspeccionado y aprobado
manualmente.

Para formular automáticamente el *concepto de aprobación asistida*, el
sistema recaerá en el *sistema LERA* para reconocer y analizar
cada lectura a la luz de los comportamientos vigentes en su configuración.


Necesidad
##############################

Esta funcionalidad surge de las siguientes situaciones:

1. ¿Cómo lidiar con el creciente volumen de muestras por aprobar? 
2. ¿En particular, cómo lo hago si para emitir un certificado se
   necesita recibir la entrada del usuario para el campo 'Concepto' de
   la muestra?
3. ¿Qué puedo hacer para agilizar la inspección minuciosa de las
   lecturas, que consume tiempo y se presta a errores?

Ante estas necesidades, esta funcionalidad responde de la siguiente manera:

1. Se habilitará  una acción para "aprobar en bloque", que permitirá aprobar
   varias muestras al mismo tiempo. Se dejará  de forzar la aprobación uno
   a uno, aunque en ciertos casos será inevitable tener que realizar una
   'aprobación manual'. 
2. Se formulará una serie de heurísticas para determinar el concepto de la
   muestra de forma automatizada. A estas heurísticas se las llamará el
   *concepto de aprobación asitida*.

   El concepto de aprobación asistida recaerá en la salida del
   *sistema LERA*. Esto quiere decir que para cada *lectura* se
   tomarán los comportamientos asociados a su Caso LERA y de ellos se
   buscará extraer información relevante para el concepto.

3. Se permitirá que el *concepto de aprobación asistido* pueda
   visibilisarze en las vistas de la aplicación donde son clave ('Sala
   de aprobación' y 'Muestras por aprobar').
   
Dificultades de diseño
##############################

Esta funcionalidad deberá lidiar con los siguientes problemas:

1. No todas las especificaciones que se registran en el sistema
   son reconocidas por LERA.

2. No todos los comportamientos de LERA dan información relevante
   sobre el concepto.

3. No es claro cuál es el momento adecuado en el que generar el
   concepto asistido. Así como tampoco es inmediatamente claro qué
   metadatos guardar para posiblemente auditar o simplemente
   inspeccionar (para una posible capa de BI).
   
4. No es claro a priori cuál será el desempeño de correr todas
   las validaciones de LERA cada vez que se desee calcular
   el concepto asistido.



Dificultades operacionales
##############################
Con este diseño, se pueden observar los siguientes 'puntos de dolor':

1. La persona que utilizará la aprobación asistida deberá ser
   consciente del significado del 'umbral de cobertura LERA' y de que
   el resultado de la aprobación asistida dependerá de este.

2. Se deberá hallar empíricamente qué valor para el 'umbral de
   cobertura LERA' sea el más conveniente para utilizar de manera
   periódica en aprobaciones asitidas que no estén supervisadas por un
   usuario (por ejemplo, si se decide someter periódicamente todas las
   muestras por aprobación final a la aprobación asistida).
   
3. Como hay una dependencia fuerte entre la aprobación asistida y el
   sistema LERA, cualquier cambio en la configuración del sistema LERA
   podría afectar la capacidad de generar el concepto asistido.

   Aunque la implementación del concepto asistido procurará gestionar
   acórdemente este tipo de situaciónes, también debe tenerse en
   cuenta que es un riesgo que siempre existe, sin importar cuánto se
   planifique contra este.
   
 

Atributos de diseño
##############################

Los atributos que considero pertinentes a destacar desde este nivel son los
siguientes:
- *observabilidad*: La solución deberá poder ser 'verificable' en
  algún sentido tangible por el usuario. Como es un sistema altamente
  dinámico en el que las reglas de reconocimiento de lecturas pueden
  cambiar, se buscará ofrecer un medio para que el usuario visualice y
  cuestione el veredicto ('Cumple' o 'No Cumple') emitido por el
  concepto asistido.

- *liviandad*: La solución busca solucionar un problema altamente
  complejo: automatizar el proceso principal del laboratorio. Por
  ello, se abordará partiendo del principio: hacer lo más sencillo
  posible para luego observar cómo se comporta.

- *sensatez*: La solución deberá gestionar correctamente los casos en que
  no se pueda llegar a un concepto asistido. Es preferible ser muy estricto,
  que muy permisivo.

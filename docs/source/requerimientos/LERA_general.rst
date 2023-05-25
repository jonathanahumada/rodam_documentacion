##############################
Sistema LERA
##############################

.. |date| date::
	  
:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  primera version 2023-05-23, último build el |date|


.. contents::



Descripción general
--------------------

Técnicamente, LERA (Lenguaje de Especificación de Rodam Análisis) es
un componente de software. El objetivo de LERA se puede sintetizar de
la siguiente manera: transformar una cadena de texto a un entidad de
la lógica de negocio (por ejemplo, una lectura de muestra o una
especificación).

Una descripción menos abstracta es: LERA toma una cadena de texto y,
si la reconoce, la interpreta como un objeto de programación. La
salida de LERA puede ser utilizada como la entrada a otros
sistemas. Por ejemplo, para mostrar elementos gráficos. Para ver como
se utiliza LERA desde la perspectiva de un usuario, ver la entrada
:doc:`/usuario/lera` de la Guía de Usuario.

Uno de los objetivos secundarios de LERA fue precisamente poder ser
utilizado por otros componentes (por una vista de Django o por un
script, por ejemplo). El porqué de este objetivo se hará claro a
medida que se avanze en el documento.



Necesidad
---------

LERA surge para resolver dos problemas concretos:

1. ¿Cómo puedo incorporar la noción de 'dato primario' a mi sistema?

2. ¿Cómo puedo automatizar el proceso aprobación de la muestra si el
   concepto es asignado por el analista?


Ante estas necesidades, LERA responde de la siguiente manera:

1. Como el dato primario estará fuertemente relacionado a su valor
   transformado, enfoquémonos en crear la capacidad de generar el
   valor transformado a partir del dato primario y su respectiva
   especificación (en el mayor de los casos, que exclusivamente
   dependa de estas dos entradas).

   Dicha capacidad debe ser *flexible* (pues si resulta exitosa, se
   debe poder propagar al resto de procesos del sistema) y además debe
   procurar evitar poner mayor carga en otros áreas de la aplicacion.

   Por ejemplo, debe evitar que durante el proceso de especificación
   de una muestra (que ya de por sí es un proceso complejo) se tengan
   que asignar manualmente más atributos (como las unidades válidas
   para la lectura, etc) o que al momento de la lectura el analista
   manualmente teclee el dato primario y luego el valor transformado.


2. Este se trata de un problema complejo y, por consiguiente, debe ser
   descompuesto en partes más manejables. Así, al momento de su
   diseño, LERA no propone una *única* solución final concreta, pero
   ofrece las siguientes *capacidades*:

    2.1 Reconocimiento

    Consideremos lo siguiente: una cadena de texto por sí misma no
    brinda suficiente información para automatizar procesos. Por esto,
    siempre es necesario el concepto del analista, para 'llenar la
    casilla' correctamente.

    Por otro lado, si se impone demasiada estructura, se añade carga
    al proceso de ingreso de muestra y de catálogo. En el argot de
    desarrollo de software, a esto se le llama 'aumentar la
    complejidad'.  La complejidad es tan indeseable como necesaria. Y
    la tarea del desarrollo es precisamente gestionarla, pero ¿cómo se
    gestiona la complejidad en este caso? Respuesta: se provee la
    capacidad de 'reconocer' las cadenas.
    
    Si a las cadenas (las especificaciones) ya existentes se
    convierten en 'algo más detallado', se empiezarán a abrir las
    posibilidades de solución. Ese 'algo más detallado' son los
    *casos* de la gramática de LERA (ver
    :doc:`/requerimientos/LERA_casos`).

    El reconocimiento de LERA aumenta la cohesión del sistema porque
    agrupa 'lo similar con lo similar' (a través de sus casos) al
    mismo tiempo que previene la acoplación entre las partes (en
    concreto, que las validaciones de las lecturas no dependan de que
    anteriormente otro usuario en su rol de 'creador de cuadros' haya
    llenado correctamente todas las dependencias).

    2.2. Asistencia

    Se brindan herramientas al analista para 'llenar las casillas' más
    fácilmente.  No se abandona el principio de responsabilidad del
    analista, pero se optimiza la usabilidad, sobre todo la capacidad
    de ejecutar acciones en bloque.
    


Dificultades de diseño
-------------------------
1. creación de una 'taxonomía' de especificaciones (se encontraron
   72,000 lecturas hechas). ¿Cómo aseguro que cubro todos los casos?

  *Respuesta*: Probablemente no se puedan cubrir todos los casos
  porque se encontrarían inconsistencias sintacticas en las lecturas
  existentes.  Pero es más importante esto: *no es necesario cubrir
  todos los casos anteriores*, por lo menos no en un principio. Basta
  con asegurar los pocos casos mayor repetición e ir *progresivamente*
  cubriendo los demás.

2. ¿Qué tecnología debo usar para interpretar la cadena?

   *Respuesta*: En un principio se presentaban varias
    posibilidades: a) 'database first', b) gramatica formal, c)
    'machine learning', d) encontrar una libreria especializada (NLTK,
    por ejemplo) o e) solo usar regexes.

    Luego de unos cortos experimentos con regexes, la gramática formal
    pareció la solución más sencilla porque:

    1) se enfrentaba a un problema de reconocimiento, su aplicación clásica
    2) no se depende de las lecturas anteriores, pero ofrece la capacidad
       de incorparlas como reglas del BNF
    3) se puede utilizar para  imponer una estructura. Es decir, el laboratorio
       puede usar el BNF para formalizar los tipos de lecturas
    4) luego de las regexes, era la solución que ofrecía un bucle de
       retroalimentación más corto. De acuerdo a las consignas del
       desarrollo ágil, entre más rápida la retroalimentación, menor
       termina siendo el costo a largo plazo.
    5) ofrecía la mayor potencia al menor costo. Una línea de código del BNF
       termina solucionando muchas cosas. Para un ejemplo, ver la Referencia
       de la grámatica en :doc:`/requerimientos/LERA_casos`. En términos
       generales, entre menos líneas de código se escriban, menor puntos de
       fallo en el sistema. 
       
    Las desventajas de la gramática formal son:

    1) que las reglas se deben escribir manualmente. No es claro como
       verificar que las reglas manuales se ajusten a la carga de
       datos que recibe. Como tampoco es claro si las reglas escritas
       son las 'óptimas'. Eso dependerá de la comunicación entre el
       programador y el 'experto del dominio'.

    2) tradicionalmente, las gramaticas formales no soportan
       ambiguedades, no es claro cómo se comportará el sistema en caso
       enfrentarse a una. Por ejemplo, que para una misma
       especificación haya dos interpretaciones igualmente
       válidas. Esto sería obvio para un humano, pero no para la
       máquina.

    3) era un desarrollo exigente, porque se trataba no tanto de
       implementar un 'lenguaje' (el `parser generator` haría la mayor
       parte del trabajo), sino de diseñarlo y luego integrarlo con el
       resto del sistema. Así ofrece máxima potencia, también ofrece
       máxima capacidad para complejizar.

       


Dificultades operacionales
-----------------------------
1. ¿Cómo modifico todos los cuadros (analíticos y abstractos),
   análisis, método, etc. para poner los nuevos atributos (dato
   primario, unidad necesario, unidad admitida caso, etc)?

   *Respuesta*: Se podrían modificar con scripts, pero las
   modificaciones continuas (aun con las \`migrations\` de Django),
   crean una carga adicional a todo el proceso de desarollo.  El más
   desgastante, es que se tienen que llenar retroactivamente atributos
   recién añadidos a modelos viejos. La tarea de llenar estos
   atributos implica análisis e implementación adicionales a las
   funcionalidades en sí.

   La solución óptima es *no modificar* los cuadros analíticos, sino
   extraer *toda la información necesaria* de la cadena de
   especificación y la cadena de lectura*

   
2. ¿Qué pasa si el diseño fracasa, cómo retorno al schema anterior sin
   perder todos los datos ingresados en el interim?

   *Respuesta*: Se podría retornar al schema anterior con una seria
   suceciva scripts, pero ya se mencionó lo costoso (sin hablar de lo
   riesgoso) que es.

   La solución óptima es *solo modificar el schema* cuando se está
   *seguro* de que se necesita, porque el coste operacional es grande
   para usuario final, el desarrollador y el dueño del negocio. La
   forma de evitar modificar lo que ya está es pasando la lógica nueva
   a un componente (un modelo de django por ejemplo), que cargue con
   esa responsabilidad.


Entorno
----------

Como componente, LERA es una `django app`. Una app de django encapsula
varias responsabilidades: modelos, vistas, etc. Por lo mismo, LERA
se subdivide varios componentes. Aquí se aprecia una distinción básica
entre backend y frontend.

.. figure:: ../assets/LERA-entorno.png

    Diagrama de entorno

En el diagrama anterior se pretende mostrar los aspectos más
relevantes de LERA. Como se ve, las aplicaciones de LERA
son variadas. Uno de los atributos detrás de su diseño fue la
**modularidad**.

Atributos de diseño
-------------------

1. Modularidad

   LERA procura ser modular en varios sentidos. El más evidente es que
   se puede configurar desde el admin en tiempo real o en la
   independencia de los comportamientos entre sí.  Otro ejemplo, es en
   el diseño del AST, cada rama es independiente, pero puede utilizar
   elementos recurrentes (tanto `desigualdad_acotada` como
   `valor_numerico` usan `unidad`, pero siguen siendo casos distintos).

   

1. Liviandad

   LERA procura ser 'liviano' porque evita modificaciones continuas a
   la estructura de datos de la base de datos relacional, pero hace
   fácil la modificación a su API (json, python).  Ejemplo,
   es más fácil modificar este JSON desde el admin de Django que
   hacer una migración o trabajar en código directamente.

   .. code-block:: json

		{
		   "operacion": "{adicional[resultado_lectura_transformado][unidad]} is not None ",
		   "precondiciones": [
		   "'resultado_lectura_transformado' in adicional.keys()"
		   ],
		   "valor_esperado": true,
		   "bloquea_ingreso": true,
		   "ocultar_por_precondiciones": true
		}		  



2. Progresividad

   Como es modular, LERA puede **ampliarse** (ampliando su API),
   **modificarse** (cambiando sus comportamientos), o **ignorarse** (no
   hay dependecias estrictas en el modelo de datos que impacten la
   operación normal de la aplicación).

   La progresividad de LERA se diseñó para poder experimentar
   continuamente con qué comportamientos son más útiles para los
   analistas, hallar experimentalmente cuáles deben ser 'forzados',
   cuales no, etc. Esto se consideró necesario porque plantear un
   diseño 'upfront' para solucionar la necesidades de negocio probó
   ser de gran dificultad.

  
Relacionados
-------------

.. toctree::
   :maxdepth: 2

   LERA_casos.rst
  

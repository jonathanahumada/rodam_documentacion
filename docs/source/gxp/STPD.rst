===================
Plan de pruebas
===================

:author: Jonatan Ahumada Fernández
:contact: box@jade.lat
:date:  21 de julio de 2025


Objetivos
==============

El propósito de este plan de pruebas es establecer un marco
sistemático para la verificación del sistema Rodam WebLab,
asegurando que:

- Las funcionalidades implementadas cumplen con los requerimientos definidos.

- Los riesgos identificados han sido mitigados mediante pruebas adecuadas.

- El software se comporta de forma predecible y confiable en condiciones normales y anómalas.

- El sistema pueda actualizarse constantemente, asegurando que con
  cada actualización la funcionalidad previa se siga comportando como
  se espera.

  
Las pruebas realizadas proporcionan evidencia documentada que respalde
la validación del sistema.

Este plan también busca:

- Definir los tipos de pruebas a realizar, sus criterios de ejecución y salida.

- Especificar la organización de las pruebas en relación con los módulos funcionales del sistema.

- Establecer un mecanismo que facilite la trazabilidad entre requerimientos y pruebas.

El alcance de este plan incluye tanto pruebas automatizadas como
manuales, abarcando pruebas unitarias, de integración, y de validación
final por parte del usuario.


Tipos de pruebas
==================

Al ser un sistema de categoría GAMP tipo 5 (a la medida), las pruebas
realizadas sobre el software son variadas y de distintas naturaleza.
Se debe entender que las pruebas automatizadas pueden ser:

**unitarias**
   Se prueba un componente mínimo (una *unidad*) del software de manera aislada con
   entradas y salidas bien delimitadas.

**de integración**
   Se prueba la interacción de varios componentes juntos, tal como sucede en la aplicación, con miras
   a que su funcionamiento no presente un error. 
   
**punta a punta**
   Se prueba grandes flujos de funcionalidad. Por
   ejemplo, la generación de un certificado partiendo desde el ingreso
   de una muestra. Estas pruebas requieren de gran inversión. Sin
   embargo, son necesarias porque permiten asegurar que en cada
   incremento el funcionamiento de la aplicación se conserva
   (*regression tests*).

Además, se hacen pruebas constantes de esta naturaleza:

**inspección manual**
   Se revisa la aplicación final, ya sea en el
   ambiente de producción o de desarrollo, y se verifica que la
   funcionalidad bajo escrutinio funcione. Típicamente estas pruebas
   se hacen en conjunto con el *product owner*, y sirven como un punto
   de validación, además de verificación, del sistema.


Estimación de riesgos
======================

Durante cada incremento, el *product owner* puede proponer pruebas
necesarias según su propia estimacion de riesgo y estas serán
incluidas como un requerimiento más.

Sin embargo, al ser díficil para el *product owner* establecer pruebas
al nivel de detalle necesario, el *desarrollador* también hace un
análisis de riesgo para cada incremento y, por medio de su ojo
experto, determina qué componentes del sistema deben ser probados y
qué tipo de pruebas deben ser utilizadas.

Como guía al ojo experto, se utiliza esta categorización de niveles de riesgos:

Riesgo alto
-----------
- el incremento genera inconsistencias en los datos o ambiguedades que luego deberán ser arregladas via script
- el incremento altera cualquiera de los aspectos del certificado de emision, sea en su presentación o en su contenido
- el incremento deja al sistema en un estado inflexible, reacio a una posterior modificación, sin un plan de contigencia en su lugar
- el incremento deja una vulnerabilidad relacionada con la Confidencialidad, Integridad Y Accesibilidad de los datos

El *desarrollador* siempre debe escribir pruebas automatizadas para
mitigar el *riesgo alto*, sin importar el mayor esfuerzo requerido,
cuidandose de mantener sus herramientas de pruebase (*fixtures*,
*factories*, *stubs*) en buen estado.

Riesgo medio
------------

- el incremento introduce funcionalidad que innova en un proceso de
  negocio, cuyo éxito depende no solo de la excelencia técnica, sino
  de la adopción del usuario, a menudo sujeta a variables sobre las
  que no hay control.
- el incremento introduce un error en los formularios y se permiten
ingresar datos erróneos o inconsecuentes.
- el incremento introduce un cambio en la lógica de negocio, dentro de
  un componente bien establecido dentro del sistema. Por ejemplo, que
  en una validación entre salas, se añada un procedimiento de
  validación adicional.

El *desarrollador* algunas veces escribe pruebas automatizadas para el *riesgo medio*.

Riesgo bajo
------------
- el incremento introduce errores estéticos o cambios en la ubicación de botones.
- el incremento introduce funcionalidades con permisos excesivos, que requieren una configuración adicional.

El *desarollador* no escribe pruebas para *riesgo bajo* (mas que nada,
sobre la interfaz de usuario), dejando que los usuarios finales del
sistema reporten cualquier no conformidad al respecto. Estos errores
siempre pueden ser arreglados a gran velocidad y no comprometen la
lógica de negocio.


La organización de las pruebas
==============================

Como se estable en la *Especificación de Requerimientos*, el software
está conceptualmente definido en áreas funcionales o submodulos. Así,
la estructura general de las pruebas se organiza según esta estructura
y no necesariamente según el tipo de prueba (unitaria o de
integración). Un ejemplo de la organización de las pruebas es::

  tests  
  ├── artefactos
  ├── emision
  ├── formularios
  ├── procesos
  ├── reporter
  ├── services
  ├── teoremas
  ├── validaciones
  └── vistas

Las utilidades de ayuda de las pruebas se separan en el módulo `factories` y siguen la misma estructura mencionada anteriormente. Por ejemplo::

	mysite/factories/
	├── model
	│   ├── anotaciones
	│   ├── calidad
	│   ├── catalogo
	│   ├── emision
	│   ├── ingreso
	│   ├── __init__.py
	│   ├── inventario
	│   ├── login
	│   ├── __pycache__
	│   └── recoleccion

	


Herramientas de pruebas
=========================

El WebLab utiliza las siguientes herramientas:

- `unittest`_ mediante `django.tests`_
- `factory_boy`_
  
.. _unittest: https://docs.python.org/3/library/unittest.html
.. _django.tests: https://docs.djangoproject.com/en/5.2/topics/testing/overview/
.. _factory_boy: https://factoryboy.readthedocs.io/en/stable/index.html
  
Trazabilidad de las pruebas
===============================

Cada vez que se escribe una prueba, esta se vincula al catálogo del
producto utilizando su código en el *docstring* del método de prueba::

     def test_multidimensiona_un_string(self):
        "ROD-33 Flujo emisión."
        tabla = self.rep._multidimensionar(
            "Esto debe quedar en una lista multidimensional. Para reportlab es una tabla"
        )

        self.assertIsInstance(tabla, list)
        self.assertIsInstance(tabla[0], list)


Luego, mediante scripts, se elabora la matriz de trazabilidad de las pruebas.

Los scripts producen una matriz en formato csv y otra en formato
PDF. Estos artefactos serán generados a pedido de la entidad regulada.

La versión csv de la matriz de trazabilidad se incorpora al repositorio principal.

Verificación
=============

El objetivo de la verificación es que el *desarollador* pueda asegurar
con un nivel alto de confiabilidad que el sistema que implementó se
comporta de acuerdo a su diseño.

El *desarrollador*, *al menos* al finalizar cada incremento, verifica que la suite de pruebas
esté pasando. De lo contrario, no se procede a la actualización del software.

El *reporte de pruebas* de este paso de verificación se incorpora por
escrito al manual a pedido de la entidad regulada.


Validación
==========
El objetivo de las pruebas de validación es
verificar que la funcionalidad sea utilizable por parte del usuario
final. Cada vez que se finaliza un sprint, la nueva funcionalidad se
sube al ambiente de producción.

La validación sucede en al menos dos momentos:

- durante una ceremonia de predespliegue en el entorno de desarrollo
- durante una ceremonia de cierre en el entorno de producción 

Adicionalmente, al entrar a producción se notifica de la actualización
al dueño del producto, haciendo énfasis en posbibles riesgos. Este
recibe un breve resumen de la funcionalidad tomada del sistema de
control de cambios. Un ejemplo de esta notificacion es::

  commit 510a495eb0bf59161765850bcfa116c8ee275e96 (correcciones_daniel_2022_02_11)
  Author: Jonathan Ahumada <jaumaf@Jonathans-MacBook-Air.local>
  Date:   Mon Feb 14 10:42:19 2022 -0500

    - RA-219 el cuadro analitico se incluye al momento de exportar el csv de la factura

      commit e91134564cf64e9eddf26c5aa79abc013e772ba6
      Author: Jonathan Ahumada <jaumaf@Jonathans-MacBook-Air.local>
      Date:   Mon Feb 14 10:29:00 2022 -0500

    - RA-218 el campo de observaciones aparece en el formulario de editar lectura en sala

     commit 740f5deac17c26790ef0081bcc97e84b6e49e294
     Author: Jonathan Ahumada <jaumaf@Jonathans-MacBook-Air.local>
     Date:   Mon Feb 14 09:44:28 2022 -0500

    - RA-217 ahora es 'Marcar inicio en laboratorio' en vez de 'Marcar inicio de lecturas'


Luego, el cliente valida (hace una inspección manual de la
funcionalidad) sobre el sistema en producción. Si la funcionalidad no
cumple con lo esperado, se abre una tarjeta en el sistema de
seguimiento de incidencias (Jira) o, en caso de ser necesario, se
realiza un *rollback*.

Criterios de entrada
=====================

Antes de ejecutar una prueba, deben cumplirse los siguientes criterios:

- Las migraciones de base de datos están aplicadas y reflejan el estado esperado del sistema.
- Los requerimientos asociados a la funcionalidad a probar están
  madurados, por lo menos a mayor detalle que un requerimiento de alto
  nivel.
- Se cuenta con los datos de prueba, fixtures o herramientas necesarias para ejecutar el escenario.
- Para pruebas manuales y de validación, el cliente o usuario final ha sido notificado y está disponible para realizar la verificación.

Criterios de salida
====================

Una prueba se considera finalizada cuando:

- Todos los pasos definidos en el caso de prueba han sido ejecutados y pasan para el estado del sistema que pasa a la actualización.
- El resultado esperado ha sido observado sin errores ni desviaciones críticas.
- El sistema ha retornado a un estado conocido y consistente, listo para pruebas futuras.


===================
Plan de pruebas
===================

.. |date| date::
	  
:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  último build el |date|




Introducción
============

Este documento constituye el plan de pruebas para el sistema
de información de Rodam análisis. El propósito de este
documento es explicar qué tipo de pruebas se necesitan llevar
a cabo y por qué, con base a la estimación de riesgos y las
funcionalidades descritas en la  *Especificación de
Requerimientos*.


Necesidades del tipo de pruebas
================================
Al ser un sistema de categoría GAMP tipo 5 (a la medida), las pruebas
realizadas sobre el software son variadas y de distintas naturaleza.
Sobre el software se realizarán pruebas a) unitarias b) de integración
c) manuales y d) de validación.


Estimación de riesgos
=====================
Aquí se hará un resumen sucinto de los riesgos más relevantes
del presente sistema.


Riesgo alto
-----------
- el modelo de datos del sistema es insuficiente y/o genera inconsistencias en los datos
- el artefacto principal, el certificado de emisión, es incompleto
- el artefacto principal, el certificado de emisión, no es flexible a posteriores cambios
- los datos no son accessibles o de difícil interpretación
- los datos en los formularios no son restringidos de forma adecuada y se permiten ingresar datos erróneos o iconsecuentes


Riesgo medio
------------

- los requerimientos cambian a medida que se avanaza el desarrollo y se obtiene mayor información sobre las necesidades
- cambiar los procesos de negocio que antiguamente se hacían con hojas de cálculo puede dar lugar a confusiones
Riesgo bajo
------------
- las componentes utilizados, tanto de software como de hardware,  son insuficientes o presentan fallas
- la interfaz gráfica no es inmediatamente comprensible o estéticamente desactualizada




La organización de las pruebas
==============================

Como se estable en la *Especificación de Requerimientos*, el
software está conceptualmente definido en áreas funcionales
o submodulos. Así, la estructura general de las pruebas
se organiza según esta estructura y no según el tipo
de prueba (unitaria o de integración). Un ejemplo
de la organización de las pruebas es::

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


Pruebas unitarias
=================
Las pruebas unitarias constituyen la parte más cuantiosa de las pruebas.
Su objetivo es asegurar que el comportamiento de una unidad de computación
sea el estipulado por los requisitos. Por este motivo, se utilizan
pruebas automatizadas. Estas pruebas son en sí mismas piezas de código
ejecutable y su salida produce un reporte similar a este::

  test_se_necesita_tener_firma_y_logo (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado) ... ok


Pruebas de integracion 
=======================
El objetivo de las pruebas de integración es asegurar que dos o más módulos
computacionales se relacionan entre sí de forma adecuada. Estas pruebas también
son automatizadas. Como la codificación de las pruebas de integración es compleja,
su número es reducido. Los criterios  para realizar una prueba de integración
son su efecto en la cadena de valor y el riesgo que conlleva el fallo de los
componentes implicados.

Las áreas que más tienen pruebas de integracion son: el área de emisión de
certificados, el área de recolección de resultados y el los procesos de
validación al ingresar, especificar y realizar lecturas de una muestra.

Por ejemplo, como la emisión de certificado es la culminación del proceso
y genera un artefacto importante (el certificado de emisión).
Hay pruebas de integración que generan una muestra automáticamente, hacen las
lecturas y luego exportan un certificado::

  test_se_imprime_con_datos_falsos (tests.reporter.test_certificado_de_emision.PDF_Reporter) ... skipped ''
  test_se_integra_con_la_muestra (tests.reporter.test_certificado_de_emision.PDF_Reporter) ... ok



Pruebas manuales
================
El objetivo de las pruebas manuales es verificar aspectos del software
para los que el desarrollo de pruebas automatizadas consumiría demasiados
recursos (tiempo de desarrollo y complejidad del sistema). Por lo
general, las pruebas manuales se utilizan para verificar: la navegación
por el sitio web,  y los opciones desplegables en formularios y la
autorización a cierta funcionalidad del sistema dependiendo del usuario.



Validación
==========
El objetivo de las pruebas de validación es
verificar que la funcionalidad sea utilizable por parte del usuario
final. Cada vez que se finaliza un sprint, la nueva funcionalidad se
sube al ambiente de producción. Luego, se notifica de la actualización
al dueño del producto. Este recibe un breve resumen  de la funcionalidad tomada
del sistema de control de cambios. Un ejemplo de esta notificacion es::

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
seguimiento de incidencias (Jira).


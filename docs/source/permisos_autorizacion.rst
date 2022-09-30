=============================================
Permisos y autorización
=============================================

Intro
====
Los permisos y autorizaciones determinan qué usuario puede utilizar
qué funcionalidad en el sistema. Esto es una parte importante de la
seguridad de la aplicación. Comúnmente, la seguridad se subdivide
en Disponibilidad, Confidencialidad e Integridad. En este documento
estamos abordando la Confidencialidad.

Síntesis
======

La implementación de la confidencialidad está dada por el Authorization
Framework de Django. Los detalles de la implementación pueden
consultarse en la documentación oficial.

El interés aquí radica en listar los permisos críticos de la aplicación.
Se desglosarán en áreas, para mantener la jerarquía utilizada en la
demás documentación:


Inventario
=======

Catálogo
======


Ingreso
=====


Calidad
=====
- solo el director de calidad puede marcar cuadro de control como listo para uso
- solo el director de calidad puede marcar cuadro analitico como listo para uso
- permiso especial de remisión para cuadro analitico
- restricción de flujo para edición de cuadros analíticos en uso 



Recolección
========



Emisión
=====
- solo el director del laboratorio puede emitir

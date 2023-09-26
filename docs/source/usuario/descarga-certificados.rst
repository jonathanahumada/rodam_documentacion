##############################
Descarga de certificados
##############################

Resumen
##############################
.. list-table:: Resumen
   :header-rows: 0

   * - Area
     - Emisión
   * - Permisos
     - `ingreso.descargar_certificado`
   * - Grupos
     - Director de calidad, Director del laboratorio


Interfaces
##############################
La descarga de certificados se puede hacer:

1. desde el Detalle de la Muestra
2. desde una tabla dinámica con la acción habilitada a través de: exportar > certificado. Ver :doc:`flujo-emision`. 


Observaciones
--------------
- Cuando un usuario descarga la muestra, se marca automaticamente el atributo `miembro_descargo` como verdadero




Exportación en bloque 
##############################

Cuando se utiliza la acción exportar > certificado, la aplicación hará lo siguiente:

- tomara el último certificado emitido de cada muestra seleccionada en la tabla, si este existe 
- generará el pdf para cada certificado existente
- comprimirá cada  pdf en un un solo archivo zip
- marcará automáticamente el atributo `miembro_descargo` como verdadadero para cada muestra con certificado existente.

.. image:: ./assets/descarga-certificados-ejemplo.png

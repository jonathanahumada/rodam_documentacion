##############################
Creación de templates
##############################

:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  primera version 2023-09-19, último build el 

Resumen
##############################
Crear templates puede ser tedioso. En este proyecto
se optó por minimizar la dependencia entre templates,
por lo que cada vista tiene un template asociado
que le corresponde a esa vista.

Una comprensión intuitiva de los patrones que se siguen
puede obtenerse viento el directorio de templates:





.. code-block:: shell 

       tree -L 2 templates/
       templates/
       ├── 403.html
       ├── admin
       │   ├── base_site.html
       │   └── base_site.html~
       ├── base
       │   ├── ajax_dropdown.html
       │   ├── base_acciones.html
       │   ├── base_ancho.html
       │   ├── base_ancho.html~
       │   ├── base_confirm_delete.html
       │   ├── base_detail_acciones.html
       │   ├── base_detail_resumen.html
       │   ├── base_detailView.html
       │   ├── base_exception.html
       │   ├── base_filtro.html
       │   ├── base_formulario_general_lectura.html
       │   ├── base.html
       │   ├── base_list_tabla.html
       │   ├── base_listView.html
       │   ├── base_tabla_especificaciones.html
       │   ├── base_tabla_general.html
       │   ├── base_tabla_lecturas.html
       │   ├── dashboard_snippet.html
       │   ├── dashboard_snippet.html~
       │   ├── datatable_snippet.js
       │   ├── filas_footers_vacias.html~
       │   ├── filas_footer_vacio.html~
       │   ├── formulario_ingreso_basico.html
       │   ├── formulario_inline.html
       │   ├── header.html
       │   ├── #header-scripts-buttons.html#
       │   ├── header-scripts-buttons.html
       │   ├── header-scripts-buttons.html~
       │   ├── header-scripts.html
       │   ├── header-scripts.html~
       │   ├── mensajes_snippet.html
       │   ├── objetos_relacionados_snippet.html
       │   ├── #pagination_snippet.html#
       │   ├── pagination_snippet.html
       │   ├── pagination_snippet_slim.html
       │   ├── pagination_snippet_slim.html~
       │   ├── tabla_resumen.html
       │   ├── tags_filas_tbody_vacio.html
       │   ├── WeblabConf_confirm_delete.html
       │   ├── WeblabConf_detail_acciones.html
       │   ├── WeblabConf_detail.html
       │   ├── WeblabConf_detail_resumen.html
       │   ├── WeblabConf_list.html
       │   └── WeblabConf_list_tabla.html
       ├── calidad
       │   ├── cuadroanalitico_list.html
       │   ├── CuadroDeControl_detail_acciones.html
       │   ├── CuadroDeControl_detail.html
       │   ├── CuadroDeControl_detail_resumen.html
       │   ├── CuadroDeControl_detail_tablaMetodos.html
       │   ├── CuadroDeControl_list.html
       │   ├── CuadroDeControl_list_tabla.html
       │   ├── dropdown_CuadroDeControl.html
       │   ├── dropwdown_CuadroDeControl.html
       │   ├── LoteDeMedio_confirm_delete.html
       │   ├── LoteDeMedio_create.html
       │   ├── LoteDeMedio_detail.html
       │   ├── LoteDeMedio_detail_resumen.html
       │   ├── LoteDeMedio_list_aprobados.html
       │   ├── LoteDeMedio_list copy.html
       │   ├── #LoteDeMedio_list.html#
       │   ├── LoteDeMedio_list.html

       .. etc..

       ├── catalogo
       │   ├── Analisis_detail_acciones.html
       │   ├── Analisis_detail.html
       │   ├── Analisis_detail_resumen.html
       │   ├── Analisis_detail_tabla.html
       │   ├── Analisis_list.html
       │   ├── Analisis_list_tabla.html
       │   ├── cuadroAbstracto_detail_acciones.html
       │   ├── cuadroAbstracto_detail_acciones.html~
       │   ├── cuadroAbstracto_detail_resumen.html
       │   ├── cuadroAbstracto_detail_resumen.html~
       │   ├── cuadroAbstracto_detalle.html
       │   ├── cuadroAbstracto_detalle.html~
       │   ├── CuadroAbstracto_list.html
       │   ├── CuadroAbstracto_list_tabla.html
       │   ├── CuadroAbstracto_list_tabla.html~
       │   ├── formulario_analisis_grupo.html
       │   ├── formulario_analisis_metodo.html
       │   ├── formulario_metodo_equipo.html
       .. etc...

       


Generación de plantillas mediante scripts
##########################################

Una forma rápida de seguir estos patrones es usando
los scripts para generar plantillas. Estos estan
prefijados con 'make'

.. code-block:: shell 

       (venv) (base) [jaumaf@Sypha mysite]$ls scripts/ | grep make
       make_delete.sh
       make_detail.sh
       make_list.sh
       make_resumen.sh

Al correr estos scripts se generar plantillas de Django listas
para ser utilizadas por las vistas.

Por ejemplo, al correr esto:

.. code-block:: shell 

       bash scripts/make_list.sh emision MuestraArchivada

   
Se generan las siguientes plantillas django, en el directorio
suministrado como primer argumento.

.. code-block:: shell 

        (venv) (base) [jaumaf@Sypha mysite]$ ls templates/emision/ | grep MuestraArchivada
        MuestraArchivada_list.html
        MuestraArchivada_list_tabla.html


Cómo funcionan las plantillas
##############################

Se parte de unos archivos base ubicados en `templates\base\`.
Estos archivos se copian al directorio correcto y luego se reemplazan
cadenas de palabras reservados con la información pasada por parámetro.

Si se quieren editar, se pueden identificad con el prefijo `base`. Ejemplo:


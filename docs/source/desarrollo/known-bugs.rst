##############################
Errores conocidos
##############################

:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  primera versión 2023-01-25

Esta es una lista de errores conocidos, que por diversas razones no
han sido solucionados.

**Retroalimentación de acciones a veces salen en diferentes páginas**
    Por ejemplo, con *exportar factura* en vista de muestras facturadas, se  agrega un mensaje al objeto messages de Django. Como la
    página no recarga, sino que descarga un archivo, el mensaje queda en la pila hasta que se cambia de página y sale de la pila. 

**Errores tipográficos en componentes**    
    En CertificadoEmitido hay atributo 'json_fima' en vez de 'json_firma'. Hay un módulo *reportab* en vez de *reportlab*.

**Certificados guardan referencia a OS para las firmas**
    Esto hace que para replicar un certificado en ambiente de desarrollo, se tenga que duplicar la estructura del sistema
    de archivos de producción, para que los certificados encuentren las firmas pertinentes.

**Empresas aún no tienen correos obligatorios**
    Esto indirectamente hace que se levanten excepciones, especialmente si tratan de emitir un certificado para un cliente sin correo. Por el momento no se puede hacer obligatorio porque se necesita que retroactivamente ingresen todos los correos que faltan.

**Siempre se puede archivar un cuadro**
      Para un usuario que tenga acceso a las vistas con la acción *archivar cuadro*, siempre se puede archivar. No hay un
      permiso dedicado para esta acción o un test de flujo.

**Los correos se almacenan con un link diferente**
     El link enviado a los clientes para descargar es correcto y funcional, pero al almacenar el envio en la base de datos queda
     con un link diferente. Se puede reconstuir el link funcional a partir del link almacenado. Simplemente es incómodo.

**La complejidad de un cuadro tiene un doble criterio**
     Además de marcarlo directamente como complejo, se consideran complejos los cuadros que tienen más de un grupo.
     Esto da lugar a confusiones. 
    
**Las tablas dinámicas causan una alerta en el navegador**
     Esto sucede cuando la tabla dinámica está vacía y se intenta usar el patrón idiomático de Django para lidiar con tablas vacías (*{% empty %}*). Esto confunde la tabla dinámica y hace que ponga un aviso en el browser. Es incómodo, pero no grave.

**Nombres de productos se desbordan de los controles**
     Los nombres muy largos no caben en los controles. Especialmente para el control *select*, es muy difícil y no recomendado alterar
     los estilos, porque estos utilizan el sistema subyacente el OS. Esto arruina la legibilidad de algunos formularios.

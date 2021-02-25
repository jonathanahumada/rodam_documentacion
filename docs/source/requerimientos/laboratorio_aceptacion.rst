=================================
Prueba de aceptación
=================================

.. |date| date::
	  
:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  último build el |date|



Resumen
-------

Este cuaderno muestra la funcionalidad de la base de datos relacional
utilizada para el módulo **Laboratorio** del sistema de información de
Rodam Análisis S.A.S. Las funcionalidades se muestran
*independientemente* de la interfaz de usuario que luego se implemente
sobre el modelo. Idealmente, el modelo deberá cumplir con todos los
casos de uso, para luego pasar a la implemenación de su interfaz.

Con este cuaderno tanto el *product owner* como el desarrollador podrán
evaluar su comprensión mutua sobre el sistema y poner a prueba nuevas
ideas.


Este cuaderno es ejecutable en Binder. Lo puedes correr aquí:


.. image:: https://img.shields.io/badge/pru%C3%A9balo%20-aqu%C3%AD-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0NDQ1NbW3Nzg4ODi5+3v8PDw8/T09PX29vb39/f5+fr7+/z8/Pz9/v7+zczCxgAABC5JREFUeAHN1ul3k0UUBvCb1CTVpmpaitAGSLSpSuKCLWpbTKNJFGlcSMAFF63iUmRccNG6gLbuxkXU66JAUef/9LSpmXnyLr3T5AO/rzl5zj137p136BISy44fKJXuGN/d19PUfYeO67Znqtf2KH33Id1psXoFdW30sPZ1sMvs2D060AHqws4FHeJojLZqnw53cmfvg+XR8mC0OEjuxrXEkX5ydeVJLVIlV0e10PXk5k7dYeHu7Cj1j+49uKg7uLU61tGLw1lq27ugQYlclHC4bgv7VQ+TAyj5Zc/UjsPvs1sd5cWryWObtvWT2EPa4rtnWW3JkpjggEpbOsPr7F7EyNewtpBIslA7p43HCsnwooXTEc3UmPmCNn5lrqTJxy6nRmcavGZVt/3Da2pD5NHvsOHJCrdc1G2r3DITpU7yic7w/7Rxnjc0kt5GC4djiv2Sz3Fb2iEZg41/ddsFDoyuYrIkmFehz0HR2thPgQqMyQYb2OtB0WxsZ3BeG3+wpRb1vzl2UYBog8FfGhttFKjtAclnZYrRo9ryG9uG/FZQU4AEg8ZE9LjGMzTmqKXPLnlWVnIlQQTvxJf8ip7VgjZjyVPrjw1te5otM7RmP7xm+sK2Gv9I8Gi++BRbEkR9EBw8zRUcKxwp73xkaLiqQb+kGduJTNHG72zcW9LoJgqQxpP3/Tj//c3yB0tqzaml05/+orHLksVO+95kX7/7qgJvnjlrfr2Ggsyx0eoy9uPzN5SPd86aXggOsEKW2Prz7du3VID3/tzs/sSRs2w7ovVHKtjrX2pd7ZMlTxAYfBAL9jiDwfLkq55Tm7ifhMlTGPyCAs7RFRhn47JnlcB9RM5T97ASuZXIcVNuUDIndpDbdsfrqsOppeXl5Y+XVKdjFCTh+zGaVuj0d9zy05PPK3QzBamxdwtTCrzyg/2Rvf2EstUjordGwa/kx9mSJLr8mLLtCW8HHGJc2R5hS219IiF6PnTusOqcMl57gm0Z8kanKMAQg0qSyuZfn7zItsbGyO9QlnxY0eCuD1XL2ys/MsrQhltE7Ug0uFOzufJFE2PxBo/YAx8XPPdDwWN0MrDRYIZF0mSMKCNHgaIVFoBbNoLJ7tEQDKxGF0kcLQimojCZopv0OkNOyWCCg9XMVAi7ARJzQdM2QUh0gmBozjc3Skg6dSBRqDGYSUOu66Zg+I2fNZs/M3/f/Grl/XnyF1Gw3VKCez0PN5IUfFLqvgUN4C0qNqYs5YhPL+aVZYDE4IpUk57oSFnJm4FyCqqOE0jhY2SMyLFoo56zyo6becOS5UVDdj7Vih0zp+tcMhwRpBeLyqtIjlJKAIZSbI8SGSF3k0pA3mR5tHuwPFoa7N7reoq2bqCsAk1HqCu5uvI1n6JuRXI+S1Mco54YmYTwcn6Aeic+kssXi8XpXC4V3t7/ADuTNKaQJdScAAAAAElFTkSuQmCC
   :target: https://mybinder.org/v2/gh/jonathanahumada/rodam-jupyter/main

Documentos relacionados
-----------------------

-  La *Especificación de Requermientos* detalla los requrimientos y los
   submódulos del laboratorio.
-  El *Documento de Diseño* estudia las relaciones y las entidades del
   módulo.

Objetivo
--------

Evaluar el alcance y las limitaciones del *backend* del módulo
Laboratorio.

Como criterios para evaluar la idoneidad del modelo, propongo estas
consideraciones:

-  ¿las tablas permiten hacer las consultas que necesito en este
   momento?
-  ¿las tablas aseguran la integridad referencial de mi modelo?
-  ¿parece posible extender el sistema con requerimientos que puedan
   salir a futuro?

Definiciones
------------

El *backend* está compuesto por dos capas. La primera de ellas es la
**capa de la base de datos relacional**. La segunda de ellas es la
**capa del ORM**, que mapea el modelo relacional al paradigma de
orientación a objetos.

Tanto en el desarrollo como en esta *prueba de aceptación* nos valdremos
del **ORM**, por las ventajas que ofrece. Sin embargo, el **modelo
relacional** es el cimiento del sistema. Por eso, la exposición vendrá
acompañada de consultas directas a una instancia de base de datos
``sqlite`` llamada ``aceptacion.bd``.

Repaso por los casos de uso
===========================

Para consultar los casos de uso en mayor detalle, consultar la
*Especificación de requerimientos* del módulo. El cuaderno seguirá el
camino de las **dependencias secuenciales** esbozadas en ese documento.
Un breve resumen del flujo de eventos del laboratorio sería:

.. image::  ../assets/flujograma.png
   :align: center

Inicio del flujo
================

Primero, carguemos el módulo de Python con el dominio:

.. code:: ipython3

    %cd ~/.devs/  # ubicarse un directorio arriba del paquete rodam
    from rodam.modelos import Dominio
    import rodam.conf as conf


.. parsed-literal::

    /Users/jaumaf/.devs


Configurando la sesion
----------------------

.. code:: ipython3

    Dominio.Base.metadata.drop_all(conf.ACEPTACION_ENG)

Probemos que no haya datos:

.. code:: ipython3

    !sqlite3 -header -column rodam/aceptacion.db '.schema' # no debe retornar nada

.. code:: ipython3

    
    conf.Base.metadata.create_all(conf.ACEPTACION_ENG)
    session = conf.sessionmaker(bind=conf.ACEPTACION_ENG)

.. code:: ipython3

    sesion = session()

Inventario
==========

Los objetos del Inventario son dependencias de los demás. Creemos,
entonces, los objetos del inventario:

.. code:: ipython3

    #ciudades
    
    bogota = Dominio.Ciudad(
    id_ciudad = 1,
    nom_ciudad = "Bogotá",
        indicativo = 1
    )
    
    medellin = Dominio.Ciudad(
    nom_ciudad = "Medellín",
    indicativo = 4,
    id_ciudad = 2)
    
    # sectores
    
    farmaceutico = Dominio.Sector(
        id_sector = 1,
        nom_sector = "Farmaceutico"
    )
    
    cosmetico = Dominio.Sector(
    id_sector = 2,
    nom_sector = "Cosmético")
    
    # origenes
    
    prod_terminado = Dominio.Origen(
    nom_origen = "Producto terminado",
    id_origen = 1
    )
    
    muestreo_planta = Dominio.Origen(
    nom_origen = "Muestreo en planta",
        id_origen = 2
    )
    
    # empresas
    conalcos = Dominio.Empresa(
    id_empresa = 1,
    nit_empresa = 90024,
    nom_empresa = "Compañía Nacional de Cosméticos CONALCOS",
    id_ciudad = bogota.id_ciudad,
    pagina = "conalcos.com.co",
    correo = "contacto@conalco.com.co",
    direccion = "calle 34 Bis 39-33",
    )
    
    remo = Dominio.Empresa(
    id_empresa = 2,
    nit_empresa = 90025,
    nom_empresa = "Laboratorios REMO S.A.S",
    id_ciudad = medellin.id_ciudad,
    pagina = "labremo.com.co",
    correo = "contacto@labremo.com.co",
    direccion = "calle 54 11-22",
    ) 
    
    #  clientes 
    conalcos_cliente = Dominio.Cliente(
    id_cliente = 1,
    id_empresa = conalcos.id_empresa,
    retencion = 0.14,
    IVA = 0.15, 
    ISA = 0.16,
    ICA = 0.17,    
    )
    
    remo_cliente = Dominio.Cliente(
    id_cliente = 2,
    id_empresa = remo.id_empresa,
    retencion = 0.14,
    IVA = 0.15,
    ISA = 0.16,
    ICA = 0.17)
    
    # cargos
    
    jefe_laboratorio = Dominio.Cargo(
        id_cargo = 1,
        nom_cargo= "Jefe de laboratorio",
        observaciones = "No sabría que poner aquí"
        
    )
    
    jefe_calidad = Dominio.Cargo(
        id_cargo = 2,
        nom_cargo= "Jefe de calidad",
        jefe = jefe_laboratorio.id_cargo,
        reemplazo = jefe_laboratorio.id_cargo,
        observaciones = "No sabría que poner aquí"
        
    )
    
    microbiologo = Dominio.Cargo(
    id_cargo = 3,
    nom_cargo = "Microbiólogo",
    jefe = jefe_calidad.id_cargo,
    observaciones = "No sabría que poner aquí"    
        
    )
    
    # equipos 
    
    cabina = Dominio.Equipo(
    id_equipo = 1,
    nom_equipo = "Cabina de flujo laminar",
    ref_documental = "E001"
    )
    
    micropipeta = Dominio.Equipo(
    id_equipo = 2,
    nom_equipo = "Micropipeta",
    ref_documental = "E019",
    )
    
    balanza = Dominio.Equipo (
    id_equipo = 3,
    nom_equipo = "Balanza",
    ref_documental = "E020",
    )
    
    incubadora = Dominio.Equipo(
    id_equipo = 4, 
        nom_equipo = "Incubadora",
        ref_documental = "E010",
    )
    
    caja_petri = Dominio.Equipo(
    id_equipo = 5, 
        nom_equipo = "Caja de Petri",
        ref_documental = "E011",
    )
    
    turbidimetro = Dominio.Equipo(
    id_equipo = 6, 
        nom_equipo = "Turbidimetro",
        ref_documental = "E012",
    )
    
    # Materiales controlados
    no_aplica = Dominio.MaterialControlado(
    nom_material = "N. A"
    )
    
    
    bacilus = Dominio.MaterialControlado(
    nom_material = "Bacillus subtilis spizizenii ATCC 6633",
    )
    
    pseudomona = Dominio.MaterialControlado(
    nom_material = "Pseudomona aeruginosa ATCC 9027",
    
    )
    
    staph_aureus = Dominio.MaterialControlado(
    nom_material = "Staphylococcus Aureus ATCC 6538",
    
    )
    candida = Dominio.MaterialControlado(
    nom_material = "Candida albicans ATCC 10231",
    )
    
    aspergillus  = Dominio.MaterialControlado(
    nom_material = "Aspergillus bresilensis ATCC 16404",
    
    )
    
    
    inventario = [bogota, medellin, cosmetico, farmaceutico,
                 prod_terminado, muestreo_planta, conalcos,
                 remo, conalcos_cliente, remo_cliente,
                 jefe_laboratorio, jefe_calidad, 
                 cabina, micropipeta, balanza, incubadora, 
                 caja_petri, turbidimetro, no_aplica, bacilus, pseudomona
                 , staph_aureus, candida, aspergillus]

Ahora agreguemos los objetos del inventario y veamos un ejemplo de cómo
se vería una de sus tablas:

.. code:: ipython3

    sesion.add_all(inventario)
    sesion.commit()

.. code:: ipython3

    !sqlite3 -header -column rodam/aceptacion.db 'select * from equipo;' # ejemplo de lo que acabamos de ingresar


.. parsed-literal::

    id_equipo  nom_equipo               ref_documental
    ---------  -----------------------  --------------
    1          Cabina de flujo laminar  E001          
    2          Micropipeta              E019          
    3          Balanza                  E020          
    4          Incubadora               E010          
    5          Caja de Petri            E011          
    6          Turbidimetro             E012          


Creación de Catálogo
====================

Con el inventario listo, ahora realizaremos el proceso de creación del
catálogo. El elemento atómico de un analisis de laboratorio es un
método. Debemos crear primero los métodos existentes en el laboratorio.

.. code:: ipython3

    # metodos 
    
    enriquecimiento = Dominio.Metodo(
          id_metodo = 1,
        nom_metodo = "Enriquecimiento",
        desc_metodo = "5g de producto en 45 de TSB, incubar 24 h a 30-25 grados",
        ref_documental = "IN006",
        observaciones= "",
        material = "Agar TSA" ,
        equipos = [cabina, balanza]
    
    )
    
    siembra_incub =  Dominio.Metodo(
          id_metodo = 2,
        nom_metodo = "Siembra e incubación",
        desc_metodo = "Siembra en superficie: 0.1 ml en TSA, incubar 3 dias a 30-35ºC",
        ref_documental = "IN007",
        observaciones= "",
        material = "Agar Sabouraud",
        equipos = [micropipeta, incubadora]
    
    )
    
    
    conteo_petri =  Dominio.Metodo(
          id_metodo = 3,
        nom_metodo = "Conteo en caja de Petri",
        desc_metodo = "Recuento en caja de petri",
        ref_documental = "IN009",
        observaciones= "",
        material = "Agar TSB",
        equipos = [balanza, caja_petri]
    
    )
    
    diluc_neutralizacion = Dominio.Metodo(
          id_metodo = 4,
        nom_metodo = "Dilución - neutralización",
        desc_metodo = "8 ml de producto (o solucion del producto) durante 1 minuto",
        ref_documental = "IN010",
        observaciones= "",
        material = "Caldo caseina",
        equipos = [balanza]  
    
    )
    
    inoculo = Dominio.Metodo(
        id_metodo= 5,
        nom_metodo = "Inóculo de material controlado",
        ref_documental = "IN011",
        observaciones = "",
        material = "Solución salina",
        equipos = [turbidimetro]
    )
    
    
    
    
    enriq_peptona = Dominio.Metodo(
    id_metodo = 8, 
    nom_metodo = "Enriquecimiento + Peptona",
    desc_metodo = "5 ml de Buffer Peptona + 45 ml de TSB, incubar 24 h a 30-35 C",
    material = "Agar TSB",
    ref_documental = "IN014"
    )
    
    
    diluc_neut5 = Dominio.Metodo(
          id_metodo = 9,
        nom_metodo = "Dilución - neutralización 5 min",
        desc_metodo = "8 ml de producto (o solucion del producto) durante 5 minutos",
        ref_documental = "IN015",
        observaciones= "",
        material = "Caldo caseina",
        equipos = [balanza]  
    
    )
    diluc_neut15 = Dominio.Metodo(
          id_metodo = 10,
        nom_metodo = "Dilución - neutralización 15 min",
        desc_metodo = "8 ml de producto (o solucion del producto) durante 15 minutos",
        ref_documental = "IN016",
        observaciones= "",
        material = "Caldo caseina",
        equipos = [balanza]  
    
    )
    
    diluc_neut30 = Dominio.Metodo(
          id_metodo = 11,
        nom_metodo = "Dilución - neutralización 30 min",
        desc_metodo = "8 ml de producto (o solucion del producto) durante 30 minutos",
        ref_documental = "IN017",
        observaciones= "",
        material = "Caldo caseina",
        equipos = [balanza]  
    
    )
    
    diluc_neut45 = Dominio.Metodo(
          id_metodo = 12,
        nom_metodo = "Dilución - neutralización 45 min",
        desc_metodo = "8 ml de producto (o solucion del producto) durante 45 minutos",
        ref_documental = "IN018",
        observaciones= "",
        material = "Caldo caseina",
        equipos = [balanza]  
    
    )
    
    
    metodos = [enriquecimiento, siembra_incub, conteo_petri, diluc_neutralizacion,
              inoculo, enriq_peptona, diluc_neut5, diluc_neut15, diluc_neut30, diluc_neut45]

.. code:: ipython3

    sesion.add_all(metodos)

.. code:: ipython3

    sesion.commit()

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db 'select nom_metodo, material, ref_documental from metodo;' # lo que acabamos de ingresar


.. parsed-literal::

    |            nom_metodo            |    material     | ref_documental |
    |----------------------------------|-----------------|----------------|
    | Enriquecimiento                  | Agar TSA        | IN006          |
    | Siembra e incubación             | Agar Sabouraud  | IN007          |
    | Conteo en caja de Petri          | Agar TSB        | IN009          |
    | Dilución - neutralización        | Caldo caseina   | IN010          |
    | Inóculo de material controlado   | Solución salina | IN011          |
    | Enriquecimiento + Peptona        | Agar TSB        | IN014          |
    | Dilución - neutralización 5 min  | Caldo caseina   | IN015          |
    | Dilución - neutralización 15 min | Caldo caseina   | IN016          |
    | Dilución - neutralización 30 min | Caldo caseina   | IN017          |
    | Dilución - neutralización 45 min | Caldo caseina   | IN018          |


Creación de análisis
--------------------

Los analisis tienen muchos métodos. Así que podremos simplemente
agregarlos al atributo ``metodos`` correspondiente:

.. code:: ipython3

    # Analisis
    
    
    meso_aerob = Dominio.Analisis(
    id_analisis = 1,
    nom_analisis = "Recuento de Mesofilos Aeorobios",
    id_sector = farmaceutico.id_sector,
    ref_documental= "PR001",
    )
    
    
    # asociaciones 
    util1 = Dominio.Utiliza(
    id_utiliza = 1,
    metodo  = enriquecimiento
    )
    
    util2 = Dominio.Utiliza(
    id_utiliza = 2,
    metodo = siembra_incub,
    
    )
    
    util3= Dominio.Utiliza(
    id_utiliza = 3,
    metodo = conteo_petri)
    
    meso_aerob.metodos= [util1,util2, util3]
    


.. code:: ipython3

    sesion.add(meso_aerob)

.. code:: ipython3

    sesion.commit()

La asociación entre ``analisis`` y ``metodo`` queda registrada en la
tabla ``utiliza``

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db 'select * from utiliza;' # lo que acabamos de ingresar


.. parsed-literal::

    | id_utiliza | id_analisis | id_metodo |
    |------------|-------------|-----------|
    | 1          | 1           | 1         |
    | 2          | 1           | 2         |
    | 3          | 1           | 3         |


.. code:: ipython3

    
    # hongos y levaduras
    
    hongos_lev =  Dominio.Analisis(
        id_analisis = 2,
    nom_analisis = "Recuento de Hongos y Levaduras",
    id_sector = farmaceutico.id_sector,
    ref_documental= "PR002",
    
    )
    
    util4 =  Dominio.Utiliza(
    id_utiliza = 4,
    metodo = enriquecimiento
    )
    
    
    util5  = Dominio.Utiliza(
    id_utiliza = 5,
    metodo  = siembra_incub
    )
    
    
    util6 = Dominio.Utiliza(
    id_utiliza = 6,
    metodo  = conteo_petri
    )
    
    hongos_lev.metodos = [util4, util5, util6]
    


.. code:: ipython3

    sesion.add(hongos_lev)
    sesion.commit()

.. code:: ipython3

    # E. Coli
    
    e_coli = Dominio.Analisis(
        id_analisis = 3,
    nom_analisis = "Presencia de E. Choli",
    id_sector = farmaceutico.id_sector,
    ref_documental= "PR003"
    )
    
    
    
    util7 =  Dominio.Utiliza(
    id_utiliza = 7,
    metodo = enriquecimiento
    )
    
    
    util8  = Dominio.Utiliza(
    id_utiliza = 8,
    metodo  = siembra_incub
    )
    
    
    util9 = Dominio.Utiliza(
    id_utiliza = 9,
    metodo  = conteo_petri
    )
    
    e_coli.metodos = [util7, util8, util9]
    
    


.. code:: ipython3

    sesion.add(e_coli)
    sesion.commit()

.. code:: ipython3

    
    
    # Actividad bactericida
    
    a_bactericida = Dominio.Analisis(
    nom_analisis = "Actividad Bactericida Básica",
    id_sector = cosmetico.id_sector,
    ref_documental = "PR004",
          
    )
    
    
    util10 =  Dominio.Utiliza(
    id_utiliza = 10,
    metodo = enriquecimiento
    )
    
    
    util11  = Dominio.Utiliza(
    id_utiliza = 11,
    metodo  = siembra_incub
    )
    
    
    util12 = Dominio.Utiliza(
    id_utiliza = 12,
    metodo  = inoculo
    )
    
    
    util15 = Dominio.Utiliza(
    id_utiliza = 15,
    metodo  = siembra_incub
    )
    
    util16 = Dominio.Utiliza(
    id_utiliza = 16,
    metodo  = conteo_petri
    )
    
    util17 = Dominio.Utiliza(
    id_utiliza = 17, 
    metodo = enriq_peptona)
    
    util18 = Dominio.Utiliza(
    id_utiliza = 18, 
    metodo = diluc_neut5)
    
    
    util20 = Dominio.Utiliza(
    id_utiliza = 20,
    metodo = diluc_neut15)
    
    util20 = Dominio.Utiliza(
    id_utiliza = 21,
    metodo = diluc_neut30)
    
    util21 = Dominio.Utiliza(
    id_utiliza = 22,
    metodo = diluc_neut45)
    
    util22 = Dominio.Utiliza(
    id_utiliza = 23,
    metodo = diluc_neutralizacion)
    
    a_bactericida.metodos = [util10, util11, util12, util15, util16,
                            util17, util18, util20, util21, util22]
    


.. code:: ipython3

    sesion.add(a_bactericida)

.. code:: ipython3

    sesion.commit()

Revisemos la relación ``utiliza`` con la siguiente consulta:

.. code:: sql

   select utiliza.id_utiliza, analisis.nom_analisis, analisis.ref_documental,  metodo.nom_metodo, metodo.ref_documental from utiliza JOIN analisis on utiliza.id_analisis = analisis.id_analisis JOIN metodo on utiliza.id_metodo = metodo.id_metodo;

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db 'select utiliza.id_utiliza, analisis.nom_analisis, analisis.ref_documental,  metodo.nom_metodo, metodo.ref_documental from utiliza JOIN analisis on utiliza.id_analisis = analisis.id_analisis JOIN metodo on utiliza.id_metodo = metodo.id_metodo;'


.. parsed-literal::

    | id_utiliza |          nom_analisis           | ref_documental |            nom_metodo            | ref_documental |
    |------------|---------------------------------|----------------|----------------------------------|----------------|
    | 1          | Recuento de Mesofilos Aeorobios | PR001          | Enriquecimiento                  | IN006          |
    | 2          | Recuento de Mesofilos Aeorobios | PR001          | Siembra e incubación             | IN007          |
    | 3          | Recuento de Mesofilos Aeorobios | PR001          | Conteo en caja de Petri          | IN009          |
    | 4          | Recuento de Hongos y Levaduras  | PR002          | Enriquecimiento                  | IN006          |
    | 5          | Recuento de Hongos y Levaduras  | PR002          | Siembra e incubación             | IN007          |
    | 6          | Recuento de Hongos y Levaduras  | PR002          | Conteo en caja de Petri          | IN009          |
    | 7          | Presencia de E. Choli           | PR003          | Enriquecimiento                  | IN006          |
    | 8          | Presencia de E. Choli           | PR003          | Siembra e incubación             | IN007          |
    | 9          | Presencia de E. Choli           | PR003          | Conteo en caja de Petri          | IN009          |
    | 10         | Actividad Bactericida Básica    | PR004          | Enriquecimiento                  | IN006          |
    | 11         | Actividad Bactericida Básica    | PR004          | Siembra e incubación             | IN007          |
    | 12         | Actividad Bactericida Básica    | PR004          | Inóculo de material controlado   | IN011          |
    | 15         | Actividad Bactericida Básica    | PR004          | Siembra e incubación             | IN007          |
    | 16         | Actividad Bactericida Básica    | PR004          | Conteo en caja de Petri          | IN009          |
    | 17         | Actividad Bactericida Básica    | PR004          | Enriquecimiento + Peptona        | IN014          |
    | 18         | Actividad Bactericida Básica    | PR004          | Dilución - neutralización 5 min  | IN015          |
    | 21         | Actividad Bactericida Básica    | PR004          | Dilución - neutralización 30 min | IN017          |
    | 22         | Actividad Bactericida Básica    | PR004          | Dilución - neutralización 45 min | IN018          |
    | 23         | Actividad Bactericida Básica    | PR004          | Dilución - neutralización        | IN010          |


Creación de Grupos
------------------

Los analisis pueden pertenecer a varios grupos.

.. code:: ipython3

    
    grupo_unico = Dominio.Grupo(
    nom_grupo = "Grupo único",
    desc_grupo = "Para análisis simples que no requieren grupos")
    
    
    recuento_inoc= Dominio.Grupo(
    nom_grupo = "Recuento del inóculo",
    desc_grupo = "Recuento del inóculo para actividad bactericida básica")
    
    toxicidad = Dominio.Grupo(
    nom_grupo = "Control de toxicidad del neutralizante",
    desc_grupo = "Pseudomonas Aeruginosa y staphylococcus Aureus",
    )
    
    control_neutralizacion = Dominio.Grupo(
    nom_grupo = "Control del método de dilución-neutralización",
    )
    
    prueba_dilucion = Dominio.Grupo(
    nom_grupo = "Prueba de dilución - neutralización"
    )
    
    
    # estos analisis quedan asociados al grupo único
    
    agrupa1 = Dominio.Agrupacion(
    id_agrupacion = 1,
    analisis = meso_aerob
    )
    
    agrupa2 = Dominio.Agrupacion(
    id_agrupacion = 2,
    analisis = hongos_lev     
    )
    
    agrupa3 = Dominio.Agrupacion(
    id_agrupacion = 3, 
    analisis = e_coli    
    )
    
    
    grupo_unico.analisis = [agrupa1, agrupa2, agrupa3]
    
    


.. code:: ipython3

    sesion.add(grupo_unico)
    sesion.commit()

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db 'select * from agrupacion'


.. parsed-literal::

    | id_agrupacion | id_grupo | id_analisis |
    |---------------|----------|-------------|
    | 1             | 1        | 1           |
    | 2             | 1        | 2           |
    | 3             | 1        | 3           |


.. code:: ipython3

    # actividad bactericida tiene estos grupos == estos grupos tienen actividad bactericida
    
    agrupa4 = Dominio.Agrupacion(
    id_agrupacion = 4, 
    analisis = a_bactericida
    )
    
    agrupa5 = Dominio.Agrupacion(
    id_agrupacion = 5, 
    analisis = a_bactericida
    )
    
    agrupa6 = Dominio.Agrupacion(
    id_agrupacion = 6,
    analisis = a_bactericida)
    
    agrupa7 = Dominio.Agrupacion(
    id_agrupacion = 7, 
    analisis = a_bactericida    
    )
    
    toxicidad.analisis.append(agrupa4)
    recuento_inoc.analisis.append(agrupa5)
    control_neutralizacion.analisis.append(agrupa6)
    prueba_dilucion.analisis.append(agrupa7)
    
    
    


.. code:: ipython3

    sesion.add_all([toxicidad, recuento_inoc,prueba_dilucion])

.. code:: ipython3

    sesion.commit()

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db 'select grupo.nom_grupo, analisis.nom_analisis from agrupacion join grupo on agrupacion.id_grupo = grupo.id_grupo join analisis on agrupacion.id_analisis =  analisis.id_analisis'


.. parsed-literal::

    |               nom_grupo                |          nom_analisis           |
    |----------------------------------------|---------------------------------|
    | Grupo único                            | Recuento de Mesofilos Aeorobios |
    | Grupo único                            | Recuento de Hongos y Levaduras  |
    | Grupo único                            | Presencia de E. Choli           |
    | Control de toxicidad del neutralizante | Actividad Bactericida Básica    |
    | Recuento del inóculo                   | Actividad Bactericida Básica    |
    | Prueba de dilución - neutralización    | Actividad Bactericida Básica    |


Ingreso de Muestras
===================

Una vez sabemos qué servicios están en nuestro catálogo, podemos empezar
a ingresar productos y a realizar análisis sobre esas muestras.

Ingreso de un producto
----------------------

En **Rodam Análisis S.A.S**, un producto se ingresa una sola vez. A
partir de allí, el producto queda enlazado con una seríe de
especificaciones que indican qué grupos, análisis y métodos deben
correrse sobre una muestra de ese producto.

Luego del ingreso del producto, cada **muestra** de ese producto siempre
tendrá las especificaciones estipuladas para el producto.

Primero empecemos con la creación de un producto:

.. code:: ipython3

    # producto 1
    xinefax = Dominio.Producto(
    id_producto= 1,                    
    nom_producto = "Xinefax" ,           # libre
    forma_farmaceutica = "Emulsión",     # libre
    id_sector = farmaceutico.id_sector,  # dependencia    
    id_cliente = conalcos_cliente.id_cliente
    )
    sesion.add(xinefax)
    sesion.commit()
    
    
    # producto 2
    
    seximax = Dominio.Producto(
    id_producto = 2, 
    nom_producto = "Seximax",
    forma_farmaceutica = "Loción",
    id_sector = cosmetico.id_sector, 
    id_cliente = remo_cliente.id_cliente
    )
    
    sesion.add(seximax)
    sesion.commit()

Ahora debemos indicar qué grupos tendrá el producto.

.. code:: ipython3

    #  El producto debe tener grupos ya existentes en el catálogo
    
    debe1 = Dominio.Debe_tener(
    id_debe_tener = 1,
    grupo = recuento_inoc
    )
    
    debe2 = Dominio.Debe_tener(
    id_debe_tener = 2,
    grupo = toxicidad
    )
    
    
    debe3 = Dominio.Debe_tener(
    id_debe_tener = 3,
    grupo = control_neutralizacion
    
        
    )
    
    debe4 = Dominio.Debe_tener(
    id_debe_tener = 4,
    grupo = prueba_dilucion
    
    )
    
    
    
    xinefax.grupos = [debe1, debe2, debe3, debe4]
    
    debe5 = Dominio.Debe_tener(
    id_debe_tener = 5,
    grupo = grupo_unico
    )
    
    seximax.grupos = [debe5]

.. code:: ipython3

    
    sesion.commit()

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db 'select * from debe_tener;'


.. parsed-literal::

    | id_debe_tener | id_producto | id_grupo |
    |---------------|-------------|----------|
    | 1             | 1           | 3        |
    | 2             | 1           | 2        |
    | 3             | 1           | 5        |
    | 4             | 1           | 4        |
    | 5             | 2           | 1        |


Especificar un producto
-----------------------

Caso complejo : especificar actividad bactericida
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sabemos que ``xinefax`` *debe tener* los grupos estipulados en el
resultado anterior. Pero aún no hemos especificado cuáles de los
analisis disponibles en esos grupos se tienen que correr.

Sin embargo, podemos saber qué analisis estan disponibles dentro de qué
grupo (esto puede ser útil, en una interfaz de usuario):

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db "select agrupacion.id_agrupacion, grupo.nom_grupo, grupo.id_grupo, analisis.nom_analisis, analisis.id_analisis  from agrupacion join grupo on agrupacion.id_grupo = grupo.id_grupo join analisis on agrupacion.id_analisis = analisis.id_analisis"


.. parsed-literal::

    | id_agrupacion |                   nom_grupo                   | id_grupo |          nom_analisis           | id_analisis |
    |---------------|-----------------------------------------------|----------|---------------------------------|-------------|
    | 1             | Grupo único                                   | 1        | Recuento de Mesofilos Aeorobios | 1           |
    | 2             | Grupo único                                   | 1        | Recuento de Hongos y Levaduras  | 2           |
    | 3             | Grupo único                                   | 1        | Presencia de E. Choli           | 3           |
    | 4             | Control de toxicidad del neutralizante        | 2        | Actividad Bactericida Básica    | 4           |
    | 5             | Recuento del inóculo                          | 3        | Actividad Bactericida Básica    | 4           |
    | 7             | Prueba de dilución - neutralización           | 4        | Actividad Bactericida Básica    | 4           |
    | 6             | Control del método de dilución-neutralización | 5        | Actividad Bactericida Básica    | 4           |


Tambien necesitaremos especificar qué metodos para qué analisis.
Entonces debemos buscar:

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db "select id_utiliza, id_analisis, metodo.nom_metodo, utiliza.id_metodo, metodo.ref_documental from utiliza join metodo on utiliza.id_metodo = metodo.id_metodo"


.. parsed-literal::

    | id_utiliza | id_analisis |            nom_metodo            | id_metodo | ref_documental |
    |------------|-------------|----------------------------------|-----------|----------------|
    | 1          | 1           | Enriquecimiento                  | 1         | IN006          |
    | 2          | 1           | Siembra e incubación             | 2         | IN007          |
    | 3          | 1           | Conteo en caja de Petri          | 3         | IN009          |
    | 4          | 2           | Enriquecimiento                  | 1         | IN006          |
    | 5          | 2           | Siembra e incubación             | 2         | IN007          |
    | 6          | 2           | Conteo en caja de Petri          | 3         | IN009          |
    | 7          | 3           | Enriquecimiento                  | 1         | IN006          |
    | 8          | 3           | Siembra e incubación             | 2         | IN007          |
    | 9          | 3           | Conteo en caja de Petri          | 3         | IN009          |
    | 10         | 4           | Enriquecimiento                  | 1         | IN006          |
    | 11         | 4           | Siembra e incubación             | 2         | IN007          |
    | 12         | 4           | Inóculo de material controlado   | 5         | IN011          |
    | 15         | 4           | Siembra e incubación             | 2         | IN007          |
    | 16         | 4           | Conteo en caja de Petri          | 3         | IN009          |
    | 17         | 4           | Enriquecimiento + Peptona        | 8         | IN014          |
    | 18         | 4           | Dilución - neutralización 5 min  | 9         | IN015          |
    | 21         | 4           | Dilución - neutralización 30 min | 11        | IN017          |
    | 22         | 4           | Dilución - neutralización 45 min | 12        | IN018          |
    | 23         | 4           | Dilución - neutralización        | 4         | IN010          |


Para este producto, hemos decidido que

Para el *recuento del inoculo* queremos: - inoculo \*Stafilococcus,

-  inoculo de *Pseudomona*.

-  siembra e incubacion para cada uno

-  conteo en caja de petri para cada uno

Para *Control de toxicidad de nautralizante*:

-  queremos nuestro enriquecimento + peptona

-  inoculo de *Stafilococcus*

-  Inoculo de *pseudomona*

-  siembra e incubacion para cada uno

-  conteo en caja de petri para cada uno

Para *Control del método de dilución - neutralización* queremos: -
nuestro enriquecimiento común

-  nuestro inoculos para *Pseudomona* y *Stafilococcus*

-  siembra e incubacion para cada uno

-  recuento en caja de petri para cada uno

Para la *prueba de dilución* queremos correr todos los metodos de
dilución :

-  IN015- IN018 para cada cepa

-  nuestro enriquecimiento TSB

-  siembra incubacion para cada uno

-  Conteo en caja de Petri para cada uno

.. code:: ipython3

    # Creamos las especificaciones 
    
    ## Recuento 
    
    # stafiloccocus e
    recuento_inoc1 = Dominio.Especificacion(
    id_debe_tener = 1,
    id_utiliza = 12,
    id_material_controlado = 4 ,   
    valor = "170<t<230 " 
    )
    
    # Pseudomona en recuento
    recuento_inoc2 = Dominio.Especificacion(
    id_debe_tener = 1,
    id_utiliza = 12,
    id_material_controlado = 3,
    valor = "170<t<230 " 
    )
    
    # Siembra
    recuento_inoc3 = Dominio.Especificacion(
    id_debe_tener = 1,
    id_utiliza = 15,
    id_material_controlado = 4,
    valor = "<200 ufc"
    )
    
    recuento_inoc4 = Dominio.Especificacion(
    id_debe_tener = 1,
    id_utiliza = 15,
    id_material_controlado = 3,
    valor = "<200 ufc"
    )
    
    
    # petri
    
    recuento_inoc5 = Dominio.Especificacion(
    id_debe_tener = 1,
    id_utiliza = 16,
    id_material_controlado = 4,
    valor = "<200 ufc"
    )
    
    recuento_inoc6 = Dominio.Especificacion(
    id_debe_tener = 1,
    id_utiliza = 16,
    id_material_controlado = 3,
    valor = "<200 ufc"
    )
    
    recuento = [recuento_inoc1, recuento_inoc2, recuento_inoc3, recuento_inoc4, recuento_inoc5, recuento_inoc6]
    
    
    ## Control de toxicidad
    # peptona
    control_toxicidad1 = Dominio.Especificacion(
    id_debe_tener= 2,
    id_utiliza = 17,
    valor = "<100 ufc",
    id_material_controlado = 4,
    )
    
    control_toxicidad1_2 = Dominio.Especificacion(
    id_debe_tener= 2,
    id_utiliza = 17,
    valor = "<100 ufc",
    id_material_controlado = 3,
    )
    # staph
    control_toxicidad2 = Dominio.Especificacion(
    id_debe_tener= 2,
    id_utiliza = 14,
    id_material_controlado = 4,
    valor = "170<t<230"   
    )
    
    # pseudo
    control_toxicidad3 = Dominio.Especificacion(
    id_debe_tener= 2,
    id_utiliza = 13,
    id_material_controlado = 3,
    valor = "170<t<230" 
    )
    
    # siembra
    control_toxicidad4 = Dominio.Especificacion(
    id_debe_tener= 2,
    id_utiliza = 15,
    id_material_controlado = 4,
    valor  = "<100"
    )
    
    control_toxicidad4_2 = Dominio.Especificacion(
    id_debe_tener= 2,
    id_utiliza = 15,
    id_material_controlado = 3,
    valor  = "<100"
    )
    
    # petri 
    control_toxicidad5 = Dominio.Especificacion(
    id_debe_tener= 2,
    id_utiliza = 16,
    valor = "<130 ufc",
    id_material_controlado = 4,
    )
    
    control_toxicidad5_2 = Dominio.Especificacion(
    id_debe_tener= 2,
    id_utiliza = 16,
    valor = "<130 ufc",
    id_material_controlado = 3,
    )
    
    control_toxicidad = [control_toxicidad1,
                         control_toxicidad1_2,
                        control_toxicidad2,
                        control_toxicidad3,
                        control_toxicidad4,
                         control_toxicidad4_2,
                        control_toxicidad5,
                        control_toxicidad5_2]
    
    ## Prueba dilucion
    
    prueba_dilucion1 = Dominio.Especificacion(
    id_debe_tener = 4, 
    id_utiliza = 18,
    valor = "tiempo de exposicion"   
    )
    prueba_dilucion2 = Dominio.Especificacion(
    id_debe_tener = 4, 
    id_utiliza = 21,
    valor = "tiempo de exposicion" 
    )
    prueba_dilucion3 = Dominio.Especificacion(
    id_debe_tener = 4, 
    id_utiliza = 22,
    valor = "tiempo de exposicion" 
    )
    
    
    prueba_dilucion = [prueba_dilucion1,
                     prueba_dilucion2,
                     prueba_dilucion3]
    
    
    ## Control de dilucion
    
    # enriq nomral
    control_dilucion1 = Dominio.Especificacion(
    id_debe_tener = 3, 
    id_utiliza = 10,
    id_material_controlado = 4,
    valor = "<150 ufc" 
    )
    
    control_dilucion1_2 = Dominio.Especificacion(
    id_debe_tener = 3, 
    id_utiliza = 10,
    id_material_controlado = 3,
    valor = "<150 ufc" 
    )
    
    
    
    
    #staph
    control_dilucion2 = Dominio.Especificacion(
    id_debe_tener = 3, 
    id_utiliza = 13,
    id_material_controlado = 4,
    valor = "170<t<230")
    
    # pseudo 
    control_dilucion3 = Dominio.Especificacion(
    id_debe_tener = 3, 
    id_utiliza = 14,
    id_material_controlado = 3,
    valor = "170<t<230"
    )
    
    # siembra
    control_dilucion4 = Dominio.Especificacion(
    id_debe_tener = 3, 
    id_utiliza = 15,
    id_material_controlado = 4,
    valor = "< 120 ufc"
    )
    
    control_dilucion4_2 = Dominio.Especificacion(
    id_debe_tener = 3, 
    id_utiliza = 15,
    id_material_controlado = 3,
    valor = "< 120 ufc"
    )
        
        
    # petri
    control_dilucion5 = Dominio.Especificacion(
    id_debe_tener = 3, 
    id_utiliza = 16,
    id_material_controlado = 4,
    valor = "<230 ufc"
    )
    
    control_dilucion5_2 = Dominio.Especificacion(
    id_debe_tener = 3, 
    id_utiliza = 16,
    id_material_controlado = 3,
    valor = "<230 ufc"
    )
    
    control_dilucion = [control_dilucion1,
                        control_dilucion1_2,
                       control_dilucion2,
                       control_dilucion3,
                       control_dilucion4,
                        control_dilucion4_2,
                       control_dilucion5,
                       control_dilucion5_2]
    


.. code:: ipython3

    # agregamos cada grupo de especificaciones
    
    sesion.add_all(recuento)
    sesion.add_all(control_toxicidad)
    sesion.add_all(prueba_dilucion)
    sesion.add_all(control_dilucion)

.. code:: ipython3

    
    sesion.commit()

Caso simple: recuento de mesofilos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    espec_2_1 = Dominio.Especificacion(
    id_debe_tener = debe5.id_debe_tener,
    id_utiliza = 1,      # Aquí no aplica el material controlado porque  
    valor = "< 140 ufc"  # mesofilos son muchos. Se puede dejar en blanco
    )
    
    espec_2_2 =  Dominio.Especificacion(
    id_debe_tener = debe5.id_debe_tener,
    id_utiliza = 2,
    valor = "< 145 ufc"
    )
    
    espec_2_3 = Dominio.Especificacion(
    id_debe_tener = debe5.id_debe_tener,
    id_utiliza = 3,
    valor = "< 150 ufc"
    )


.. code:: ipython3

    sesion.add_all([espec_2_1, espec_2_2, espec_2_3])

.. code:: ipython3

    sesion.commit()

Esta vista resume los datos relevantes para especificaciones:

.. code:: ipython3

    !sqlite3  -header -markdown rodam/aceptacion.db 'select * from especificaciones_con_nombres'


.. parsed-literal::

    | nom_producto |                   nom_grupo                   |          nom_analisis           |            nom_metodo            |    material     |       material_controlado       |        valor         |
    |--------------|-----------------------------------------------|---------------------------------|----------------------------------|-----------------|---------------------------------|----------------------|
    | Xinefax      | Recuento del inóculo                          | Actividad Bactericida Básica    | Inóculo de material controlado   | Solución salina | Staphylococcus Aureus ATCC 6538 | 170<t<230            |
    | Xinefax      | Recuento del inóculo                          | Actividad Bactericida Básica    | Inóculo de material controlado   | Solución salina | Pseudomona aeruginosa ATCC 9027 | 170<t<230            |
    | Xinefax      | Recuento del inóculo                          | Actividad Bactericida Básica    | Siembra e incubación             | Agar Sabouraud  | Staphylococcus Aureus ATCC 6538 | <200 ufc             |
    | Xinefax      | Recuento del inóculo                          | Actividad Bactericida Básica    | Siembra e incubación             | Agar Sabouraud  | Pseudomona aeruginosa ATCC 9027 | <200 ufc             |
    | Xinefax      | Recuento del inóculo                          | Actividad Bactericida Básica    | Conteo en caja de Petri          | Agar TSB        | Staphylococcus Aureus ATCC 6538 | <200 ufc             |
    | Xinefax      | Recuento del inóculo                          | Actividad Bactericida Básica    | Conteo en caja de Petri          | Agar TSB        | Pseudomona aeruginosa ATCC 9027 | <200 ufc             |
    | Xinefax      | Control de toxicidad del neutralizante        | Actividad Bactericida Básica    | Enriquecimiento + Peptona        | Agar TSB        | Staphylococcus Aureus ATCC 6538 | <100 ufc             |
    | Xinefax      | Control de toxicidad del neutralizante        | Actividad Bactericida Básica    | Enriquecimiento + Peptona        | Agar TSB        | Pseudomona aeruginosa ATCC 9027 | <100 ufc             |
    | Xinefax      | Control de toxicidad del neutralizante        | Actividad Bactericida Básica    | Siembra e incubación             | Agar Sabouraud  | Staphylococcus Aureus ATCC 6538 | <100                 |
    | Xinefax      | Control de toxicidad del neutralizante        | Actividad Bactericida Básica    | Siembra e incubación             | Agar Sabouraud  | Pseudomona aeruginosa ATCC 9027 | <100                 |
    | Xinefax      | Control de toxicidad del neutralizante        | Actividad Bactericida Básica    | Conteo en caja de Petri          | Agar TSB        | Staphylococcus Aureus ATCC 6538 | <130 ufc             |
    | Xinefax      | Control de toxicidad del neutralizante        | Actividad Bactericida Básica    | Conteo en caja de Petri          | Agar TSB        | Pseudomona aeruginosa ATCC 9027 | <130 ufc             |
    | Xinefax      | Prueba de dilución - neutralización           | Actividad Bactericida Básica    | Dilución - neutralización 5 min  | Caldo caseina   | N. A                            | tiempo de exposicion |
    | Xinefax      | Prueba de dilución - neutralización           | Actividad Bactericida Básica    | Dilución - neutralización 30 min | Caldo caseina   | N. A                            | tiempo de exposicion |
    | Xinefax      | Prueba de dilución - neutralización           | Actividad Bactericida Básica    | Dilución - neutralización 45 min | Caldo caseina   | N. A                            | tiempo de exposicion |
    | Xinefax      | Control del método de dilución-neutralización | Actividad Bactericida Básica    | Enriquecimiento                  | Agar TSA        | Staphylococcus Aureus ATCC 6538 | <150 ufc             |
    | Xinefax      | Control del método de dilución-neutralización | Actividad Bactericida Básica    | Enriquecimiento                  | Agar TSA        | Pseudomona aeruginosa ATCC 9027 | <150 ufc             |
    | Xinefax      | Control del método de dilución-neutralización | Actividad Bactericida Básica    | Siembra e incubación             | Agar Sabouraud  | Staphylococcus Aureus ATCC 6538 | < 120 ufc            |
    | Xinefax      | Control del método de dilución-neutralización | Actividad Bactericida Básica    | Siembra e incubación             | Agar Sabouraud  | Pseudomona aeruginosa ATCC 9027 | < 120 ufc            |
    | Xinefax      | Control del método de dilución-neutralización | Actividad Bactericida Básica    | Conteo en caja de Petri          | Agar TSB        | Staphylococcus Aureus ATCC 6538 | <230 ufc             |
    | Xinefax      | Control del método de dilución-neutralización | Actividad Bactericida Básica    | Conteo en caja de Petri          | Agar TSB        | Pseudomona aeruginosa ATCC 9027 | <230 ufc             |
    | Seximax      | Grupo único                                   | Recuento de Mesofilos Aeorobios | Enriquecimiento                  | Agar TSA        | N. A                            | < 140 ufc            |
    | Seximax      | Grupo único                                   | Recuento de Mesofilos Aeorobios | Siembra e incubación             | Agar Sabouraud  | N. A                            | < 145 ufc            |
    | Seximax      | Grupo único                                   | Recuento de Mesofilos Aeorobios | Conteo en caja de Petri          | Agar TSB        | N. A                            | < 150 ufc            |


Ingreso de una muestra
----------------------

Una vez ingresado el ``xinefax``, con sus respectivas especificaciones,
se puede ahora ingresar una *muestra* de ese producto. Un producto podra
tener muchas muestras, pero como las especificaciones están asociadas al
producto, no se tendrá que repetir el proceso de especificación.

.. code:: ipython3

    
    # Creo que en el proceso de laboratorio alguien es responsable del ingreso de la muestra
    # Voy a inventar a alguien por el momento que quede asociado al ingreso de muestra.
    
    ernesto_segura = Dominio.MiembroRodam(
    id_miembro = 3,
    nom_miembro = "Ernesto Segura",
    id_cargo = jefe_calidad.id_cargo)
    
    
    muestra = Dominio.Muestra(
    id_muestra = 1,
    id_producto = xinefax.id_producto,
    id_origen = muestreo_planta.id_origen,
    presentacion = 'tabletas',
    lote_muestra = "12345",
    tamano_muestra= 500,
    unidades_tamano = "mg",
    registra = ernesto_segura.id_miembro
        
    )

.. code:: ipython3

    sesion.add(ernesto_segura)
    sesion.add(muestra)
    sesion.commit()

.. code:: ipython3

    !sqlite3 -header -column rodam/aceptacion.db 'select id_muestra as id, id_producto as prod, id_origen as orig, presentacion as pres, lote_muestra as lote, tamano_muestra as tamaño, ingreso_muestra as ingreso, registra from muestra;'


.. parsed-literal::

    id  prod  orig  pres      lote   tamaño  ingreso                     registra
    --  ----  ----  --------  -----  ------  --------------------------  --------
    1   1     2     tabletas  12345  500     2021-02-02 16:42:05.599979  3       


Ingreso de lectura
------------------

Viendo las especificaciones del ``xinefax``, el microbiólogo ha corrido
cuidadosamente cada uno de los métodos de laboratorio asociados a ese
producto. Es hora, entonces,de crear una lectura. Para ingresar una
lectura, necesitamos ser un MiembroRodam. Primero creemoslo.

.. code:: ipython3

    yuli_largo = Dominio.MiembroRodam(
    id_miembro = 1,
    nom_miembro = "Yuli Largo",
    id_cargo = microbiologo.id_cargo
    )
    
    daniel_arias = Dominio.MiembroRodam(
    id_miembro= 2,
    nom_miembro = "Daniel Arias",
    id_cargo = jefe_laboratorio.id_cargo )
    


.. code:: ipython3

    
    sesion.add_all([yuli_largo, daniel_arias])
    sesion.commit()

.. code:: ipython3

    !sqlite3 -header -column rodam/aceptacion.db 'select * from miembro_rodam;'


.. parsed-literal::

    id_miembro  nom_miembro     id_cargo  ingreso  salida
    ----------  --------------  --------  -------  ------
    1           Yuli Largo      3                        
    2           Daniel Arias    1                        
    3           Ernesto Segura  2                        


.. code:: ipython3

    # cuántas especificaciones hay?
    
    !sqlite3 rodam/aceptacion.db 'select count(*) from especificacion'


.. parsed-literal::

    28


Vemos que la remisión del producto es bastante extensa. Para este
ejemplo, solo recolectaremos la lectura de *algunas* de las
especificaciones.

.. code:: ipython3

    
    lectura1 = Dominio.Lectura(
    id_muestra = muestra.id_muestra,
    id_especificacion = 1,
    valor_lectura = "112 ufc",
    lote_medio = "M314-20",
    registra = yuli_largo.id_miembro,
    verifica = daniel_arias.id_miembro,
    concepto = False
    )
    
    lectura2 = Dominio.Lectura(
    id_muestra = muestra.id_muestra,
    id_especificacion = 2,
    valor_lectura = "211 ufc",
    registra = yuli_largo.id_miembro,
    verifica = daniel_arias.id_miembro,
    lote_medio = "M315-20",
        concepto = False
    
    )
    lectura3 = Dominio.Lectura(
    id_muestra = muestra.id_muestra,   
    id_especificacion = 3,
    valor_lectura = "211 ufc",
    registra = yuli_largo.id_miembro,
    verifica = daniel_arias.id_miembro,
    lote_medio = "M316-20",
    concepto = False
    )
    
    lectura4 = Dominio.Lectura(
    id_muestra = muestra.id_muestra,   
    id_especificacion = 4,
    valor_lectura = "211 ufc",
    registra = yuli_largo.id_miembro,
    verifica = daniel_arias.id_miembro,
    lote_medio = "M316-20",
    concepto = False
    )
    lectura5 = Dominio.Lectura(
    id_muestra = muestra.id_muestra,   
    id_especificacion = 5,
    valor_lectura = "211 ufc",
    registra = yuli_largo.id_miembro,
    verifica = daniel_arias.id_miembro,
    lote_medio = "M316-20",
    concepto = False)
        
    lectura6 = Dominio.Lectura(
    id_muestra = muestra.id_muestra,   
    id_especificacion = 6,
    valor_lectura = "211 ufc",
    registra = yuli_largo.id_miembro,
    verifica = daniel_arias.id_miembro,
    lote_medio = "M316-20",
    concepto = False)
    
    lectura7 = Dominio.Lectura(
    id_muestra = muestra.id_muestra,   
    id_especificacion = 7 ,
    valor_lectura = "211 ufc",
    registra = yuli_largo.id_miembro,
    verifica = daniel_arias.id_miembro,
    lote_medio = "M316-20",
    concepto = False)
    
    # Para control de los medios
    lectura18 = Dominio.Lectura(
    id_muestra = muestra.id_muestra,
    id_especificacion = 18,
    valor_lectura = "211 ufc",
    lote_medio = "M341-22",
    registra = yuli_largo.id_miembro,
    verifica = daniel_arias.id_miembro,
    concepto = True 
    )
    
    lecturas = [lectura1, lectura2, lectura3, lectura4, lectura5, lectura6, lectura7, lectura18]

.. code:: ipython3

    sesion.add_all(lecturas)

.. code:: ipython3

    sesion.commit()


.. code:: ipython3

    !sqlite3 -header -column rodam/aceptacion.db 'select * from lectura;'


.. parsed-literal::

    id_lectura  id_especificacion  id_muestra  valor_lectura  fecha_lectura               lote_medio  registra  verifica  concepto  observaciones
    ----------  -----------------  ----------  -------------  --------------------------  ----------  --------  --------  --------  -------------
    1           1                  1           112 ufc        2021-02-02 16:42:06.181797  M314-20     1         2         0                      
    2           2                  1           211 ufc        2021-02-02 16:42:06.183285  M315-20     1         2         0                      
    3           3                  1           211 ufc        2021-02-02 16:42:06.183608  M316-20     1         2         0                      
    4           4                  1           211 ufc        2021-02-02 16:42:06.183816  M316-20     1         2         0                      
    5           5                  1           211 ufc        2021-02-02 16:42:06.184012  M316-20     1         2         0                      
    6           6                  1           211 ufc        2021-02-02 16:42:06.184231  M316-20     1         2         0                      
    7           7                  1           211 ufc        2021-02-02 16:42:06.184489  M316-20     1         2         0                      
    8           18                 1           211 ufc        2021-02-02 16:42:06.184865  M341-22     1         2         1                      


Unamos las lecturas con las especificaciones para obtener un resumen del
analisis

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db "select * from  especificacion, lectura where lectura.id_especificacion   = especificacion.id_especificacion"


.. parsed-literal::

    | id_especificacion | id_debe_tener | id_utiliza | id_material_controlado |   valor    | id_lectura | id_especificacion | id_muestra | valor_lectura |       fecha_lectura        | lote_medio | registra | verifica | concepto | observaciones |
    |-------------------|---------------|------------|------------------------|------------|------------|-------------------|------------|---------------|----------------------------|------------|----------|----------|----------|---------------|
    | 1                 | 1             | 12         | 4                      | 170<t<230  | 1          | 1                 | 1          | 112 ufc       | 2021-02-02 16:42:06.181797 | M314-20    | 1        | 2        | 0        |               |
    | 2                 | 1             | 12         | 3                      | 170<t<230  | 2          | 2                 | 1          | 211 ufc       | 2021-02-02 16:42:06.183285 | M315-20    | 1        | 2        | 0        |               |
    | 3                 | 1             | 15         | 4                      | <200 ufc   | 3          | 3                 | 1          | 211 ufc       | 2021-02-02 16:42:06.183608 | M316-20    | 1        | 2        | 0        |               |
    | 4                 | 1             | 15         | 3                      | <200 ufc   | 4          | 4                 | 1          | 211 ufc       | 2021-02-02 16:42:06.183816 | M316-20    | 1        | 2        | 0        |               |
    | 5                 | 1             | 16         | 4                      | <200 ufc   | 5          | 5                 | 1          | 211 ufc       | 2021-02-02 16:42:06.184012 | M316-20    | 1        | 2        | 0        |               |
    | 6                 | 1             | 16         | 3                      | <200 ufc   | 6          | 6                 | 1          | 211 ufc       | 2021-02-02 16:42:06.184231 | M316-20    | 1        | 2        | 0        |               |
    | 7                 | 2             | 17         | 4                      | <100 ufc   | 7          | 7                 | 1          | 211 ufc       | 2021-02-02 16:42:06.184489 | M316-20    | 1        | 2        | 0        |               |
    | 18                | 3             | 10         | 4                      | <150 ufc   | 8          | 18                | 1          | 211 ufc       | 2021-02-02 16:42:06.184865 | M341-22    | 1        | 2        | 1        |               |




Podemos revisar los datos más relevantes de la lectura con la vista:

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db "select * from lectura_con_nombres;"


.. parsed-literal::

    | nom_producto | id_muestra |                   nom_grupo                   |         nom_analisis         |           nom_metodo           |          nom_material           | especificacion | resultado |    material     | lote_medio | registra | verifica | concepto |
    |--------------|------------|-----------------------------------------------|------------------------------|--------------------------------|---------------------------------|----------------|-----------|-----------------|------------|----------|----------|----------|
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Inóculo de material controlado | Staphylococcus Aureus ATCC 6538 | 170<t<230      | 112 ufc   | Solución salina | M314-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Inóculo de material controlado | Pseudomona aeruginosa ATCC 9027 | 170<t<230      | 211 ufc   | Solución salina | M315-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Siembra e incubación           | Staphylococcus Aureus ATCC 6538 | <200 ufc       | 211 ufc   | Agar Sabouraud  | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Siembra e incubación           | Pseudomona aeruginosa ATCC 9027 | <200 ufc       | 211 ufc   | Agar Sabouraud  | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Conteo en caja de Petri        | Staphylococcus Aureus ATCC 6538 | <200 ufc       | 211 ufc   | Agar TSB        | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Conteo en caja de Petri        | Pseudomona aeruginosa ATCC 9027 | <200 ufc       | 211 ufc   | Agar TSB        | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Control de toxicidad del neutralizante        | Actividad Bactericida Básica | Enriquecimiento + Peptona      | Staphylococcus Aureus ATCC 6538 | <100 ufc       | 211 ufc   | Agar TSB        | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Control del método de dilución-neutralización | Actividad Bactericida Básica | Enriquecimiento                | Staphylococcus Aureus ATCC 6538 | <150 ufc       | 211 ufc   | Agar TSA        | M341-22    | 1        | 2        | 1        |





Control de calidad de los medios
================================

El control de calidad se debe asociar a una muestra. En esa muestra,
tendríamos que ver qué medios son suceptibles al control de calidad, y
realizar varios controles por cada medio. En este caso, observamos que
el Agar TSA del necesita un control de calidad del medio. Haremos el
ejemplo con el lote ``M341-22``, teniendo en mente que cada uno de los
lotes implicados en una muestra tendríanque pasar por control del medio:

.. code:: ipython3

    # lectura 15 (Enriquecimiento normal - medio TSA)
    
    control_medio1 = Dominio.Control_Material(
    lote_material = "M341-22",
    id_material_controlado = bacilus.id_material,
    lote_material_controlado = "486-862-5-a10-4",
    especificacion = "Entre 50 y 150 ufc",
    resultado = "98 ufc",
    concepto = True
    )
    
    control_medio2 = Dominio.Control_Material(
    lote_material = "M341-22",
    id_material_controlado = pseudomona.id_material,
    lote_material_controlado = "484-862-5-a10-4",
    especificacion = "Entre 50 y 150 ufc",
    resultado = "98 ufc",
    concepto = True
    
    )
    
    
    control_medio3 = Dominio.Control_Material(
    lote_material = "M341-22",
    id_material_controlado = staph_aureus.id_material,
    lote_material_controlado = "483-862-5-a10-4",
    especificacion = "Entre 50 y 150 ufc",
    resultado = "98 ufc",
    concepto = True
    )
    
    control_medio4 = Dominio.Control_Material(
    lote_material = "M341-22",
    especificacion = "Entre 50 y 150 ufc",
    lote_material_controlado = "286-862-5-a10-4",
    resultado = "98 ufc",
    concepto = True
    )
    
    control_medio5 = Dominio.Control_Material(
    lote_material = "M341-22",
    id_material_controlado = aspergillus.id_material,
    especificacion = "Entre 50 y 150 ufc",
    lote_material_controlado = "386-862-5-a10-4",
    resultado = "98 ufc",
    concepto = True
    )
    
    control_del_medio = [control_medio1, control_medio2, control_medio3, control_medio4, control_medio5]
    


.. code:: ipython3

    sesion.add_all(control_del_medio)
    sesion.commit()

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db 'select lote_medio, nom_microorganismo, ATC, lote_cepa, especificacion, resultado, fecha_resultado from control_medio, microorganismo where microorganismo.id_microorganismo = control_medio.id_microorganismo '


.. parsed-literal::

    | lote_medio |      nom_microorganismo      |  ATC  |    lote_cepa    |   especificacion   | resultado |      fecha_resultado       |
    |------------|------------------------------|-------|-----------------|--------------------|-----------|----------------------------|
    | M341-22    | Bacillus subtilis spizizenii | 6633  | 486-862-5-a10-4 | Entre 50 y 150 ufc | 98 ufc    | 2021-01-29 12:48:14.117903 |
    | M341-22    | Pseudomona aeruginosa        | 9027  | 484-862-5-a10-4 | Entre 50 y 150 ufc | 98 ufc    | 2021-01-29 12:48:14.120013 |
    | M341-22    | Staphylococcus Aureus        | 6538  | 483-862-5-a10-4 | Entre 50 y 150 ufc | 98 ufc    | 2021-01-29 12:48:14.120613 |
    | M341-22    | Aspergillus bresilensis      | 16404 | 386-862-5-a10-4 | Entre 50 y 150 ufc | 98 ufc    | 2021-01-29 12:48:14.121559 |


+-----+----------------+---+--------+----------+-----+---------------+
| l   | nom_           | A | lot    | especi   | res | fe            |
| ote | microorganismo | T | e_cepa | ficacion | ult | cha_resultado |
| _me |                | C |        |          | ado |               |
| dio |                |   |        |          |     |               |
+=====+================+===+========+==========+=====+===============+
| M   | Bacillus       | 6 | 486    | Entre 50 | 98  | 2021-01-29    |
| 341 | subtilis       | 6 | -862-5 | y 150    | ufc | 12            |
| -22 | spizizenii     | 3 | -a10-4 | ufc      |     | :48:14.117903 |
|     |                | 3 |        |          |     |               |
+-----+----------------+---+--------+----------+-----+---------------+
| M   | Pseudomona     | 9 | 484    | Entre 50 | 98  | 2021-01-29    |
| 341 | aeruginosa     | 0 | -862-5 | y 150    | ufc | 12            |
| -22 |                | 2 | -a10-4 | ufc      |     | :48:14.120013 |
|     |                | 7 |        |          |     |               |
+-----+----------------+---+--------+----------+-----+---------------+
| M   | Staphylococcus | 6 | 483    | Entre 50 | 98  | 2021-01-29    |
| 341 | Aureus         | 5 | -862-5 | y 150    | ufc | 12            |
| -22 |                | 3 | -a10-4 | ufc      |     | :48:14.120613 |
|     |                | 8 |        |          |     |               |
+-----+----------------+---+--------+----------+-----+---------------+
| M   | Aspergillus    | 1 | 386    | Entre 50 | 98  | 2021-01-29    |
| 341 | bresilensis    | 6 | -862-5 | y 150    | ufc | 12            |
| -22 |                | 4 | -a10-4 | ufc      |     | :48:14.121559 |
|     |                | 0 |        |          |     |               |
|     |                | 4 |        |          |     |               |
+-----+----------------+---+--------+----------+-----+---------------+

Emisión de certificados
=======================

En esta sección veremos cómo podemos construir un certificado de
análisis a partir de las tablas que tenemos. Con consultas más
elaboradas, podemos reconstruir los aspectos principales del certificado
de análisis actual:

Informacion del cliente
-----------------------

Con una consulta como:

.. code:: sql

   select nom_empresa as empresa, nit_empresa as nit,  direccion, pagina, correo from empresa, ciudad where empresa.id_ciudad = ciudad.id_ciudad and empresa.id_empresa = 1;

Podemos generar:

.. code:: ipython3

    !sqlite3 -header -line rodam/aceptacion.db 'select nom_empresa as empresa, nit_empresa as nit,  direccion, pagina, correo from empresa, ciudad where empresa.id_ciudad = ciudad.id_ciudad and empresa.id_empresa = 1;'


.. parsed-literal::

      empresa = Compañía Nacional de Cosméticos CONALCOS
          nit = 90024
    direccion = calle 34 Bis 39-33
       pagina = conalcos.com.co
       correo = contacto@conalco.com.co


Información de la muestra
-------------------------

Con una consulta como :

.. code:: sql

   select  nom_producto, presentacion,tamano_muestra as tamano, unidades_tamano as unidades, ingreso_muestra, nom_miembro as registra from producto, muestra, miembro_rodam m where producto.id_producto = muestra.id_muestra and muestra.registra = m.id_miembro

produce:

.. code:: ipython3

    !sqlite3 -header -line rodam/aceptacion.db 'select  nom_producto, presentacion,tamano_muestra as tamano, unidades_tamano as unidades, ingreso_muestra, nom_miembro as registra from producto, muestra, miembro_rodam m where producto.id_producto = muestra.id_muestra and muestra.registra = m.id_miembro'


.. parsed-literal::

       nom_producto = Xinefax
       presentacion = tabletas
             tamano = 500
           unidades = mg
    ingreso_muestra = 2021-02-02 16:42:05.599979
           registra = Ernesto Segura


Resumen analisis
----------------

.. code:: ipython3

    !sqlite3 -header -markdown rodam/aceptacion.db "select * from lectura_con_nombres"


.. parsed-literal::

    | nom_producto | id_muestra |                   nom_grupo                   |         nom_analisis         |           nom_metodo           |          nom_material           | especificacion | resultado |    material     | lote_medio | registra | verifica | concepto |
    |--------------|------------|-----------------------------------------------|------------------------------|--------------------------------|---------------------------------|----------------|-----------|-----------------|------------|----------|----------|----------|
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Inóculo de material controlado | Staphylococcus Aureus ATCC 6538 | 170<t<230      | 112 ufc   | Solución salina | M314-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Inóculo de material controlado | Pseudomona aeruginosa ATCC 9027 | 170<t<230      | 211 ufc   | Solución salina | M315-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Siembra e incubación           | Staphylococcus Aureus ATCC 6538 | <200 ufc       | 211 ufc   | Agar Sabouraud  | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Siembra e incubación           | Pseudomona aeruginosa ATCC 9027 | <200 ufc       | 211 ufc   | Agar Sabouraud  | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Conteo en caja de Petri        | Staphylococcus Aureus ATCC 6538 | <200 ufc       | 211 ufc   | Agar TSB        | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Recuento del inóculo                          | Actividad Bactericida Básica | Conteo en caja de Petri        | Pseudomona aeruginosa ATCC 9027 | <200 ufc       | 211 ufc   | Agar TSB        | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Control de toxicidad del neutralizante        | Actividad Bactericida Básica | Enriquecimiento + Peptona      | Staphylococcus Aureus ATCC 6538 | <100 ufc       | 211 ufc   | Agar TSB        | M316-20    | 1        | 2        | 0        |
    | Xinefax      | 1          | Control del método de dilución-neutralización | Actividad Bactericida Básica | Enriquecimiento                | Staphylococcus Aureus ATCC 6538 | <150 ufc       | 211 ufc   | Agar TSA        | M341-22    | 1        | 2        | 1        |


Equipos utilizados
------------------

======================= ==============
nom_equipo              ref_documental
======================= ==============
Cabina de flujo laminar E001
Balanza                 E020
Balanza                 E020
Micropipeta             E019
Incubadora              E010
Balanza                 E020
Caja de Petri           E011
======================= ==============




miércoles, 14 de julio de 2021, 16:57:37 -05
============================================

Ya me ha pasado en varias ocasiones que 
el init de django corre todas las vistas
en urls.py

No la definición de la vista, sino que corre 
de hecho el `solicitan_aprobacion_de_lecturas`
 
.. code-block:: python

   class MuestrasPorAprobacionFinal(ListView):
    """
    El QA ve solo las *muestras* remitidas por el microbiólogo.
    Debe hacer el control de calidad de los medios
    y dar el visto bueno final.
    """
    
    selector = MuestraSelector()
    queryset = selector.solicitan_aprobacion_de_lecturas()
    template_name = "calidad/muestras_para_QA.html"
    paginate_by = 10
    mensajes= None

como levanto una excepción, no deja que django 
inicie. Ni siquiera para tests 

.. code-block:: python
		
   def solicitan_aprobacion_de_lecturas(self):
        try:
            estado = self.traductor.get_estado("Solicita aprobación de lecturas")
            return self.object_manager.all().filter(estado= estado)
        except TraductorDeEstadoException:
            return self.none

me tocó gestionar esto así. No sé si me cause problemas
más tard


jueves, 15 de julio de 2021, 20:44:52 -05
============================================

Me doy cuenta que el comportamiento del inline form
de django no es igual dependiento de cuál elemento
escoga como padre del inline.

No sé si esto puede producir errores, pero
hoy me confundió bastante eso.

Entonces no se si dejar por funcionalidad:

.. code-block:: python

   class LecturaDeMuestra(LecturaGeneral):
    id_lectura = models.AutoField(primary_key= True)
    especificacion= models.ForeignKey('ingreso.Especificacion', on_delete=models.CASCADE, related_name="lectura_de_muestra")
    muestra = models.ForeignKey('ingreso.Muestra', on_delete=models.CASCADE, related_name="lecturas_de_muestra")
    lote_de_medio = models.ForeignKey('calidad.LoteDeMedio',on_delete=models.PROTECT, default=1)


pruebo manualmente que acceder a la lectura desde ambos related names sean equivalentes:

.. code-block:: python
		
		>>> especificacion2.lectura_de_muestra.all()
		<QuerySet [<Lectura(id='1', especificacion=' Dilución de ácido : entre 50 y 100 ufc')>, <Lectura(id='2', especificacion=' Dilución de ácido : entre 50 y 100 ufc')>]>

		>>> muestra1.lecturas_de_muestra.all()
		<QuerySet [<Lectura(id='1', especificacion=' Dilución de ácido : entre 50 y 100 ufc')>]>


Mon Jul 19 09:31:42 -05 2021
============================

¿Qué es lo más importante?

- que el formulario de especificaciones funcione completo 

  - cambiar queryset de analisis

  la idea general es algo así.

  .. code-block:: python

   form.fields['utiliza'].queryset = utilizas

  - cambiar queryset de grupos:

  pero con los grupos es más complicado.

  debo hacer dos consultas.



Al final, esto parece funcionar. Aunque no he hecho pruebas:

.. code-block:: python

        for form in formset.forms:
            form.fields['utiliza'].queryset = utilizas
            form.fields['grupo'].queryset = grupos_relevantes


Ahora el problema está en el empty_form. Contaba con que se pudiera
manipular. Pero parece que no. Lo único en SO es esto:
https://stackoverflow.com/questions/14160436/change-the-queryset-in-a-empty-form

https://stackoverflow.com/questions/68186351/cannot-edit-fields-of-djangos-formets-empty-form-in-views

Veo solo 2 soluciones: 1) reemplazar el html con js o 2) configurar
el BaseInlineFormset.

Pero configurar el BaseInlineFormset no me pareció viable.
Este ejemplo de SO lo hace ver fácil (https://stackoverflow.com/questions/28201123/django-how-can-i-set-initial-values-to-formsets-empty-form/28734723#28734723).


.. code-block:: python

	class YourBaseInlineFormSet(forms.BaseInlineFormSet):
	    @property
	    def empty_form(self):  # This is almost the same as Django 3.1 code
	        form = self.form(
	            auto_id=self.auto_id,
	            prefix=self.add_prefix("__prefix__"),
	            empty_permitted=True,
	            use_required_attribute=False,
	            initial={"verification": self.initial_extra[0]["verification"]},  # This is the extra parameter
	            **self.get_form_kwargs(None),
	        )
	        self.add_fields(form, None)
	        return form


Pero si reviso el código fuente del `BaseInlineFormSet`no encuentro el `empty_form`.
No sé realmente qué es lo que hace. Además aquí solo le pasan datos al `initial`, pero
yo necesito modificar el queryset.

Estimo que es muy probable que el queryset solo se pueda manipular en el `__init__`.
Pero sin dominar el tema a fondo, eso puede causar problemas. No he visto en la documentación
que recomienden tocar el `__init__`


La solución final fue esta:

.. code-block:: python

	// en .click() de Añadir especificacion

	...
	
	// cambio las opciones disponibles para el dropdown
        utilizas_table_data = `#id_especificaciones-${form_index}-utiliza`
        grupo_tabla_data = `#id_especificaciones-${form_index}-grupo`
        $(utilizas_table_data).html(utilizas)
        $(grupo_tabla_data).html(grupos)


El papel de los compositores
============================
Básicamente, quiero aislar la lógica del formulario
de la lógica de la vista.


El API de un compositor, en principio, solo me ofrece GET y POST

.. code-block:: python

     
     LecturaDeMuestraInlineForm(request, id_muestra):
     	if request.method == "POST":
     	   form = compositor.POST(POST_data=request.POST)
     	   if form.is_valid():
     	       form.save()
     	       return redirect("recoleccion:gestionar_muestras")
     	else:
     	   compositor.generar_data_inicial(miembro_rodam=request.user.miembro_rodam)
     	   form = compositor.GET()


Tue Jul 20 10:22:37 -05 202
===========================

Resumen despliege:
- actualizar
- set host name
- crear usuario con privilegios reducidos
- crear llave RSA para SSH
- quitar la posibilidad de logearse al sistema con password
- configurar firewall (usar `ufw`)
- transferir el proyecto a VM
- cambiar `settings.py` para ambiente de producción
  ALLOWED_HOSTS
  STATIC
- instalar python3 y python3-(no legible) en ubuntu
- descargar apache con mod wsgi
- activar configuracioón con `a2ensite`, desactivar con `a2ensite`
- ocultar la información confidencial
  secret key
  `DEBUG false`
- revisar los permisos de unix para todo el path de la aplicación

anotaciones sobre el primer despliegue:
- hay que separar el viertualenv del proyecto Django e
  instalar el virtualenv usando el python del sistema

- en ubuntu se instala python3 y python3-virtualenv
  con el gestor de paquetes del sistema

- hay que reorganizar el static

- es preferible no poner el proyecto en un directorio de usuario
  donde los permisos están configuradaos para el. Apache necesita
  tener los acceso a todo el directorio.

- se requiere practicar más para entender la comunicación del protocolo
  wsgi
  
algo sobre la arquitectura
==========================
En general la responsabilidad de la vista es gestionar
peticiones http.

De esto naturalmente han emergido dos conceptos:

1) Compositors
   componen formularios. como estoy usando un framework
   es natural que 'dependa' (hace llamadas directas)
   de los formularios de Django. Sin embargo, esto
   está separado en alguna medida. Por ejemplo:

   .. code-block:: python

	EspecificacionCompositor(instance= adaptor.debeTener, form_class=EspecificacionForm, adaptor =adaptor)

   Aquí el formulario se separa del compositor como tal.
   Lo único 'impuro' es la llamada directa a una factory de Django.
   Pero eso simplemente se puede parametrizar
	
   Pero es necesario separar las respnsabilidades
   para que el código sea más comprensible y mucho más mantenibles.
   La práctica ha apoyado este precepto de la teoría. Me siento más
   seguro así.
   
2) Adaptors
   modelan casos de uso directamente de la lógica de negocios.
   En principio pensaba que un adaptador podía tener una
   relacion 1 a 1 con un modelo, pero ese pensamiento es
   limitante, y la práctica me dice que podría desmunuzar más cada adaptor.
   Aunque no es sabio desgastarse tanto por eso. En este momento
   las responsabilidades están suficientemente claras.
   

CBV vs FCV

Al fin y al cabo, tanto en la una como en la otra se puede:

.. code-block:: python

	if form.is_valid():
            object =  form.save(commit=False)               
            object.registra_ingreso = request.user.miembro_rodam
            object.save()
            return redirect("ingreso:cuadroAnalitico_detalle", id_cuadroAnalitico=id_cuadroAnalitico)



En realidad lo único que está mal del formulario individual
es que es un inline form.

Wed Jul 21 11:25:21 -05 2021
============================
- hacer formulario [


- hay que desmenuzar esto:

::
   Django uses request and response objects to pass state through the system.



Detalles
--------

Como `generar_data_inicial` es un método del compositor, no tengo que verificar
que en el POST, se vuelva a pre-llenar el formulario. Solo tengo que probar
que llena un formulario.

.. code-block:: python

    def get(self, request,*args, **kwargs):
        data_inicial = self.compositor.generar_data_inicial(miembro_rodam=request.user.miembro_rodam, muestra=self.muestra)
        form = self.compositor.GET()

        
        return self.render_to_response(self.get_context_data(form=form))
        
    def post(self,request, *args, **kwargs):
        data_inicial = self.compositor.generar_data_inicial(miembro_rodam=request.user.miembro_rodam, muestra=self.muestra)
        form  = self.compositor.POST(POST_DATA=request.POST)

Nota. Esto *no* funcina porque

::
   
   These values (initial) are only displayed for unbound forms, and they’re not used as fallback values if a particular value isn’t provided.


Nota sobre las pruebas
----------------------
Pero aún así hay una ventaja y es que puedo simular una *bound form* sin tener
que lidiar con el test client.

Solo necesito simuar un `QueryDict` de un `Request`: https://docs.djangoproject.com/en/3.2/ref/request-response/#django.http.QueryDict


Problemas con la fecha
----------------------

resulta que el auto_now_add *no* guarda la fecha localizada, sino en UTC
.. code-block:: python

   class LecturaGeneral(models.Model):
        #puede existir sin resultado
        resultado_lectura = models.CharField(max_length=30)
        fecha_resultado_lectura = models.DateTimeField(blank=True, null=True, auto_now_add=True)


entonces, para leerlo bien, tocaría usar:

.. code-block:: python

	>>> from django.utils import timezone
	>>> timezone.localtime(lectura.fecha_resultado_lectura)
	datetime.datetime(2021, 7, 21, 14, 37, 36, 813625, tzinfo=<DstTzInfo 'America/Bogota' -05-1 day, 19:00:00 STD>)


Pero al parecer se puede en los templates directamente: https://stackoverflow.com/questions/42124050/timezone-aware-datetime-objects-in-django-templates



Tengo problemas con el bootstrap. No me está tomando el `table-dark`. En general no hay clases de la tabla

El medio del metodo
-------------------

El medio del método debe cambiar a 'Tipo de medio', para restringir más el formulario de lectura 

Thu Jul 22 10:51:23 -05 2021
=============================

¿Qué se debe mostar en la sala de lecturas?
Un resumen del estado de lecturas.

- Para cada especificacion, debo poder enumerar sus lecturas DONE
- Saber rápidamente cuantas especificaciones faltan por lecturas DONE



Podría esto causar problemas?
-----------------------------

.. code-block:: python

	#primero genero la tabla
        adaptor.tabla_de_especificaciones
        especificaciones_completas =  adaptor.especificaciones_completas

        self.assertTrue(len(especificaciones_completas) == 1)
        self.assertEquals(especificaciones_completas[0], especificacion_de_la_lectura)

No puedo saber las especificaciones completas o pendientes si primero
no genero la tabla. Es lógico que funcione así.

Pero siendo hiperriguroso, un método público no debería tener una dependencia temporal


El dilema de abstraer
---------------------

No se si pasar esto:

.. code-block:: html

	<h1 id="titulo_detalle"> Muestra {{ object.lote_muestra }} de {{muestra.cuadroAnalitico.producto.nom_producto}} </h1>
	<h2 class="atributos_detalle"> Origen : {{ object.origen.nom_origen}} </h2>
	<h2 class="atributos_detalle"> Presentacion :  {{muestra.cuadroAnalitico.producto.forma_farmaceutica }} {{ object.presentacion}} </h2>
	<h2 class="atributos_detalle"> Lote: {{ object.lote_muestra }} </h2>
	<h2 class="atributos_detalle"> Tamaño : {{ object.tamano_muestra }} {{ object.unidades_tamano }} </h2>
	<h2 class="atributos_detalle"> Estado : {{ object.estado.nom }} </h2>


A un método del adaptor.

los adaptors y el refresh
-------------------------


tuve que poner esto en la sala de lecturas

.. code-block:: python

	def _cleanup(self):

	self.especificaciones_pendientes = []
        self.especificaciones_completas = []


Por alguna razón las especificaciones pendientes
se acumulaban cuando refrescaba la página.

Esto quiere decir que un nuevo adaptor no se crea
cuando refresco la vista. ¿Esto lo hace Django
automáticamente? Quien sabe.


Una solución más autocontenida es esta :


.. code-block:: python

    def _registrar_especificacion_pendiente(self, lecturas_hechas=None, especificacion=None):
      """Si no hay lecturas hechas, agrega la especificacion a las pendientes """
      especificaciones_pendientes = self.especificaciones_pendientes

      if len(lecturas_hechas) == 0 and especificacion not in especificaciones_pendientes:
            self.especificaciones_pendientes.append(especificacion)

    def _registrar_especificacion_completa(self, especificacion = None, lecturas_hechas=None):
       """Si una especificacion tiene lecturas hechas, llevamos una cuenta de las especificaciones
      completas"""
       
       especificaciones_completas = self.especificaciones_completas

       if len(lecturas_hechas) > 0 and especificacion not in especificaciones_completas :
          self.especificaciones_completas.append(especificacion)

Aquí evito duplicados.

Sin embargo, la idea de un _cleanup es buena. Porque lo tengo es algo parecido
al template pattern.


Pero *al final* tuve que poner el _cleanup. Cuando el


cerrar el dia
-------------
- no alcancé a probar la validación antes de remitir el lote
- queda pendiente lo de bootstrap. Parece que no está cargando bien.
- sospecho que hay clases que comparten estado de calidad y otras que no. Eso es confuso.
- el criterio de validación aún es difuso. toca discutirlo
- queda pendiente localizar la hora en la sala de lecturas
- me di cuenta de que el reporte de medios está mostrango el control de un mismo medio tantas veces como lecturas DONE

Fri Jul 23 10:42:55 -05 2021
==============================

- hoy lo primero es terminar la validación DONE
- luego, permmitir una edición básica DONE
- luego, la vista de aprobación final 
- luego, arreglar el formulario de ingreso de cuadros analiticos
 
 

dudas de abstraccion
--------------------

Debería generar mensajes para mostrar en la validación?
.. code-block:: python

    def es_valida_para_solicitar_aprobacion_de_lecturas(self):
        es_valida= False
        self.tabla_de_especificaciones
        if len(self.especificaciones_pendientes) == 0: es_valida=True
  
        return es_valida


Terminé haciendolo. Hace todo más transparente

.. code-block:: python

    def _registrar_error_de_validacion(self, especificaciones_pendientes=None):
      string_de_especificaciones = "Las especificaciones con id's : {"
      for espec in especificaciones_pendientes:
          id = " {},".format(espec.id) 
          string_de_especificaciones = string_de_especificaciones + id

      string_de_especificaciones += " }"

      msg = string_de_especificaciones + " tienen lecturas pendientes."

      self.errores_de_validacion.append(msg)		
   



Residuos
--------

En inventario hay esto. Esta lectura es vieja

.. code-block:: python

	class Lectura(LecturaGeneral):
	...
	muestra = models.ForeignKey('ingreso.Muestra', on_delete=models.CASCADE, related_name="lecturas")


El 'related_name' se confunde con `lecturas_de_muestra`, que es el realmente funcional.

Hay que quitar esto, pero ahora estoy enfocado en otra cosa.


services/recoleccion/services  ya está demasiado grande. Toca separarlo

habrá variaciones que ahora mismo no ves

cerrar el dia
-------------
- no pude extender una modelform con campos que no pertenecen al modelo
- pero eso no es fundamental en este momento
- lo fundamental es ponder lo de emision
- y no olvidar mejorar la validación del login 
- la funcionalidad se está acumulando y hay que ver cómo redirigir mejor. 

Mon Jul 26 09:45:06 -05 2021
==============================
prioridades;
- la vista de aprobacion final DONE
- la vista da entender que es calidad, hay que cambiar eso DONE
- falta lo de localizar DONE

¿Debo hacer una sala de aprobacion?

No sé como llegó una muestra a emision sin tener lecturas. Es un misterio


Tue Jul 27 10:07:07 -05 2021
==============================

No se si debería volver esto su propia clase de adaptador.

Mezclo funcionalidad de dos adaptores.
- se cambí el inline form de ingresar cuadro analitico a formulario de creación

.. code-block:: python

	def get_context_data(self, **kwargs):
        	context = super().get_context_data(**kwargs)  
        	self.id_muestra = self.kwargs['id_muestra']
        	adaptor = MuestraAdaptor(id_muestra=self.id_muestra, muestra_manager=Muestra.objects)
        	sala_de_lecturas = SalaDeLecturasAdaptor(id_muestra=self.id_muestra, muestra_manager=Muestra.objects)
        	context['tabla_de_especificacion'] = sala_de_lecturas.tabla_de_especificaciones
        	context["titulo_tabla"] = "lecturas"
        	context["encabezados"] = adaptor.encabezados_lecturas
        	context["tabla_generica"] = adaptor.tabla_de_lecturas
        	context["resumen"] = sala_de_lecturas.resumen
        	context["resumen"]["título"] = "Resumen de lecturas"
        	context["tabla_de_especificaciones"] = {'encabezados' :sala_de_lecturas.encabezados_especificaciones, 
        	    'data': sala_de_lecturas.tabla_de_especificaciones,
        	    'titulo': 'Tabla de especificaciones'}



terminé mejorando la vista :


.. code-block:: python

	def get_context_data(self, **kwargs):
	        context = super().get_context_data(**kwargs)  
	        self.id_muestra = self.kwargs['pk']
	        adaptor = SalaDeAprobacionAdaptor(id_muestra=self.id_muestra, muestra_manager=Muestra.objects)    
	        context["resumen"] = adaptor.resumen
	        #la tabla generica presenta las lecturas 
	        context["titulo_tabla"] = "lecturas"
	        context["encabezados"] = adaptor.encabezados_lecturas
	        context["tabla_generica"] = adaptor.tabla_de_lecturas
	
	        return context

En realidad lo unico que tengo que añadir son las especificaciones completas vs las totales


separé a django de mi código


.. code-block:: python

    @property
    def fecha_localizada(self):
        return timezone.localtime(self.fecha_resultado_lectura)


- creo que ya estoy listo para desplegar nuevamente
- checklist de despliege


Wed Jul 28 10:25:41 -05 2021
==============================

objetivos
---------
- usuario daniel
- borrar datos
- cuidarse de que no encuentre los tempates

el segundo despliege
--------------------
- duré como 45 minutos intentano arrancar
- el error era el mismo

- el `error.log` de apache era:
  
.. code-block:: sh
		
    [Wed Jul 28 10:18:19.147822 2021] [wsgi:error] [pid 563933:tid 140379357771520] [remote 186.80.52.63:28302]   File "/home/jonatan/weblab-deploy/venv/lib/python3.8/site-packages/django/utils/log.py", line 75, in configure_logging
[Wed Jul 28 10:18:19.147824 2021] [wsgi:error] [pid 563933:tid 140379357771520] [remote 186.80.52.63:28302]     logging_config_func(logging_settings)
[Wed Jul 28 10:18:19.147829 2021] [wsgi:error] [pid 563933:tid 140379357771520] [remote 186.80.52.63:28302]   File "/usr/lib/python3.8/logging/config.py", line 808, in dictConfig
[Wed Jul 28 10:18:19.147831 2021] [wsgi:error] [pid 563933:tid 140379357771520] [remote 186.80.52.63:28302]     dictConfigClass(config).configure()
[Wed Jul 28 10:18:19.147836 2021] [wsgi:error] [pid 563933:tid 140379357771520] [remote 186.80.52.63:28302]   File "/usr/lib/python3.8/logging/config.py", line 570, in configure
[Wed Jul 28 10:18:19.147838 2021] [wsgi:error] [pid 563933:tid 140379357771520] [remote 186.80.52.63:28302]     raise ValueError('Unable to configure handler '
[Wed Jul 28 10:18:19.147846 2021] [wsgi:error] [pid 563933:tid 140379357771520] [remote 186.80.52.63:28302] ValueError: Unable to configure handler 'file'


Esto pasa por que el componente logger no puede crear handers porque la ruta no existe o no tiene accesos

En el primer despliege pensé que lo había solucionado con permisos. Entonces:

.. code-block:: sh

	-rw-r--r--  1 jonatan www-data  519 Jun 20 03:00 CHANGELOG.txt
	-rw-r--r--  1 jonatan www-data  126 Jun 20 03:00 CHANGELOG.txt~
	drwxrwxr-x 17 jonatan www-data 4096 Jul 27 22:04 mysite
	-rw-r--r--  1 jonatan www-data  177 Jun 20 03:28 requirements.txt
	drwxrwxr-x  6 jonatan jonatan  4096 Jun 21 01:37 venv

Pero eso no estaba funcionando esta vez.

Una solución drástica fue modificar el `settings.py` para:


.. code-block:: python

	LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/jonatan/weblab-deploy/mysite/logs/debug.log',
        },
        'calidad_file':{
        'level': 'DEBUG',
        'formatter': 'basico',
        'class': 'logging.FileHandler',
        'filename': '/home/jonatan/weblab-deploy/mysite/logs/calidad.log'
        },
        'ingreso_file':{
        'level': 'DEBUG',
        'formatter': 'basico',
        'class': 'logging.FileHandler',
        'filename': '/home/jonatan/weblab-deploy/mysite/logs/ingreso.log'
        },
        'recoleccion_file': {
        'level': 'DEBUG',
        'formatter': 'basico',
        'class': 'logging.FileHandler',
        'filename': '/home/jonatan/weblab-deploy/mysite/logs/recoleccion.log'
      }
    },


Con el nombre completo sí sirve. Así que era cuestión de que el directorio que se usaba no era el adecuado.
No sé por qué en mi máquina /logs evalúa a jaumaf/logs, mientras que en ubuntu no.


Ahora, queda la duda de por qué en el primer despliege sí sirvó.

Ya. Había hecho esto y no me acordaba

.. code-block:: python

	            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
        },

   



encontré un bug
---------------

El resumen tiene un comportamiento extraño
y seeguía sumando especificaciones

por ahora me tocó gestionarlo así:

.. code-block:: python
   
    @property
    def resumen(self):
        self._cleanup()
        self.tabla_de_especificaciones
        resumen = {
          'título': 'Resumen de Sala de Aprobación',
          'data' :{
          'id. muestra' :self.muestra.id,
          'núm. lote ': self.muestra.lote_muestra,
           'producto': self.muestra.cuadroAnalitico.producto.nom,
           'cliente' : self.muestra.cuadroAnalitico.producto.cliente,
           'origen' : self.muestra.origen.nom,
           'sector' : self.muestra.cuadroAnalitico.producto.sector.nom_sector,
          'especificaciones completas': len(self.especificaciones_completas),
          'especificaciones en cuadro' : len(self.especificaciones)
           }

        }
        return resumen



Esto  causaba esto `InvalidTemplateEngineError at /calidad/control/medio/MetodoDeControl/detalle/2'

- lo de collect static me jodío
- lo de pasar las acciones como un diccionario en el contexto no me sirvió bien


- en el nuevo
 STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'static_prod')

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
APP_DIRS = True

- en el viejo

  STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static_prod')
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
APP_DIRS = True


momento de reflexión
---------------------
- qué hacer ahora
- qué tests faltan
- cómo consolido lo que ya está de la mejor manera?


- hay que cambiar el fulano nadies por algo progresivo
s
- la lectura de control tambien hay que localizarla manualmente

Thu Jul 29 11:48:27 -05 2021
===============================

- ahora hay que setear este enironment variable

  .. code-block:: python
   
  self.directorio_salida = os.environ['WEBLAB']+"/tests/artefactos"


- algo causa que la hoja de calculos en mac no coga bien los separadores del csv. Pero no sé por qué 



viernes, 30 de julio de 2021, 10:06:36 -05
===========================================

hoy:

- terminar con el test del reporter [x]
- explorar diferencia entre factories y stubs [x]
- disenar el pdf reporter []

vamos ...

la lectura de muestra pide un lote de medio. creo
que eso aguanta para un subfactory

Cuales son los pros/cons de usar factories y no stubs: https://martinfowler.com/articles/mocksArentStubs.html#TheDifferenceBetweenMocksAndStubs


los stubs vs los mocks
=======================
Quedé más confundido luego de verificar la biblio.

Voy a usar el test completo, para que quede como si fuera
integracion


desenmarañando lo que hice
==========================

el main del report:

1. creo un doc template
2. creo una lista historia
3. creo la tabla del cliente
4. creo la tabla de la muestra
5. creo la tabla de resultados
6. creo espacio de parametros
7. creo notas al pie
8. creo disclaimer
9. espacio firma



lunes,  2 de agosto de 2021, 09:17:15 -05
========================================

- hay reunion
- ¿qué es lo más importante?

Para reunion
------------

- lecturas calidad/lecturas
- puntos de verificación explicita
- un lote de medio  necesitará historia de lecturas?

pasos a seguir
++++++++++++++
 
  
- backup de base de datos
- cómo accedera a consultas SQL
  - consultas preprogramadas
  - accesso por ssh
  - prueba por GC

- generación de certificado y espacio de clientes
- Módulo de trazabilidad
- Mejora de lecturas
  
- ¿Hago diagramas?


- creo que lo óptimo es hacer un objeto emisión
- que guarde un pdf para siempre 


Dilema del pipe
-----------------------------


.. code-block:: python

    def _pipe(self, item):
        
        tabulizado = self._tabularizar(item)
        paragrafizado = self._envolver_en_parrafos(tabulizado) 
        return paragrafizado


Es decir, primero tabulizo y luego paragrafizo


- al documento le faltan notas al pie

  
miércoles,  4 de agosto de 2021
===============================
- estoy enredandome con los tests del pdfreporter
- creo que tengo que separar:
  - mi builder básico
  - el formato rodam
  - el certificado
- y luego hacer un adapter especial para acomodar los datos

jueves,  5 de agosto de 2021
==============================
- necesito agilidad así que por ahora omitiré lo del formato
- en los reportes de la muestra no encuentor al cliente
- le hice un cambio al adaptor, revisar con los tests
- se me salió el corazón y era que habia importado el testcase de unittest y no de django.tests entonces estaba destruyendo mi base de datos
- se me ocurrio de golpe poner la bandera de exportar en el metodo o incluso en el analisis

viernes,  6 de agosto de 2021
==============================


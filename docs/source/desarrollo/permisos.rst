##############################
Permisos y autorización
##############################


Uso general de los permisos
##############################

Se crean permisos solo
si hay una acción concreta para
la que se necesite un permiso y
los permisos genéricos que trae Django
(create, delete, change ) no son
suficientes.

.. warning::
   Los permisos *no* estan relacionados
   con el componente Dashboard. Si a
   un usuario o grupo se le asigna un permiso
   no quiere decir que automaticamente las
   vistas que requieran ese permiso aparecerán
   en el dashboard.

Utilizar permisos
##############################

Los permisos se referencian utilizando
el el ciclo de vida descrito en
`services.protocols.ciclo_de_vida`.

Asignación de permisos
-----------------------
Los permisos no son visibles hasta que
se declaren en los modelos de Django.

Para asegurar que haya una sola fuente de
informacion con respecto a los permisos,
se declaran importando las tuplas de
`services.protocols.ciclo_de_vida.[nombre del modelo]`

Por ejemplo, los permisos definidos aquí:

.. code-block:: python
	
	REMITIR = "remitir_cuadroanalitico"
	APROBAR = "aprobar_cuadroanalitico"
	
	
	PERMISOS_DJANGO = [
	    (REMITIR, "Puede marcar como listo para ser aprobado"),
	    (APROBAR, "Puede aprobar un cuadro analítico para que las muestras pasen a recolección")]


son utilizados aquí:

.. code-block:: python

	from services.protocols.permisos.cuadro_analitico import PERMISOS_DJANGO

	
	class CuadroAnalitico(models.Model):
		class Meta:
		    ordering = ['-fecha_creacion']
		    permissions = PERMISOS_DJANGO



Chequeo de permisos
------------------------------
¿Como chequear si los permisos declarados existen en la base de datos?
Por medio de de un script. Ver :doc:`/operaciones/scripts`.

	
CBV
------------------------------
En las CBV los permisos se utilizan con
los mixins incluidos en Django.

Por ejemplo, aquí el PermissionRequiredMixin
no afecta para nada el otro mixin de RedirigeALogin.

.. code-block:: python
		
   from django.contrib.auth.mixins import PermissionRequiredMixin
   
   class FacturacionMaestra(AreaMixin,
                         DashboardMixin,
                         TitleMixin,
                         RedirigeALogin, # < -- el mixin custom
                         PermissionRequiredMixin, # <-- el mixin de django
                         PaginarConFiltroMixin,
                         ListView):
    """Interactuar con facturación independientemente del ciclo de vida.





Existen casos en donde la funcionalidad se complejiza,
y se recomienda hacer un Mixin dentro del módulo correspondiente.
Por ejemplo, para chequear si un cuadro analitico cumple con
cierta condición, se puede hacer esto:

.. code-block:: python

   class TieneQueEstarSinRemitirMixin(UserPassesTestMixin):
    """
    Mixin para verificar si el cuadro analitico puede modificarse.

    Sigue la lógica de django.contrib.auth. Por lo tanto,
    otros mixins pueden llamar a test_func o handle_no_permission.
    """

    raise_exception = True

    def test_func(self):
        """
        Se verifica una condición puntual.

        La responsabilidad de si un cuadro
        es verificable se delega al modelo.

        Retorna un booleano.
        """

        self.cuadro = self.get_object()
        return self.cuadro.es_modificable(self.request.user)

    def handle_no_permission(self):
         # se customiza que se hace si falla 


   # y el mixin se puede usar en las n vistas siguientes
   
   class Especificacion_ingresar(
 	RedirigeALogin,
	TieneQueEstarSinRemitirMixin, # <-- utilizado aquí
	PermissionRequiredMixin,
	DashboardMixin,
	SingleObjectMixin,
	View,
	):

	# bla, bla , bla




Por lo general no vale la pena escribir un mixin en
la app `base` porque si se necesita escribir uno
custom, no necesita ser generalizado.


FBV
------------------------------
En las FBV los permisos se pueden
poner con los decorators de `django.contrib.auth.decorators`.



.. code-block:: python

   from django.contrib.auth.decorators import permission_required

   @permission_required(f'ingreso.{EMITIR_CERTIFICADO}', raise_exception=True)
   def darAprobacionFinal(request, id_muestra):
   """Cambia estado de la muestra y produce un certificado
    una vez aprobado"""

       remisor = RemisorDeMuestra(id_remitible=id_muestra)
       veredicto = int(request.POST.get("veredicto"))
       adaptor = PDFAdaptor(id_muestra=id_muestra, muestra_manager=Muestra.objects)
       remisor.dar_aprobacion_final(solicitante=request.user.miembro_rodam, veredicto=bool(veredicto),
                                               adaptor=adaptor, request=request)

       remisor.agregar_mensajes(messages=messages, request=request)

       return redirect('emision:muestras_por_aprobacion')


.. note::

   `raise_exception=True` es necesario para que se presente la pagina 404.
   De lo contrario, redirigirá a LOGIN_URL, independientemente de qué
   otros decorators esten encargandose de esto.
   
.. note::

   Notese que los permisos se referencian como constantes
   que son importadas desde el ciclo de vida
   
Los decorators se pueden anidar (eso es lo que hacen
mejor), de modo que no solo se verifique si el usuario tiene el permiso,
sino tambien si hizo login.



.. code-block:: python

	from django.contrib.auth.decorators import permission_required, login_required
	from django.shortcuts import redirect
	from services.ingreso import AprobadorDeCuadroAnalitico
	from  inventario.views import producto_detalle
	from services.protocols.permisos.cuadro_analitico import REMITIR
	from django.contrib import messages
	
	@login_required(login_url='login:login')
	@permission_required(f'ingreso.{REMITIR}',  raise_exception=True)
	def CuadroAnalitico_remitir(request, id_cuadroAnalitico,):
	    """
	    Cambia el estado de control de calidad para que
	    Q.A pueda analizarlo.
	    """
	
	    # bla, bla, bla
	


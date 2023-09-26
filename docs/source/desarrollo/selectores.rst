##############################
Selectores
##############################

Gestionar el caso nulo para que las vistas no se preocupen por eso.
Sobre todo con el bootstrap que hace Django al principio.
.. code-block:: python
		
	def muestras_aprobadas(self):

        try:
            con_aprobacion_final = self.traductor.get_estado("con aprobación final")
            return self.object_manager.filter(estado= con_aprobacion_final)
        except:
            return self.object_manager.none()

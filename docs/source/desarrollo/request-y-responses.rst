##############################
Requests y responses
##############################

Inevitablemente se tiene que lidiar con requests
y responses directamente por que la funcionalidad
de vistas genericas es límitada. Aqui hay unas quias



Booleanos en los request
##############################

La forma más sencilla es usando el builtin `bool()`,
que recibe un entero.

Entonces, en las plantillas se debe codificar en los
/key, value/ del formulario como un entero.

Ejemplo,

.. code-block:: python

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

====================
Reporte de pruebas
====================

	  
:author: Jonatan Ahumada Fernández
:contact: box@jade.lat
:date:  18 de julio de 2025


Aquí se presenta el reporte de cada prueba unitaria o de integración automatizada.
Si se desea revisar con más detalle cada prueba se debe buscar en la carpeta `tests`
del proyecto de Django cada prueba individual.

.. code-block:: text

	System check identified 2 issues (0 silenced).
	test_caso_es_numerico (tests.LERA.test_validacion.TestValidacion)
	RA-331 El caso de la lectura es de un tipo determinado. ... ok
	test_gramatica_bien_definida (tests.LERA.test_validacion.TestValidacion)
	RA-331 La gramática formal compila y puede parcelar. ... ok
	test_operacion_desigualdad (tests.LERA.test_validacion.TestValidacion)
	RA-331 Se crea una validación cuya operación utiliza el atributo ... ok
	test_unidades_coinciden (tests.LERA.test_validacion.TestValidacion)
	RA-331 Dada una especificación completa y una lectura, ... ok
	test_consolidar_falla (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado)
	ROD-33 Si falta algun parámetro (distinto a la firma y logo), el paso de ... ok
	test_conversion_modelo_a_protocolo (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado)
	ROD-33 ... ok
	test_datos_muestra_generan_hash (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado)
	ROD-33 Hash generado por datos de la muestra debe ser ... ok
	test_hash_cambia_si_alteran_datos (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado)
	ROD-33 ... ok
	test_se_necesita_tener_firma_y_logo (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado)
	ROD-33 Debe levantar una excepción si no existe firma o logo cuando ... ok
	test_resolver_concepto (tests.emision.test_lera_validacion_backend.TestLeraValidacionBackend)
	RA-331 Prueba que para una muestra se pueda resolver concepto. ...	ok
	test_validaciones_corren (tests.emision.test_lera_validacion_backend.TestLeraValidacionBackend)
	RA-331 Prueba que `lera_validar()` retorne recibos de validación para la lectura. ...	ok
	test_dropdowns_de_grupo_son_restringidos (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis)
	ROD-30 Usuario solo ve grupos pertinentes ... ok
	test_dropdowns_de_metodo_son_restringidos (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis)
	ROD-30 Usuario solo ve métodos pertinentes para análisis ... ok
	test_el_compositor_se_instancia (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis)
	ROD-30 ... ok
	test_genera_data_inicial (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis)
	ROD-30 Usuario solo ve especificaciones pertinentes ... ok
	test_genera_el_formset_al_init (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis)
	ROD-30 ... ok
	test_enlaza_datos_del_post (tests.formularios.test_lecturaDeMuestra.TestFormularioDeLecturasDeMuestraCompuesto)
	RA-213. Mock del client y pasar un formulario gigante de post ... ok
	test_produce_numero_de_formularios_correcto (tests.formularios.test_lecturaDeMuestra.TestFormularioDeLecturasDeMuestraCompuesto)
	RA-213 ... ok
	test_se_instancia_correctamente (tests.formularios.test_lecturaDeMuestra.TestFormularioDeLecturasDeMuestraCompuesto)
	RA-213 atributos se calculan según lo esperado. ... ok
	test_formulario_recibe_muestra_y_quien_registra_automaticamente (tests.formularios.test_lectura_individual.TestFormularioDeLecturaDeMuestraIndividual)
	ROD-32 ... ok
	test_retorna_formulario_a_partir_de_especificacion (tests.formularios.test_lectura_individual.TestFormularioDeLecturaDeMuestraIndividual)
	ROD-32 ... ok
	test_envio (tests.login.test_correo.TestCorreoRegistro)
	RA-336 Seguridad. Envia correo notificación. ... ok
	test_bloqueo_estado_inicial (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 Tras su creación, el miembro no está bloqueado. ... ok
	test_bloqueo_intentos_fallidos (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 Usuario se bloquea dependiendo del contador. ... ok
	test_intentos_restantes (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 ... ok
	test_login_contasena_invalida_sin_bloqueo (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 ... ok
	test_login_contrasena_invalida_tiene_bloqueo (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 ... ok
	test_login_contrasena_valida_pero_tiene_bloqueo (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 ... ok
	test_login_exito (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 ... ok
	test_login_usuario_no_existe (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 Cuando el usuario no existe, retorna False ... ok
	test_registrar_fallo_incrementa (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 Al registrar un fallo el contador incrementa solo si está dentro de la ventana. ... ok
	test_registrar_fallo_primera_vez (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 Se asigna el momento del fallo e incrementa el contador ... ok
	test_registrar_fallo_tres_veces (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 ... ok
	test_signal_creates_django_user (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 Django user se crea tras registro. ... ok
	test_ventana_dentro (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 Si un momento está por dentro de la ventana, método retorna True. ... ok
	test_ventana_fuera (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 Si un momento está por fuera de la ventana, método retorna False. ... ok
	test_ventana_fuera_sin_ultimo_fallo (tests.login.test_login.TestMiembroRodamLogin)
	RA-539 Gestiona el caso en que fecha_ultimo_fallo no exista. ... ok
	test_cambio_el_certificado_vigente_por_uno_nuevo (tests.procesos.base.test_configuracionCambiaEnTiempoReal.TestConfiguracionCambieEnTiempoDeEjecucion)
	ROD-33. Configuración ... ok
	test_remisor_marca_el_uso (tests.procesos.calidad.medios.test_cuadro_control_marca_uso.TestFlujoRegularDeCalidad)
	ROD-33 Remisor cambia de estado. ... ok
	test_flujo (tests.procesos.calidad.test_flujo_regular.TestFlujoRegularDeCalidad)
	ROD-33 flujo inventario ... ok
	test_analisis_repetidos_se_copian (tests.procesos.catalogo.test_copiado_especificaciones.TestCopiadoDeEspecificaciones)
	RA-475 Si un mismo analisis esta asociado dos veces ... ok
	test_especificaciones_se_copian (tests.procesos.catalogo.test_copiado_especificaciones.TestCopiadoDeEspecificaciones)
	RA-475 Un cuadro abstracto copia especificaciones ... ok
	test_analisis_repetidos_se_copian (tests.procesos.catalogo.test_copiado_especificaciones_a_abstracto.TestCopiadoDeEspecificacionesHaciaAbstracto)
	RA-475 Si un mismo analisis esta asociado dos veces ... ok
	test_especificaciones_se_copian (tests.procesos.catalogo.test_copiado_especificaciones_a_abstracto.TestCopiadoDeEspecificacionesHaciaAbstracto)
	RA-475 Un cuadro analítico copia especificaciones ... ok
	test_metodos_asociados_al_analisis (tests.procesos.catalogo.test_datos_asociados_al_analisis.TestMetodosAsociadosAlAnalisis)
	ROD-33 Director de la informacion ingresa analisis y le ... ok
	test_datos_asociados_al_metodo (tests.procesos.catalogo.test_datos_asociados_al_metodo.test_datos_asociados_al_metodo)
	ROD-33 Los metodos quedan con equipos ... ok
	test_el_grupo_tiene_analisis (tests.procesos.catalogo.test_el_grupo_tiene_analisis.TestGrupoTieneAnalisis)
	ROD-46 Verifica que grupos quedan asociados con el análisis ... ok
	test_el_cuadro_queda_aprobado_por_calidad (tests.procesos.ingreso.test_cuadro_queda_aprobado_por_calidad.TestCuadroQuedaAprobadoPorCalidad)
	ROD-33 Flujo ingreso. ... ok
	test_el_cuadro_queda_con_analisis_asignados (tests.procesos.ingreso.test_cuadro_queda_con_analisis_asignados.TestCuadroQuedaConAnalisisAsignados)
	ROD-33 Flujo ingreso. Los cuadros quedan con analisis. ... ok
	test_datos_asociados_al_cuadro (tests.procesos.ingreso.test_datos_asociados_al_cuadro.TestDatosAsociadosAlCuadro)
	ROD-33 Flujo ingreso. Los cuadros quedan con responsable, ... ok
	test_especificaciones_se_crean (tests.procesos.ingreso.test_especificaciones_se_crean.TestDatosAsociadosAlCuadro)
	ROD-33 Flujo ingreso.Las especificaciones quedan registradas en la ... ok
	test_datos_asociados_al_cuadro (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	ROD-33 Flujo inventario. Los cuadros quedan con responsable, un producto y un estado. ... ok
	test_datos_asociados_al_metodo (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	ROD-33 Flujo inventario. Los metodos quedan con equipos. ... ok
	test_datos_asociados_al_producto (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	ROD-33 Flujo inventario. El producto queda con el cliente y ... ok
	test_el_cuadro_queda_aprobado_por_calidad (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	ROD-33. Flujo calidad. ... skipped ''
	test_el_cuadro_queda_con_analisis_asignados (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	ROD-33 Flujo inventario. Los cuadros quedan con analisis. ... ok
	test_el_grupo_tiene_analisis (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	ROD-33 Flujo inventario. Los grupos quedan asociados con el analisis. ... ok
	test_especificaciones_se_crean (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	ROD-33. Flujo catálogo. Especificaciones quedan registradas en la ... ok
	test_metodos_asociados_al_analisis (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	ROD-33 Flujo inventario. Director de la informacion ingresa analisis y le ... ok
	test_metodos_pertenecen_al_analisis (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	ROD-33. Flujo catálogo.Reviso si el servicicio de especficacion obtiene los metodos utilizados en el análisis. ... skipped ''
	test_flujo (tests.procesos.inventario.test_flujo.TestFlujo)
	ROD-33. Flujo inventario. Simula procesos de inventario hasta ingreso de muestra. ... ok
	test_carga_configuracion (tests.procesos.login.test_dashboard_carga_configuracion.TestConfiguracionDeDashboard)
	Se carga  un diccionario de configuración que en settings ... ok
	test_miembro_rodam_genera_django_user (tests.procesos.login.test_miembro_rodam_genera_django_user.TestMiembroRodamGeneraUsuarioDjango)
	Director de información crea un miembroRodam y automáticamente se crea un django_user ... ok
	test_remitir_lote_permiso_custom (tests.procesos.no_funcionales.test_permisos.TestPermisos) ... skipped 'Django bug'
	test_remitir_lote_verifica_permiso (tests.procesos.no_funcionales.test_permisos.TestPermisos)
	usuario aleatorio no puede remitir lote ... skipped 'Django bug'
	test_se_imprime_con_datos_falsos (tests.reporter.test_certificado_de_emision.TestCertificadoEmision)
	ROD-33 Flujo emisión. ... skipped ''
	test_se_integra_con_la_muestra (tests.reporter.test_certificado_de_emision.TestCertificadoEmision)
	"ROD-33 Flujo emisión. ... ok
	test_el_archivo_tiene_numero_de_filas_correctas (tests.reporter.test_lote_de_medio_reporter.TestMediosReporter)
	RA-183 integridad de los datos ... ok
	test_el_reporter_escribe_a_un_file_object (tests.reporter.test_lote_de_medio_reporter.TestMediosReporter)
	RA-183 interfaces externas ... ok
	test_la_tabla_extrae_correctamente_las_lecturas_de_los_lotrs (tests.reporter.test_lote_de_medio_reporter.TestMediosReporter)
	RA-183 integridad de los datos ... ok
	test_se_crea_un_csv_en_los_artefactos (tests.reporter.test_muestra_reporter.TestMuestraReporter)
	RA-183 integridad de los datos. ... ok
	test_api_fila (tests.reporter.test_spans.TestSpan)
	RA-537. El caso simple es en el que hay un solo span. ... ok
	test_api_seccion (tests.reporter.test_spans.TestSpan)
	RA-537. El caso simple para una seccion. ... ok
	test_caso_1 (tests.reporter.test_spans.TestSpan)
	RA-537. En este caso no hay ningún span que ocupe más de 2 espacios. ... ok
	test_caso_2 (tests.reporter.test_spans.TestSpan)
	RA-537. En este caso el primer elemento ocupa 2 columnas. ... ok
	test_caso_3 (tests.reporter.test_spans.TestSpan)
	RA-537. En este caso el segundo elemento ocupa 3 columnas. ... ok
	test_caso_4 (tests.reporter.test_spans.TestSpan)
	RA-537. En este caso el segundo elemento ocupa 2 columnas. ... ok
	test_caso_5 (tests.reporter.test_spans.TestSpan)
	RA-537. En este caso el primer elemento ocupa 2 columnas y el tercero también. ... ok
	test_no_hay_errores_en_init (tests.services.test_EspecificacionDeAnalisisEnCuadroAdaptor.TestEspecificacionDeAnalisisEnCuadroAdaptor)
	ROD-45 ... ok
	test_puede_cargar_objetos_de_los_managers (tests.services.test_EspecificacionDeAnalisisEnCuadroAdaptor.TestEspecificacionDeAnalisisEnCuadroAdaptor)
	ROD-45 ... ok
	test_retorna_los_grupos_relevantes (tests.services.test_EspecificacionDeAnalisisEnCuadroAdaptor.TestEspecificacionDeAnalisisEnCuadroAdaptor)
	ROD-45 ... ok
	test_retorna_los_utilizas (tests.services.test_EspecificacionDeAnalisisEnCuadroAdaptor.TestEspecificacionDeAnalisisEnCuadroAdaptor)
	ROD-45 ... ok
	test_cada_fila_en_especificaciones_solo_tiene_str (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor)
	ROD-33 ... ok
	test_carga_cuadro_al_inicializar (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor)
	ROD-33 ... ok
	test_carga_lote_de_medio (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor)
	ROD-33 el adaptador carga el objeto ... ok
	test_carga_metodos_al_inicializar (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor)
	ROD-33 ... ok
	test_el_diccionario_tiene_los_metodos_del_objeto (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor)
	ROD-33 ... ok
	test_especificaciones_se_muestran_como_lista_de_listas (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor)
	ROD-33 ... ok
	test_identifica_muestras_que_han_utilizado_el_lote (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor)
	ROD-33 integridad de los datos. ... ok
	test_retorna_un_diccionario (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor)
	ROD-33 ... ok
	test_carga_la_muestra (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 ... ok
	test_columnas_para_normalizacion (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 ... ok
	test_distintos_analisis_aparecen_en_diccionario (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 Cada analisis tiene su propia llave ... ok
	test_get_all_especificaciones (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 ... ok
	test_get_analisis_asignados (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 ... ok
	test_llaves_de_dicionaro_son_strings (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 ... ok
	test_se_extraen_los_equipos_utilizados (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 ... ok
	test_tabla_de_emision_filtra_por_marcas_de_emision (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 ... ok
	test_tabla_de_lecturas_es_una_lista_de_listas (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 ... ok
	test_tabla_especificaciones_es_lista_de_listas (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	ROD-33 ... ok
	test_pdf_adaptor_saca_los_equipos_del_sector_del_producto_y_marcados_para_todos (tests.services.test_MuestraAdaptorEquipos.TestConEquipoTodos)
	RA-356 Espero que el adaptador me retorne el equipo con el sector ... ok
	test_verifico_que_haya_2_equipos_en_metodo (tests.services.test_MuestraAdaptorEquipos.TestConEquipoTodos)
	Verifico que el setup haya dejado el metodo con 2 equipos. ... ok
	test_verifico_que_los_2_equipos_sean_de_sectores_diferentes (tests.services.test_MuestraAdaptorEquipos.TestConEquipoTodos)
	RA-356 Verifico que los 2 equipos del setup tengan diferente sector. ... ok
	test_pdf_adaptor_saca_los_equipos_del_sector_del_producto (tests.services.test_MuestraAdaptorEquipos.TestSinEquipoTodos)
	RA-356 Espero que el adaptador me retorne el equipo con el sector ... ok
	test_verifico_que_haya_2_equipos_en_metodo (tests.services.test_MuestraAdaptorEquipos.TestSinEquipoTodos)
	RA-356 Verifico que el setup haya dejado el metodo con 2 equipos. ... ok
	test_verifico_que_los_2_equipos_sean_de_sectores_diferentes (tests.services.test_MuestraAdaptorEquipos.TestSinEquipoTodos)
	RA-356 Verifico que los 2 equipos del setup tengan diferente sector. ... ok
	test_se_identifican_los_lotes_de_medio_utilizados (tests.services.test_MuestraAdaptorGestionaLotes.TestMuestraAdaptorGestionaLotes)
	ROD-33 ... ok
	test_se_pueden_extraer_las_lecturas_de_control (tests.services.test_MuestraAdaptorGestionaLotes.TestMuestraAdaptorGestionaLotes)
	ROD-33 Prueba que adaptador de *muestra* es capaz de extraer lecturas de *control*. ... ok
	test_visibilidad_cuadro_control (tests.services.test_MuestraAdaptorGestionaLotes.TestMuestraAdaptorGestionaLotes)
	ROD-33 Prueba efecto de la visibilidad del cuadro en el adaptor. ... ok
	test_cambia_el_adaptor_de_lote (tests.services.test_PdfAdaptor.TestPDFAdaptor)
	ROD-33. Flujo emisión. ... ok
	test_el_formato_es_inmutable (tests.services.test_PdfAdaptor.TestPDFAdaptor)
	ROD-33. Flujo emisión. Pruebo que el formato de clase no cambie por accidente luego de formatear un item. ... ok
	test_exporta_data_de_certificado (tests.services.test_PdfAdaptor.TestPDFAdaptor)
	ROD-33. Integridad de los datos. ... ok
	test_exporta_firma_implicados (tests.services.test_PdfAdaptor.TestPDFAdaptor)
	RA-420. Debe retornar una lista de FirmaMiembroRodam según los protocolos. ... ok
	test_extrae_implicados_correctamente (tests.services.test_PdfAdaptor.TestPDFAdaptor)
	RA-420. Prueba que los implicados se cuenten correctamente. ... ok
	test_puede_formatear_un_item (tests.services.test_PdfAdaptor.TestPDFAdaptor)
	ROD-33. Flujo emisión. Prueba que al formatear se retorna un string. ... ok
	test_se_puede_construir_una_fila (tests.services.test_PdfAdaptor.TestPDFAdaptor)
	ROD-33. Flujo emisión. Prueba que se hagan listas. ... ok
	test_seccion_cliente_dimensiones (tests.services.test_PdfAdaptor.TestPDFAdaptor)
	ROD-33. Flujo emisión. ... ok
	test_seccion_muestra_dimensiones (tests.services.test_PdfAdaptor.TestPDFAdaptor)
	ROD-33. Flujo emisión. ... ok
	test_cuenta_correctamente_las_especificaciones_completas (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor)
	RA-56 ... ok
	test_cuenta_correctamente_las_especificaciones_pendientes (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor)
	RA-56 ... ok
	test_genera_resumen (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor)
	RA-56 ... ok
	test_se_generan_mensajes_para_errores_de_validacion (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor)
	RA-56 ... ok
	test_valida_si_pueden_aprobarse_las_lecturas (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor)
	RA-56 ... ok
	test_encabezados_de_lectura_cambian (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor)
	ROD-5 ... ok
	test_hace_el_init (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor)
	ROD-5 ... ok
	test_muestra_mensaje_de_validacion (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor)
	ROD-5 ... ok
	test_no_valida_si_hay_especificaciones_pendientes (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor)
	ROD-5 ... ok
	test_produce_resumen (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor)
	ROD-5 ... ok
	test_reporta_lecturas_completas (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor)
	ROD-5 ... ok
	test_reporta_lecturas_pendientes (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor)
	ROD-5 ... ok
	test_tabla_de_lecturas_es_reducida (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor)
	ROD-5 ... ok
	test_valida_cuando_las_especificaciones_estan_completas_y_hay_fecha_de_inicio (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor)
	ROD-5 ... ok
	test_armar_dashboard_para_rol (tests.services.test_dashboard_dinamico.TestDashboard)
	NF. Confidencialidad. Se muestra un menú de acuerdo al rol. ... ok
	test_boooleano_cambia_a_string (tests.services.test_loteDeMedioParaCertificadoDeEmision.TestLoteDeMedioParaCertificadoDeEmision)
	ROD-33. Flujo emisión. Descontinuar. ... skipped ''
	test_cambios_quedan_en_log_entry (tests.teoremas.test_LogEntry.TestLogEntry)
	ROD-33 Registro auditoría. ... ok
	test_email_usando_smtp_externo (tests.teoremas.test_email.TestEmail)
	ROD-455 Envia mail usando un servicio SMTP real. ... skipped ''
	test_email_usando_smtp_local (tests.teoremas.test_email.TestEmail)
	ROD-455 Envía correo con adjunto usando un servidor SMTP Local ... ok
	test_por_defecto_en_memoria (tests.teoremas.test_email.TestEmail)
	ROD-455 Muestra comportamiento básico del backend en tests. ... ok
	test_como_hacer_una_muestra (tests.teoremas.test_factories.TestFactories)
	ROD-33 Intrumentos de testeo. ... ok
	test_no_puedo_inicializar_atributos_en_un_stub (tests.teoremas.test_factories.TestFactories)
	ROD-33 Intrumentos de testeo. ... ok
	test_es_hashable (tests.teoremas.test_named_tuple_es_hashable.TestNamedTupleEsHashable)
	NF. Integridad de los datos. ... ok
	test_comparaciones_basicas (tests.teoremas.test_organizar_fechas.TestFactories)
	NF. Integridad de los datos ... ok
	test_comparaciones_con_datetimes_localizadas (tests.teoremas.test_organizar_fechas.TestFactories)
	NF. Integridad de los datos ... ok
	test_localizacion (tests.teoremas.test_organizar_fechas.TestFactories)
	NF. Integridad de los datos. ... ok
	test_se_ordenan_en_una_lista (tests.teoremas.test_organizar_fechas.TestFactories)
	NF. Integridad de los datos ... ok
	test_reglas_no_permiten_aprobar_un_lote (tests.validaciones.lote_de_medio.test_validar_aprobacion.TestValidacionesLoteDeMedio)
	ROD-33 El lote se intenta aprobar, pero, como *no* cumple las reglas de remisión, el ... ok
	test_reglas_permiten_aprobar_un_lote (tests.validaciones.lote_de_medio.test_validar_aprobacion.TestValidacionesLoteDeMedio)
	ROD-33 Como el lote cumple con las reglas, se puede aprobar sin problemas ... ok
	test_remisor_remite (tests.validaciones.lote_de_medio.test_validar_aprobacion.TestValidacionesLoteDeMedio)
	ROD-33 Confirma que los datos del lote están ... ok
	test_especificaciones_completas_pero_no_cumplen_no_puede_solicitar (tests.validaciones.lote_de_medio.test_validar_solicitar_aprobacion.TestValidacionesLoteDeMedio)
	ROD-33 ... ok
	test_especificaciones_completas_y_cumplen_puede_solicitar (tests.validaciones.lote_de_medio.test_validar_solicitar_aprobacion.TestValidacionesLoteDeMedio)
	ROD-33 ... ok
	test_especificaciones_incompletas_no_puede_solicitar_aprobacion (tests.validaciones.lote_de_medio.test_validar_solicitar_aprobacion.TestValidacionesLoteDeMedio)
	ROD-33 ... ok
	test_CuadrosPorAprobar (tests.vistas.calidad.test_views_retornan_ok.TestViewsRetornanOk)
	Aprobar cuadros analíticos ... skipped ''
	test_aprobarCuadroAnalitico (tests.vistas.calidad.test_views_retornan_ok.TestViewsRetornanOk)
	Vista aprobar cuadro analítico ... skipped ''
	test_ingresar_analisis (tests.vistas.catalogo.test_views_retornan_ok.TestViewsRetornanOk)
	Formulario de análisis ... skipped ''
	test_ingresar_grupo (tests.vistas.catalogo.test_views_retornan_ok.TestViewsRetornanOk)
	Formulario de grupo ... skipped ''
	test_ingresar_metodo (tests.vistas.catalogo.test_views_retornan_ok.TestViewsRetornanOk)
	Formulario de método ... skipped ''
	test_CambiaConceptoDeLecturaPorId (tests.vistas.emision.test_views_retornan_ok.TestViewsRetornanOk)
	Modificar lectura ... skipped ''
	test_MuestrasPendientesPorAprobacionFinal (tests.vistas.emision.test_views_retornan_ok.TestViewsRetornanOk)
	Muestras por aprobacion final ... skipped ''
	test_CuadroAnalitico_detalle (tests.vistas.ingreso.test_views_retornan_ok.TestViewsRetornanOk) ... skipped ''
	test_CuadroAnalitico_ingresar (tests.vistas.ingreso.test_views_retornan_ok.TestViewsRetornanOk) ... skipped ''
	test_cuadroAnaltico_remitir (tests.vistas.ingreso.test_views_retornan_ok.TestViewsRetornanOk) ... skipped ''
	test_especificacion_ingresar (tests.vistas.ingreso.test_views_retornan_ok.TestViewsRetornanOk) ... skipped ''
	test_muestra_ingresar (tests.vistas.ingreso.test_views_retornan_ok.TestViewsRetornanOk) ... skipped ''
	test_muestra_lista (tests.vistas.ingreso.test_views_retornan_ok.TestViewsRetornanOk) ... skipped ''
	test_construye_historia (tests.emision.test_baseBuilder.TestPDFBuilder)
	ROD-33 Flujo emisión. ... ok
	test_envolver_en_parrafos_ignora_items_que_no_son_strings (tests.emision.test_baseBuilder.TestPDFBuilder)
	ROD-33 Flujo emisión. ... ok
	test_envuelve_en_parrafos_los_items_de_una_tabla (tests.emision.test_baseBuilder.TestPDFBuilder)
	ROD-33 Flujo emisión. ... ok
	test_multidimensiona_un_string (tests.emision.test_baseBuilder.TestPDFBuilder)
	ROD-33 Flujo emisión. ... ok
	test_pipe_funciona (tests.emision.test_baseBuilder.TestPDFBuilder)
	ROD-33 Flujo emisión. ... ok

	----------------------------------------------------------------------
	Ran 169 tests in 173.817s

	OK (skipped=20)

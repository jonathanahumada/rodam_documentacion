====================
Reporte de pruebas
====================


.. |date| date::
	  
:author: Jonatan Ahumada Fernández
:contact: jaumaf@hotmail.com
:date:  último build el |date|


Aquí se presenta el reporte de cada prueba unitaria o de integración automatizada.
Si se desea revisar con más detalle cada prueba se debe buscar en la carpeta `tests`
del proyecto de Django cada prueba individual.

.. code-block::
   
	Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
	test_crea_un_certificado_y_reconstruye_objetos (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado) ... ok
	test_datos_muestra_generan_hash (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado) ... ok
	test_hash_cambia_si_alteran_datos (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado) ... ok
	test_se_necesita_tener_firma_y_logo (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado) ... ok
	test_transforma_datos_a_json (tests.emision.test_emisorDeCertificado.Test_EmisorDeCertificado) ... ok
	test_dropdowns_de_grupo_son_restringidos (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis) ... ok
	test_dropdowns_de_metodo_son_restringidos (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis) ... ok
	test_el_compositor_se_instancia (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis) ... ok
	test_genera_data_inicial (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis) ... ok
	test_genera_el_formset_al_init (tests.formularios.test_especificar_un_analisis.TestFormularioParaEspecificarUnAnalisis) ... ok
	test_enlaza_datos_del_post (tests.formularios.test_lecturaDeMuestra.TestFormularioDeLecturasDeMuestraCompuesto)
	Me toca hacer un mock del client y pasar un formulario gigante de post ... ok
	test_produce_numero_de_formularios_correcto (tests.formularios.test_lecturaDeMuestra.TestFormularioDeLecturasDeMuestraCompuesto) ... ok
	test_se_instancia_correctamente (tests.formularios.test_lecturaDeMuestra.TestFormularioDeLecturasDeMuestraCompuesto)
	atributos se calculan según lo esperado ... ok
	test_formulario_recibe_muestra_y_quien_registra_automaticamente (tests.formularios.test_lectura_individual.TestFormularioDeLecturaDeMuestraIndividual) ... ok
	test_retorna_formulario_a_partir_de_especificacion (tests.formularios.test_lectura_individual.TestFormularioDeLecturaDeMuestraIndividual) ... ok
	test_cambio_el_certificado_vigente_por_uno_nuevo (tests.procesos.base.configuracionCambiaEnTiempoReal.ConfiguracionCambieEnTiempoDeEjecucion) ... ok
	test_remisor_marca_el_uso (tests.procesos.calidad.medios.test_cuadro_control_marca_uso.TestFlujoRegularDeCalidad) ... ok
	test_flujo (tests.procesos.calidad.test_flujo_regular.TestFlujoRegularDeCalidad) ... ok
	test_metodos_asociados_al_analisis (tests.procesos.catalogo.test_datos_asociados_al_analisis.TestMetodosAsociadosAlAnalisis)
	Director de la informacion ingresa analisis y le ... ok
	test_datos_asociados_al_metodo (tests.procesos.catalogo.test_datos_asociados_al_metodo.test_datos_asociados_al_metodo)
	Los metodos quedan con equipos ... ok
	test_el_grupo_tiene_analisis (tests.procesos.catalogo.test_el_grupo_tiene_analisis.GrupoTieneAnalisis)
	los grupos quedan asociados con el analisis ... ok
	test_el_cuadro_queda_aprobado_por_calidad (tests.procesos.ingreso.test_cuadro_queda_aprobado_por_calidad.TestCuadroQuedaAprobadoPorCalidad)
	Luego de que el cuadro se aprueba por el servicio, ... ok
	test_el_cuadro_queda_con_analisis_asignados (tests.procesos.ingreso.test_cuadro_queda_con_analisis_asignados.TestCuadroQuedaConAnalisisAsignados)
	los cuadros quedan con analisis ... ok
	test_datos_asociados_al_cuadro (tests.procesos.ingreso.test_datos_asociados_al_cuadro.TestDatosAsociadosAlCuadro)
	Los cuadros quedan con responsable, ... ok
	test_especificaciones_se_crean (tests.procesos.ingreso.test_especificaciones_se_crean.TestDatosAsociadosAlCuadro)
	las especificaciones quedan registradas en la ... ok
	test_datos_asociados_al_cuadro (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	Los cuadros quedan con responsable, un producto y un estado ... ok
	test_datos_asociados_al_metodo (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	Los metodos quedan con equipos ... ok
	test_datos_asociados_al_producto (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	El producto queda con el cliente y el sector ... ok
	test_el_cuadro_queda_aprobado_por_calidad (tests.procesos.inventario.test_desglose.TestFlujoRegular) ... skipped ''
	test_el_cuadro_queda_con_analisis_asignados (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	los cuadros quedan con analisis ... ok
	test_el_grupo_tiene_analisis (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	los grupos quedan asociados con el analisis ... ok
	test_especificaciones_se_crean (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	las especificaciones quedan registradas en la ... ok
	test_metodos_asociados_al_analisis (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	Director de la informacion ingresa analisis y le ... ok
	test_metodos_pertenecen_al_analisis (tests.procesos.inventario.test_desglose.TestFlujoRegular)
	Reviso si el servicicio de especficacion obtiene los metodos utilizados en el analisis ... skipped ''
	test_flujo (tests.procesos.inventario.test_flujo.Flujo) ... ok
	test_carga_configuracion (tests.procesos.login.test_dashboard_carga_configuracion.TestConfiguracionDeDashboard)
	Se carga  un diccionario de configuración que en settings ... ok
	test_miembro_rodam_genera_django_user (tests.procesos.login.test_miembro_rodam_genera_django_user.TestMiembroRodamGeneraUsuarioDjango)
	Director de información crea un miembroRodam y automáticamente se crea un django_user ... ok
	test_se_imprime_con_datos_falsos (tests.reporter.test_certificado_de_emision.PDF_Reporter) ... skipped ''
	test_se_integra_con_la_muestra (tests.reporter.test_certificado_de_emision.PDF_Reporter) ... ok
	test_el_archivo_tiene_numero_de_filas_correctas (tests.reporter.test_lote_de_medio_reporter.TestMediosReporter) ... ok
	test_el_reporter_escribe_a_un_file_object (tests.reporter.test_lote_de_medio_reporter.TestMediosReporter) ... ok
	test_la_tabla_extrae_correctamente_las_lecturas_de_los_lotrs (tests.reporter.test_lote_de_medio_reporter.TestMediosReporter) ... ok
	test_se_crea_un_csv_en_los_artefactos (tests.reporter.test_muestra_reporter.TestMuestraReporter) ... ok
	test_no_hay_errores_en_init (tests.services.test_EspecificacionDeAnalisisEnCuadroAdaptor.TestEspecificacionDeAnalisisEnCuadroAdaptor) ... ok
	test_puede_cargar_objetos_de_los_managers (tests.services.test_EspecificacionDeAnalisisEnCuadroAdaptor.TestEspecificacionDeAnalisisEnCuadroAdaptor) ... ok
	test_retorna_los_grupos_relevantes (tests.services.test_EspecificacionDeAnalisisEnCuadroAdaptor.TestEspecificacionDeAnalisisEnCuadroAdaptor) ... ok
	test_retorna_los_utilizas (tests.services.test_EspecificacionDeAnalisisEnCuadroAdaptor.TestEspecificacionDeAnalisisEnCuadroAdaptor) ... ok
	test_cada_fila_en_especificaciones_solo_tiene_str (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor) ... ok
	test_carga_cuadro_al_inicializar (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor) ... ok
	test_carga_lote_de_medio (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor)
	el adaptador carga el objeto ... ok
	test_carga_metodos_al_inicializar (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor) ... ok
	test_el_diccionario_tiene_los_metodos_del_objeto (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor) ... ok
	test_especificaciones_se_muestran_como_lista_de_listas (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor) ... ok
	test_identifica_muestras_que_han_utilizado_el_lote (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor) ... ok
	test_retorna_un_diccionario (tests.services.test_LoteDeMedioAdaptor.TestLoteDeMedioAdaptor) ... ok
	test_carga_la_muestra (tests.services.test_MuestraAdaptor.TestMuestraAdaptor) ... ok
	test_columnas_para_normalizacion (tests.services.test_MuestraAdaptor.TestMuestraAdaptor) ... ok
	test_distintos_analisis_aparecen_en_diccionario (tests.services.test_MuestraAdaptor.TestMuestraAdaptor)
	Cada analisis tiene su propia llave ... ok
	test_get_all_especificaciones (tests.services.test_MuestraAdaptor.TestMuestraAdaptor) ... ok
	test_get_analisis_asignados (tests.services.test_MuestraAdaptor.TestMuestraAdaptor) ... ok
	test_llaves_de_dicionaro_son_strings (tests.services.test_MuestraAdaptor.TestMuestraAdaptor) ... ok
	test_se_extraen_los_equipos_utilizados (tests.services.test_MuestraAdaptor.TestMuestraAdaptor) ... ok
	test_tabla_de_emision_filtra_por_marcas_de_emision (tests.services.test_MuestraAdaptor.TestMuestraAdaptor) ... ok
	test_tabla_de_lecturas_es_una_lista_de_listas (tests.services.test_MuestraAdaptor.TestMuestraAdaptor) ... ok
	test_tabla_especificaciones_es_lista_de_listas (tests.services.test_MuestraAdaptor.TestMuestraAdaptor) ... ok
	test_se_identifican_los_lotes_de_medio_utilizados (tests.services.test_MuestraAdaptorGestionaLotes.TestMuestraAdaptorGestionaLotes) ... ok
	test_se_pueden_extraer_las_lecturas_de_control (tests.services.test_MuestraAdaptorGestionaLotes.TestMuestraAdaptorGestionaLotes) ... ok
	test_cambia_el_adaptor_de_lote (tests.services.test_PdfAdaptor.ComportamientoPDFAdaptor) ... ok
	test_el_formato_es_inmutable (tests.services.test_PdfAdaptor.ComportamientoPDFAdaptor) ... ok
	test_exporta_data_de_certificado (tests.services.test_PdfAdaptor.ComportamientoPDFAdaptor) ... ok
	test_puede_formatear_un_item (tests.services.test_PdfAdaptor.ComportamientoPDFAdaptor) ... ok
	test_se_puede_construir_una_fila (tests.services.test_PdfAdaptor.ComportamientoPDFAdaptor) ... ok
	test_seccion_cliente_es_una_fila_con_3_columnas (tests.services.test_PdfAdaptor.ComportamientoPDFAdaptor) ... ok
	test_seccion_muestra_es_una_tabla_de_5_por_4 (tests.services.test_PdfAdaptor.ComportamientoPDFAdaptor) ... ok
	test_cuenta_correctamente_las_especificaciones_completas (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor) ... ok
	test_cuenta_correctamente_las_especificaciones_pendientes (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor) ... ok
	test_genera_resumen (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor) ... ok
	test_se_generan_mensajes_para_errores_de_validacion (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor) ... ok
	test_valida_si_pueden_aprobarse_las_lecturas (tests.services.test_SalaDeControlAdaptor.TestSalaDeControlAdaptor) ... ok
	test_encabezados_de_lectura_cambian (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor) ... ok
	test_hace_el_init (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor) ... ok
	test_muestra_mensaje_de_validacion (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor) ... ok
	test_no_valida_si_hay_especificaciones_pendientes (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor) ... ok
	test_produce_resumen (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor) ... ok
	test_reporta_lecturas_completas (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor) ... ok
	test_reporta_lecturas_pendientes (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor) ... ok
	test_tabla_de_lecturas_es_reducida (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor) ... ok
	test_valida_cuando_las_especificaciones_estan_completas_y_hay_fecha_de_inicio (tests.services.test_SalaDeLecturasParaMuestra.TestSalaDeLecturasAdaptor) ... ok
	test_armar_dashboard_para_rol (tests.services.test_dashboard_dinamico.TestDashboard) ... ok
	test_boooleano_cambia_a_string (tests.services.test_loteDeMedioParaCertificadoDeEmision.TestLoteDeMedioParaCertificadoDeEmision)
	Esto ya no aplica. Hay que quitarlo ... skipped ''
	test_cambios_quedan_en_log_entry (tests.teoremas.test_LogEntry.TestLogEntry) ... ok
	test_email_usando_smtp_externo (tests.teoremas.test_email.TestEmail)
	Envia mail usando un servicio SMTP real. ... ok
	test_email_usando_smtp_local (tests.teoremas.test_email.TestEmail)
	Envía correo con adjunto usando un servidor SMTP Local ... ok
	test_por_defecto_en_memoria (tests.teoremas.test_email.TestEmail)
	Muestra comportamiento básico del backend en tests. ... ok
	test_como_hacer_una_muestra (tests.teoremas.test_factories.TestFactories) ... ok
	test_no_puedo_inicializar_atributos_en_un_stub (tests.teoremas.test_factories.TestFactories) ... ok
	test_es_hashable (tests.teoremas.test_named_tuple_es_hashable.TestNamedTupleEsHashable) ... ok
	test_comparaciones_basicas (tests.teoremas.test_organizar_fechas.TestFactories) ... ok
	test_comparaciones_con_datetimes_localizadas (tests.teoremas.test_organizar_fechas.TestFactories) ... ok
	test_localizacion (tests.teoremas.test_organizar_fechas.TestFactories) ... ok
	test_se_ordenan_en_una_lista (tests.teoremas.test_organizar_fechas.TestFactories) ... ok
	test_reglas_no_permiten_aprobar_un_lote (tests.validaciones.lote_de_medio.test_validar_aprobacion.TestValidacionesLoteDeMedio)
	El lote se intenta aprobar. Pero como *no* cumple las reglas de remisión el ... ok
	test_reglas_permiten_aprobar_un_lote (tests.validaciones.lote_de_medio.test_validar_aprobacion.TestValidacionesLoteDeMedio)
	Como el lote cumple con las reglas, se puede aprobar sin problemas ... ok
	test_remisor_remite (tests.validaciones.lote_de_medio.test_validar_aprobacion.TestValidacionesLoteDeMedio)
	Remitir es confirmar que los datos del lote están ... ok
	test_especificaciones_completas_pero_no_cumplen_no_puede_solicitar (tests.validaciones.lote_de_medio.test_validar_solicitar_aprobacion.TestValidacionesLoteDeMedio) ... ok
	test_especificaciones_completas_y_cumplen_puede_solicitar (tests.validaciones.lote_de_medio.test_validar_solicitar_aprobacion.TestValidacionesLoteDeMedio) ... ok
	test_especificaciones_incompletas_no_puede_solicitar_aprobacion (tests.validaciones.lote_de_medio.test_validar_solicitar_aprobacion.TestValidacionesLoteDeMedio) ... ok
	test_CuadrosPorAprobar (tests.vistas.calidad.test_views_retornan_ok.ViewsRetornanOk)
	Aprobar cuadros analíticos ... skipped ''
	test_aprobarCuadroAnalitico (tests.vistas.calidad.test_views_retornan_ok.ViewsRetornanOk)
	Vista aprobar cuadro analítico ... skipped ''
	test_ingresar_analisis (tests.vistas.catalogo.test_views_retornan_ok.ViewsRetornanOk)
	Formulario de análisis ... skipped ''
	test_ingresar_grupo (tests.vistas.catalogo.test_views_retornan_ok.ViewsRetornanOk)
	Formulario de grupo ... skipped ''
	test_ingresar_metodo (tests.vistas.catalogo.test_views_retornan_ok.ViewsRetornanOk)
	Formulario de método ... skipped ''
	test_CambiaConceptoDeLecturaPorId (tests.vistas.emision.test_views_retornan_ok.ViewsRetornanOk)
	Modificar lectura ... skipped ''
	test_MuestrasPendientesPorAprobacionFinal (tests.vistas.emision.test_views_retornan_ok.ViewsRetornanOk)
	Muestras por aprobacion final ... skipped ''
	test_CuadroAnalitico_detalle (tests.vistas.ingreso.test_views_retornan_ok.ViewsRetornanOk) ... skipped ''
	test_CuadroAnalitico_ingresar (tests.vistas.ingreso.test_views_retornan_ok.ViewsRetornanOk) ... skipped ''
	test_cuadroAnaltico_remitir (tests.vistas.ingreso.test_views_retornan_ok.ViewsRetornanOk) ... skipped ''
	test_especificacion_ingresar (tests.vistas.ingreso.test_views_retornan_ok.ViewsRetornanOk) ... skipped ''
	test_muestra_ingresar (tests.vistas.ingreso.test_views_retornan_ok.ViewsRetornanOk) ... skipped ''
	test_muestra_lista (tests.vistas.ingreso.test_views_retornan_ok.ViewsRetornanOk) ... skipped ''
	test_el_pipe_funciona (tests.emision.test_baseBuilder.PDFBuilder) ... ok
	test_envolver_en_parrafos_ignora_items_que_no_son_strings (tests.emision.test_baseBuilder.PDFBuilder) ... ok
	test_envuelve_en_parrafos_los_items_de_una_tabla (tests.emision.test_baseBuilder.PDFBuilder) ... ok
	test_multidimensiona_un_string (tests.emision.test_baseBuilder.PDFBuilder) ... ok
	test_se_construye_la_historia (tests.emision.test_baseBuilder.PDFBuilder) ... ok
	
	----------------------------------------------------------------------
	Ran 125 tests in 105.408s
	
	OK (skipped=17)
	Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
	

Historia del proyecto
==================================

:author: Jonatan Ahumada Fernández
:contact: box@jade.lat
:date: 2025-07-01

Rodam WebLab, como proyecto, ha pasado por varias fases. Como se verá
más adelante, estas fases se ven reflejadas en la documentación.

En términos simples, se debe entender que desde su incepción en el 16
de noviembre de 2020, el proyecto pasó de ser un proyecto estilo
*waterfall*, a un proyecto con un marco *ágil*.

La razón principal de esto es que hubieron cambios en el alcance del
proyecto, que imposibilitaron la concreción del proyecto dentro del
plazo inicialmente pactado y según el primer levantamiento de
requerimientos.

Aquí se hará un breve resumen de las fases

Primera fase: incepción
  Desde el 16 de noviembre de 2020 hasta el 24 de febrero de
  2021. Aquí se hicieron dos prototipos: una aplicación de escritorio
  usando TKinter y luego un cuaderno de Jupyter que muestra el flujo de los
  datos. El cuaderno de Jupyter se consideró una *prueba de aceptación*, en el
  que se puede evidenciar el flujo principal de los datos de la aplicación.
  Teniendo esto claro, se pasó a la siguiente fase.
  
Segunda fase: desarrollo Django
  Desde el 24 de febrero de 2021 hasta  el 17 de mayo de 2021.
  Gracias a la prueba de aceptación, se tenia
  un prototipo de la aplicación a construir.  Así que se seleccionó
  Django y Postgres como el stack tecnológico a utilizar.  Fue durante
  esta fase, que correspondería a la fase de *implementación*, dentro
  del ciclo de vida de *waterfall*, que el proyecto presentó las
  primeras dificultades. La principal era que el flujo de calidad
  no estaba dentro de los requerimientos iniciales, porque se estimó
  que se podía delegar para después. Sin embargo, para la creación
  del certificado de emisión se hizo patente que eran necesarios
  datos de calidad que no se podían obviar. Así, fue necesario incorporar
  el flujo de calidad dentro de la primera iteración del WebLab.
  
Tercera fase: fase crítica de reconfiguración del proyecto
   Desde el 18 de mayo hasta el 29 de septiembre de 2021.
   En esta fase se buscan incorprar funcionalidades que faltaron
   en el primer levantamiento de requerimientos. Ejemplo de esto
   fue: el flujo de calidad y las marcas de emisión. Este fue el
   periodo más crítico y, por lo tanto, no está registrado dentro
   de ningún tablero de tareas. Sin embargo, se lograron sortear
   las dificultades y dieron paso a la siguiente fase
   

Cuarta fase: primer despliegue y desarrollo ágil
  Desde su primer despliegue el 29 de septiembre de 2021 y, en adelante, el proyecto
  viró paulatinamente hacia un marco de desarrollo ágil. Con esto se entiende
  que es un proyecto de software con alcance variable, al que puede añadirse
  funcionalidad o descartar funcionalidad según los objetivos y circunstancias
  externas del negocio cambien y, en cambio, se desarrolla en incrementos más
  pequeños y predecibles. Consecuentemente, la aplicación se actualiza al final
  de cada incremento, que no corresponde con un periodo regular de tiempo, sino
  con la terminación de todo el ciclo de vida del software para una funcionalidad
  pactada con el cliente. 
  
  

¿Cómo se ve reflejada la historia del proyecto en la documentación?
----------------------------------------------------------------------

Aquí hay cuadro sinóptico de la relación entre la fases del proyecto
y las partes del manual.

+------------+------------+
|Sección     |   Fases    |
+============+============+
| Incepción  | 1, 2       | 
+------------+------------+
| Guías      |    4       |
+------------+------------+
| Tablero ROD|   1        |
+------------+------------+
| Tablero RA | 4          |
+------------+------------+


##############################
CBV
##############################

Las Class Based Views son un componente
de Django muy útil, pero que rápidamente
gana complejidad. Aquí hay algunos lineamentos
para trabajar con ellas. 

¿Cómo modificar Modificar CBV?
##############################
Se hace por override, pero
hay que conocer bien el orden de
los llamados que hace la vista.


- `get_initial`
- `post`
- `form_valid`
- `get_context_data`



Checklist para una vista
##############################
Cualquier vista que se haga, necesita
adicionalmente gestionar la siguiente
funcionalidad.

- permisos
- mensajes
- redirect


¿Cómo poner permisos en CBV?
##############################
Revisar estas opciones:

- `PermissionRequiredMixin`
- recuerda `raise_exception`
- `RedirigeALogin` (Mixin propio)
  
Ver :doc:`permisos`

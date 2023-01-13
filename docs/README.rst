==============================
Guia Documentación
==============================

Ambiente
==============================
La documentación es un proyecto Sphinx.
Utiliza reStructuredText y otras utilidades.

- Sphinx
- make
- dot
- plantuml

Componentes
============

La documentación cubre diversas áreas.
Cada una debe considerarse como un componente.
Esto debe verse reflejado en el sistema de archivos.


.. code-block:: bash

	(rodam) tree -L 1 ./docs/source/./docs/source/
		├── assets
		├── conf.py
		├── desarrollo // componente 
		├── index.rst
		├── log.html
		├── log.rst
		├── operaciones // componente
		├── procesos    // componente 
		├── requerimientos // componente 
		└── ui


Dentro de un componente, se sigue convencion entre `src` y `build`.
La razón de esto es que se utiliza `make` para procesar los diagramas
y demás artefactos que se embeben dentro de rst.


Build de componente
==============================

Dentro de un componente, se utiliza `make` para procesar artefactos y ponerlos
en `./build`

.. code-block::

	docs/source/desarrollo/
	├── assets
	│   ├── ejemplo-integracion-datatables-botones.png
	│   └── ejemplo-integracion-datatables.png
	├── diagramas
	│   ├── arquitectura-snippets.dia~
	│   ├── #arquitectura-snippets.dot#
	│   ├── arquitectura-snippets.dot
	│   ├── build
	│   │   ├── arquitectura-snippets.dia.png
	│   │   ├── arquitectura-snippets.dot.png
	│   │   └── out.png
	│   ├── Makefile
	│   └── Makefile~
	├── #guia_desarrollo.rst#
	├── #guia.rst#
	├── guia.rst
	├── guia.rst~
	└── out.html

Los artefactos en `/diagramas` son procesados y puestos en `/assets`.
Los documentos .rst luego importan los assets por medio de directiva
`.. image-block:: [URL-RELATIVA]`

El Makefile de un componente puede verse de la siguiente manera

.. code-block:: makefile

	BUILD_DIR=./build/
	
	mover : plantuml dot 
		mv *.png  $(BUILD_DIR)
	
	plantuml :
		plantuml *.uml
	
	dot :
		dot *.dot -Tpng -O 
	

El build de componente **no** se hace automaticamente cuando se llama
al `make [html | pdf | tex]` o `sphinx-build -b [BUILDER] sourcedir builddir`.

Es responsabilidad del programador mantener los componentes para que sphinx
haga el build correctamente. 

BUILD_DIR=./build/

# poner resultados en build dir
mover : dot 
	mv *.png  $(BUILD_DIR)

# procesar con plantuml
#plantuml :
#	plantuml *.uml
# procesar con dot 
dot :
	dot *.dot -Tpng -O 

BUILD_DIR=./build/

mover : plantuml dot 
	mv *.png  $(BUILD_DIR)

plantuml :
	plantuml *.uml

dot :
	dot *.dot -Tpng -O 

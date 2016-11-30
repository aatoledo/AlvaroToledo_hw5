all: a.out resultados.csv corner_plot.png densityPlot.png jointPlot.png

corner_plot.png densityPlot.png jointPlot.png: resultados.csv grafica.py
	python grafica.py

resultados.csv: a.out
	./a.out

a.out: sismica.c sismica.txt
	gcc sismica.c -lm
 
clean: 
	rm *.png resultados.csv a.out

all: a.out prueba.csv resultados.csv corner_plot.png lv_obs.png lv_c.png

corner_plot.png lv_obs.png lv_c.png: resultados.csv prueba.csv grafica.py
	python grafica.py

prueba.csv resultados.csv: a.out
	./a.out

a.out: bio.c data.txt
	gcc bio.c -lm

clean:
	rm *.png resultados.csv a.out prueba.csv

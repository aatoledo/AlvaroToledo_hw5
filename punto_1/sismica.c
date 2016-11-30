#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

void modelo (float xT, float yT, float *x, float *y, float v, int n, float *ti);
float like (float *t, float *ti, int n);
float fRand(float fMin, float fMax);

int main (void){
  /*Constantes*/
  float x[6];
  float y[6];
  float t[6]; /*Tiempo Real*/
  float ti[6]; /*Tiempo EXperimental*/
  float v = 5;
  float xT = 16;
  float yT = 6;
  float xn;
  float yn;
  float alpha;
  float moneda;
  float tn[6];
  char buffer[100];
  char *record,  *line1, *line2, *line3;
  int n = 6;
  int i;
  int maxi = 100000;
  float l1;
  float l0;
  FILE *resultados = fopen("resultados.csv","w");
 
  /*Carga Data*/
  FILE *texto = fopen("sismica.txt","r");
  for (i = 0; i < n; i++){
    fscanf(texto, "%f,%f,%f\n", &x[i], &y[i], &t[i]);
  }
  modelo ( xT, yT, x, y, v, n,ti);
  l0 = like (t, ti, n);
  /*Metropolis*/
  for (i = 0; i < maxi; i++){
    xn = xT + fRand(-2,2);  
    yn = yT + fRand(-2,2);
    modelo (xn, yn, x, y, v, n,tn);
    l1 = like (t, tn, n);
    
    alpha = l1/l0;
    if (alpha >= 1.0){
      xT = xn;
      yT = yn;
      l0 = l1;
    }
    else{
      moneda = fRand(0,1);
      if(moneda <= alpha){
	xT = xn;
	yT = yn;
	l0 = l1;
      }
    }
    fprintf (resultados, "%f,%f,%f\n", xT, yT, l0);
  }
  return 0;
}

void modelo (float xT, float yT, float *x, float *y, float v, int n, float *ti){
  /*Pass By Reference*/
  float d;
  int i;
  for ( i = 0; i < n; i++){
    d = pow(pow(x[i]-xT,2) + pow(y[i]-yT,2), 0.5);
    ti[i] = d/v;
  }
}

float like (float *t, float *ti, int n){
  float c = 0;
  int i;
  for (i  = 0; i < n; i++){
    c = c + pow(t[i] - ti[i],2);
  }
  return exp(-c);
}

float fRand(float fMin, float fMax){
/* http://stackoverflow.com/questions/2704521/generate-random-double-numbers-in-c */
float f = (float)rand() / RAND_MAX;
return fMin + f * (fMax - fMin);
}

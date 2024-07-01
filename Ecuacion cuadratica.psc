//Desarrolla un algoritmo que permite obtener el resultado de una ecuaci�n cuadratica,
//teniendo en cuenta que se conoce el valor a, b y c
Algoritmo ec_cuadratica_pseint
	Definir a, b, c, base, x1, x2, r, i Como Real;
	Escribir 'Bienvenido a la ecuacion cuadratica';
	Escribir 'Ingresa el valor de a';
	Leer a;
	Escribir 'Ingresa el valor de b';
	Leer b;
	Escribir 'Ingresa el valor de c';
	Leer c;
	base = ((b*b)-(4*a*c));
	Escribir 'Base', base;
	//dos soluciones 1, 6, 8
	//solucion doble con el mismo valor 1, -4, 4
	//solucion imaginaria 2, -1, 2
	Si (a = 0) Entonces
		Escribir 'Error, no puedes dividir entre 0';
	SiNo
		Si (base >= 0) Entonces
			x1 = (-b+raiz(base))/(2*a);
			x2 = (-b-raiz(base))/(2*a);
			Escribir 'x1=', x1, ' x2=', x2;
		SiNo
			Escribir 'El resultado es imaginario';
			r = (-b/(2*a));
			i = raiz(-(base))/(2+a);
			Escribir 'x1=', r '+', i, 'i';
			Escribir 'x2=', r '-', i, 'i';
			
		Fin Si
	Fin Si
FinAlgoritmo

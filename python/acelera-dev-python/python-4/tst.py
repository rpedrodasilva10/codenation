import math
from main import calc_angle_mbc

#tst.py
"""

![Triangulo](triangulo.png)

![Triangulo](https://s3-us-west-1.amazonaws.com/codenation-challenges/python-4/triangulo.png)

## Observações

Arredonde o ângulo para o inteiro mais próximo.

Exemplos:

- Se o ângulo for 56.5000001 °, então retorne 57 °.
- Se o ângulo for 56.5000000 °, então retorne 57 °.
- Se o ângulo for de 56,4999999 °, retorno 56 °.

- O retorno deve ser em graus.


Exemplo:

	Entrada:
		10, 10
	Saida:
		45°


----------------------------------
- ABC é um triangulo retângulo, de *90°* a B.
- Assim o ângulo de *ABC = 90°*
- O ponto **M** é o ponto médio da hipotenusa **AC**.
- Você receberá os comprimentos **AB** e **BC**.

O objetivo é encontrar o ângulo **MBC**, como mostrado na figura abaixo.

"""
 
ab = 90
bc = 90

A = 90
B = 90
#C = 9.899
#print(degrees(acos(hypot(10,10))))
#print(ceil(degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))))

#print(calc_angle_mbc(ab, bc))

ab = 10
bc = 10

print(calc_angle_mbc(10,10))
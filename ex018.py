from math import sin, cos, tan, radians
Valor = float(input('Digite um ângulo: '))
print(f'''O seno de {Valor}° é {sin(radians(Valor)):.2f}
A tangente de {Valor}° é {tan(radians(Valor)):.2f}
O cosceno de {Valor}° é {cos(radians(Valor)):.2f}''')
a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Equilátero')
    if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        print('Isósceles')
    if a != b != c:
        print('Escaleno')
else:
    print('Não é um triângulo.')
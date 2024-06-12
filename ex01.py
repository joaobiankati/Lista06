numero1 = int(input("Informe o um número inteiro: "))
numero2 = int(input("Informe o um segundo número inteiro: "))
numero3 = int(input("Informe o um terceiro número inteiro: "))

if numero1 < numero2 and numero1 < numero3:
    menor_valor = numero1

if numero2 < numero1 and numero2< numero3:
    menor_valor = numero2

else:
    menor_valor = numero3

if menor_valor % 2 == 0:
    print('O menor valor é par!')

else:
    print('O menor valor é impar!')
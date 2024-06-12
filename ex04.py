saldo_medio = float(input("Informe o saldo médio do cliente no ultimo ano: "))

if saldo_medio <= 500:
    credito_banco = 0

elif 1000 <= saldo_medio >= 501:
    credito_banco = saldo_medio * 0.20

elif 1600 <= saldo_medio >= 1001:
    credito_banco = saldo_medio * 0.30

elif saldo_medio > 1600:
    credito_banco = saldo_medio * 0.40

print(f'O saldo médio é de {saldo_medio}, e o valor do crédito do banco é de {credito_banco}')
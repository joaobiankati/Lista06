votos_primeiro_candidato = int(input("Informe os votos do primeiro candidato: "))
votos_segundo_candidato = int(input("Informe os votos do segundo candidato: "))
votos_terceiro_candidato = int(input("Informe os votos do terceiro candidato: "))

total_votos = votos_primeiro_candidato + votos_segundo_candidato + votos_terceiro_candidato
percentual_votos_primeiro_candidato = (votos_primeiro_candidato / total_votos) * 100
percentual_votos_segundo_candidato = (votos_segundo_candidato / total_votos) * 100
percentual_votos_terceiro_cadidato = (votos_terceiro_candidato / total_votos) * 100

print(f'O percentual de votos do primeiro candidato é {percentual_votos_primeiro_candidato:.2f}%')
print(f'O percentual de votos do segundo candidato é {percentual_votos_segundo_candidato:.2f}%')
print(f'O percentual de votos do terceiro candidato é {percentual_votos_terceiro_cadidato:.2f}%')

if votos_primeiro_candidato > votos_segundo_candidato and votos_primeiro_candidato > votos_terceiro_candidato:
    vencedor = votos_primeiro_candidato
    print(f'O vencedor é o primeiro candidato!')

elif votos_segundo_candidato > votos_primeiro_candidato and votos_segundo_candidato > votos_terceiro_candidato:
    vencedor = votos_segundo_candidato
    print(f'O vencedor é o segundo candidato!')

else:
    print(f'O vencedor é o terceiro candidato!')
primeira_nota = float(input("Informe a primeiro nota do aluno: "))
segunda_nota= float(input("Informe a segundo nota do aluno: "))

media_notas = (primeira_nota + segunda_nota) / 2
print(media_notas)
if media_notas > 9:
    nota = "Superior"

elif media_notas <= 8.9 and media_notas >= 7:
    nota = "Médio Superior"

elif media_notas <= 6.9 and media_notas >= 5:
    nota = "Médio"

elif media_notas <= 4.9 and media_notas >= 3:
    nota = "Médio Inferior"

elif media_notas <= 2.9 and media_notas > 0.1:
    nota = "Inferior"

elif media_notas == 0:
    nota = "Sem Rendimento"

print(f'A média da nota do aluno é {media_notas}, e a sua nota é {nota}')
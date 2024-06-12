limite_curso_idiomas = 40
limite_participacao_eventos = 40
limite_visitas_tecnicas = 20
limite_cursos_extensao = 80

horas_curso_idiomas = int(input("Informe a quantidade de horas do academico no curso de idiomas: "))
horas_participacao_eventos = int(input("Informe a quantidade de horas do academico na participação de eventos: "))
horas_visitas_tecnicas = int(input("Informe a quantidade de horas do academico em visitas técnicas: "))
horas_cursos_extensao = int(input("Informe a quantidade de horas do academico em cursos de extensão: "))

total_horas = horas_curso_idiomas + horas_participacao_eventos + horas_visitas_tecnicas + horas_cursos_extensao
print(f'O total de horas do academico é de {total_horas} horas.')

horas_validas_idiomas = min(limite_curso_idiomas, horas_curso_idiomas)
horas_validas_particapacao_eventos = min(limite_participacao_eventos, horas_participacao_eventos)
horas_validas_visitas_tecnicas = min(limite_visitas_tecnicas, horas_visitas_tecnicas)
horas_validas_cursos_extensao = min(limite_cursos_extensao, horas_cursos_extensao)

total_horas_validas = horas_validas_idiomas + horas_validas_particapacao_eventos + horas_validas_visitas_tecnicas + horas_validas_cursos_extensao


print(f"Soma total das horas de todas as categorias: {total_horas} horas")
print(f"Total de horas válidas no Curso de Idiomas: {horas_validas_idiomas} horas")
print(f"Total de horas válidas na Participação em Eventos: {horas_validas_particapacao_eventos} horas")
print(f"Total de horas válidas nas Visitas Técnicas: {horas_validas_visitas_tecnicas} horas")
print(f"Total de horas válidas nos Cursos de Extensão: {horas_validas_cursos_extensao} horas")
print(f"Soma total das horas válidas de todas as categorias: {total_horas_validas} horas")

if total_horas >= 100:
    print(f'O academico atingiu as horas validas no curso!')

else:
    print('O academico não atingiu o número mínimo de horas necessárias!')
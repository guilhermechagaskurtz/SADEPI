pc_artigos_qualis_a1_cinco_autores = 8
pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo = 8
pc_artigos_qualis_a1_mais_cinco_autores_demais = 6
pc_artigos_qualis_a2_cinco_autores = 6
pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo = 6
pc_artigos_qualis_a2_mais_cinco_autores_demais = 4
pc_artigos_qualis_b1_b2_cinco_autores = 4
pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo = 4
pc_artigos_qualis_b1_b2_mais_cinco_autores_demais = 2
pc_artigos_qualis_b3_b4_cinco_autores = 3
pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo = 3
pc_artigos_qualis_b3_b4_mais_cinco_autores_demais = 1.5
pc_artigos_qualis_b5_c_cinco_autores = 2
pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo = 2
pc_artigos_qualis_b5_c_mais_cinco_autores_demais = 1
pc_trabalhos_anais_eventos = 0.2
pc_resumos_anais_eventos = 0.1
pc_licenca_direito = 3
pc_autoria_livros = 4
pc_autoria_livros_capitulos = 1
pc_orientador_teses_doutorado = 2
pc_orientador_mestrado = 1
pc_orientador_iniciacao_cientifica = 1
pc_orientador_trabalho_final_curso = 0.5

dicionario_pesos = {
 	"pc_artigos_qualis_a1_cinco_autores" : 8,
 	"pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo" : 8,
 	"pc_artigos_qualis_a1_mais_cinco_autores_demais" : 6,
 	"pc_artigos_qualis_a2_cinco_autores" : 6,
 	"pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo" : 6,
 	"pc_artigos_qualis_a2_mais_cinco_autores_demais" : 4,
 	"pc_artigos_qualis_b1_b2_cinco_autores" : 4,
 	"pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo" : 4,
 	"pc_artigos_qualis_b1_b2_mais_cinco_autores_demais" : 2,
 	"pc_artigos_qualis_b3_b4_cinco_autores" : 3,
 	"pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo" : 3,
 	"pc_artigos_qualis_b3_b4_mais_cinco_autores_demais" : 1.5,
 	"pc_artigos_qualis_b5_c_cinco_autores" : 2,
 	"pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo" : 2,
 	"pc_artigos_qualis_b5_c_mais_cinco_autores_demais" : 1,
 	"pc_trabalhos_anais_eventos" : 0.2,
 	"pc_resumos_anais_eventos" : 0.1,
 	"pc_licenca_direito" : 3,
 	"pc_autoria_livros" : 4,
 	"pc_autoria_livros_capitulos" : 1, 
 	"pc_orientador_teses_doutorado" : 2,
 	"pc_orientador_mestrado" : 1,
 	"pc_orientador_iniciacao_cientifica" : 1,
 	"pc_orientador_trabalho_final_curso" : 0.5
}

# print('Peso desta variável: ', dicionario_pesos["pc_artigos_qualis_a1_cinco_autores"])

print('Relação índice do dicionário -> resultado')
for i in dicionario_pesos:
	# print(i, ' -> ', dicionario_pesos[i])
    print(i)

print(dicionario_pesos.get("pc_orientador_trabalho_final_curso"))


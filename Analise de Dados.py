"""
O objetivo desse projeto é, à partir de uma base de dados e, por meio de análises exploratórias
usando Python, gerar insights para uma rede de lojas de açaí, de modo que seja possível entender melhor
o negócio, e tomar decisões assertivas sobre ele.
Os dados serão disponibilizados em páginas HTML, pensando na facilidade de encaminhar e projetar um link
de modo simples, evitando problemas com apresentações complexas.
"""

# Utilizaremos as bibliotecas, Pandas e Plotly
import pandas as pd
import plotly.express as px

# Importando dados da planilha
dados = pd.read_excel("vendas.xlsx")

"""
Tendo a planilha em mãos, podemos realizar os primeiros passos da análise exploratória, afim de 
aferir que tipo de informação podemos extrair da planilha.
"""
#visualisando as primeiras linhas
#dados.head()

#Verificando o formato da tabela de dados (linhas, colunas)
#dados.shape

# visualisando informações das colunas, útil para saber se há valores nulos em nossa base que necessitam
#tratamento
#dados.info()


# Um dado interessante de se avaliar, é o faturamento
# Podemos fazê-lo do ponto de vista de qualquer parâmetro. Estado, Cidade, Loja, Forma de Pagamento
# Para obter essa visualização, iremos criar uma nova base, à partir da base primária
# Agrupando dados e exportando para uma planilha
dados_agrupados = dados.groupby(["estado", "cidade", "loja", "forma_pagamento"])["preco"].sum().to_frame()
dados_agrupados.to_excel("Faturamento.xlsx")


# Gerando gráfico de faturamento por parâmetro e exportando para html

lista_colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna, 
                    y="preco",
                    text_auto=True,
                    title="Faturamento",
                    color="forma_pagamento")
    grafico.show()
    grafico.write_html(f"Faturamento-{coluna}.html")

"""
O resultado serão gráficos interativos, exportados para arquivos HTLM, onde se é possível visualizar
o faturamento dessa rede de açaí por loja, por cidade, estado, tamanho e local de consumo, bem como, 
as formas de pagamento mais usadas.

De posse dessa análise, o dono dessa rede poderia, por exemplo, avaliar um método para incentivar 
venda via pix em suas lojas, usando, por exemplo, um pequeno toten ou tag próximo ao caixa.
Isso faria com que ao ver de forma mais imediata a disponibilidade do código pix para pagamento, 
muito clientes optassem pela modalidade, ao invés de utilizarem seus cartões, o que traria benefícios
para a rede no que diz respeito à evitar pagas demasiadas taxas das máquinas de cartões.
"""
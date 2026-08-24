# README — Módulo 2: Exploração de Dados no Excel

**Trilha:** Análise de Dados — Data Analytics com Dados Abertos da PRF<br>
**Atividades:** Carregamento do CSV e Análise Inicial / Tabelas Dinâmicas e Visualizações Exploratórias

---

## Sobre esta etapa

Após a definição do problema realizada no Módulo 1, por meio do Documento de Compreensão do Negócio, a etapa seguinte dentro do CRISP-DM é a **Compreensão dos Dados**. Nesta fase, o Excel será utilizado em dois momentos: inicialmente para carregar e conhecer a base de dados e, em seguida, para investigar possíveis padrões utilizando tabelas dinâmicas e gráficos.

---

## Parte 1: Importação do CSV e Análise Inicial

**Objetivo:** carregar os registros de acidentes da PRF no Excel e verificar a estrutura e o conteúdo da base antes de iniciar as análises.

- Carregar o arquivo CSV pelo caminho (Dados > Obter Dados > De Texto/CSV), conferindo o delimitador utilizado e a codificação dos caracteres.
- Verificar a quantidade de registros (linhas) e de variáveis (colunas) disponíveis na base.
- Avaliar o formato dos campos, como texto, números e datas, realizando os ajustes necessários quando houver alguma inconsistência.
- Procurar dados ausentes, incorretos ou inconsistentes em variáveis relevantes, como `mortos`, `feridos`, `uf`, `br` e `causa_acidente`.

**Por que essa etapa é importante:** realizar essa conferência antes das análises ajuda a evitar problemas posteriores. Dados com formatos incorretos ou informações preenchidas de maneira inconsistente podem comprometer os indicadores calculados nas etapas seguintes.

---

## Parte 2: Tabelas Dinâmicas e Gráficos Exploratórios

**Objetivo:** iniciar a investigação das perguntas definidas no Módulo 1, utilizando tabelas dinâmicas para organizar e resumir os dados e gráficos para facilitar a identificação de padrões.

- Construir tabelas dinâmicas para analisar a quantidade de acidentes por UF, BR, tipo de acidente, causa, condição meteorológica, entre outras variáveis.
- Determinar a proporção de acidentes classificados como fatais (`acidente_fatal`).
- Elaborar visualizações básicas, como gráficos de barras e colunas, para facilitar a comparação entre os diferentes grupos.
- Comparar os resultados encontrados com as perguntas orientadoras e as hipóteses formuladas durante o Módulo 1.

**Por que essa etapa é importante:** essa exploração representa o primeiro momento de análise efetiva da base. A partir dos números observados, é possível confrontar as impressões e hipóteses levantadas inicialmente com aquilo que os dados realmente demonstram.

---

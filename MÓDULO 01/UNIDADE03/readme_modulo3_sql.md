# README — Módulo 3: Análises em SQL com SQLite (Configuração para SQLiteOnline)

**Trilha:** Análise de Dados — Data Analytics com Dados Abertos da PRF<br>
**Base de dados:** Registros de acidentes de 2025 organizados por ocorrência (tabela `acidentes_prf_2025`)

---

## Sobre esta etapa

Após a análise exploratória realizada no Excel durante o Módulo 2, o Módulo 3 dá continuidade à investigação utilizando SQL. Nesta fase, os dados passam a ser consultados e organizados por meio do SQLite.

---

## Atividades previstas:

**Preparação e validação**
1. Conferir a versão instalada do SQLite e verificar se ela atende aos requisitos de compatibilidade.<br>
2. Consultar a definição da tabela `acidentes_prf_2025`, identificando suas colunas e respectivos tipos.<br>
3. Levantar a quantidade total de ocorrências existentes na base.<br>

**Construção da view principal** <br>
4. Remover a view principal caso ela já esteja criada, evitando conflitos durante a execução do script.<br>
5. Montar a view base contendo a variável `acidente_fatal` (1 quando `mortos >= 1` e 0 nos demais casos), mantendo a mesma definição da variável-alvo estabelecida no Módulo 1.<br>

**Indicadores gerais e análise geográfica**<br>
6. Obter os principais indicadores gerais: quantidade total de acidentes, número de ocorrências fatais e percentual de letalidade.<br>
7. Resumir os dados por UF, apresentando acidentes, mortos e percentual de fatalidade, considerando apenas estados com no mínimo 100 ocorrências para reduzir o efeito de amostras muito pequenas.<br>
8. Identificar as 30 rodovias (BRs) com maior quantidade absoluta de mortes registradas.<br>

**Análise da dimensão temporal** <br>
9. Organizar a distribuição dos acidentes por ano e mês, utilizando a data da ocorrência como referência.<br>

**Análises bivariadas (variável explicativa x acidente_fatal)**<br>
10. Avaliar a relação entre o tipo de acidente e o percentual de ocorrências fatais.<br>
11. Selecionar as 30 principais causas de acidentes e classificá-las de acordo com a maior taxa de letalidade.<br>
12. Comparar a fase do dia (noite, pleno dia, entre outras) com a gravidade das ocorrências.<br>
13. Verificar como a condição meteorológica se relaciona com o percentual de acidentes fatais.<br>
14. Analisar a letalidade de acordo com o tipo de pista (simples, dupla ou múltipla).<br>

**Análise combinada de fatores**<br>
15. Avaliar simultaneamente Tipo de Pista e Fase do Dia, verificando também a representatividade de cada combinação em relação ao conjunto total de registros.<br>
16. Determinar o **Lift**, comparando a taxa de letalidade de cada categoria com a taxa média geral. Valores de Lift acima de 1 representam uma taxa superior à média, enquanto valores abaixo de 1 representam uma taxa inferior.<br>

**Views destinadas ao dashboard**<br>
17. Desenvolver a view `vw_indicadores_mensais`, voltada à organização dos indicadores ao longo do tempo.<br>
18. Criar a view `vw_indicadores_uf_br`, reunindo os indicadores por localização para utilização no dashboard.<br>

---

## Entregáveis

| Entrega | Descrição |
|---|---|
| **Script SQL documentado** | Arquivo `.sql` contendo as consultas explicadas e estruturadas de forma que possam ser executadas novamente por outro aluno ou avaliador |
| **Resultados em CSV** | Exportação das análises por UF, BR, mês, causa, tipo, clima e fase do dia para o diretório `resultados/` |
| **Consultas Bivariadas** | Conjunto de análises relacionando as variáveis explicativas à variável `acidente_fatal` |
| **View Consolidada** | Uma visão agregada preparada para fornecer dados ao dashboard |

---

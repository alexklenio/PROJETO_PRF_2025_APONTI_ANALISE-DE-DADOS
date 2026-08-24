<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="60px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3stUt2QFbqjexHtCMzc3bdeSS-W3C2Gerq49irznS_CMTcI5IBJ9_ZSM&s=10"></a>
    <span> APONTI - PROJETO PRF 2025</span>
</h1>

   
## Detalhes da formação
A Formação Acelerada em Programação (FAP) da APONTI, na trilha de Análise de Dados, é uma capacitação intensiva voltada à preparação de novos profissionais para o mercado de tecnologia. Na edição de 2026, o programa passou a oferecer três trilhas — Análise de Dados, DevOps e Teste de Software — com 215 horas de formação, distribuídas entre atividades presenciais e virtuais.

# Projeto PRF 2025 — Jornada de Análise de Dados

Este repositório apresenta a construção do projeto desenvolvido ao longo da trilha de Análise de Dados da Aponti Academy, utilizando como fonte dados públicos sobre acidentes ocorridos nas rodovias federais brasileiras.

A documentação acompanha a evolução do aprendizado durante as aulas, passando pela definição e entendimento do problema, exploração e preparação dos dados, consultas utilizando SQL e etapas iniciais voltadas à modelagem e à construção de dashboards.

---

## Sobre o projeto

O propósito deste trabalho é investigar os fatores relacionados aos acidentes que resultaram em vítimas fatais nas rodovias federais do Brasil, tendo como referência os registros disponibilizados pela PRF (Polícia Rodoviária Federal) referentes ao ano de 2025.

### Questão principal

Quais características e circunstâncias apresentam relação com a ocorrência de acidentes fatais nas rodovias federais brasileiras?

### Objetivo

Encontrar padrões, relações e métricas que contribuam para uma melhor compreensão dos fatores ligados à gravidade dos acidentes, considerando aspectos como:

- Estados (UF) e rodovias (BR) com maior número de acidentes fatais
- Períodos do dia e meses com maior ocorrência
- Principais tipos e causas de acidentes
- Relação entre condições climáticas, período do dia e características da pista
- Diferenças entre acidentes fatais e aqueles sem vítimas fatais

---

## Contexto da análise

O estudo parte dos dados públicos disponibilizados pela PRF, concentrando-se nos acidentes registrados nas rodovias federais brasileiras. Para a análise, a principal variável de interesse é um indicador de fatalidade derivado da quantidade de pessoas mortas em cada ocorrência.

### Definição da variável-alvo

- `acidente_fatal = 1` quando o número de mortos for maior ou igual a 1
- `acidente_fatal = 0` quando não houver registro de mortos

Com essa classificação, torna-se possível separar os registros entre acidentes fatais e não fatais, permitindo analisar a participação e a taxa de letalidade em diferentes recortes da base.

---

## Organização do repositório

```text
Estrutura do projeto
PROJETO_PRF_2025_APONTI_ANALISE-DE-DADOS/
├── README.md
└── MÓDULO 01/
    ├── UNIDADE01/
    │   ├── atividade01.txt
    │   └── atividade02.txt
    │
    ├── UNIDADE02/
    │   └── Entrega desafio aponti excel.xlsx
    │
    ├── UNIDADE03/
    │   ├── resultados/
    │   │   ├── indicadores_br.csv
    │   │   ├── indicadores_causa.csv
    │   │   ├── indicadores_clima.csv
    │   │   ├── indicadores_fase_dia.csv
    │   │   ├── indicadores_mes.csv
    │   │   ├── indicadores_tipo.csv
    │   │   └── indicadores_uf.csv
    │   │
    │   ├── RESUMO_mod_3.pdf
    │   ├── dadosprf.csv
    │   ├── dadosprf.sql
    │   └── entrega desafio aponti sql.txt
    │
    └── UNIDADE04/
        ├── familias_exemplo.csv
        ├── ods1_apresentacao.pptx
        └── ods1v5.py

---

## Progresso da trilha

### Módulo 1 — Fundamentos de Data Analytics

#### Unidade 1 — Entendimento do negócio

- Delimitação do problema a ser investigado
- Estabelecimento do objetivo do projeto
- Formulação de perguntas e hipóteses de negócio
- Definição da variável-alvo e do público interessado

#### Unidade 2 — Excel

- Primeiro contato e exploração da base
- Estruturação, organização e conferência dos dados
- Levantamento dos primeiros indicadores para compreender as informações disponíveis

#### Unidade 3 — SQL

- Investigação da estrutura dos dados
- Construção de consultas e agregações
- Apuração de indicadores de letalidade
- Análises segmentadas por UF, BR, causa, clima, tipo de acidente e período do dia
- Desenvolvimento de views destinadas ao suporte de dashboards

#### Unidade 4 — Preparação dos dados com Python

- Limpeza e tratamento das informações
- Organização dos dados para futuras análises e modelagens
- Geração de conjuntos de dados estruturados para as próximas etapas do projeto

### Repositório destinado às entregas dos desafios de projeto da formação.

<div align="center">
  <p>
      <img src="https://img.shields.io/github/languages/count/alexklenio/PROJETO_PRF_2025_APONTI_ANALISE-DE-DADOS"/>
      <img src="https://img.shields.io/github/repo-size/alexklenio/PROJETO_PRF_2025_APONTI_ANALISE-DE-DADOS"/>
      <img src="https://img.shields.io/github/last-commit/alexklenio/PROJETO_PRF_2025_APONTI_ANALISE-DE-DADOS"/>
      <img src="https://img.shields.io/github/issues/alexklenio/PROJETO_PRF_2025_APONTI_ANALISE-DE-DADOS"/>
  </p> 
</div>

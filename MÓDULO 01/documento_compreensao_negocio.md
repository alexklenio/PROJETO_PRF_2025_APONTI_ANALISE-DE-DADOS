# Documento de Compreensão do Negócio

**Trilha:** Análise de Dados — Data Analytics com Dados Abertos da PRF<br>
**Módulo 1:** Fundamentos de Data Analytics<br>
**Fase do CRISP-DM:** Compreensão do Negócio

---

## 1. Contexto e Problema

**Título do projeto:** Fatores Associados a Acidentes Fatais em Rodovias Federais Brasileiras

**Tema:** Acidentes em rodovias federais brasileiras.

**Problema central:** Quais fatores estão associados a acidentes com vítimas fatais nas rodovias federais brasileiras?

**Por que importa:** Acidentes fatais em rodovias representam perdas humanas significativas e têm alto custo social e econômico. Compreender quais fatores estão associados a desfechos fatais pode apoiar ações de prevenção, priorização de fiscalização e políticas públicas de segurança viária.

**Quem precisa da análise:** Gestores públicos de segurança viária, órgãos de fiscalização (como a própria PRF) e equipes de planejamento de infraestrutura rodoviária, que precisam priorizar onde e como atuar para reduzir a gravidade dos acidentes.

---

## 2. Objetivo e Público

**Objetivo analítico:** Identificar e descrever fatores associados à ocorrência de acidentes fatais em rodovias federais brasileiras, utilizando os Dados Abertos da PRF de 2025, para apoiar indicadores, visualizações e regras explicáveis.


**Público-alvo da análise:** Gestores e equipes técnicas responsáveis por segurança viária e políticas de prevenção de acidentes em rodovias federais.

**Que decisões podem ser apoiadas:** Priorização de trechos, horários ou condições para fiscalização e campanhas de prevenção; direcionamento de investimento em infraestrutura viária.

---

## 3. Dados e Variável-Alvo

**Fonte de dados:** Dados Abertos da PRF — CSV de Acidentes 2025, agrupados por ocorrência.

**Unidade de análise:** Cada linha representa uma ocorrência de acidente (não uma pessoa, nem um veículo), com data, local, causa registrada, tipo de acidente, número de pessoas envolvidas, feridos e mortos.

**Variável-alvo:** `acidente_fatal` — variável binária derivada do campo `mortos`.

| Regra | Resultado |
|---|---|
| `mortos ≥ 1` | `acidente_fatal = 1` |
| `mortos = 0` | `acidente_fatal = 0` |

Essa variável permite comparar acidentes fatais e não fatais, calcular proporções de fatalidade.
**Classificação binária do problema:**
- Classe 1 = acidente fatal
- Classe 0 = acidente não fatal

**Variáveis candidatas (explicativas), por grupo:**

| Grupo | Exemplos de variáveis | Uso analítico |
|---|---|---|
| Temporais | `data_inversa`, `horario`, `dia_semana` | Padrões no tempo |
| Geográficas | `uf`, `br`, `municipio`, `km` | Localização do problema |
| Explicativas do acidente | `causa_acidente`, `tipo_acidente`, `fase_dia`, `tipo_pista` | Contexto da ocorrência |
| Gravidade / Desfecho | `mortos`, `feridos`, `pessoas` | Consequências — **cuidado com vazamento**, não usar como explicativas |

---

## 4. Perguntas e Hipóteses

### 4.1 Perguntas orientadoras

1. Quais UFs e BRs concentram maior proporção de acidentes fatais?
2. Existe maior fatalidade em determinados meses ou horários do dia?
3. Quais tipos de acidente apresentam maior proporção de fatalidade?
4. Quais causas registradas estão mais associadas a acidentes fatais?
5. Condições meteorológicas adversas aumentam a proporção de acidentes fatais?
6. Pistas simples (sem separação física) apresentam maior proporção de fatalidade que pistas duplas?
7. Há diferença na proporção de fatalidade entre as diferentes fases do dia (plena noite, amanhecer, pleno dia, anoitecer)?

### 4.2 Hipóteses explicativas iniciais


1. **Condição meteorológica** — condições chuvosas ou de baixa visibilidade estão associadas a maior proporção de fatalidade.
2. **Fase do dia** — acidentes ocorridos em plena noite estão associados a maior proporção de fatalidade.
3. **Tipo de acidente** — colisões frontais estão associadas a maior proporção de fatalidade do que colisões traseiras ou saídas de pista.
4. **Tipo de pista** — pistas simples estão associadas a maior proporção de fatalidade do que pistas duplas.
5. **Traçado da via** — trechos em curva estão associados a maior proporção de acidentes fatais.
6. **Causa do acidente** — causas como ultrapassagem indevida e velocidade incompatível estão associadas a maior proporção de fatalidade do que causas como falha mecânica.
7. **Dia da semana** — acidentes em fins de semana estão associados a maior proporção de fatalidade.
8. **Localização (BR)** — determinadas rodovias concentram maior proporção de acidentes fatais, independentemente do volume total de acidentes.


---

## 5. Limites e Relação com o CRISP-DM

**Limitações iniciais da base:**
- Dados observacionais, impossibilidade de provar causalidade isoladamente.
- Categorias amplas e possíveis registros ausentes.
- Classificações genéricas e campos não preenchidos.
- Possível ausência de variáveis relevantes não registradas na base.
- Necessidade de validação das informações.
- Possíveis diferenças na forma de registro ao longo do tempo.

**Relação com as fases do CRISP-DM:**

| Fase | Aplicação no projeto |
|---|---|
| 1. Compreensão do Negócio | Este documento — define problema, objetivo, perguntas e variável-alvo |
| 2. Compreensão dos Dados | Exploração inicial no Excel e SQL  |
| 3. Preparação dos Dados | Tratamento, criação de variáveis derivadas |
| 4. Modelagem | Árvore de decisão explicável, classificando `acidente_fatal`  |
| 5. Avaliação | Verificação de coerência entre pergunta e resultado, checagem de vazamento |
| 6. Comunicação | Dashboard, relatório gerencial e apresentação final |


---



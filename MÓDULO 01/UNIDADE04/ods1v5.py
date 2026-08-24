"""
ODS 1: Erradicação da Pobreza
Mapeamento de famílias vulneráveis para priorização de auxílio emergencial,
com Score de Vulnerabilidade multicritério.
"""

import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

LINHA_DE_POBREZA = 218.00  # renda per capita de referência (R$) - ajuste conforme o critério do município

PONTOS_VULNERABILIDADE = {
    "renda_per_capita_abaixo_pobreza": 30,
    "desempregado": 20,
    "crianca_menor_6": 10,
    "idoso": 10,
    "pessoa_com_deficiencia": 15,
    "sem_saneamento": 15,
    "casa_madeira_lona": 20,
    "nao_concluiu_fundamental": 10,
}

VALORES_AUXILIO = {
    "Muito Baixa": 0.00,
    "Baixa": 200.00,
    "Média": 400.00,
    "Alta": 700.00,
    "Extrema": 1000.00,
}

COLUNAS_EXIBICAO = {
    "nome": "nome",
    "renda_familiar": "renda_fam",
    "num_dependentes": "dependentes",
    "renda_per_capita": "renda_pc",
    "score_vulnerabilidade": "score",
    "classificacao_vulnerabilidade": "classificacao",
    "valor_auxilio_sugerido": "auxilio",
}

CAMPOS_BOOLEANOS = [
    "desempregado",
    "crianca_menor_6",
    "idoso",
    "pessoa_com_deficiencia",
    "sem_saneamento",
    "casa_madeira_lona",
    "nao_concluiu_fundamental",
]

COLUNAS_CSV_ENTRADA = [
    "nome",
    "renda_familiar",
    "num_dependentes",
    "desempregado",
    "crianca_menor_6",
    "idoso",
    "pessoa_com_deficiencia",
    "sem_saneamento",
    "casa_madeira_lona",
    "nao_concluiu_fundamental",
]


def calcular_renda_per_capita(renda_familiar, num_dependentes):
    """Calcula a renda per capita da família, tratando divisão por zero.

    Quando não há dependentes informados, considera-se que toda a renda
    pertence à própria pessoa responsável pela família.
    """
    try:
        return renda_familiar / num_dependentes
    except ZeroDivisionError:
        return renda_familiar


def calcular_score_vulnerabilidade(familia, linha_de_pobreza=LINHA_DE_POBREZA):
    """Soma os pontos de vulnerabilidade da família de acordo com os critérios da ONG."""
    score = 0

    if familia["renda_per_capita"] < linha_de_pobreza:
        score += PONTOS_VULNERABILIDADE["renda_per_capita_abaixo_pobreza"]
    if familia["desempregado"]:
        score += PONTOS_VULNERABILIDADE["desempregado"]
    if familia["crianca_menor_6"]:
        score += PONTOS_VULNERABILIDADE["crianca_menor_6"]
    if familia["idoso"]:
        score += PONTOS_VULNERABILIDADE["idoso"]
    if familia["pessoa_com_deficiencia"]:
        score += PONTOS_VULNERABILIDADE["pessoa_com_deficiencia"]
    if familia["sem_saneamento"]:
        score += PONTOS_VULNERABILIDADE["sem_saneamento"]
    if familia["casa_madeira_lona"]:
        score += PONTOS_VULNERABILIDADE["casa_madeira_lona"]
    if familia["nao_concluiu_fundamental"]:
        score += PONTOS_VULNERABILIDADE["nao_concluiu_fundamental"]

    return score


def classificar_vulnerabilidade(score):
    """Converte o score numérico na faixa de vulnerabilidade correspondente."""
    if score >= 80:
        return "Extrema"
    elif score >= 60:
        return "Alta"
    elif score >= 40:
        return "Média"
    elif score >= 20:
        return "Baixa"
    else:
        return "Muito Baixa"


def calcular_auxilio_emergencial(classificacao):
    """Retorna o valor de auxílio emergencial sugerido para a classificação da família."""
    return VALORES_AUXILIO[classificacao]


def obter_valor_float(mensagem):
    """Lê um número decimal do usuário, validando a entrada."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")


def obter_valor_inteiro(mensagem):
    """Lê um número inteiro do usuário, validando a entrada."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def obter_valor_booleano(mensagem):
    """Lê uma resposta sim/não do usuário e converte para booleano."""
    while True:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


def converter_booleano_csv(valor):
    """Converte um valor de célula do CSV (texto ou número) em booleano.

    Aceita variações comuns: sim/nao, s/n, true/false, 1/0.
    """
    texto = str(valor).strip().lower()
    if texto in ("s", "sim", "true", "verdadeiro", "1", "1.0"):
        return True
    if texto in ("n", "nao", "não", "false", "falso", "0", "0.0", "", "nan"):
        return False
    raise ValueError(f"Valor booleano inválido no CSV: '{valor}'")


def coletar_familias():
    """Coleta os dados das famílias cadastradas pela ONG via input do usuário."""
    familias = []
    print("Cadastro de famílias para mapeamento de vulnerabilidade")
    print("(digite 'fim' no nome do responsável para encerrar)\n")

    while True:
        nome = input("Nome do responsável familiar: ").strip()
        if nome.lower() == "fim":
            break

        renda_familiar = obter_valor_float("Renda familiar total (R$): ")
        num_dependentes = obter_valor_inteiro("Número de dependentes: ")
        desempregado = obter_valor_booleano("Responsável está desempregado?")
        crianca_menor_6 = obter_valor_booleano("Há criança menor de 6 anos na família?")
        idoso = obter_valor_booleano("Há idoso na família?")
        pessoa_com_deficiencia = obter_valor_booleano("Há pessoa com deficiência na família?")
        sem_saneamento = obter_valor_booleano("Residência sem saneamento básico?")
        casa_madeira_lona = obter_valor_booleano("Residência é de madeira/lona?")
        nao_concluiu_fundamental = obter_valor_booleano("Responsável não concluiu o ensino fundamental?")

        familias.append({
            "nome": nome,
            "renda_familiar": renda_familiar,
            "num_dependentes": num_dependentes,
            "desempregado": desempregado,
            "crianca_menor_6": crianca_menor_6,
            "idoso": idoso,
            "pessoa_com_deficiencia": pessoa_com_deficiencia,
            "sem_saneamento": sem_saneamento,
            "casa_madeira_lona": casa_madeira_lona,
            "nao_concluiu_fundamental": nao_concluiu_fundamental,
        })
        print()

    return familias


def carregar_familias_csv(caminho):
    """Carrega as famílias a partir de um arquivo CSV.

    O CSV deve conter as colunas:
    nome, renda_familiar, num_dependentes, desempregado, crianca_menor_6,
    idoso, pessoa_com_deficiencia, sem_saneamento, casa_madeira_lona,
    nao_concluiu_fundamental
    (os campos booleanos aceitam sim/nao, s/n, true/false ou 1/0)
    """
    df_bruto = pd.read_csv(caminho)

    colunas_faltando = [col for col in COLUNAS_CSV_ENTRADA if col not in df_bruto.columns]
    if colunas_faltando:
        raise ValueError(
            f"O CSV está sem as colunas: {', '.join(colunas_faltando)}"
        )

    familias = []
    for _, linha in df_bruto.iterrows():
        familia = {
            "nome": str(linha["nome"]).strip(),
            "renda_familiar": float(linha["renda_familiar"]),
            "num_dependentes": int(linha["num_dependentes"]),
        }
        for campo in CAMPOS_BOOLEANOS:
            familia[campo] = converter_booleano_csv(linha[campo])
        familias.append(familia)

    return familias


def escolher_modo_entrada():
    """Pergunta ao usuário se os dados virão de um CSV ou de digitação manual."""
    print("Como deseja informar as famílias?")
    print("1 - Importar de um arquivo CSV")
    print("2 - Inserir manualmente")
    while True:
        escolha = input("Escolha uma opção (1/2): ").strip()
        if escolha in ("1", "2"):
            return escolha
        print("Opção inválida. Digite 1 ou 2.")


def processar_familias(familias):
    """Adiciona renda per capita, score de vulnerabilidade e classificação a cada família."""
    for familia in familias:
        familia["renda_per_capita"] = calcular_renda_per_capita(
            familia["renda_familiar"], familia["num_dependentes"]
        )
        familia["score_vulnerabilidade"] = calcular_score_vulnerabilidade(familia)
        familia["classificacao_vulnerabilidade"] = classificar_vulnerabilidade(
            familia["score_vulnerabilidade"]
        )
        familia["valor_auxilio_sugerido"] = calcular_auxilio_emergencial(
            familia["classificacao_vulnerabilidade"]
        )
    return familias


def filtrar_familias_prioritarias(familias):
    """Filtra as famílias elegíveis para auxílio emergencial (valor sugerido acima de zero) usando List Comprehension."""
    return [
        familia for familia in familias
        if familia["valor_auxilio_sugerido"] > 0
    ]


def gerar_dataframe_prioritarias(familias_prioritarias):
    """Gera o DataFrame das famílias prioritárias, ordenado da mais para a menos vulnerável."""
    colunas = [
        "nome", "renda_familiar", "num_dependentes", "renda_per_capita",
        "score_vulnerabilidade", "classificacao_vulnerabilidade", "valor_auxilio_sugerido",
    ]
    df = pd.DataFrame(familias_prioritarias, columns=colunas)

    if not df.empty:
        df = df.sort_values(
            by=["score_vulnerabilidade", "renda_per_capita"],
            ascending=[False, True],
        ).reset_index(drop=True)
        df["renda_per_capita"] = df["renda_per_capita"].round(2)
        df.index = df.index + 1  # exibição começando em 1, não em 0
        df = df.rename(columns=COLUNAS_EXIBICAO)

    return df


def formatar_moeda(valor):
    """Formata um valor numérico como moeda brasileira (ex.: R$ 1.900,00)."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "#").replace(".", ",").replace("#", ".")
    return f"R$ {texto}"


def exportar_csv(df, caminho="familias_prioritarias.csv"):
    """Exporta o DataFrame de famílias prioritárias para CSV."""
    df.to_csv(caminho, index=False, encoding="utf-8-sig")
    print(f"\nArquivo exportado: {caminho}")


def main():
    modo = escolher_modo_entrada()

    if modo == "1":
        caminho_csv = input(
            "Caminho do arquivo CSV (Enter para usar 'familias_exemplo.csv'): "
        ).strip()
        if not caminho_csv:
            caminho_csv = "familias_exemplo.csv"
        try:
            familias = carregar_familias_csv(caminho_csv)
        except (FileNotFoundError, ValueError) as erro:
            print(f"\nErro ao carregar o CSV: {erro}")
            return
    else:
        familias = coletar_familias()

    if not familias:
        print("Nenhuma família cadastrada.")
        return

    familias = processar_familias(familias)
    prioritarias = filtrar_familias_prioritarias(familias)
    df_prioritarias = gerar_dataframe_prioritarias(prioritarias)

    print(f"\nTotal de famílias cadastradas: {len(familias)}")
    print(f"Famílias elegíveis para auxílio emergencial: {len(prioritarias)}\n")
    print(df_prioritarias)

    if not df_prioritarias.empty:
        total_auxilio = df_prioritarias["auxilio"].sum()
        print(f"\nTotal de auxílio emergencial a ser distribuído: {formatar_moeda(total_auxilio)}")
        exportar_csv(df_prioritarias)


if __name__ == "__main__":
    main()

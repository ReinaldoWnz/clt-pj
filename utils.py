def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calcular_pj(salario, beneficios, incluir_ferias, incluir_13, imposto_pj, despesas):
    # Custo anual CLT
    custo_anual = salario * 12 + beneficios * 12

    if incluir_13:
        custo_anual += salario  # 13º

    if incluir_ferias:
        custo_anual += salario + (salario / 3)  # férias + 1/3 constitucional

    custo_mensal_clt = custo_anual / 12

    # Agora converte para PJ
    # Fórmula: valor_pj = (custo_mensal_clt + despesas) / (1 - imposto)
    pj_equivalente = (custo_mensal_clt + despesas) / (1 - imposto_pj)

    return {
        "custo_anual_clt": custo_anual,
        "custo_mensal_clt": custo_mensal_clt,
        "pj_equivalente": pj_equivalente
    }

import streamlit as st
from utils import calcular_pj, format_currency

st.set_page_config(
    page_title="Calculadora CLT → PJ",
    page_icon="💼",
    layout="centered"
)

# CSS opcional
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("💼 Calculadora CLT → PJ")
st.write("Descubra quanto você precisaria faturar como **PJ** para equivaler ao seu salário **CLT**.")

# Inputs
st.header("Dados CLT")

col1, col2 = st.columns(2)

with col1:
    salario = st.number_input("Salário CLT bruto (mensal)", min_value=0.0, step=100.0)
    beneficios = st.number_input("Benefícios mensais (alimentação, transporte etc)", min_value=0.0, step=50.0)

with col2:
    ferias = st.radio("Incluir Férias?", ["Sim", "Não"])
    decimo_terceiro = st.radio("Incluir 13º salário?", ["Sim", "Não"])

st.header("Dados PJ")
colp1, colp2 = st.columns(2)

with colp1:
    imposto_pj = st.number_input("Alíquota total (INSS + ISS + Simples/MEI) (%)", value=6.0, min_value=0.0) / 100

with colp2:
    despesas = st.number_input("Despesas fixas mensais (contador, nota fiscal, banco etc)", value=0.0)

if st.button("Calcular valor equivalente"):
    resultado = calcular_pj(
        salario,
        beneficios,
        ferias == "Sim",
        decimo_terceiro == "Sim",
        imposto_pj,
        despesas
    )

    st.success("Cálculo concluído!")

    st.header("Resultado 📊")

    st.metric("Faturamento PJ equivalente (mensal)", format_currency(resultado["pj_equivalente"]))

    st.subheader("Detalhamento")
    st.write(f"**Custo anual CLT:** {format_currency(resultado['custo_anual_clt'])}")
    st.write(f"**Custo mensal CLT:** {format_currency(resultado['custo_mensal_clt'])}")
    st.write(f"**Despesas PJ consideradas:** {format_currency(despesas)}")
    st.write(f"**Alíquota total aplicada:** {imposto_pj * 100:.2f}%")

    st.subheader("Comparativo CLT → PJ")
    st.table({
        "Categoria": ["CLT", "PJ"],
        "Custo Mensal": [format_currency(resultado["custo_mensal_clt"]), format_currency(resultado["pj_equivalente"])]
    })

st.markdown("---")
st.caption("Feito com ❤️ usando Streamlit")

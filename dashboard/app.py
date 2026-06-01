"""Dashboard interativo (Streamlit) do projeto de risco de crédito.

Apresenta de forma visual e interativa os principais resultados da análise e
do modelo de previsão de inadimplência. Executar com:

    uv run streamlit run dashboard/app.py

TODO: construir os componentes do dashboard (filtros, gráficos, previsões).
"""

import streamlit as st


def main() -> None:
    """Ponto de entrada do dashboard Streamlit."""
    st.set_page_config(page_title="Risco de Crédito", layout="wide")
    st.title("Análise de Risco de Crédito")
    st.write("TODO: implementar o dashboard interativo.")


if __name__ == "__main__":
    main()

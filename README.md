# Análise de Risco de Crédito 💳

Trabalho da disciplina de **Data Science**: previsão de **inadimplência em
operações de crédito** com um modelo de classificação binária treinado sobre um
dataset do Kaggle.

## Como Executar

O projeto usa [**uv**](https://docs.astral.sh/uv/) e **Python 3.12**.

```bash
# 1. reproduzir o ambiente
uv sync

# 2. rodar os notebooks
uv run jupyter lab

# 3. iniciar o dashboard
uv run streamlit run dashboard/app.py
```

> O dataset não é versionado: baixe-o do Kaggle e coloque os arquivos em
> `data/raw/`.

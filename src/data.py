"""Carregamento e limpeza dos dados de risco de crédito.

Responsável por ler o dataset bruto em ``data/raw/``, aplicar a limpeza
inicial (tratamento de valores ausentes, tipos, duplicatas, outliers) e
persistir o resultado em ``data/processed/`` para uso nas etapas seguintes.
"""

from __future__ import annotations

import pandas as pd


def load_raw_data(path: str) -> pd.DataFrame:
    """Carrega o dataset original (Kaggle) a partir de ``data/raw/``."""
    ...


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica a limpeza inicial: ausentes, duplicatas, tipos e outliers."""
    ...


def save_processed_data(df: pd.DataFrame, path: str) -> None:
    """Salva o dataset limpo/transformado em ``data/processed/``."""
    ...

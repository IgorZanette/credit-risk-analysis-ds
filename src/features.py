"""Engenharia de features para o modelo de risco de crédito.

Responsável por transformar as variáveis limpas em features prontas para a
modelagem: criação de novas variáveis, codificação de categóricas,
normalização/padronização e separação entre features (X) e alvo (y).
"""

from __future__ import annotations

import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Cria e transforma features a partir do dataset limpo."""
    ...


def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """Codifica variáveis categóricas (ex.: one-hot, ordinal)."""
    ...


def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza/padroniza as variáveis numéricas."""
    ...


def split_features_target(
    df: pd.DataFrame, target: str
) -> tuple[pd.DataFrame, pd.Series]:
    """Separa o DataFrame em features (X) e variável-alvo (y)."""
    ...

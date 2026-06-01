"""Treino e avaliação dos modelos de classificação de inadimplência.

Responsável por dividir os dados em treino/teste, treinar os algoritmos de
classificação binária, avaliá-los com métricas adequadas a dados
desbalanceados (ex.: ROC AUC, recall, F1) e persistir/carregar o modelo final.
"""

from __future__ import annotations

from typing import Any

import pandas as pd


def split_train_test(
    X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, random_state: int = 42
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Divide os dados em conjuntos de treino e teste."""
    ...


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> Any:
    """Treina um modelo de classificação binária de risco de crédito."""
    ...


def evaluate_model(model: Any, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    """Avalia o modelo e retorna as métricas de performance."""
    ...


def save_model(model: Any, path: str) -> None:
    """Persiste o modelo treinado em disco."""
    ...


def load_model(path: str) -> Any:
    """Carrega um modelo previamente treinado."""
    ...

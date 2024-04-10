# W tym pliku znajdują się rozwiązania do zadań z notatnika Google Colab.
# Zaglądaj tu tylko jeśli naprawdę nie możesz uzyskać poprawnej odpowiedzi.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv('../data/pokemon.csv', index_col=0)

def zad_1(df: pd.DataFrame, hint=False):
    if hint:
        print('\U0001f4a1 Spróbuj użyć funckji head().')
    assert type(df) == pd.DataFrame, f'Zły typ odpowiedzi. Oczekiwano: {pd.DataFrame}. Wprowadzono: {type(df)}.'

    ans = pokemon_df.head(10)

    if df.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

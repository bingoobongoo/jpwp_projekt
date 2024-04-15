# W tym pliku znajdują się rozwiązania do zadań z notatnika Google Colab.
# Zaglądaj tu tylko jeśli naprawdę nie możesz uzyskać poprawnej odpowiedzi.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv('../data/pokemon.csv', index_col=0)

def zad_1(df: pd.DataFrame, hint=False):
    if hint:
        print('\U0001f4a1 Spróbuj użyć funkcji head().')
    assert type(df) == pd.DataFrame, f'Zły typ odpowiedzi. Oczekiwano: {pd.DataFrame}. Wprowadzono: {type(df)}.'

    ans = pokemon_df.head(10)

    if df.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_2(df: pd.DataFrame, hint=False):
    if hint:
        print('\U0001f4a1 Spróbuj użyć funkcji tail().')
    assert type(df) == pd.DataFrame, f'Zły typ odpowiedzi. Oczekiwano: {pd.DataFrame}. Wprowadzono: {type(df)}.'

    ans = pokemon_df.tail()

    if df.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_3(count: int, hint=False):
    if hint:
        print('\U0001f4a1 Sprawdź atrybut `shape` obiektu `pokemon_df.')
    assert type(count) == int, f'Zły typ odpowiedzi. Oczekiwano: {int}. Wprowadzono: {type(count)}.'

    ans = pokemon_df.shape[0]

    if count == ans:
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')
    
def zad_4(count: int, hint=False):
    if hint:
        print('\U0001f4a1 Sprawdź atrybut `shape` obiektu `pokemon_df.')
    assert type(count) == int, f'Zły typ odpowiedzi. Oczekiwano: {int}. Wprowadzono: {type(count)}.'

    ans = pokemon_df.shape[1]

    if count == ans:
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_5(series: pd.Series, hint=False):
    if hint:
        print('\U0001f4a1 Spróbuj wybrać kolumnę stosując nawiasy kwadratowe [].')
    assert type(series) == pd.Series, f'Zły typ odpowiedzi. Oczekiwano: {pd.Series}. Wprowadzono: {type(series)}.'

    ans = pokemon_df['Speed']

    if series.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_6(name: str, hint=False):
    if hint:
        print('\U0001f4a1 Sprawdź atrybut `dtype` kolumny `speed_col`.')
    assert type(name) == str, f'Zły typ odpowiedzi. Oczekiwano: {str}. Wprowadzono: {type(name)}.'

    ans = pokemon_df['Speed'].dtype.name

    if name == ans:
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

# zad_7
# (pokemon_df.dtypes == 'object).sum()

def zad_8(count: int, hint=False):
    if hint:
        print('\U0001f4a1 Wybierz odpowiednią kolumnę i wykorzytaj funkcję max().')
    assert type(count) == int, f'Zły typ odpowiedzi. Oczekiwano: {int}. Wprowadzono: {type(count)}.'

    ans = pokemon_df['HP'].max()

    if count == ans:
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_9(df: pd.DataFrame, hint=False):
    if hint:
        print('\U0001f4a1 Użyj nawiasów kwadratowych [], a w nich spróbuj zapisać wyrażenie, które zwraca wartość logiczną True lub False: `pokemon_df[pokemon_df[\'HP\'] == ...]`.')
    assert type(df) == pd.DataFrame, f'Zły typ odpowiedzi. Oczekiwano: {pd.DataFrame}. Wprowadzono: {type(df)}.'

    ans = pokemon_df[pokemon_df['HP'] == pokemon_df['HP'].max()]
    # ans = pokemon_df[pokemon_df['HP'] == max_hp]

    if df.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_10(count: int, hint=False):
    if hint:
        print('\U0001f4a1 Wybierz odpowiednią kolumnę i wykorzytaj funkcję min().')
    assert type(count) == int, f'Zły typ odpowiedzi. Oczekiwano: {int}. Wprowadzono: {type(count)}.'

    ans = pokemon_df['HP'].min()

    if count == ans:
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_11(df: pd.DataFrame, hint=False):
    if hint:
        print('\U0001f4a1 Użyj nawiasów kwadratowych [], a w nich spróbuj zapisać wyrażenie, które zwraca wartość logiczną True lub False: `pokemon_df[pokemon_df[\'HP\'] == ...]`.')
    assert type(df) == pd.DataFrame, f'Zły typ odpowiedzi. Oczekiwano: {pd.DataFrame}. Wprowadzono: {type(df)}.'

    ans = pokemon_df[pokemon_df['HP'] == pokemon_df['HP'].min()]
    # ans = pokemon_df[pokemon_df['HP'] == min_hp]

    if df.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_12(series: pd.Series, hint=False):
    if hint:
        print('\U0001f4a1 Spróbuj wybrać 2 kolumny i zastosować odpowiedni operator.')
    assert type(series) == pd.Series, f'Zły typ odpowiedzi. Oczekiwano: {pd.Series}. Wprowadzono: {type(series)}.'

    ans = pokemon_df['Attack']/pokemon_df['Defense']

    if series.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_13(series: pd.Series, hint=False):
    if hint:
        print('\U0001f4a1 Spróbuj znaleźć indeks maksymalnej wartości korzystając ze zmiennej z poprzedniego zadania. Następnie użyj tego indeksu korzystając z `iloc`.')
    assert type(series) == pd.Series, f'Zły typ odpowiedzi. Oczekiwano: {pd.Series}. Wprowadzono: {type(series)}.'

    att_to_def_ratio = pokemon_df['Attack']/pokemon_df['Defense']
    max_att_def_ratio = att_to_def_ratio.max()
    idx = att_to_def_ratio[att_to_def_ratio == max_att_def_ratio].index[0]
    ans = pokemon_df.iloc[idx]

    if series.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_14(df: pd.DataFrame, hint=False):
    if hint:
        print('\U0001f4a1 Wykorzystaj filtrowanie DataFrame\'u przez połączenie kilku warunków znakiem `&`. Pamiętaj też o nawiasach między warunkami.')
    assert type(df) == pd.DataFrame, f'Zły typ odpowiedzi. Oczekiwano: {pd.DataFrame}. Wprowadzono: {type(df)}.'

    ans = pokemon_df[
            (pokemon_df['Type 2'] == 'Fighting') &
            (pokemon_df['Speed'] > 50)
        ]

    if df.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

# zad_15
# legendary_pokemon = pokemon_df[
#     (pokemon_df['Legendary'] == True) &
#     (pokemon_df['Type 1'] == 'Steel') &
#     (pokemon_df['Generation'] > 3) &
#     (pokemon_df['Speed'] > 100)
# ]

def zad_16(df: pd.DataFrame, hint=False):
    if hint:
        print('\U0001f4a1 Wykorzystaj filtrowanie DataFrame\'u przez połączenie kilku warunków znakiem `&`. Pamiętaj też o nawiasach między warunkami.')
    assert type(df) == pd.DataFrame, f'Zły typ odpowiedzi. Oczekiwano: {pd.DataFrame}. Wprowadzono: {type(df)}.'

    ans = pokemon_df[
            (pokemon_df['Total'] == 420) &
            (pokemon_df['Type 1'] == 'Dragon')
        ]

    if df.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_17(df: pd.DataFrame, hint=False):
    if hint:
        print('\U0001f4a1 Użyj filtrowania, a potem spróbuj posortować obiekt i w ten sposób wybrać odpowiedniego pokemona z pomocą funkcji `head()`.')
    assert type(df) == pd.DataFrame, f'Zły typ odpowiedzi. Oczekiwano: {pd.DataFrame}. Wprowadzono: {type(df)}.'

    ans = pokemon_df[pokemon_df['Type 1'] == 'Fire'].sort_values(by=['Defense'], ascending=False).head(1)

    if df.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_18(name: str, hint=False):
    if hint:
        print('\U0001f4a1 Spróbuj wykorzystać filtrowanie i funkcję `value_counts()`.')
    assert type(name) == str, f'Zły typ odpowiedzi. Oczekiwano: {str}. Wprowadzono: {type(name)}.'

    # pokemon_df[pokemon_df['Legendary'] == True]['Type 1'].value_counts()
    ans = 'Fire'

    if name == ans:
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

def zad_20(series: pd.Series, hint=False):
    if hint:
        print('\U0001f4a1 Wykorzystaj funkcję `value_counts()` na odpowiedniej kolumnie.')
    assert type(series) == pd.Series, f'Zły typ odpowiedzi. Oczekiwano: {pd.Series}. Wprowadzono: {type(series)}.'

    ans = pokemon_df['Generation'].value_counts()

    if series.equals(ans):
        print('\u2713 Wynik poprawny!')
    else:
        print('\u2717 Zły wynik!')

# zad_21
# generations.plot(kind='pie',
#                  title='Liczebność pokemonów w poszczególnych generacjach', 
#                  autopct='%.2f%%')

# zad_22
# flying_pokemons = pokemon_df[
#     (pokemon_df['Type 1'] == 'Flying') |
#     (pokemon_df['Type 2'] == 'Flying')
# ]

# flying_pokemons.plot(kind='scatter',
#                      title='Obrona i atak latających pokemonów',
#                      x=['Defense'],
#                      y=['Attack'],
#                      xlabel='Defense',
#                      ylabel='Attack',
#                      grid=True)
# ============================================================
# SIH/SUS - SÃO PAULO - 2024
# Construção da base amostral
# ============================================================

import os
import pandas as pd
import pyarrow.parquet as pq

# ------------------------------------------------------------
# Configurações
# ------------------------------------------------------------

N_POR_MES = 50_000
RANDOM_STATE = 42

PASTA = "/root/pysus/downloads/ducklake/sih"

dfs = []

# ------------------------------------------------------------
# Ler os 12 meses
# ------------------------------------------------------------

for mes in range(1, 13):

    nome = f"RDSP24{mes:02d}.parquet"
    caminho = os.path.join(PASTA, nome)

    print(f"\nProcessando {nome}...")

    if not os.path.exists(caminho):
        print("Arquivo não encontrado.")
        continue

    # Ler todas as colunas
    df_mes = pd.read_parquet(caminho)

    print(f"Registros disponíveis: {len(df_mes):,}")
    print(f"Variáveis: {len(df_mes.columns)}")

    # --------------------------------------------------------
    # Amostragem
    # --------------------------------------------------------

    if len(df_mes) > N_POR_MES:
        df_mes = df_mes.sample(
            n=N_POR_MES,
            random_state=RANDOM_STATE
        )

    print(f"Registros selecionados: {len(df_mes):,}")

    dfs.append(df_mes)

# ------------------------------------------------------------
# Consolidar
# ------------------------------------------------------------

df = pd.concat(
    dfs,
    ignore_index=True
)

print("\n" + "=" * 60)
print("BASE CONSOLIDADA")
print("=" * 60)

print(f"Linhas:   {len(df):,}")
print(f"Colunas:  {len(df.columns)}")

# ------------------------------------------------------------
# Visualização inicial
# ------------------------------------------------------------

print("\nPrimeiras linhas:")

display(df.head())

# ------------------------------------------------------------
# Lista de todas as variáveis
# ------------------------------------------------------------

print("\nTodas as variáveis:")

for i, coluna in enumerate(df.columns, 1):
    print(f"{i:3d} - {coluna}")

# ------------------------------------------------------------
# MORTE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("MORTE")
print("=" * 60)

display(
    df["MORTE"]
    .value_counts(dropna=False)
)

print("\nProporções:")

display(
    df["MORTE"]
    .value_counts(
        normalize=True,
        dropna=False
    )
)

# ------------------------------------------------------------
# Salvar
# ------------------------------------------------------------

os.makedirs(
    "/content/sih_2024",
    exist_ok=True
)

saida = "/content/sih_2024/sih_sp_2024_amostra.parquet"

df.to_parquet(
    saida,
    index=False
)

print("\nBase salva em:")
print(saida)

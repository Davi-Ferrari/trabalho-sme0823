from pathlib import Path
import pandas as pd

# CONFIGURAÇÕES

ARQUIVO = Path("../data/processed/sih_sp_2024_amostra.parquet")

df = pd.read_parquet(ARQUIVO)

# INFORMAÇÕES GERAIS

print("=" * 70)
print("ANÁLISE EXPLORATÓRIA - SIH/SUS")
print("=" * 70)

print(f"\nInternações: {len(df):,}")
print(f"Variáveis: {len(df.columns)}")

# VARIÁVEL RESPOSTA

print("\n" + "=" * 70)
print("ÓBITO")
print("=" * 70)

print("\nQuantidade:")
print(df["MORTE"].value_counts())

print("\nProporção (%):")
print(
    (df["MORTE"].value_counts(normalize=True) * 100)
    .round(2)
)

print(f"\nTotal de óbitos: {int(df['MORTE'].sum()):,}")
print(
    f"Proporção de óbitos: "
    f"{df['MORTE'].mean() * 100:.2f}%"
)

# ESTATÍSTICAS DESCRITIVAS

print("\n" + "=" * 70)
print("IDADE")
print("=" * 70)

print(df["IDADE"].describe())

print("\n" + "=" * 70)
print("DIAS DE PERMANÊNCIA")
print("=" * 70)

print(df["DIAS_PERM"].describe())

# DISTRIBUIÇÃO DAS VARIÁVEIS CATEGÓRICAS

for coluna in ["SEXO", "RACA_COR", "COMPLEX"]:
    print("\n" + "=" * 70)
    print(coluna)
    print("=" * 70)
    print(df[coluna].value_counts())

# UTILIZAÇÃO DE UTI

print("\n" + "=" * 70)
print("UTILIZAÇÃO DE UTI")
print("=" * 70)

print(
    df["UTI"]
    .map({0: "Não utilizou UTI", 1: "Utilizou UTI"})
    .value_counts()
)

print("\nTaxa de óbito:")

taxa_uti = (
    df.groupby("UTI")["MORTE"]
    .agg(["count", "sum", "mean"])
)

taxa_uti["mean"] *= 100

print(taxa_uti)

# FAIXAS ETÁRIAS

df["FAIXA_IDADE"] = pd.cut(
    df["IDADE"],
    bins=[-1, 17, 29, 44, 59, 74, 99],
    labels=[
        "0-17",
        "18-29",
        "30-44",
        "45-59",
        "60-74",
        "75-99"
    ]
)

print("\n" + "=" * 70)
print("TAXA DE ÓBITO POR FAIXA ETÁRIA")
print("=" * 70)

idade_morte = (
    df.groupby("FAIXA_IDADE", observed=False)["MORTE"]
    .agg(["count", "sum", "mean"])
)

idade_morte["mean"] *= 100

print(idade_morte)

# ÓBITO POR SEXO

print("\n" + "=" * 70)
print("TAXA DE ÓBITO POR SEXO")
print("=" * 70)

sexo_morte = (
    df.groupby("SEXO")["MORTE"]
    .agg(["count", "sum", "mean"])
)

sexo_morte["mean"] *= 100

print(sexo_morte)

# ÓBITO POR COMPLEXIDADE

print("\n" + "=" * 70)
print("TAXA DE ÓBITO POR COMPLEXIDADE")
print("=" * 70)

complex_morte = (
    df.groupby("COMPLEX")["MORTE"]
    .agg(["count", "sum", "mean"])
)

complex_morte["mean"] *= 100

print(complex_morte)

# DIAGNÓSTICOS MAIS FREQUENTES

print("\n" + "=" * 70)
print("20 DIAGNÓSTICOS PRINCIPAIS MAIS FREQUENTES")
print("=" * 70)

print(
    df["DIAG_PRINC"]
    .value_counts()
    .head(20)
)

# TAXA DE ÓBITO POR DIAGNÓSTICO

diag_morte = (
    df.groupby("DIAG_PRINC")["MORTE"]
    .agg(["count", "sum", "mean"])
)

diag_morte = (
    diag_morte[diag_morte["count"] >= 100]
    .sort_values("mean", ascending=False)
)

diag_morte["mean"] *= 100

print("\n" + "=" * 70)
print("DIAGNÓSTICOS COM MAIOR TAXA DE ÓBITO")
print("=" * 70)

print(diag_morte.head(20))

# IDADE E PERMANÊNCIA SEGUNDO ÓBITO

print("\n" + "=" * 70)
print("IDADE SEGUNDO ÓBITO")
print("=" * 70)

print(
    df.groupby("MORTE")["IDADE"]
    .describe()[["count", "mean", "50%", "std", "min", "max"]]
)

print("\n" + "=" * 70)
print("DIAS DE PERMANÊNCIA SEGUNDO ÓBITO")
print("=" * 70)

print(
    df.groupby("MORTE")["DIAS_PERM"]
    .describe()[["count", "mean", "50%", "std", "min", "max"]]
)

# VALIDAÇÕES

print("\n" + "=" * 70)
print("VERIFICAÇÕES")
print("=" * 70)

print(
    "Valores ausentes:",
    df.isna().sum().sum()
)

print(
    "Idades inválidas:",
    ((df["IDADE"] < 0) | (df["IDADE"] > 99)).sum()
)

print(
    "Dias de permanência negativos:",
    (df["DIAS_PERM"] < 0).sum()
)

print(
    "Valores inválidos em MORTE:",
    (~df["MORTE"].isin([0, 1])).sum()
)

print("\n" + "=" * 70)
print("ANÁLISE CONCLUÍDA")
print("=" * 70)

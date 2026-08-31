from pathlib import Path
import pandas as pd
import pyarrow.parquet as pq

# ============================================================
# CONFIGURAÇÕES
# ============================================================

PASTA_RAW = Path("../data/raw")
PASTA_PROCESSED = Path("../data/processed")

PASTA_PROCESSED.mkdir(parents=True, exist_ok=True)

ARQUIVO_SAIDA = PASTA_PROCESSED / "sih_sp_2024_amostra.parquet"

# Variáveis utilizadas na análise
COLUNAS = [
    "MORTE",
    "IDADE",
    "SEXO",
    "RACA_COR",
    "DIAS_PERM",
    "COMPLEX",
    "UTI_MES_TO",
    "DIAG_PRINC",
    "MUNIC_RES"
]

# ============================================================
# LEITURA DOS ARQUIVOS
# ============================================================

print("=" * 60)
print("LEITURA E PREPARAÇÃO DOS DADOS")
print("=" * 60)

arquivos = sorted(PASTA_RAW.glob("*.parquet"))

if not arquivos:
    raise FileNotFoundError(
        "Nenhum arquivo Parquet encontrado em data/raw/"
    )

print(f"Arquivos encontrados: {len(arquivos)}")

dfs = []

for arquivo in arquivos:
    print(f"Lendo: {arquivo.name}")

    tabela = pq.read_table(
        arquivo,
        columns=COLUNAS
    )

    df_temp = tabela.to_pandas()
    dfs.append(df_temp)

# ============================================================
# CONSOLIDAÇÃO
# ============================================================

df = pd.concat(dfs, ignore_index=True)

print(f"\nTotal de registros: {len(df):,}")

# ============================================================
# TRATAMENTO DOS TIPOS
# ============================================================

df["MORTE"] = pd.to_numeric(df["MORTE"], errors="coerce")
df["IDADE"] = pd.to_numeric(df["IDADE"], errors="coerce")
df["DIAS_PERM"] = pd.to_numeric(df["DIAS_PERM"], errors="coerce")
df["UTI_MES_TO"] = pd.to_numeric(df["UTI_MES_TO"], errors="coerce")

# Indicador de utilização de UTI
df["UTI"] = (df["UTI_MES_TO"] > 0).astype(int)

# ============================================================
# REMOÇÃO DE REGISTROS INCONSISTENTES
# ============================================================

df = df[
    df["MORTE"].isin([0, 1])
    & df["IDADE"].between(0, 99)
    & (df["DIAS_PERM"] >= 0)
].copy()

# ============================================================
# AMOSTRAGEM
# ============================================================

# Mantém uma quantidade manejável para a análise inicial
N_AMOSTRA = min(600_000, len(df))

df = df.sample(
    n=N_AMOSTRA,
    random_state=42
).reset_index(drop=True)

# ============================================================
# SALVAMENTO
# ============================================================

df.to_parquet(
    ARQUIVO_SAIDA,
    index=False
)

print("\n" + "=" * 60)
print("BASE PROCESSADA")
print("=" * 60)
print(f"Linhas: {len(df):,}")
print(f"Colunas: {len(df.columns)}")
print(f"Arquivo salvo em: {ARQUIVO_SAIDA}")

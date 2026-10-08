
import os
import gc
import pandas as pd
import pysus


PASTA = "/root/pysus/downloads/ducklake/sih"

N_POR_MES = 50_000
RANDOM_STATE = 42

VARIAVEIS = [
    "MORTE",
    "IDADE",
    "SEXO",
    "RACA_COR",
    "DIAS_PERM",
    "COMPLEX",
    "UTI_MES_IN",
    "UTI_MES_AN",
    "UTI_MES_AL",
    "UTI_MES_TO",
    "DIAG_PRINC",
    "MUNIC_RES"
]

# Criar pasta caso ainda não exista
os.makedirs(PASTA, exist_ok=True)

amostras = []

for mes in range(1, 13):

    arquivo_rd = f"RDSP24{mes:02d}.parquet"
    caminho_rd = os.path.join(PASTA, arquivo_rd)

    print("\n" + "=" * 65)
    print(f"MÊS {mes:02d}/2024")
    print("=" * 65)


    if not os.path.exists(caminho_rd):

        print("Baixando dados do mês...")

        arquivos = pysus.sih(
            state="SP",
            year=2024,
            month=mes
        )

        # Procurar especificamente o arquivo RD de SP
        candidatos = [
            arq for arq in arquivos
            if os.path.basename(arq) == arquivo_rd
        ]

        if len(candidatos) == 0:
            raise FileNotFoundError(
                f"\nNão foi encontrado o arquivo esperado:\n"
                f"{arquivo_rd}\n\n"
                f"Arquivos retornados pelo PySUS:\n{arquivos}"
            )

        caminho_rd = candidatos[0]

    else:
        print("Arquivo já encontrado no cache.")

  
    df_mes = pd.read_parquet(
        caminho_rd,
        columns=VARIAVEIS
    )

    print(f"Registros disponíveis: {len(df_mes):,}")

    n = min(N_POR_MES, len(df_mes))

    df_mes = df_mes.sample(
        n=n,
        random_state=RANDOM_STATE
    ).reset_index(drop=True)

    print(f"Registros selecionados: {len(df_mes):,}")

    
    amostras.append(df_mes)

    # Liberar objetos temporários
    del df_mes

    gc.collect()

    print("Memória temporária liberada.")


print("\n" + "=" * 65)
print("CONCATENANDO AS AMOSTRAS")
print("=" * 65)

df = pd.concat(
    amostras,
    ignore_index=True
)

# Liberar lista intermediária
del amostras
gc.collect()


print("\n" + "=" * 65)
print("BASE FINAL")
print("=" * 65)

print(f"Dimensão: {df.shape}")
print(f"Registros: {len(df):,}")
print(f"Variáveis: {len(df.columns)}")

print("\nColunas:")
for coluna in df.columns:
    print(f"  - {coluna}")

print("\nDistribuição da variável resposta:")
print(df["MORTE"].value_counts(dropna=False))

print("\nPercentuais:")
print(
    df["MORTE"]
    .value_counts(normalize=True, dropna=False)
    .mul(100)
    .round(2)
)

print("=" * 70)
print("DIMENSÃO DA BASE")
print("=" * 70)

print(f"Linhas:    {df.shape[0]:,}")
print(f"Colunas:   {df.shape[1]}")


print("\n" + "=" * 70)
print("NOMES DAS VARIÁVEIS")
print("=" * 70)

for i, coluna in enumerate(df.columns, start=1):
    print(f"{i:2d}. {coluna}")


print("\n" + "=" * 70)
print("TIPOS DAS VARIÁVEIS")
print("=" * 70)

print(df.dtypes)


print("\n" + "=" * 70)
print("PRIMEIRAS 5 OBSERVAÇÕES")
print("=" * 70)

display(df.head())


print("\n" + "=" * 70)
print("ÚLTIMAS 5 OBSERVAÇÕES")
print("=" * 70)

display(df.tail())


print("\n" + "=" * 70)
print("MEMÓRIA UTILIZADA")
print("=" * 70)

memoria_mb = df.memory_usage(deep=True).sum() / 1024**2

print(f"{memoria_mb:.2f} MB")



print("=" * 70)
print("VALORES AUSENTES POR VARIÁVEL")
print("=" * 70)

faltantes = pd.DataFrame({
    "Ausentes": df.isna().sum(),
    "Percentual (%)": (
        df.isna().mean() * 100
    ).round(4)
})

print(faltantes)


print("\n" + "=" * 70)
print("TOTAL DE VALORES AUSENTES")
print("=" * 70)

total_ausentes = df.isna().sum().sum()

print(f"Total: {total_ausentes:,}")


print("\n" + "=" * 70)
print("LINHAS COM PELO MENOS UM VALOR AUSENTE")
print("=" * 70)

linhas_ausentes = df.isna().any(axis=1).sum()

print(f"Linhas: {linhas_ausentes:,}")
print(
    f"Percentual: "
    f"{linhas_ausentes / len(df) * 100:.4f}%"
)



print("=" * 70)
print("1. MORTE")
print("=" * 70)

print(df["MORTE"].value_counts(dropna=False).sort_index())


print("\n" + "=" * 70)
print("2. IDADE")
print("=" * 70)

idade_num = pd.to_numeric(df["IDADE"], errors="coerce")

print("Valores não numéricos:")
print(idade_num.isna().sum())

print("\nMínimo:", idade_num.min())
print("Máximo:", idade_num.max())

print("\nValores únicos menores que 0:")
print(sorted(idade_num[idade_num < 0].unique()))

print("\nValores únicos:")
print(sorted(idade_num.unique())[:20], "...",
      sorted(idade_num.unique())[-20:])


print("\n" + "=" * 70)
print("3. SEXO")
print("=" * 70)

print(df["SEXO"].value_counts(dropna=False).sort_index())


print("\n" + "=" * 70)
print("4. RACA_COR")
print("=" * 70)

print(df["RACA_COR"].value_counts(dropna=False).sort_index())


print("\n" + "=" * 70)
print("5. DIAS_PERM")
print("=" * 70)

dias_num = pd.to_numeric(df["DIAS_PERM"], errors="coerce")

print("Valores não numéricos:")
print(dias_num.isna().sum())

print("\nMínimo:", dias_num.min())
print("Máximo:", dias_num.max())

print("\nValores negativos:")
print(dias_num[dias_num < 0].value_counts().sort_index())


print("\n" + "=" * 70)
print("6. COMPLEX")
print("=" * 70)

print(df["COMPLEX"].value_counts(dropna=False).sort_index())


print("\n" + "=" * 70)
print("7. VARIÁVEIS DE UTI")
print("=" * 70)

for coluna in [
    "UTI_MES_IN",
    "UTI_MES_AN",
    "UTI_MES_AL",
    "UTI_MES_TO"
]:

    valores = pd.to_numeric(
        df[coluna],
        errors="coerce"
    )

    print(f"\n{coluna}")
    print("-" * 30)
    print("Não numéricos:", valores.isna().sum())
    print("Mínimo:", valores.min())
    print("Máximo:", valores.max())
    print("Negativos:", (valores < 0).sum())


print("\n" + "=" * 70)
print("8. DIAG_PRINC")
print("=" * 70)

print("Quantidade de categorias:",
      df["DIAG_PRINC"].nunique())

print("\nPrimeiras categorias:")
print(
    df["DIAG_PRINC"]
    .value_counts()
    .head(20)
)


print("\n" + "=" * 70)
print("9. MUNIC_RES")
print("=" * 70)

print("Quantidade de municípios:",
      df["MUNIC_RES"].nunique())

print("\nPrimeiros códigos:")
print(
    df["MUNIC_RES"]
    .value_counts()
    .head(20)
)

df_analise = df.copy()

df_analise["MORTE"] = pd.to_numeric(
    df_analise["MORTE"],
    errors="raise"
).astype(int)

df_analise["IDADE"] = pd.to_numeric(
    df_analise["IDADE"],
    errors="raise"
).astype(int)

df_analise["DIAS_PERM"] = pd.to_numeric(
    df_analise["DIAS_PERM"],
    errors="raise"
).astype(int)

for coluna in [
    "UTI_MES_IN",
    "UTI_MES_AN",
    "UTI_MES_AL",
    "UTI_MES_TO"
]:
    df_analise[coluna] = pd.to_numeric(
        df_analise[coluna],
        errors="raise"
    ).astype(int)


for coluna in [
    "SEXO",
    "RACA_COR",
    "COMPLEX",
    "DIAG_PRINC",
    "MUNIC_RES"
]:
    df_analise[coluna] = df_analise[coluna].astype("category")


df_analise["UTI"] = (
    df_analise["UTI_MES_TO"] > 0
).astype(int)


print("=" * 70)
print("TIPOS APÓS TRANSFORMAÇÃO")
print("=" * 70)

print(df_analise.dtypes)


print("\n" + "=" * 70)
print("DIMENSÃO")
print("=" * 70)

print(df_analise.shape)


print("\n" + "=" * 70)
print("DISTRIBUIÇÃO DO INDICADOR DE UTI")
print("=" * 70)

print(
    df_analise["UTI"]
    .value_counts()
    .sort_index()
)

print("\nPercentuais:")

print(
    df_analise["UTI"]
    .value_counts(normalize=True)
    .sort_index()
    .mul(100)
    .round(2)
)


print("\n" + "=" * 70)
print("VERIFICAÇÃO DE AUSENTES APÓS TRANSFORMAÇÃO")
print("=" * 70)

print(df_analise.isna().sum())


contagem_morte = df_analise["MORTE"].value_counts().sort_index()

percentual_morte = (
    df_analise["MORTE"]
    .value_counts(normalize=True)
    .sort_index()
    .mul(100)
    .round(2)
)

tabela_morte = pd.DataFrame({
    "Frequência": contagem_morte,
    "Percentual (%)": percentual_morte
})

print("=" * 70)
print("DISTRIBUIÇÃO DA VARIÁVEL RESPOSTA — MORTE")
print("=" * 70)
print(tabela_morte)

print("\n" + "=" * 70)
print("RAZÃO ENTRE NÃO ÓBITOS E ÓBITOS")
print("=" * 70)

n_nao_obito = (df_analise["MORTE"] == 0).sum()
n_obito = (df_analise["MORTE"] == 1).sum()

print(f"Não óbitos: {n_nao_obito:,}")
print(f"Óbitos:     {n_obito:,}")
print(f"Razão não óbito : óbito = {n_nao_obito / n_obito:.2f} : 1")



variaveis_quantitativas = ["IDADE", "DIAS_PERM"]

tabela_descritiva = pd.DataFrame({
    "Mínimo": df_analise[variaveis_quantitativas].min(),
    "Q1": df_analise[variaveis_quantitativas].quantile(0.25),
    "Mediana": df_analise[variaveis_quantitativas].median(),
    "Média": df_analise[variaveis_quantitativas].mean(),
    "Q3": df_analise[variaveis_quantitativas].quantile(0.75),
    "Máximo": df_analise[variaveis_quantitativas].max(),
    "Desvio-padrão": df_analise[variaveis_quantitativas].std()
})

tabela_descritiva = tabela_descritiva.round(2)

print("=" * 70)
print("ESTATÍSTICAS DESCRITIVAS")
print("=" * 70)
print(tabela_descritiva)

tabela_por_morte = (
    df_analise
    .groupby("MORTE", observed=True)[["IDADE", "DIAS_PERM"]]
    .agg([
        "count",
        "mean",
        "median",
        "std",
        "min",
        "max"
    ])
    .round(2)
)

print("=" * 70)
print("ESTATÍSTICAS DESCRITIVAS POR MORTE")
print("=" * 70)
print(tabela_por_morte)



import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

plt.hist(
    df_analise.loc[df_analise["MORTE"] == 0, "IDADE"],
    bins=20,
    alpha=0.6,
    label="Não óbito",
    density=True
)

plt.hist(
    df_analise.loc[df_analise["MORTE"] == 1, "IDADE"],
    bins=20,
    alpha=0.6,
    label="Óbito",
    density=True
)

plt.xlabel("Idade")
plt.ylabel("Densidade")
plt.title("Distribuição da idade segundo ocorrência de óbito")
plt.legend()
plt.grid(axis="y", alpha=0.2)

plt.show()

plt.figure(figsize=(9, 5))

df_analise.boxplot(
    column="DIAS_PERM",
    by="MORTE"
)

plt.xlabel("Morte")
plt.ylabel("Dias de permanência")
plt.title("Distribuição dos dias de permanência segundo ocorrência de óbito")
plt.suptitle("")
plt.grid(axis="y", alpha=0.2)

plt.show()



tabela_sexo = (
    df_analise
    .groupby("SEXO", observed=True)
    .agg(
        Internacoes=("MORTE", "size"),
        Obitos=("MORTE", "sum")
    )
)

tabela_sexo["Percentual (%)"] = (
    tabela_sexo["Internacoes"]
    / tabela_sexo["Internacoes"].sum()
    * 100
).round(2)

tabela_sexo["Taxa_de_obito (%)"] = (
    tabela_sexo["Obitos"]
    / tabela_sexo["Internacoes"]
    * 100
).round(2)

print("=" * 70)
print("ANÁLISE DE SEXO SEGUNDO MORTE")
print("=" * 70)
print(tabela_sexo)




tabela_raca = (
    df_analise
    .groupby("RACA_COR", observed=True)
    .agg(
        Internacoes=("MORTE", "size"),
        Obitos=("MORTE", "sum")
    )
)

tabela_raca["Percentual (%)"] = (
    tabela_raca["Internacoes"]
    / tabela_raca["Internacoes"].sum()
    * 100
).round(2)

tabela_raca["Taxa_de_obito (%)"] = (
    tabela_raca["Obitos"]
    / tabela_raca["Internacoes"]
    * 100
).round(2)

print("=" * 70)
print("ANÁLISE DE RACA_COR SEGUNDO MORTE")
print("=" * 70)
print(tabela_raca)



tabela_complex = (
    df_analise
    .groupby("COMPLEX", observed=True)
    .agg(
        Internacoes=("MORTE", "size"),
        Obitos=("MORTE", "sum")
    )
)

tabela_complex["Percentual (%)"] = (
    tabela_complex["Internacoes"]
    / tabela_complex["Internacoes"].sum()
    * 100
).round(2)

tabela_complex["Taxa_de_obito (%)"] = (
    tabela_complex["Obitos"]
    / tabela_complex["Internacoes"]
    * 100
).round(2)

print("=" * 70)
print("ANÁLISE DE COMPLEX SEGUNDO MORTE")
print("=" * 70)
print(tabela_complex)



tabela_uti = (
    df_analise
    .groupby("UTI", observed=True)
    .agg(
        Internacoes=("MORTE", "size"),
        Obitos=("MORTE", "sum")
    )
)

tabela_uti["Percentual (%)"] = (
    tabela_uti["Internacoes"]
    / tabela_uti["Internacoes"].sum()
    * 100
).round(2)

tabela_uti["Taxa_de_obito (%)"] = (
    tabela_uti["Obitos"]
    / tabela_uti["Internacoes"]
    * 100
).round(2)

print("=" * 70)
print("ANÁLISE DE UTI SEGUNDO MORTE")
print("=" * 70)
print(tabela_uti)



taxa_uti = tabela_uti.reset_index()

plt.figure(figsize=(7, 5))

plt.bar(
    taxa_uti["UTI"].astype(str),
    taxa_uti["Taxa_de_obito (%)"]
)

plt.xlabel("Registro de UTI")
plt.ylabel("Taxa de óbito (%)")
plt.title("Taxa de óbito segundo registro de UTI")

for i, valor in enumerate(taxa_uti["Taxa_de_obito (%)"]):
    plt.text(
        i,
        valor + 0.5,
        f"{valor:.2f}%",
        ha="center"
    )

plt.ylim(0, max(taxa_uti["Taxa_de_obito (%)"]) * 1.2)
plt.grid(axis="y", alpha=0.2)

plt.show()


tabela_diag = (
    df_analise
    .groupby("DIAG_PRINC", observed=True)
    .agg(
        Internacoes=("MORTE", "size"),
        Obitos=("MORTE", "sum")
    )
)

tabela_diag["Percentual (%)"] = (
    tabela_diag["Internacoes"]
    / len(df_analise)
    * 100
).round(2)

tabela_diag["Taxa_de_obito (%)"] = (
    tabela_diag["Obitos"]
    / tabela_diag["Internacoes"]
    * 100
).round(2)

top20_diag = (
    tabela_diag
    .sort_values("Internacoes", ascending=False)
    .head(20)
)

print("=" * 70)
print("20 DIAGNÓSTICOS PRINCIPAIS MAIS FREQUENTES")
print("=" * 70)
print(top20_diag)



frequencia_diag = (
    df_analise["DIAG_PRINC"]
    .value_counts()
)

print("=" * 70)
print("CONCENTRAÇÃO DOS DIAGNÓSTICOS")
print("=" * 70)

for n in [10, 20, 50, 100, 500, 1000]:
    quantidade = frequencia_diag.head(n).sum()
    percentual = quantidade / len(df_analise) * 100

    print(
        f"Top {n:4d} diagnósticos: "
        f"{quantidade:7d} internações "
        f"({percentual:6.2f}%)"
    )

print("\n" + "=" * 70)
print("NÚMERO DE CATEGORIAS")
print("=" * 70)

print(f"Total de diagnósticos distintos: {frequencia_diag.size}")
print(
    f"Diagnósticos com apenas 1 internação: "
    f"{(frequencia_diag == 1).sum()}"
)
print(
    f"Diagnósticos com até 5 internações: "
    f"{(frequencia_diag <= 5).sum()}"
)
print(
    f"Diagnósticos com mais de 100 internações: "
    f"{(frequencia_diag > 100).sum()}"
)


diag_prefixo = (
    df_analise["DIAG_PRINC"]
    .astype(str)
    .str[0]
)

tabela_diag_prefixo = (
    pd.DataFrame({
        "DIAG_GRUPO": diag_prefixo,
        "MORTE": df_analise["MORTE"].values
    })
    .groupby("DIAG_GRUPO")
    .agg(
        Internacoes=("MORTE", "size"),
        Obitos=("MORTE", "sum")
    )
)

tabela_diag_prefixo["Percentual (%)"] = (
    tabela_diag_prefixo["Internacoes"]
    / len(df_analise)
    * 100
).round(2)

tabela_diag_prefixo["Taxa_de_obito (%)"] = (
    tabela_diag_prefixo["Obitos"]
    / tabela_diag_prefixo["Internacoes"]
    * 100
).round(2)

tabela_diag_prefixo = tabela_diag_prefixo.sort_index()

print("=" * 70)
print("DIAG_PRINC — AGRUPAMENTO PELO PRIMEIRO CARACTERE")
print("=" * 70)
print(tabela_diag_prefixo)



print("=" * 70)
print("DISTRIBUIÇÃO DOS GRUPOS DE DIAG_PRINC")
print("=" * 70)

print(tabela_diag_prefixo[[
    "Internacoes",
    "Obitos",
    "Percentual (%)",
    "Taxa_de_obito (%)"
]])

print("\n" + "=" * 70)
print("VERIFICAÇÃO DE GRUPOS COM BAIXA FREQUÊNCIA")
print("=" * 70)

print(
    "Grupos com menos de 100 internações:",
    (tabela_diag_prefixo["Internacoes"] < 100).sum()
)

print(
    "Grupos com menos de 500 internações:",
    (tabela_diag_prefixo["Internacoes"] < 500).sum()
)

print(
    "Grupos com pelo menos 1.000 internações:",
    (tabela_diag_prefixo["Internacoes"] >= 1000).sum()
)



df_analise["DIAG_GRUPO"] = (
    df_analise["DIAG_PRINC"]
    .astype(str)
    .str[0]
    .astype("category")
)

print("=" * 70)
print("VARIÁVEL DIAG_GRUPO")
print("=" * 70)

print("Número de categorias:", df_analise["DIAG_GRUPO"].nunique())

print("\nCategorias:")
print(df_analise["DIAG_GRUPO"].cat.categories.tolist())

print("\nTipos:")
print(df_analise["DIAG_GRUPO"].dtype)

print("\nAusentes:")
print(df_analise["DIAG_GRUPO"].isna().sum())


frequencia_municipio = (
    df_analise["MUNIC_RES"]
    .value_counts()
)

print("=" * 70)
print("CONCENTRAÇÃO DE MUNIC_RES")
print("=" * 70)

for n in [10, 20, 50, 100, 500, 1000]:
    quantidade = frequencia_municipio.head(n).sum()
    percentual = quantidade / len(df_analise) * 100

    print(
        f"Top {n:4d} municípios: "
        f"{quantidade:7d} internações "
        f"({percentual:6.2f}%)"
    )

print("\n" + "=" * 70)
print("NÚMERO DE MUNICÍPIOS")
print("=" * 70)

print(
    f"Total de municípios distintos: "
    f"{frequencia_municipio.size}"
)

print(
    f"Municípios com apenas 1 internação: "
    f"{(frequencia_municipio == 1).sum()}"
)

print(
    f"Municípios com até 5 internações: "
    f"{(frequencia_municipio <= 5).sum()}"
)

print(
    f"Municípios com mais de 1000 internações: "
    f"{(frequencia_municipio > 1000).sum()}"
)

tabela_municipio = (
    df_analise
    .groupby("MUNIC_RES", observed=True)
    .agg(
        Internacoes=("MORTE", "size"),
        Obitos=("MORTE", "sum")
    )
)

tabela_municipio["Taxa_de_obito (%)"] = (
    tabela_municipio["Obitos"]
    / tabela_municipio["Internacoes"]
    * 100
)

print("=" * 70)
print("TAXA DE ÓBITO POR MUNICÍPIO")
print("=" * 70)

print(
    tabela_municipio["Taxa_de_obito (%)"]
    .describe()
    .round(2)
)

print("\n" + "=" * 70)
print("MUNICÍPIOS COM MAIOR FREQUÊNCIA")
print("=" * 70)

print(
    tabela_municipio
    .sort_values("Internacoes", ascending=False)
    .head(20)
    .round(2)
)


frequencia_diagnostico = df_analise["DIAG_PRINC"].value_counts()

print("=" * 70)
print("CONCENTRAÇÃO DE DIAG_PRINC")
print("=" * 70)

for n in [10, 20, 50, 100, 500, 1000, 2000]:
    quantidade = frequencia_diagnostico.head(n).sum()
    percentual = quantidade / len(df_analise) * 100

    print(
        f"Top {n:4d} diagnósticos: "
        f"{quantidade:6d} internações "
        f"({percentual:6.2f}%)"
    )

print("\n" + "=" * 70)
print("NÚMERO DE DIAGNÓSTICOS")
print("=" * 70)

print(
    f"Total de diagnósticos distintos: "
    f"{frequencia_diagnostico.size}"
)

print(
    f"Diagnósticos com apenas 1 internação: "
    f"{(frequencia_diagnostico == 1).sum()}"
)

print(
    f"Diagnósticos com até 5 internações: "
    f"{(frequencia_diagnostico <= 5).sum()}"
)

print(
    f"Diagnósticos com mais de 100 internações: "
    f"{(frequencia_diagnostico > 100).sum()}"
)



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

contagem_morte = df_analise["MORTE"].value_counts().sort_index()
percentual_morte = (
    df_analise["MORTE"].value_counts(normalize=True).sort_index() * 100
)

plt.figure(figsize=(6, 4))

barras = plt.bar(
    ["Não óbito (0)", "Óbito (1)"],
    contagem_morte.values
)

plt.title("Distribuição do desfecho hospitalar")
plt.ylabel("Número de internações")

for barra, percentual in zip(barras, percentual_morte.values):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height(),
        f"{percentual:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 4))

plt.hist(
    df_analise.loc[df_analise["MORTE"] == 0, "IDADE"],
    bins=20,
    alpha=0.65,
    label="Não óbito"
)

plt.hist(
    df_analise.loc[df_analise["MORTE"] == 1, "IDADE"],
    bins=20,
    alpha=0.65,
    label="Óbito"
)

plt.title("Distribuição da idade segundo o desfecho")
plt.xlabel("Idade")
plt.ylabel("Número de internações")
plt.legend()

plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 4))

plt.boxplot(
    [
        df_analise.loc[df_analise["MORTE"] == 0, "DIAS_PERM"],
        df_analise.loc[df_analise["MORTE"] == 1, "DIAS_PERM"]
    ],
    labels=["Não óbito", "Óbito"],
    showfliers=False
)

plt.title("Dias de permanência segundo o desfecho")
plt.ylabel("Dias de permanência")

plt.tight_layout()
plt.show()


taxa_uti = (
    df_analise.groupby("UTI", observed=True)["MORTE"]
    .mean()
    .mul(100)
)

plt.figure(figsize=(6, 4))

barras = plt.bar(
    ["Sem UTI", "Com UTI"],
    taxa_uti.values
)

plt.title("Taxa de óbito segundo utilização de UTI")
plt.ylabel("Taxa de óbito (%)")

for barra, valor in zip(barras, taxa_uti.values):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height(),
        f"{valor:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


taxa_sexo = (
    df_analise.groupby("SEXO", observed=True)["MORTE"]
    .mean()
    .mul(100)
)

plt.figure(figsize=(6, 4))

barras = plt.bar(
    taxa_sexo.index.astype(str),
    taxa_sexo.values
)

plt.title("Taxa de óbito segundo sexo")
plt.xlabel("Código de sexo")
plt.ylabel("Taxa de óbito (%)")

for barra, valor in zip(barras, taxa_sexo.values):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height(),
        f"{valor:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


taxa_raca = (
    df_analise.groupby("RACA_COR", observed=True)["MORTE"]
    .mean()
    .mul(100)
)

plt.figure(figsize=(7, 4))

barras = plt.bar(
    taxa_raca.index.astype(str),
    taxa_raca.values
)

plt.title("Taxa de óbito segundo raça/cor")
plt.xlabel("Código de raça/cor")
plt.ylabel("Taxa de óbito (%)")

for barra, valor in zip(barras, taxa_raca.values):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height(),
        f"{valor:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


taxa_complex = (
    df_analise.groupby("COMPLEX", observed=True)["MORTE"]
    .mean()
    .mul(100)
)

plt.figure(figsize=(6, 4))

barras = plt.bar(
    taxa_complex.index.astype(str),
    taxa_complex.values
)

plt.title("Taxa de óbito segundo complexidade")
plt.xlabel("Código de complexidade")
plt.ylabel("Taxa de óbito (%)")

for barra, valor in zip(barras, taxa_complex.values):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height(),
        f"{valor:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


top20_diag = df_analise["DIAG_PRINC"].value_counts().head(20)

plt.figure(figsize=(9, 6))

plt.barh(
    top20_diag.index.astype(str)[::-1],
    top20_diag.values[::-1]
)

plt.title("20 diagnósticos principais mais frequentes")
plt.xlabel("Número de internações")
plt.ylabel("Diagnóstico principal")

plt.tight_layout()
plt.show()


diag_20 = top20_diag.index

taxa_diag = (
    df_analise[df_analise["DIAG_PRINC"].isin(diag_20)]
    .groupby("DIAG_PRINC", observed=True)["MORTE"]
    .mean()
    .mul(100)
    .sort_values()
)

plt.figure(figsize=(9, 6))

plt.barh(
    taxa_diag.index.astype(str),
    taxa_diag.values
)

plt.title("Taxa de óbito dos 20 diagnósticos mais frequentes")
plt.xlabel("Taxa de óbito (%)")
plt.ylabel("Diagnóstico principal")

plt.tight_layout()
plt.show()


frequencia_grupo = df_analise["DIAG_GRUPO"].value_counts().sort_index()

plt.figure(figsize=(9, 4))

plt.bar(
    frequencia_grupo.index.astype(str),
    frequencia_grupo.values
)

plt.title("Distribuição dos grupos de diagnóstico")
plt.xlabel("Primeiro caractere do código do diagnóstico")
plt.ylabel("Número de internações")

plt.tight_layout()
plt.show()


taxa_grupo = (
    df_analise.groupby("DIAG_GRUPO", observed=True)["MORTE"]
    .mean()
    .mul(100)
    .sort_values()
)

plt.figure(figsize=(9, 5))

plt.barh(
    taxa_grupo.index.astype(str),
    taxa_grupo.values
)

plt.title("Taxa de óbito segundo grupo de diagnóstico")
plt.xlabel("Taxa de óbito (%)")
plt.ylabel("Grupo de diagnóstico")

plt.tight_layout()
plt.show()


frequencia_municipio = df_analise["MUNIC_RES"].value_counts()

n_municipios = np.array([10, 20, 50, 100, 500, 1000])

percentuais_municipio = [
    frequencia_municipio.head(n).sum() / len(df_analise) * 100
    for n in n_municipios
]

plt.figure(figsize=(7, 4))

plt.plot(
    n_municipios,
    percentuais_municipio,
    marker="o"
)

plt.title("Concentração das internações por município de residência")
plt.xlabel("Número de municípios mais frequentes")
plt.ylabel("Internações acumuladas (%)")

plt.xticks(n_municipios)
plt.ylim(0, 105)

plt.tight_layout()
plt.show()


top20_municipios = frequencia_municipio.head(20).index

taxa_municipio = (
    df_analise[df_analise["MUNIC_RES"].isin(top20_municipios)]
    .groupby("MUNIC_RES", observed=True)["MORTE"]
    .mean()
    .mul(100)
    .sort_values()
)

plt.figure(figsize=(9, 6))

plt.barh(
    taxa_municipio.index.astype(str),
    taxa_municipio.values
)

plt.title("Taxa de óbito nos 20 municípios mais frequentes")
plt.xlabel("Taxa de óbito (%)")
plt.ylabel("Código do município")

plt.tight_layout()
plt.show()
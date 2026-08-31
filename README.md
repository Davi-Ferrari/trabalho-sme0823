\# Análise dos fatores associados ao óbito hospitalar em internações do SUS



Projeto desenvolvido para a disciplina \*\*SME0823 – Modelos de Regressão e Aprendizado Supervisionado II\*\*, do Instituto de Ciências Matemáticas e de Computação (ICMC/USP).



\## Objetivo



Investigar características dos pacientes e das internações hospitalares associadas à ocorrência de óbito durante internações realizadas no âmbito do Sistema Único de Saúde (SUS).



A variável resposta do estudo é `MORTE`, que indica se ocorreu óbito durante a internação:



\- `0` – não ocorreu óbito;

\- `1` – ocorreu óbito.



A modelagem será inicialmente realizada por meio de \*\*regressão logística\*\*, utilizando a família Binomial e a função de ligação logit.



\## Dados



Os dados são provenientes do \*\*Sistema de Informações Hospitalares do SUS (SIH/SUS)\*\*, disponibilizados pelo DATASUS.



O estudo considera inicialmente internações do \*\*estado de São Paulo em 2024\*\*.



A base original possui \*\*113 variáveis\*\*. Para a análise exploratória inicial, foram selecionadas principalmente:



\- `MORTE`

\- `IDADE`

\- `SEXO`

\- `RACA\_COR`

\- `DIAS\_PERM`

\- `COMPLEX`

\- `UTI`

\- `DIAG\_PRINC`

\- `MUNIC\_RES`



\## Análise exploratória



Na amostra inicial foram analisadas \*\*600.000 internações\*\*, sendo:



\- \*\*568.946\*\* sem ocorrência de óbito;

\- \*\*31.054\*\* com ocorrência de óbito;

\- proporção de óbitos de aproximadamente \*\*5,18%\*\*.



A análise exploratória investiga principalmente:



\- distribuição da ocorrência de óbito;

\- idade dos pacientes;

\- tempo de permanência hospitalar;

\- sexo;

\- raça/cor;

\- complexidade da internação;

\- utilização de UTI;

\- diagnósticos principais.



A seleção definitiva das variáveis será realizada posteriormente, durante a construção e comparação dos modelos.



\## Estrutura do projeto



```text

trabalho-sme0823/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── scripts/

│   ├── 01\_download.py

│   ├── 02\_limpeza.py

│   └── 03\_exploracao.py

│

├── output/

│   ├── figuras/

│   └── tabelas/

│

└── README.md


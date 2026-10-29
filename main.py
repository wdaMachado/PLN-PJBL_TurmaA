# %% [markdown]
# # PLN PjBL - BERTScore e SBERT
#
# Lê uma lista de frases, gera uma paráfrase e uma contradição para cada uma e compara as versões com a original usando BERTScore e SBERT.

# %% [markdown]
# ## 1. Configuração
#
# Instala as bibliotecas e o modelo do spaCy em português. Rode uma vez por sessão do Colab.

# %%
import subprocess
import sys

subprocess.run(
    [sys.executable, "-m", "pip", "install", "-q", "bert-score", "sentence-transformers", "deep-translator", "spacy", "pandas"],
    check=True,
)
subprocess.run([sys.executable, "-m", "spacy", "download", "pt_core_news_sm"], check=True)

# %% [markdown]
# ## 2. Entrada
#
# Lê o arquivo de frases: uma frase por linha, sem espaços nas pontas e sem linhas vazias, na ordem original.

# %%
from pathlib import Path


def ler_frases(caminho):
    linhas = Path(caminho).read_text(encoding="utf-8-sig").splitlines()

    frases = []

    for linha in linhas:
        frase = linha.strip()

        if frase:
            frases.append(frase)

    return frases


frases = ler_frases("frases.txt")
print(f"{len(frases)} frases carregadas de frases.txt")

# %% [markdown]
# ## 3. Paráfrase

# %% [markdown]
# ## 4. Contradição

# %% [markdown]
# ## 5. Métricas

# %% [markdown]
# ## 6. Pipeline

# %% [markdown]
# ## 7. Resultados

# %% [markdown]
# ## 8. Novo arquivo
#
# Coloque o arquivo trazido pelo professor no dia da defesa na mesma pasta, com o nome `novo_arquivo.txt` e no mesmo formato de `frases.txt`.

# %%
def carregar_novo_arquivo(caminho):
    frases = ler_frases(caminho)

    print(f"{len(frases)} frases carregadas de {caminho}")

    return frases


if Path("novo_arquivo.txt").exists():
    frases = carregar_novo_arquivo("novo_arquivo.txt")

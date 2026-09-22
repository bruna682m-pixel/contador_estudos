
# %%

arquivo = open("teste.txt", "w")

arquivo.write("Estou aprendendo Python")

arquivo.close()

# %%
arquivo = open("teste.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# %%
arquivo = open("teste.txt", "a")

arquivo.write("\nHoje estou aprendendo arquivos.")

arquivo.close()

# %%
arquivo = open("teste.txt", "w")

arquivo.write("Primeiro estudo.")

arquivo.close()

# %%
arquivo = open("teste.txt", "a")

arquivo.write("\nSegundo estudo")

arquivo.close()

# %%
arquivo = open("teste.txt", "r")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()

# %%
arquivo = open("teste.txt", "w")

arquivo.write("21/09/2026\n")
arquivo.write("22/09/2026\n")
arquivo.write("23/09/2026\n")

arquivo.close()

# %%
arquivo = open("teste.txt", "r")

linhas = arquivo.readlines()

arquivo.close()

print(linhas)

# %%
arquivo = open("teste.txt", "r")

linhas = arquivo.readlines()

arquivo.close()

for linha in linhas:
    linha = linha.strip()
    print(linha)


# %%

import datetime

texto = "21/09/2026"

data = datetime.datetime.strptime(texto, "%d/%m/%Y").date()

print(data)

# %%
import datetime

arquivo = open("teste.txt", "r")

linhas = arquivo.readlines()

arquivo.close()

for linha in linhas:
    linha = linha.strip()
    data = datetime.datetime.strptime(linha, "%d/%m/%Y").date()

    print(data)

# %%

import datetime

historico_dias_estudados = []

arquivo = open("teste.txt", "r")

linhas = arquivo.readlines()

arquivo.close()

for linha in linhas:
    linha = linha.strip()

    data = datetime.datetime.strptime(linha, "%d/%m/%Y").date()

    historico_dias_estudados.append(data)

print(historico_dias_estudados)

# %%
import datetime

data_atual = datetime.date.today()

arquivo = open("teste.txt", "a")

arquivo.write(data_atual.strftime("%d/%m/%Y") + "\n")

arquivo.close

# %%

import datetime

data = datetime.date(2026, 9, 24)

arquivo = open("teste.txt", "a")

arquivo.write(data.strftime("%d/%m/%Y") + "\n")

arquivo.close()



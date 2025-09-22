#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Enunciado:

Crie um programa em Python para avaliar uma competição de bandas de música. O programa deve:

Perguntar a quantidade de bandas participantes (mínimo 3).

Perguntar o nome de cada banda.

Para cada banda, receber as notas de 5 jurados (valores de 0 a 10).

Calcular a média das notas de cada banda e armazenar o resultado em um dicionário, onde a chave será o 
nome da banda e o valor será a média das notas.

Ao final, mostrar:

A média de cada banda.

O nome da banda vencedora (a que tiver maior média).


# In[20]:


while True:
    try:
        num_bandas = int(input("Digite a quantidade de bandas participantes (mínimo 3): "))
        if num_bandas >= 3:
            break
        else:
            print("A quantidade de bandas deve ser no mínimo 3.")
    except ValueError:
        print("Por favor, insira um número válido.")

medias_bandas = {}

for i in range(num_bandas):
    nome_banda = input(f"\nDigite o nome da {i+1}ª banda: ")

    notas = []
    for j in range(1, 6):
        while True:
            try:
                nota = float(input(f"Digite a nota do jurado {j} para a banda '{nome_banda}' (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota) 
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Por favor, insira um valor numérico válido.")

    media_banda = sum(notas) / len(notas)
    medias_bandas[nome_banda] = media_banda

print("\nMédia das bandas:")
for banda, media in medias_bandas.items():
    print(f"{banda}: {media:.2f}")

banda_vencedora = max(medias_bandas, key=medias_bandas.get)
print(f"\nA banda vencedora é: {banda_vencedora} com média {medias_bandas[banda_vencedora]:.2f}")


# Enunciado:
# 
# Crie um programa que conte quantas vezes cada palavra aparece em uma frase.
# 
# Pedir ao usuário para digitar uma frase
# 
# Imprimir a palavra e quantas vezes ela aparece

# In[8]:


frase = input("Digite uma frase: ")
palavras = frase.lower().split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print("\nContagem de palavras:")
for palavra, qtd in contagem.items():
    print(f"{palavra}: {qtd}")


# In[ ]:


Enunciado:

Crie um programa em python que imprima números pares

Pedir o usuário para digitar uma lista com mínimo 10 números

Criar uma nova somente com numeros pares

Imprimir números pares


# In[15]:


while True:
    try:
        entrada = input("Digite pelo menos 10 números, separados por espaço: ")
        numeros = list(map(int, entrada.split()))
        
        if len(numeros) >= 10:
            break
        else:
            print("Você deve digitar no mínimo 10 números.")
    except ValueError:
        print("Por favor, insira apenas números inteiros.")

pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("\nNúmeros pares:", pares)


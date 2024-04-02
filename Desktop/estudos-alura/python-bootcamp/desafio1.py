# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

# TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
#  Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#  Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

# ENTRADA
# Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta. .

# SAÍDA 
# O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

if quantidade_passos > 0: 
    for i in range(1, quantidade_passos + 1):
        if(i == 1):
            print(f"Explorador: {i} passo")
        else: 
            print(f"Explorador: {i} passos")
else:
    print("Nenhum passo dado na floresta.")








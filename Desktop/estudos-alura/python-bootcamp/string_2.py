nome = "Isabella"
idade = 19 
profissao = "Desenvolvedora Full-Stack Pleno"
linguagem = "React"
saldo = 46.676

# dicionários
dados = {"nome": "Isabella", "idade": 19}

# OLD STYLE %
# s = string, d = inteiro 
print("Nome: %s  Idade: %d" % (nome, idade))

# FORMAT 
print("Nome: {}  Idade: {}".format(nome, idade))
# passando indices 
print("Nome: {0}  Idade: {1}".format(nome, idade))
#exibir mais de uma vez
print("Nome: {0}  Idade: {1} {1}".format(nome, idade))
# nomeado
print("Nome: {nome}  Idade: {idade}".format(nome=nome, idade=idade))
# percorrer dicionário 
print("Nome: {nome}  Idade: {idade}".format(**dados))

# F STRING 
print(f"Nome: {nome}  Idade: {idade}")

# FORMATAÇÃO 
print(f"Nome: {nome}  Idade: {idade}")
# o dois representa o número de casas que queremos colocar o dez representa o tamanho para exibir, seguir os dois com a letra f 
print(f"Nome: {nome}  Idade: {idade} Saldo: {saldo: 10.2f}")




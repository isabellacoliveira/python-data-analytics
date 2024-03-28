nome = "Isabella"

# técnica F STRING
mensagem = f"""
Olá, meu nome é {nome}
Eu estou aprendendo Python
"""

# mesma coisa que a de cima , preserva os espaços
mensagem1 = f'''
    Olá, meu nome é {nome}
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos 
'''

print(mensagem)
print(mensagem1)

print("""
      ========== MENU ==========

      1 - Depositar 
      1 - Sacar 
      1 - Sair 

      ==========================

      Obrigado por usar nosso sistema!
      """)
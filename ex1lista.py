# Exercicio 1 

# class Pessoa:
#     def __init__(self,nome,idade):
#         self.__nome = nome 
#         self.__idade = idade 
        
#     def get_nome (self):
#         return self.__nome
    
#     def get_idade (self):
#         return self.__idade
    
#     def set_nome (self, nome):
#         if nome.strip ():
#             self.nome = nome
#         else:
#             print("Nome não identificado!")
    
#     def set_idade (self,idade):
#         if idade >= 0:
#             self.__idade = idade
#         else:
#             print("Idade nao identificada ('Idade não pode ser negativa')")

# nome_usuario = input("Digite seu nome completo: ")
# idade_usuario = int(input("Digite sua idade: "))

# pessoa = Pessoa(nome_usuario,idade_usuario)

# print(f"Nome do usuario: {pessoa.get_nome()}")
# print(f"idade do usuario: {pessoa.get_idade()}, anos de idade!")




# ------------------------------------------------------------------------------------------------------------------

# exercicio 2

# class Pessoa:
#     def __init__(self,nome,idade):
#         self.__nome = nome 
#         self.__idade = idade 
        
#     def get_nome (self):
#         return self.__nome
    
#     def get_idade (self):
#         return self.__idade
    
#     def set_nome (self, nome):
#         if nome.strip ():
#             self.nome = nome
#         else:
#             print("Nome não identificado!")
    
#     def set_idade (self,idade):
#         if idade >= 0:
#             self.__idade = idade
#         else:
#             print("Idade nao identificada ('Idade não pode ser negativa')")

# nome_usuario = input("Digite o nome completo do usuario: ")
# idade_usuario = int(input("Digite a idade completa do usuario: "))

# pessoa = Pessoa(nome_usuario,idade_usuario)

# print(f"Nome do usuario: {pessoa.get_nome()}")
# print(f"idade do usuario: {pessoa.get_idade()}, anos de idade!")


# novo_nome = input("Digite um novo nome do usuario: ")
# pessoa.set_nome (novo_nome)

# print (f"O novo nome do usuario é: {pessoa.get_nome()}")

# nova_idade = int(input("Digite sua nova idade do usuario: "))
# pessoa.set_idade (nova_idade)

# print (f" A nova idade do usuario é: {pessoa.get_idade()}")



# ------------------------------------------------------------------------------------------------------------------
# EXERCICIO 3


# class Carro:
#     def __init__ (self, modelo, cor):
#         self.__modelo = modelo 
#         self.__cor = cor 
    
    
#     def get_modelo (self):
#         return self.__modelo
    
#     def get_cor (self):
#         return self.__cor
    
#     def set_modelo (self,modelo):
#         if modelo.strip():
#             self.__modelo = modelo 
#         else:
#             print ("modelo de carro nao identificado.")

#     def set_cor (self,cor):
#         if cor.strip():
#             self.__cor = cor 
#         else:
#             print ("cor do carro nao identificado.")
        
# modelo_carro = input("Digite o modelo do seu carro: ")
# cor_carro = input("Digite a cor do seu carro: ")

# carro = Carro (modelo_carro, cor_carro)

# print (f" O modelo do carro é : {carro.get_modelo()}")
# print (f" A cor do carro é: {carro.get_cor()}")

# novo_carro = input("Digite O novo modelo do seu carro: ")
# carro.set_modelo (novo_carro)

# print (f"O novo modelo do carro é: {carro.get_modelo()}")

# nova_cor = input("Digite a nova cor do seu carro: ")
# carro.set_cor (nova_cor)

# print (f" A nova cor do seu carro é: {carro.get_cor()}")





# ------------------------------------------------------------------------------------------------------------------
# EXERCICIO 4


# class ContaBancaria:
#     def __init__(self,saldo):
#         self.__saldo = saldo
    
    
#     def get_saldo (self):
#         return self.__saldo
    
#     def set_depositar(self,valor):
#         if valor > 0:
#             self.__saldo += valor
#             print(f"Deposito de R${valor}, realizado com sucesso!")
#         else:
#             print("Valor de deposito deve ser positivo!")
    
#     def set_sacar (self,valor):
#         if valor > 0 :
#             if valor <= self.__saldo:
#                 self.__saldo -= valor
#                 print(f" Saque de R$ {valor} Reais, efetuado com sucesso!")
#             else:
#                 print(f"Saldo insuficiente, por favor tente novamente!")
#         else:
#             print(f" Valor do saque nao pode ser negativo!")
    
#     def consultar_saldo (self):
#         return self.__saldo
    

# saldo = float(input("Informe o saldo inicial da sua conta: "))

# resposta = 's'
# while resposta != 'n':

#     conta = ContaBancaria(saldo)
#     print (" Selecione uma opção de operação:")
#     print (" Digite 1 para deposito em conta corrente.")
#     print (" Digite 2 para saque em conta corrente.")
#     print (" Digite 3 para saldo de conta corrente. ")
#     print (" Digite 4 para sair das operaçoes.")

#     escolha = input("Digite o numero da opção desejada: ")
#     if escolha == '1':
#             valor_deposito = float(input(" Informe o valor que deseja depositar em conta corrente: R$"))
#             saldo = valor_deposito + saldo
#             conta.set_depositar(valor_deposito)

#     elif escolha == '2':
#             valor_saque = float(input(" Informe o valor que deseja sacar de sua conta corrente: R$"))
#             saldo = saldo - valor_saque
#             conta.set_sacar(valor_saque)

#     elif escolha == '3':
#             print(f" Saldo atual é de : R$ {conta.consultar_saldo()}")

#     elif escolha == '4':
#             print("operação encerrada.")
        
#     else:
#         print(" opção invalida, escolha uma opção valida.")

#     resposta = input("Deseja repetir (s ou n): ").lower
#     if resposta == 'n':
#          print("operação encerrada.")

# ------------------------------------------------------------------------------------------------------------------
# EXERCICIO 5

# class Aluno:
#     def __init__(self,nome,nota):
#         self.__nome = nome 
#         self.__nota = nota 
        
#     def get_nome (self):
#         return self.__nome
    
#     def get_nota (self):
#         return self.__nota
    
#     def set_nome (self, nome):
#         if nome.strip ():
#             self.nome = nome
#         else:
#             print("Nome não identificado!")
    
#     def set_nota (self,nota):
#         if nota >= 0:
#             self.__nota = nota
#         else:
#             print("Valor de nota nao identificada ('Nota não pode ser negativa')")

# nome_aluno = input("Digite nome completo do aluno: ")
# nota_aluno = float(input("Digite a nota do aluno: "))

# aluno = Aluno(nome_aluno,nota_aluno)

# print("Aluno inserido com sucesso!")

# print(f"Nome do aluno: {aluno.get_nome()}")
# print(f"Nota final do aluno: {aluno.get_nota()}!")

# novo_nome = input("Digite o nome do proximo aluno que deseja inserir:")
# aluno.set_nome (novo_nome)
# nova_nota = float(input("Digite a nova nota que deseja inserir: "))
# aluno.set_nota (nova_nota)

# print("Novo aluno inserido com sucesso!")
# print(f"Nome do aluno: {aluno.get_nome()}")
# print(f"Nota final do aluno: {aluno.get_nota()}!")

# ------------------------------------------------------------------------------------------------------------------
# EXERCICIO 6


class Produto:
    def __init__(self,produto,preco):
        self.__produto = produto
        self.__preco = preco
        
    def get_produto (self):
        return self.__produto
    
    def get_preco (self):
        return self.__preco
    
    def set_produto (self, produto):
        if produto.strip ():
            self.__produto = produto
        else:
            print("Nome do produto não identificado!")
    
    def set_preco (self,preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print(" Valor nao identificada (' Valor não pode ser negativo')")

nome_produto = input("Digite nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))

produto = Produto(nome_produto,preco_produto)

print (f"Nome do produto: {produto.get_produto()}")
print (f'Preço do produto: {produto.get_preco():,.3f} Reais!')

novo_produto = input("Digite o nome do novo produto a ser inserido")
produto.set_produto (novo_produto)
novo_preco = float(input("Digite o novo preço do produto: "))
produto.set_preco (novo_preco)

print (f"Nome do produto: {produto.get_produto()}")
print (f'Preço do produto: {produto.get_preco():,.3f} Reais!')

# ------------------------------------------------------------------------------------------------------------------
# EXERCICIO 7


# class Livro:
#     def __init__(self, titulo, autor):
#         self.__titulo = titulo
#         self.__autor = autor 
    
#     def get_titulo (self):
#         return self.__titulo
    
#     def set_titulo (self, titulo):
#         if titulo.strip ():
#             self.__titulo = titulo
#         else:
#             Print(" Titulo do livro nao identificado!")
    
#     def get_autor (self):
#         return self.__autor
    
#     def set_autor (self, autor):
#         if autor.strip ():
#             self.__autor = autor
#         else:
#             print("Autor do livro não identificado")

# titulo_livro = (input(" Digite o titulo do livro que deseja adicionar: "))
# autor_livro = (input("Digite o autor do livro que deseja adicionar: "))

# livro = Livro (titulo_livro,autor_livro)

# print("Livro adicionado com sucesso!")
# print(f" Titulo do livro adicionado {livro.get_titulo}")
# print(f" Autor do livro adicionado {livro.get_autor}")


# novo_titulo = (input(" Digite o titulo do novo livro que deseja adicionar: "))
# livro.set_titulo(novo_titulo)
# novo_autor = (input("Digite o autor do novo livro que deseja adicionar: "))
# livro.set_autor(novo_autor)

# print("Novo livro adicionado com sucesso!")
# print(f" Titulo do livro adicionado {livro.set_titulo}")
# print(f" Autor do livro adicionado {livro.set_autor}")


# ------------------------------------------------------------------------------------------------------------------
# EXERCICIO 8

# class Funcionario:
#     def __init__(self,nome, salario):
#         self.__nome = nome 
#         self.__salario = salario 

#     def get_nome (self):
#         return self.__nome
    
#     def set_nome (self, nome):
#         if nome.strip ():
#             self.__nome = nome
#         else:
#             print("Nome do funcionario nao identificado!")
    
#     def get_salario (self):
#         return self.__salario
    
#     def set_salario (self,salario):
#         if salario >= 0:
#             self.__salario = salario 
#         else:
#             print(" Salario não pode ser negativo!")

# nome_funcionario = input("Digite o nome completo do funcionario que deseja inserir: ")
# salario_funcionario = float(input("Digite o salario do funcionario inserido: "))

# funcionario = Funcionario (nome_funcionario, salario_funcionario)

# print(f"Funcionario: {funcionario.get_nome},\nregistrado com o valor do salario de: R${funcionario.get_salario:,.3f} Reais!")

# print("Insira o novo funcionario!")

# novo_funcionario = input("Digite o nome completo do funcionario que deseja inserir: ")
# funcionario.set_nome (novo_funcionario)
# novo_salario = float(input("Digite o salario do funcionario inserido: "))
# funcionario.set_salario (novo_salario)

# print(f"Funcionario: {funcionario.set_nome},\nregistrado com o valor do salario de: R${funcionario.set_salario:,.3f} Reais!")



# ------------------------------------------------------------------------------------------------------------------
# EXERCICIO 9


# class Casa:
#     def __init__(self,endereço,bairro, cidade, estado, valor):
#         self.__endereço = endereço 
#         self.__valor = valor
#         self.__bairro = bairro
#         self.__cidade = cidade 
#         self.__estado = estado 
        
#     def get_endereço (self):
#         return self.__endereço
    
#     def set_endereço (self,endereço):
#         if endereço.strip ():
#             self.__endereço = endereço
#         else:
#             print("Endereço invalido!")
            
#     def get_bairro (self):
#         return self.__bairro
    
#     def set_bairro (self, bairro):
#         if bairro.strip ():
#             self.__bairro = bairro 
#         else:
#             print("Bairro nao localizado!")
    
#     def get_cidade (self):
#         return self.__cidade
    
#     def set_cidade (self,cidade):
#         if cidade.strip ():
#             self.__cidade = cidade 
#         else:
#             print("Cidade nao localizada!")
            
#     def get_estado (self):
#         return self.__estado
    
#     def set_estado (self,estado):
#         if estado.strip ():
#             self.__estado = estado
#         else:
#             print(" Estado nao localizado!")
    
#     def get_valor (self):
#         return self.__valor
    
#     def set_valor (self,valor):
#         if valor >= 0:
#             self.__valor = valor
#         else:
#             print("Valor nao pode ser negativo!")
            
# endereco_casa = input("Digite o endereço da casa à venda: ")
# bairro_casa = input("Digite o bairro da casa à venda: ")
# cidade_casa = input("Digite a cidade da casa à venda: ")
# estado_casa = input("Digite o estado da casa à venda: ")
# valor_casa = float(input("Digite o valor da casa à venda: "))

# casa = Casa (endereco_casa,bairro_casa,cidade_casa,estado_casa,valor_casa)

# print("Casa adicionada com sucesso!")
# print(f"Casa à venda localizado na {casa.get_endereço},\nbairro : {casa.get_bairro},\nna cidade de : {casa.get_cidade},\nno estado de: {casa.get_estado},\n pelo valor de : R$ {casa.get_valor:,.3f} reais ")

# print ("Insira os dados da nova casa no sistema!")

# novo_endereco = input("Digite o endereço da casa à venda: ")
# casa.set_endereço
# novo_bairro = input("Digite o bairro da casa à venda: ")
# casa.set_bairro
# nova_cidade = input("Digite a cidade da casa à venda: ")
# casa.set_cidade
# novo_estado = input("Digite o estado da casa à venda: ")
# casa.set_estado
# novo_valor = float(input("Digite o valor da casa à venda: "))
# casa.set_valor

# print(" Nova casa adicionada com sucesso!")
# print(f"Casa à venda localizado na {casa.set_endereço},\nbairro : {casa.set_bairro},\nna cidade de : {casa.set_cidade},\nno estado de: {casa.set_estado},\n pelo valor de : R$ {casa.set_valor:,.3f} reais ")


# ----------------------------------------------------------------------
# exercicio 10


# class Celular:
#     def __init__(self,marca,modelo, avaria):
#         self.__marca = marca 
#         self.__modelo = modelo
#         self.__avaria = avaria

#     def get_marca (self):
#         return self.__marca 

#     def set_marca (self,marca):
#         if marca.strip ():
#             self.__marca = marca
#         else:
#             print(" marca de celular nao encontrado! ")

#     def get_modelo (self):
#         return self.__modelo
    
#     def set_modelo (self,modelo):
#         if modelo.strip () :
#             self.__modelo = modelo
#         else:
#             print(" Modelo de celular nao encontrado!")

#     def get_avaria (self):
#         return self.__avaria

#     def set_avaria (self,avaria):
#         if avaria.strip ():
#             self.__avaria = avaria
#         else:
#             print("Avaria nao detectada")

# marca_celular = input("Insira a marca do celular: ")
# modelo_celular = input("Insira o modelo do celular: ")
# avaria_celular = input("Infomr a avaria detectada: ")

# celular = Celular (marca_celular,modelo_celular,avaria_celular)

# print("Celular classificado com sucesso!")
# print (f"Celular da marca: {celular.get_marca()}, do modelo: {celular.get_modelo()}, foi detectado a avaria: {celular.get_avaria()}.")

# print("Celular adicionado com sucesso a garantia!")

# nova_marca = input(" Insira a marca do celular: ")
# celular.set_marca (nova_marca)
# novo_modelo = input("Insira o modelo do celular: ")
# celular.set_modelo (novo_modelo)
# nova_avaria = input("Informe a avaria detectada: ")
# celular.set_avaria (nova_avaria)
# print("Celular classificado com sucesso!")

# print(f"Celular da marca: {celular.get_marca()}, do modelo: {celular.get_modelo()}, foi detectado a avaria: {celular.get_avaria()}.")

# ---------------------------------------------------------------------------------------------
# exercicio 11 


# class Animal:
#     def __init__(self,idade):
#        self.__idade = idade
       
#     def get_idade(self):
#         if self.__idade >= 0:
#             return self.__idade 
        
#         else:
#             print("Idade nao pode ser negativa!")
    
#     def set_idade (self,idade):
#         if self.__idade >= 0 :
#             self.__idade = idade
        
#         else:
#             print("Idade nao pode ser negativa!")
            
# idade_animal = int(input("Insira a idade do seu animal: "))

# animal = Animal (idade_animal)

# print ("Idade do animal adicionado com sucesso!")

# print (f"Seu animal tem {animal.get_idade()} anos de idade!")


# ----------------------------------------------------------------------------
# exercicio 12 

# class Estudante :
#     def __init__(self, nome, matricula ):
#         self.__nome = nome 
#         self.__matricula = matricula
        
#     def get_nome (self):
#         return self.__nome
    
#     def set_nome (self,nome):
#         if nome.strip ():
#             self.__nome = nome
#         else:
#             print("Nome de aluno nao encontrado!")
    
#     def get_matricula (self):
#         return self.__matricula
    
#     def set_matricula (self,matricula):
#         if matricula >= 0:
#             self.__matricula = matricula
#         else:
#             print("Matricula invalida!")
            
# nome_aluno = input("Digite o nome completo do aluno: ")
# matricula_aluno = int(input(" Digite o numero de matricula do aluno: "))

# estudante = Estudante(nome_aluno,matricula_aluno)

# print ("Aluno inserido com sucesso!")

# print(f"Aluno: {estudante.get_nome()},Numero de matricula: {estudante.get_matricula()}")

# print("insira novo nome e nova matricula de aluno existente:")

# novo_nome = input("Digite o nome completo do aluno: ")
# estudante.set_nome (novo_nome)
# nova_matricula = int(input("Digite o numero de matricula do aluno: "))
# estudante.set_matricula (nova_matricula)

# print ("Nome modificado com sucesso!")
# print(f"Aluno: {estudante.get_nome()},Numero de matricula: {estudante.get_matricula()}")

# --------------------------------------------------------------------------------
# exercicio 13

# class Veiculo:
#     def __init__ (self,velocidade_maxima):
#         self.set_velocidade_maxima (velocidade_maxima)
        
#     def get_velocidade_maxima (self):
#         return self.__velocidade_maxima 

        
    
#     def set_velocidade_maxima (self,velocidade_maxima):
#         if velocidade_maxima > 0:
#             self.__velocidade_maxima = velocidade_maxima
#         else:
#             print("velocidade maxima nao detectada! velocidade precisa ser maior que '0'")
#             self.__velocidade_maxima = 0
            
# def obter_velocidade():
#     while True:
#         try:
#             velocidade_maxima = int(input("Digite a velocidade do seu veículo: "))
#             if velocidade_maxima > 0:
#                 return velocidade_maxima 
#             else:
#                 print("Erro: A velocidade precisa ser maior que zero. Tente novamente.")
#         except ValueError:
#             print("Erro: Entrada inválida. Por favor, insira um número inteiro.")

# velocidade_maxima = obter_velocidade()

# veiculo = Veiculo (velocidade_maxima)

# print("Velocidade maxima do veiculo adicionado com sucesso!")
# print(f"A velocidade maxima do veiculo é de : {veiculo.get_velocidade_maxima()} km por hora!")

# nova_velocidade = obter_velocidade()
# veiculo.set_velocidade_maxima (nova_velocidade)

# print("nova velocidade maxima adicionada com sucesso!")

# print(f"A nova velocidade maxima do veiculo é de: {veiculo.get_velocidade_maxima()} km por hora!")

# -------------------------------------------------------------------------------------------
# exercicio 14
# class Computador:
#     def __init__ (self,memoria_ram):
#         self.set_memoria_ram (memoria_ram)
        
#     def get_memoria_ram (self):
#         return self.__memoria_ram 

        
    
#     def set_memoria_ram (self,memoria_ram):
#         if memoria_ram > 0:
#             self.__memoria_ram = memoria_ram
#         else:
#             print("Memoria nao detectada! valor precisa ser maior que '0'")
#             self.__memoria_ram = 0
            
# def obter_memoria():
#     while True:
#         try:
#             memoria_ram = int(input("Digite a velocidade do seu veículo: "))
#             if memoria_ram > 0:
#                 return memoria_ram 
#             else:
#                 print("Erro: O valor precisa ser maior que zero. Tente novamente.")
#         except ValueError:
#             print("Erro: Entrada inválida. Por favor, insira um número inteiro.")

# memoria_ram = obter_memoria()

# computador = Computador (memoria_ram)

# print("Capacidade da memoria adicionado com sucesso!")
# print(f"A capacidade da memoria ram é de : {computador.get_memoria_ram()}.")

# nova_memoria = obter_memoria()
# computador.set_memoria_ram (nova_memoria)

# print("nova capacidade de memoria adicionada com sucesso!")

# print(f"A nova capacidade da memoria ram é de : {computador.get_memoria_ram()}.")

# -------------------------------------------------------------------------------
# exercicio 15

# class Curso:
#     def __init__ (self, nome, duraçao):
#         self.__nome = nome 
#         self.__duraçao = duraçao
        
#     def get_nome (self):
#         return self.__nome

#     def set_nome (self, nome):
#         if nome.strip ():
#             self.__nome = nome
#         else:
#             print (" Nome de curso nao encontrado!")
    
#     def get_duraçao (self):
#         return self.__duraçao
    
#     def set_duraçao (self,duraçao):
#         if duraçao.strip ():
#             self.__duraçao = duraçao
#         else:
#             print ("Valor de duração de curso nao identificado!")

# nome_curso = input("Digite o nome do curso: ")
# duracao_curso = int(input("Digite a duraçao em horas desse curso: "))

# curso = Curso (nome_curso,duracao_curso)

# print  (f"Você está cursando: {curso.get_nome()}, com a duração de: {curso.get_duraçao()} horas.")

# novo_curso = input("Digite o nome do proximo curso: ")
# curso.set_nome(novo_curso)
# nova_duraçao = int(input("Digite a duraçao em horas desse curso: "))
# curso.set_duraçao (nova_duraçao)

# print  (f"Você mudou seu curso para: {curso.get_nome()}, com a duração de: {curso.get_duraçao()} horas.")

# ---------------------------------------------------------------------------------------------------------

# exercicio 16

# class Jogo:
#     def __init__(self,pontos):
#         self.__pontos = pontos
        
#     def get_ponto (self):
#         return self.__pontos
    
#     def set_ponto (self, pontos):
#         self.__pontos = pontos

# pontuacao = float(input("Qual seu recorde de pontos no jogo? "))

# jogo = Jogo(pontuacao)

# print(f"Seu recorde de pontos no jogo é de: {jogo.get_ponto()} pontos!")

# print("Vamos analisar seu novo recorde?")

# nova_pontuacao = float(input("Qual seu novo recorde de pontos no jogo? "))
# jogo.set_ponto (nova_pontuacao)

# print(f"Seu novo recorde de pontos no jogo é de: {jogo.get_ponto()} pontos!")

# --------------------------------------------------------------------------
# exercicio 17

# class Empresa:
#     def __init__ (self,nome,numero_funcionarios):
#         self.__nome = nome 
#         self.__numero_funcionarios = numero_funcionarios
        
#     def get_nome (self):
#         return self.__nome
    
#     def set_nome (self,nome):
#         if nome.strip ():
#             return self.__nome
        
#         else:
#             print("Nome da empresa nao identificado!")
            
#     def get_funcionarios (self):
#         if self.__numero_funcionarios > 0:
#             return self.__numero_funcionarios
        
#         else:
#             print("Numero de funcionarios nao identificado ('valor nao pode ser igual ou menor a 0')")
    
#     def set_funcionarios (self,numero_funcionarios):
#         if self.__numero_funcionarios > 0:
#             self.__numero_funcionarios = numero_funcionarios
        
#         else:
#             print("Numero de funcionarios nao identificado ('Valor nao pode ser igual ou menor a 0')")

# nome_empresa = input("Digite o nome da empresa solicitada: ")
# numero_funcionarios = int(input("Digite o numero de funcionarios ativos na empresa: "))

# empresa = Empresa (nome_empresa,numero_funcionarios)

# print("cadastro efetuado com sucesso!")

# print(f"A empresa : {empresa.get_nome()}, possui o total de: {empresa.get_funcionarios()} ativos em sua empresa!")

# print("Cadastro de nova empresa!")
# novo_nome = input("Digite o nome da empresa solicitada: ")
# empresa.set_nome(novo_nome)
# novo_numero = int(input("Digite o numero de funcionarios ativos na empresa: "))
# empresa.set_funcionarios(novo_numero)

# print("cadastro efetuado com sucesso!")

# print(f"A empresa : {empresa.get_nome()}, possui o total de: {empresa.get_funcionarios()} ativos em sua empresa!")

# -----------------------------------------------------------------------------------

# exercicio 18

# class Filmes:
#     def __init__ (self,nome,ano):
#         self.__nome = nome 
#         self.__ano = ano 
    
#     def get_nome (self):
#         return self.__nome
    
#     def set_nome (self,nome):
#         if nome.strip ():
#             self.__nome = nome
            
#         else:
#             print("nome de filme nao localizado!")
    
#     def get_ano (self):
#         return self.__ano
    
#     def set_ano (self,ano):
#         if ano > 0:
#             self.__ano = ano 
#         else:
#             print("Ano de filme nao localizado!")

# nome_filme = input("Digite o nome do filme que deseja cadastrar: ")
# ano_filme = int(input("Digite o ano do filme cadastrado: "))

# filme = Filmes (nome_filme,ano_filme)

# print("Cadastro efetivdo com sucesso!")

# print(f"Filme: {filme.get_nome()}, lançado em: {filme.get_ano()}, foi cadastrado com sucesso!")

# print("Proximo filme a ser cadastrado")

# novo_nome = input("Digite o nome do filme que deseja cadastrar: ")
# filme.set_nome (novo_nome)
# novo_ano = int(input("Digite o ano do filme cadastrado: "))
# filme.set_ano (novo_ano)

# print("Cadastro efetivdo com sucesso!")

# print(f"Filme: {filme.get_nome()}, lançado em {filme.get_ano()}, foi cadastrado com sucesso!")

# ------------------------------------------------------------------------------------------------
# exercicio 19

# class Cidade:
#     def __init__ (self,nome, populacao):
#         self.__nome = nome 
#         self.__populacao = populacao
        
#     def get_nome (self):
#         return self.__nome
    
#     def set_nome (self,nome):
#         if nome.strip ():
#             self.__nome = nome
#         else:
#             print("Nome de cidade nao encontrado!")
    
#     def get_população (self):
#         return self.__populacao
    
#     def set_populacao (self,populacao):
#         if populacao >= 0:
#             self.__populacao = populacao
            
#         else:
#             print("Numero de populaçao invalida ('numero nao pode ser menor que 0')")

# nome_cidade = input("Digite o nome da cidade que deseja cadastrar: ")
# populacao_cidade = float(input("Digite a quantidade de habitantes da cidade: "))

# cidade = Cidade (nome_cidade, populacao_cidade)

# print ("Cidade cadastrada com sucesso!")

# print (f"Cidade: {cidade.get_nome()}, com o total de: {cidade.get_população()} habitantes, foi cadastrada com sucesso!")

# print ("Cadastro da proxima cidade")

# novo_nome = input("Digite o nome da cidade que deseja cadastrar: ")
# cidade.set_nome (novo_nome)
# nova_populacao = float(input("Digite a quantidade de habitantes da cidade: "))
# cidade.set_populacao (nova_populacao)

# print ("Cadastro de cidade concluida com sucesso")

# print(f"A cidade de: {cidade.get_nome()}, com o total de: {cidade.get_população()} habitantes, foi cadastrada com sucesso!")

# ---------------------------------------------------------------------------------------
# exercicio 20

# class Professor:
#     def __init__ (self, nome, disciplina):
#         self.__nome = nome 
#         self.__disciplina = disciplina 
        
#     def get_nome (self):
#         return self.__nome
    
#     def set_nome (self,nome):
#         if nome.strip():
#             self.__nome = nome
#         else:
#             print("Nome de professor nao encontrado!")
            
#     def get_disciplina (self):
#         return self.__disciplina
    
#     def set_disciplina (self, disciplina):
#         if disciplina.strip():
#             self.__disciplina = disciplina
#         else:
#             print("Disciplina não encontrada!")
            
# nome_professor = input("Digite o nome do professor que deseja cadastrar: ")
# disciplina_professor = input("Digite a disciplina lecionada pelo professor: ")

# professor = Professor (nome_professor,disciplina_professor)

# print("Professor cadastrado com sucesso!")

# print(f"O professor: {professor.get_nome()}, que leciona a disciplina: {professor.get_disciplina()}, foi cadastrado com sucesso!")

# print("Cadastro de novo professor!")

# novo_nome = input("Digite o nome do professor que deseja cadastrar: ")
# professor.set_nome(novo_nome)
# nova_disciplina = input("Digite a disciplina lecionada pelo professor: ")
# professor.set_disciplina(nova_disciplina)

# print("Professor cadastrado com sucesso!")

# print(f"O professor: {professor.get_nome()}, que leciona a disciplina: {professor.get_disciplina()}, foi cadastrado com sucesso!")

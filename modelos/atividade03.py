# Questão 1
# class Pessoa:
  
#     def __init__(self,nome,idade,profissao):
#         self.nome=nome
#         self.idade=idade
#         self.profissao=profissao

#     def __str__(self):
#         return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
#     def saudacao(self):
#         if self.profissao:
#             print( f'Olá sou {self.nome}! Trabalho como {self.profissao}.')
#         else:
#             print( f'Olá sou {self.nome}!')

#     def aniversario(self):
#         self.idade +=1

# pessoa1=Pessoa('Silvia',30,'Psicóloga')
# print(pessoa1)
# print('')
        
# pessoa1.aniversario()
# print(pessoa1)
# print('')

# pessoa1.saudacao()
# print('')


# Questão 2 
# class ContaBancaria:

#     def __init__(self,titular,saldo):
#         self.titular=titular
#         self.saldo=saldo
#         self._ativo=False
        
# Questão 3
    # def __str__(self):
    #     return f'Conta de {self.titular} - Saldo: R$ {self.saldo}'
    
# conta1=ContaBancaria('Natan',3000)
# conta2=ContaBancaria('Yara',2000)

# print(conta1)
# print('')
# print(conta2)

# Questão 4
#     @classmethod
#     def ativar_conta(cls,conta):
#         conta._ativo=True
        
# conta3=ContaBancaria('Mickaela',5000)
# print(f'Antes de ativar: Conta ativa? {conta3._ativo}')
# ContaBancaria.ativar_conta(conta3)
# print(f'Depois de ativar: Conta ativa? {conta3._ativo}')

# Questão 5
# class ContaBancariaPythonica:
#     def __init__(self,titular,saldo):
#         self._titular=titular
#         self._saldo=saldo
#         self._ativo=False
        
#     @property
#     def titular(self):
#         return self._titular
    
#     @property
#     def saldo(self):
#         return self._saldo
    
#     @property
#     def ativo(self):
#         return self._ativo
    
# Questão 6
# conta4=ContaBancariaPythonica('Safira',1500)
# print(f'Titular da conta 4 é: {conta4.titular}')


# Questão 7
class ClienteBanco:

    def __init__(self,nome,sobrenome,idade,email,telefone):
        self.nome=nome
        self.sobrenome=sobrenome
        self.idade=idade
        self.email=email
        self.telefone=telefone

# cliente1=ClienteBanco('Mary','Alvez',30,'mary@email.com','412223343')
# cliente2=ClienteBanco('Marcos','Alvez',39,'marcos@email.com','412223444')
# cliente3=ClienteBanco('Marly','Alvez',16,'marly@email.com','412223322')

# # Questão 8
    @classmethod
    def criar_conta(cls,titular,saldo_inicial):
        conta=ClienteBanco(titular,saldo_inicial)
        return conta
    
conta_cliente1=ClienteBanco.criar_conta('Petulia',8000)
print(f'Conta de {conta_cliente1.titular} Com saldo de R${conta_cliente1.saldo_inicial}')

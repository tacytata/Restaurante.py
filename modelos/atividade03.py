# Questão 1
class Pessoa:
  
    def __init__(self,nome,idade,profissao):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'
    
    def aniversario(self):
        self.idade+=1

    @property
    def saudacao(self):
        


        pessoa1=Pessoa('Silvia',30,'Engenheira')
        print(pessoa1)
        
        pessoa1.aniversario()
        print(pessoa1.idade)
        print(pessoa1.saudacao)


# Questão 2 
class ContaBancaria:

    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
        self.ativo=False

        ContaBancaria
        conta1=ContaBancaria('José', 1000)

# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.ativo)

# Questão 3
    def __str__(self):
        return f'{self._titular} | {self._saldo}'
        
    @classmethod
    def listar_titulares(cls):
        for ContaBancaria in cls.contas:
            print(f'{ContaBancaria.titular} | {ContaBancaria.saldo} | {ContaBancaria.ativo}')

# Questão 4
            
    def ativar_conta(self):
        self._ativo=not self._ativo

titular_Renan=ContaBancaria('Renan',3000)
titular_Luiza=ContaBancaria('Luiza',5000)

titular_Renan=ativar_conta()
titular_Luiza=ativar_conta()

ContaBancaria.listar_titulares()



# Questão 5





# Questão 6



# Questão 7
class ClienteBanco:

    def __init__(self,nome,sobrenome,idade,email,telefone):
        self.nome=nome
        self.sobrenome=sobrenome
        self.idade=idade
        self.email=email
        self.telefone=telefone

cliente1=ClienteBanco('Mary','Alvez',30,'mary@email.com','412223343')
cliente2=ClienteBanco('Marcos','Alvez',39,'marcos@email.com','412223444')
cliente3=ClienteBanco('Marly','Alvez',16,'marly@email.com','412223322')

# Questão 8
conta_cliente1=cliente1.criar_conta(cliente1.nome,cliente1.sobrenome)
print(conta_cliente1.titular)
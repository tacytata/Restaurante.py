# 1 Atividade
class Carro:
    modelo=''
    cor=''
    ano=''

carro_civic=Carro()
carro_civic.modelo='Turbo'
carro_civic.cor='Branco'
carro_civic.ano='2023'

print(vars(carro_civic))
print('')

# 2 Atividade
class Restaurante:
    nome=''
    categoria=''
    ativo=False
    localizacao=''
    estrelas=''

restaurante_centro=Restaurante()
restaurante_centro.nome='Centro'
restaurante_centro.categoria='Oriental'
restaurante_centro.localizacao='Japão'
restaurante_centro.estrelas='5'

# 3 Atividade
class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria,localizacao,estrelas):
        self.nome=nome
        self.categoria=categoria
        self.localizacao=localizacao
        self.estrelas=estrelas
        self.ativo=False

        Restaurante.restaurantes.append(self)

# 4 Atividade
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.localizacao} | {restaurante.estrelas} | {restaurante.ativo}')

restaurante_centro=Restaurante('Centro', 'Oriental', 'Japão', '5')

# 5 Atividade
class Cliente:
    clientes=[]

    def __init__(self,nome,idade,pais,nascimento):
        self.nome=nome
        self.idade=idade
        self.pais=pais
        self.nascimento=nascimento

        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.pais} | {self.nascimento}'

    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} | {cliente.idade} | {cliente.pais} | {cliente.nascimento}')

cliente_Natan=Cliente('Natan', '20', 'Brasil', '2004')
cliente_Yara=Cliente('Yara', '23', 'Japão', '2001')
cliente_Filipa=Cliente('Filipa', '18', 'Dinamarca', '2006')

Cliente.listar_clientes()
    # atividade







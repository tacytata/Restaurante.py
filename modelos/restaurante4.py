# 1 tornando o projeto aderente ao padrão de mercado

# import da classe Avaliacao
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._avaliacao=[]
        self._ativo=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

   
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliações'.ljust(20)} |  {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    

    
    def alternar_estado(self):
        self._ativo=not self._ativo
        
    # criando método para receber as avaliações  
    def receber_avaliacao(self,cliente,nota):
        avaliacao=Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas=sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas=len(self._avaliacao)
        media=round(soma_das_notas/quantidade_de_notas,1)
        return media


# 2 criação de objetos
# restaurante_praca=Restaurante('praça', 'Gourmet')
# restaurante_praca._nome='biqueira'
# restaurante_praca.alternar_estado()

# restaurante_pizza=Restaurante('pizza express', 'Italiana')




#Restaurante.listar_restaurantes()
# Questão 1
class Livro:
    livros=[]
    
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo=titulo
        self.autor=autor
        self.ano_publicacao=ano_publicacao
        self.disponivel=True
        Livro.livros.append(self)
    
# Questão 2
    def __str__(self):
        return f'O livro {self.titulo} foi escrito por {self.autor}, no ano de {self.ano_publicacao}.'
    
# livro1=Livro('Príncipe cruel','Holly Black',2018)
# livro2=Livro('A Seleção','Kiera Cass',2009)
# print(livro1)
# print('')
# print(livro2)

# Questão 3

    def emprestar(self):
        self.disponivel=False
        
#livro1=Livro('Príncipe Cruel','Holly Black',2018)

        if self.disponivel:
            print(f'Esse livro está disponível: {self.titulo}')
        else:
            print(f'Esse livro não está disponível: {self.titulo}')
#livro1.emprestar()
#print('')

# Questão 4
    @staticmethod
    def verificar_disponibilidade(ano):
        disponiveis = []
        for livro in Livro.livros:
            if livro.ano_publicacao == ano and livro.disponivel:
                disponiveis.append(livro)
        return disponiveis


# livro1 = Livro('Príncipe Cruel', 'Holly Black', 2020)
# livro2 = Livro('A Seleção', 'Kiera Cass', 2020)
# livro3 = Livro('A Elite', 'Kiera Cass', 2021)


livros_disponiveis_2020 = Livro.verificar_disponibilidade(2020)
for livro in livros_disponiveis_2020:
    print(f'O livro {livro.titulo} está disponível.')


    
    











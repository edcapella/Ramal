'''

Projeto ramal;
 - Apresente funções de procura por nome ou ordem alfabética;
 - Apresente funções de adicionar pessoas e ramais;
 - Apresente funções excluir pessoas e ramais;
 - Apresente funções de trocar ramais de pessoas;
 - Apresente funções mostrar todos ramais;

'''
import time
from time import sleep

class Ramal:
    ''' Programa principal'''

    fones = [{'nome': 'Eduardo', 'numero': 5}, {'nome': 'Sheron', 'numero': 7}, {'nome': 'Jose', 'numero': 6}]

    def __init__(self):
        self.escolha()
        self.lista()

    def escolha(self):
        print('''      
          [1] Pesquisar ramal
          [2] Todos Ramais
          [3] Configuração
          [4] Fechar
              ''')
        while True:
            # Localizar o ramal desejado.
            self.opcao = int(input(' Escolha a opção desejada: '))
            if self.opcao == 1:
                localiza = str(input('Localizar Ramal: '))
                print('-'*35)
                print(self.find(localiza.title()))
                print('-'*35)
                self.lista()


            # Mostra lista de ramais cadastrados!
            elif self.opcao == 2:
                for ramal in Ramal.fones:
                    if ramal != {}:  # para mostrar somente os ramais que não estão em branco.
                        print('-'*35)
                        print(f'nome:{ramal["nome"]} | Ramal:{ramal["numero"]}')
                print('-'* 35)
                self.lista()

            # Parte da configuração. Adicionar cadastro / Remover cadastro
            elif self.opcao == 3:
                '''Escolha opção desejada: '''
                print('''
                [1] Adicionar RAMAL:
                [2] Remover RAMAL:
                [3] Sair ''')

                while True:
                    self.opcao = int(input('Escolha a opção desejada: '))

                    # adicionar ramal
                    if self.opcao == 1:
                        self.nome = str(input('nome do Ramal:').title())
                        self.numero = int(input('numero do Ramal: '))
                        self.adicionar(self.nome, self.numero)

                    # remover ramal
                    elif self.opcao == 2:
                        self.nome = str(input('nome do Ramal:').title())
                        self.remover(self.nome)
                    else:
                        time.sleep(1)
                        print('Saindo...')
                        self.lista()
                        break
            elif self.opcao == 3:
                return Ramal.fones
            else:
                print('Volte sempre!')
                exit(22)

    def lista(self):
        print(
            '''     [1] Pesquisar ramal
                [2] Todos Ramais
                [3] Configuração
                [4] Fechar''')

    def find(self, procura):
        ''' função em que vai localizar a primeira letra. Retornando uma lista com todos os nomes e ramais com a letra
        digitada. Caso digite o nome inteiro vai retorna somente o nome e o ramal
        fizemos uma verificação (len) para ver se vai retornar a (LISTA) ou retornar (nao ha cadastro)'''
        lista = []
        for l in Ramal.fones:
            if procura in l['nome']:
                lista.append(l)
        if len(lista) > 0:
            return lista
        return f'não há cadastro'

    def adicionar(self, nome, numero):
        '''função vai adicionar o nome e o numero dentro de outra lista.
        foi criado um while para que faça um loop adicionando os nomes e numeros até o usuario desejar.
        criamos uma lista (NovaLista) dentro da função para que os atributos (nome) e (numero) para que
        não ficassem aleatórios dentro
         da lista (Ramal.fones) assim criando uma lista dentro de outra.'''
        parar = False
        NovaLista = {}
        while not parar:
            print('Adicionar RAMAL')
            NovaLista.update({'nome': nome})
            NovaLista.update({'numero': numero})
            Ramal.fones.append(NovaLista.copy())
            NovaLista.clear()
            parar = str(input('deseja continuar? [S/N]').upper())
            if parar == 'N':
                break
        print(Ramal.fones)
        self.lista()

    def remover(self, name):
        for v in Ramal.fones:
            if name in v.values():
                del v['nome']
                del v['numero']
        print(Ramal.fones)


# teste
Ramal()

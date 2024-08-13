class Veiculo:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)
        self.preco = float(preco)
        
    def exibir_detalhe(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Preço R${self.preco}')
    

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco, num_portas):
        super().__init__(marca, modelo, ano, preco)
        self.num_portas = num_portas
        
    def exibir_detalhe(self):
        super().exibir_detalhe()
        print(f'Portas: {self.num_portas}')
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, preco, tipo_guidao):
        super().__init__(marca, modelo, ano, preco)
        self.tipo_guidao = tipo_guidao
    
    def exibir_detalhe(self):
        super().exibir_detalhe()
        print(f'Tipo de guidão: {self.tipo_guidao}')

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, preco, carga):
        super().__init__(marca, modelo, ano, preco)
        self.carga = carga
        
    def exibir_detalhe(self):
        super().exibir_detalhe()
        print(f'Carga maxima: {self.carga}')

class Concessionaria:
    def __init__(self):
        self.veiculos = []
    
    def adicionar_veiculo(self):
        qualVeiculo = input('''
            Qual o veiculo que deseja colocar
            [C] carro
            [M] moto
            [N] Caminhão
            >''').upper()
        marca = input('Marca: ')
        modelo = input('Modelo: ')
        ano = input('Ano: ')
        preco = input('Preço: ')
        
        if qualVeiculo == 'C':
            num_portas = input('Numero de portas: ')
            veiculo = Carro(marca, modelo, ano, preco, num_portas)
            self.veiculos.append(veiculo)
            return qualVeiculo
        elif qualVeiculo == 'M':
            tipo_guidao = input('Qual tipo de guidao: ')
            veiculo = Moto(marca, modelo, ano, preco, tipo_guidao)
            self.veiculos.append(veiculo)
        elif qualVeiculo == 'N':
            carga = input('Quantidade de carga que aguenta: ')
            veiculo = Caminhao(marca, modelo, ano, preco, carga)
            self.veiculos.append(veiculo)
        else:
            print('Resposta inválida.')
            return None
        
        print('Adicionado com sucesso!!!')
        
    
    def listar_veiculos(self):
        if not self.veiculos:
            print('Nenhum veiculo disponível nessa concenssionaria.')
        else:
            print('Veiculos disponiveis')
            print('=' * 60)
            for veiculo in self.veiculos:
                veiculo.exibir_detalhe()
                print('=' * 60)
    
    def vender_veiculos(self):
        modelo = input('Qual modelo deseja comprar: ')
        print('=' * 60)
        for veiculo in self.veiculos:
            if veiculo.modelo == modelo:
                veiculo.exibir_detalhe()
                print('=' * 60)
                self.veiculos.remove(veiculo)
                print(f'veiculo {modelo} vendido')
                return
        print(f'Nenhum modelo {modelo} foi encontrado')
    
    
def inicio_programa(concessionaria):
    interface = '''
    =============Menu para vendedores============= 
    [A] adicionar veiculo
    [L] listra veiculo
    [V] vender
    [S] Sair
    
    >'''
    
    while True:
        
        #pegando a entrada do usuario
        entrada = input(interface).upper()
        
        #vendo a opção escolhida
        if entrada == 'A':
            concessionaria.adicionar_veiculo()
        elif entrada == 'L':
            concessionaria.listar_veiculos()
        elif entrada == 'V':
            concessionaria.vender_veiculos()
        elif entrada == 'S':
            break
        else:
            print('Opção inválida')


concessionaria = Concessionaria()
    
inicio_programa(concessionaria)    
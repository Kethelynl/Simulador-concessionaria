# Desafio: Sistema de Gerenciamento de Concessionária

Pedi para o chatGPT fazer um desafio para mim para treinamendo do uso de classes, e esse foi o desafio proposto

## Descrição:
Você vai criar um sistema para gerenciar uma concessionária de veículos. O sistema deve permitir que os usuários cadastrem diferentes tipos de veículos, façam consultas, e registrem vendas. Cada tipo de veículo (Carro, Moto, Caminhão) terá características específicas, mas todos compartilham algumas propriedades comuns, como marca, modelo, ano, e preço.

## Requisitos:

### Classes Principais:

- Veiculo: Classe base que representa um veículo genérico.
- Carro, Moto, Caminhão: Classes derivadas que herdam de Veiculo e possuem propriedades e métodos específicos.

### Atributos da Classe Veiculo:

- marca: String representando a marca do veículo.
- modelo: String representando o modelo do veículo.
- ano: Inteiro representando o ano de fabricação.
- preco: Float representando o preço do veículo.
### Métodos da Classe Veiculo:
- exibir_detalhes(): Exibe os detalhes do veículo, como marca, modelo, ano, e preço.
- aplicar_desconto(percentual): Aplica um desconto ao preço do veículo, baseado em um percentual fornecido.
### Atributos Específicos das Subclasses:

- Carro: Adiciona o atributo num_portas (número de portas).
- Moto: Adiciona o atributo tipo_guidão (tipo de guidão).
- Caminhão: Adiciona o atributo capacidade_carga (capacidade de carga em toneladas).
### Classe Concessionaria:

#### Atributos:
- veiculos: Lista de veículos disponíveis na concessionária.

### Métodos:
- adicionar_veiculo(veiculo): Adiciona um novo veículo à lista.
- listar_veiculos(): Lista todos os veículos disponíveis.
- vender_veiculo(modelo): Remove um veículo da lista com base no modelo e registra a venda.
consultar_veiculo(modelo): Exibe os detalhes de um veículo específico com base no modelo.
### Regras:
- A classe Concessionaria deve ser capaz de gerenciar diferentes tipos de veículos.
- O método vender_veiculo deve verificar se o veículo está disponível antes de removê-lo da lista.
- Implementar tratamentos de exceções para garantir que operações como venda ou consulta de veículos inexistentes sejam tratadas de forma adequada.

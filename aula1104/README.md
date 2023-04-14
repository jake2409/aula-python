# Semáforo Inteligente

## Descrição do problema

Analisando o sistema de transito do local onde moramos, percebemos a necessidade de pen-
sar em uma solução viável para evitar o problema do tempo de espera desnecessário nos 
semáforos locais. Vimos que não existe nenhuma inteligência nesses semáfaros que identi-
fica o tempo de sinal verde que deve permanecer de acordo com a quantidade de carros pa-
rados. Também não possui a capacidade de perceber veículos que possuem prioridade no tran-
sito, como ambulâncias ou viaturas.
Levamos em consideração tambem que as pessoas não desligam seu carro durante esse tempo
parado no semáforo e dessa forma o carro continua consumindo combustível e consequente-
mente continua soltando poluentes.

## Solução encontrada

Desenvolveremos uma aplicação capaz de ler e identificar a quantidade de carros parados no 
lado oposto do semáforo e distinguir a quantidade de tempo que permacerá com o sinal vermelho
ou verde para o lado oposto. Além de usar algumas variáveis como veiculos que possuem priori
dade para tomar essas decisões que ajudaram as pessoas no seu dia a dia.

## O que desenvolvemos para esta sprint 

Para esta sprint planejamos desenvolver afim de utilizar o conhecimento apredido nas aulas
o primeiro passo para nosso sistema. Identificamos que para a primeira sprint desse sistema
o melhor cenário possivel dentro dos nossos conhecimentos, seria começar a desenvolver o sis-
tema pela parte de venda e controle de estoque do produto futuramente.
Planejamos agregar nesse mesmo sistema toda a outra parte do projeto que controlará as infor-
mações recebidas desse sistema de tráfego.
O sistema desenvolvido, deverá apresentar em primeiro momento um menu para o usuário com opções
de ver estoque, comprar, cadastrar e sair.

### Opção 1: Estoque

Aqui o sistema deve informar quantas peças de semáforo inteligente existem armazenadas para
venda. E em seguida se o usuário deseja comprar ou voltar ao menu anterior.

### Opção 2: Compra

Aqui o sistema deve perguntar a quantidade que o usuário deseja comprar. Caso escolha uma quanti-
dade maior do que existe em estoque, o sistema deve informar que quantidade está indisponível e 
perguntar quantos semáforos ele deseja comprar novamente.
Caso o usuário escolha uma quantidade que existe no estoque, o sistema identifica se ele já realizou
um cadastro. Se já realizou vai informar a onde o produto será entregue e o valor final da compra.
Após isso perguntará qual a forma de pagamento. Se for dinheiro deverá informar se necessita de troco 
e pra quanto.
Após a compra ser confirmada, o estoque deve ser atualizado.
### Opção 3: Cadastro

Aqui o sistema deve coletar as informações básicas de entrega do produto para o cliente, seu endereço
e número da casa.

# Integrantes do grupo:
Gabriel Aparecido Cassalho Xavier - rm99794
Gustavo Carmo S. S. L. - rm98279
Lucas Rodrigues D. - rm550196
Luísa Cristina S. N. - rm551889
Pedro Henrique S. M. - rm98804

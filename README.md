<h2 align="center"> REDES NEURAIS E ALGORITMOS GENÉTICOS </h2>

<p align="center"><img src="https://user-images.githubusercontent.com/106620307/228858222-39c047cb-b7fb-4e71-ab86-97d5eb0da13d.png"></p>

<p align=""> Fonte: <a href="https://xkcd.com/720/"> XKCD </a> </p>

## Introdução
<p align="justify">
"Algoritmos genéticos e redes neurais são duas técnicas amplamente utilizadas em aprendizado de máquina e inteligência artificial. Os algoritmos genéticos são um método de busca e otimização inspirado no processo evolutivo, onde soluções candidatas são avaliadas e modificadas iterativamente, visando encontrar a melhor solução para um determinado problema. Por outro lado, as redes neurais são modelos computacionais inspirados no funcionamento do cérebro humano, que consistem em camadas de neurônios interconectados capazes de aprender a partir de dados e realizar tarefas complexas, como classificação e previsão. Ambas as técnicas são capazes de lidar com problemas complexos e oferecem diversas aplicações práticas em áreas como ciência dos dados, robótica, visão computacional e jogos." </p>
GPT, Chat - 2023

## Sobre o projeto
<p align="justify">
Esse repositório é dedicado às atividades da disciplina do terceiro semestre, na Ilum Escola de Ciência, ministrada pelo <a href="https://github.com/drcassar"> Prof. Daniel R. Cassar </a>, na qual aprendemos ferramentas computacionais inspiradas na biologia. Os experimentos foram propostos pelo professor e realizados pelo aluno <a href="https://github.com/Karl-Marcos"> Marcos de Cerqueira Leite </a>  em sala e estão separados em duas pastas:  </p>
<p align="justify"> </p>

+  <a href="https://github.com/Karl-Marcos/Redes_Neurais_1S23/tree/main/AlgoritmosGeneticos"> Algoritmos Genéticos </a> : Doze experimentos de algoritmos genéticos, cada um em um arquivo de Jupyter (.ipynb) além de arquivos de python (.py) contendo funções e classes utilizadas nos experimentos.
  
+  <a href="https://github.com/Karl-Marcos/Redes_Neurais_1S23/tree/main/RedesNeurais"> Redes Neurais </a> (vazio por enquanto): X experimentos de redes neurais, cada um em um arquivo de Jupyter (.ipynb) além de arquivos de python (.py) contendo funções e classes utilizadas nos experimentos. </p>

<p align="justify">
Ao final do semestre, foi elaborado um trabalho final sobre o conteúdo, presente em <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final"> RNAG_Trabalho_Final</a>, que consiste na aplicação de Algoritmo Genético, mais especificamente de Programação Genética, para resolver equações diferenciais simbólicamente. </p>
<p align="justify"> </p>

## Resultados interessantes

### Caixeiro viajante

<p align="justify">
Nos experimentos <a href="https://github.com/Karl-Marcos/Redes_Neurais_1S23/blob/main/AlgoritmosGeneticos/experimento%20A.06%20-%20o%20caixeiro%20viajante.ipynb"> o caixeiro viajante </a> e <a href="https://github.com/Karl-Marcos/Redes_Neurais_1S23/blob/main/AlgoritmosGeneticos/experimento%20GA.03%20-%20caixeiro%20com%20gasolina%20infinita.ipynb"> o caixeiro com gasolina infinita </a>, usamos um algoritmo genético para encontrar menor e o maior caminho, respectivamente, que passa por todas as cidades. O interessante é que em um caso usamos uma função seleção por torneio em que o vencedor é caminho de menor distância,
enquanto no outro caso o vencedor é o caminho de maior distância. Apenas com essa simples mudança, conseguimos mudar o comportamento da população ao longo das gerações. Com isso chegamos ao resultado: </p>

<p align="center"><img src="https://user-images.githubusercontent.com/106620307/233842601-6c65bfee-6a77-4ac9-83a6-cc7d7bac3641.png"></p>

### Função de Himmelblau

<p align="justify">
No experimento <a href="https://github.com/Karl-Marcos/Redes_Neurais_1S23/blob/main/AlgoritmosGeneticos/experimento%20GA.06%20-%20Himmelblau%20e%20sua%20funcao.ipynb"> Himmelblau e sua função </a>, utilizamos um algoritmo genético para encontrar mínimos locais da função de Himmelblau. O domínio da função é o plano (x,y), de maneira que podemos plotar os indivíduos como pontos 2D. Abaixo podemos ver como a população de indivíduos evolui com o passar das gerações onde cada cor representa uma repetição do experimento: </p> 

<p align="center"><img src="https://user-images.githubusercontent.com/106620307/233873524-dbb114fa-34f9-4f25-b93c-068edde259dd.png"></p>

### Rede neural do zero!

<p align="justify">
Ao longo das aulas de redes neurais, aprendemos a programar uma rede neural com python puro! Desde como criar a classe Valor, que armazena a informação de um neuronio, parâmetro, input ou output da rede. Além disso, aprendemos a plotar o gráfico computacional de uma rede. Aqui está enorme grafo de uma rede extremamente simples: </p> 

<p align="center"><img src="https://github.com/Karl-Marcos/Redes_Neurais_1S23/blob/main/RedesNeurais/rede_neural.png"></p>

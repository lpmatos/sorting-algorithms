# Selection Sort

Nesse algoritmo, para cada posição procuramos o menor elemento do array e mudamos para a atual posição.

Funciona da seguinte forma: setamos o menor elemento como o atual, ou seja, como o primeiro. Após isso percorremos os próximos elementos um por um avaliando se o próximo elemento é menor do que o elemento do índice menor. Se for, o elemento menor é atualizado. Fazemos isso até acharmos o índice do menor elemento. Ao finalizar esse loop entre todos os próximos, trocamos a posição do elemento atual com a do elemento menor.

Sua ideia é achar o menor elemento da iteração e após isso, trocar o elemento atual por esse menor elemento.

O **Selection Sort** encontra o menor elemento a cada iteração e o troca com o atual.

Uma das coisas boas desse algoritmo é que ele não precisa de memória extra para fazer a ordenação, uma vez que ele faz a troca in-place, não precisando de dados auxiliares. 

O ponto negativo é que ele possui um tempo de resposta lento para arrays com grandes itens. Se o número de itens do array for grande, a análise do algoritmo terá que ser quadrática, ou seja, O^2.

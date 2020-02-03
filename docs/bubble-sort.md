# Bubble Sort

Pega o elemento atual, compara com o próximo elemento e se o elemento atual for maio que o próximo elemento, então fazemos a troca. Isso é feito até que todos os elementos do array terminem em sua posição final. 

Devido a esse comportamento esse algoritmo é bastante lento, uma vez que ele irá fazer um número de trocar bem elevado caso o array não estiver devidamente ordenado. 

O único caso que esse algoritmo é bom é quando o array está quase sorteado. Nesse contexto o número de trocas será mínimo.

Caso os elementos estiverem, existe uma flag para dizer se ainda está sendo feito alguma troca. Caso não estiver, então o algoritmo para.

A ideia é percorremos o array salvando o elemento atual e com base no atual percorrer todos os próximo e realizando a troca. Caso não exista mais trocas, então paramos.

Em termos de complexidade, no pior caso esse algoritmo é O^2, ou seja, quadrático (eleva ao quadrado o tempo), portanto não é tão performático.

O melhor caso seria quando o array já está quase ordenado, assim o algoritmo não faria tantas trocas, o que pouparia tempo.

Esse algoritmo não é tão implementado no dia-a-dia, mas é um dos mais fácies de se entender.

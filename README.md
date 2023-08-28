# Simulador de Autômatos Finitos Determinísticos
O objetivo deste projeto é implementar um interpretador de autômatos determinísticos em Python. O programa deverá ler a descrição de um autômato finito determinístico presente em um arquivo-texto e então aguardar (até que o usuário termine o programa) a entrada de cadeias que serão simuladas pelo autômato. Assim que uma cadeia é entrada no programa, o programa deverá simular o funcionamento do autômato com esta cadeia, apresentando na tela os pares (𝑞, 𝑐) a partir de um estado inicial, onde 𝑞 é um estado e 𝑐 é um símbolo de entrada. Deverá apresentar, no final, se esta cadeia foi aceita ou rejeitada e, neste caso, imprimir o motivo: estado de não aceitação com a cadeia vazia ou a cadeia não está vazia mas não conseguiu aplicar uma transição.
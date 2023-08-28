from main import criarautomato

def automato1(cadeia:str):
    automato = criarautomato("testes/teste1.txt")
    return automato.verificarCadeia(cadeia)

def automato2(cadeia:str):
    automato = criarautomato("testes/teste2.txt")
    return automato.verificarCadeia(cadeia)

def automato3(cadeia:str):
    automato = criarautomato("testes/teste3.txt")
    return automato.verificarCadeia(cadeia)

def automato4(cadeia:str):
    automato = criarautomato("testes/teste4.txt")
    return automato.verificarCadeia(cadeia)


def teste1_cadeia1_verdadeira():
    assert automato1("000000") == True

def teste1_cadeia2_verdadeira():
    assert automato1("101110100") == True

def teste1_cadeia3_verdadeira():
    assert automato1("01111001110") == True

def teste1_cadeia1_falsa():
    assert automato1("0000001") == False

def teste1_cadeia2_falsa():
    assert automato1("1011101001") == False

def teste1_cadeia3_falsa():
    assert automato1("011110011101") == False


def teste2_cadeia1_verdadeira():
    assert automato2("000010") == True

def teste2_cadeia2_verdadeira():
    assert automato2("111111111111101111111111000") == True

def teste2_cadeia3_verdadeira():
    assert automato2("10111111") == True

def teste2_cadeia1_falsa():
    assert automato2("0000100") == False

def teste2_cadeia2_falsa():
    assert automato2("1111111111111011111111110000") == False

def teste2_cadeia3_falsa():
    assert automato2("101111110") == False


def teste3_cadeia1_verdadeira():
    assert automato3("011111111101") == True

def teste3_cadeia2_verdadeira():
    assert automato3("10000000000000001101") == True

def teste3_cadeia3_verdadeira():
    assert automato3("11111111111111111101") == True

def teste3_cadeia1_falsa():
    assert automato3("0111111111011") == False

def teste3_cadeia2_falsa():
    assert automato3("100000000000000011011") == False

def teste3_cadeia3_falsa():
    assert automato3("111111111111111111011") == False


def teste4_cadeia1_verdadeira():
    assert automato4("aaaaaaaaabbbbbbbbcba") == True

def teste4_cadeia2_verdadeira():
    assert automato4("cccaaaabbbcca") == True

def teste4_cadeia3_verdadeira():
    assert automato4("aaababaacaaaabccccca") == True

def teste4_cadeia1_falsa():
    assert automato4("aaaaaaaaabbbbbbbbcbac") == False

def teste4_cadeia2_falsa():
    assert automato4("cccaaaabbbccab") == False

def teste4_cadeia3_falsa():
    assert automato4("aaababaacaaaabcccccac") == False
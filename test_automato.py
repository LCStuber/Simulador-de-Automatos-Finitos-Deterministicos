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
    assert automato1("abbbaba") == True

def teste1_cadeia2_verdadeira():
    assert automato1("abbbababbababbabbbbb") == True

def teste1_cadeia3_verdadeira():
    assert automato1("abbbabaababbababb") == True

def teste1_cadeia1_falsa():
    assert automato1("ababbbbbbbababababab") == False

def teste1_cadeia2_falsa():
    assert automato1("abbbabaab") == False

def teste1_cadeia3_falsa():
    assert automato1("abbbabaababbabab") == False


def teste2_cadeia1_verdadeira():
    assert automato2("abbbaba") == True

def teste2_cadeia2_verdadeira():
    assert automato2("abbbababbababbabbbbb") == True

def teste2_cadeia3_verdadeira():
    assert automato2("abbbabaababbababb") == True

def teste2_cadeia1_falsa():
    assert automato2("ababbbbbbbababababab") == False

def teste2_cadeia2_falsa():
    assert automato2("abbbabaab") == False

def teste2_cadeia3_falsa():
    assert automato2("abbbabaababbabab") == False


def teste3_cadeia1_verdadeira():
    assert automato3("abbbaba") == True

def teste3_cadeia2_verdadeira():
    assert automato3("abbbababbababbabbbbb") == True

def teste3_cadeia3_verdadeira():
    assert automato3("abbbabaababbababb") == True

def teste3_cadeia1_falsa():
    assert automato3("ababbbbbbbababababab") == False

def teste3_cadeia2_falsa():
    assert automato3("abbbabaab") == False

def teste3_cadeia3_falsa():
    assert automato3("abbbabaababbabab") == False


def teste4_cadeia1_verdadeira():
    assert automato4("abbbaba") == True

def teste4_cadeia2_verdadeira():
    assert automato4("abbbababbababbabbbbb") == True

def teste4_cadeia3_verdadeira():
    assert automato4("abbbabaababbababb") == True

def teste4_cadeia1_falsa():
    assert automato4("ababbbbbbbababababab") == False

def teste4_cadeia2_falsa():
    assert automato4("abbbabaab") == False

def teste4_cadeia3_falsa():
    assert automato4("abbbabaababbabab") == False
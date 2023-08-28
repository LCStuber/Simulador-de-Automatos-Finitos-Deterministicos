import sys

class Autômato:
    estados:list
    sigma:list
    delta:list
    estado_inicial:str
    estados_finais:list

    def __init__(self, estados:list, sigma:list, delta:list, estado_inicial:str, estados_finais:list):
        self.estados = estados
        self.sigma = sigma
        self.delta = delta
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.__testar()

    def __testarEstados(self):
        if self.estado_inicial not in self.estados:
            raise ReferenceError(f"O autômato não pôde ser criado, pois o estado {self.estado_inicial} de estado inicial não está no conjunto de estados {self.estados}.")
        for estado in self.estados_finais:
            if self.estados_finais == ['']:
                break
            else:
                if estado not in self.estados:
                    raise ReferenceError(f"O autômato não pôde ser criado, pois o estado {estado} dentro de estados finais {self.estados_finais} não está no conjunto de estados {self.estados}.")
        for estado_atual, proximo_estado in self.delta:
            if estado_atual[0] not in self.estados:
                raise ReferenceError(f"O autômato não pôde ser criado, pois o estado {estado_atual[0]} dentro do seguinte passo de delta (({estado_atual[0]},{estado_atual[1]}),{proximo_estado}) não está no conjunto de estados {self.estados}.")
            if proximo_estado not in self.estados:
                raise ReferenceError(f"O autômato não pôde ser criado, pois o estado {proximo_estado} dentro do seguinte passo de delta (({estado_atual[0]},{estado_atual[1]}),{proximo_estado}) não está no conjunto de estados {self.estados}.")
        return True

    def __testarSigma(self):
        for estado_atual, proximo_estado in self.delta:
            if estado_atual[1] not in self.sigma:
                raise ReferenceError(f"O autômato não pôde ser criado, pois o símbolo {estado_atual[1]} dentro do seguinte passo de delta (({estado_atual[0]},{estado_atual[1]}),{proximo_estado}) não está no alfabeto {self.sigma}.")
        return True

    def __testar(self):
        if self.__testarEstados() and self.__testarSigma():
            print("Autômato criado com sucesso!")

    def __testarCadeia(self, cadeia:str):
        if cadeia == '':
            return True
        else:
            for i,símbolo in enumerate(cadeia):
                if símbolo not in self.sigma:
                    print(f"O autômato não pôde ser testado, pois o símbolo {símbolo} dentro da posição {i+1} da cadeia {cadeia} não está no alfabeto {self.sigma}.")
                    return False
        return True

    def verificarCadeia(self, cadeia:str):
        if self.__testarCadeia(cadeia):
            estadoAtual = self.estado_inicial
            if cadeia == "":
                return estadoAtual in self.estados_finais
            for símbolo in cadeia:
                contador = 0
                for eAtual, ePróx in self.delta:
                    if estadoAtual == eAtual[0] and símbolo == eAtual[1]:
                        estadoAtual = ePróx
                        print(f"({estadoAtual}, '{símbolo}') -> {ePróx}")
                        break
                    contador += 1
                if contador == len(self.delta):
                    print(f"Não é possível realizar a transição do estado {estadoAtual} com entrada {símbolo}")
                    return False
            return estadoAtual in self.estados_finais

def lerArquivo():
    arquivo = open("autômato.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

def interpretarArquivo():
    dados = {
    "estados":None,
    "sigma":None,
    "delta":None,
    "estado_inicial":None,
    "estados_finais":None
    }

    for linha in lerArquivo():
        if linha[0] == "#" or linha == "\n":
            continue
        linha = linha.replace(" ","").strip()
        index = linha.find("=")
        if index == -1:
            raise ValueError('''O arquivo autômato.txt foi escrito de maneira incorreta. Por favor, verifique se todos os campos contém o "=" e tente novamente.''')
        chave = linha[0:index].lower()
        valor = linha[index+1:]
        if chave == "estados":
            dados["estados"] = valor
        elif chave == "sigma":
            dados["sigma"] = valor
        elif chave == "delta":
            dados["delta"] = valor
        elif chave == "estado_inicial":
            dados["estado_inicial"] = valor
        elif chave == "estados_finais":
            dados["estados_finais"] = valor

    if (None in dados.values()):
        raise ValueError("Os campos do arquivo autômato.txt foram escritos de maneira incorreta. Por favor, verifique se estão todos os campos presentes e tente novamente.\nOs campos devem ser os seguintes: estados, sigma, delta, estado_inicial e estados_finais.")
    
    return transcreverParaPython(dados)

def transcreverParaPython(dados):
    dados["estados"] = list(dados["estados"][1:-1].split(","))
    dados["sigma"] = list(dados["sigma"][1:-1].split(","))
    if dados["delta"] == "{}":
        dados["delta"] = []
    else:
        try:
            dados["delta"] = [[d[1:dados["delta"].index(")")-2].split(","), d[dados["delta"].index(")"):]] for d in dados["delta"][2:-2].split("),(")]
        except:
            raise ValueError('''O campo "delta" do arquivo autômato.txt foi escrito de maneira incorreta. Por favor, verifique-o e tente novamente.\nEsse campo deve ser escrito da seguinte maneira: {((estado_atual,simbolo),proximo_estado),((estado_atual,simbolo),proximo_estado)}''')
    dados["estados_finais"] = list(dados["estados_finais"][1:-1].split(","))
    
    return Autômato(dados["estados"],dados["sigma"],dados["delta"],dados["estado_inicial"],dados["estados_finais"])

def criarAutômato():
    autômato = interpretarArquivo()
    return autômato

def inputCadeia():
    return input("Digite a cadeia que deseja testar com o seu autômato: ")

if __name__ == "__main__":
    sys.tracebacklimit = 0
    autômato = criarAutômato()
    try:
        while True:
            cadeia = inputCadeia()
            if autômato.verificarCadeia(cadeia):
                print(f"A cadeia {cadeia} foi aceita pelo autômato!")
            else:
                print(f"A cadeia {cadeia} foi rejeitada pelo autômato!")
    except KeyboardInterrupt:
        print("\nPrograma finalizado pelo usuário!")
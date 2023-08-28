import sys, argparse

class Automato:
    estados:list
    sigma:list
    delta:list
    estado_inicial:str
    estados_finais:list

    # Construtor da classe Autômato
    def __init__(self, estados:list, sigma:list, delta:list, estado_inicial:str, estados_finais:list):
        self.estados = estados
        self.sigma = sigma
        self.delta = delta
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.__testar() # Método privado para testar as propriedades do autômato ao inicializar


    # Método privado para testar se os estados estão definidos corretamente
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

    # Método privado para testar se os símbolos estão definidos corretamente no alfabeto
    def __testarSigma(self):
        for estado_atual, proximo_estado in self.delta:
            if estado_atual[1] not in self.sigma:
                raise ReferenceError(f"O autômato não pôde ser criado, pois o símbolo {estado_atual[1]} dentro do seguinte passo de delta (({estado_atual[0]},{estado_atual[1]}),{proximo_estado}) não está no alfabeto {self.sigma}.")
        return True


    # Método privado para testar tanto os estados quanto os símbolos usando os métodos __testarEstados e __testarSigma
    def __testar(self):
        if self.__testarEstados() and self.__testarSigma():
            print("Autômato criado com sucesso!")


    # Método privado para testar se os símbolos em uma cadeia de entrada estão no alfabeto
    def __testarCadeia(self, cadeia:str):
        if cadeia == '':
            return True
        else:
            for i,simbolo in enumerate(cadeia):
                if simbolo not in self.sigma:
                    print(f"O autômato não pôde ser testado, pois o símbolo {simbolo} dentro da posição {i+1} da cadeia {cadeia} não está no alfabeto {self.sigma}.")
                    return False
        return True


    # Método público para verificar se uma determinada cadeia é aceita pelo autômato
    def verificarCadeia(self, cadeia:str):
        if self.__testarCadeia(cadeia):
            estadoAtual = self.estado_inicial
            if cadeia == "":
                return estadoAtual in self.estados_finais
            for simbolo in cadeia:
                contador = 0
                for eAtual, eProx in self.delta:
                    if estadoAtual == eAtual[0] and simbolo == eAtual[1]:
                        estadoAtual = eProx
                        print(f"({estadoAtual}, '{simbolo}') -> {eProx}")
                        break
                    contador += 1
                if contador == len(self.delta):
                    print(f"Não é possível realizar a transição do estado {estadoAtual} com entrada {simbolo}")
                    return False
            return estadoAtual in self.estados_finais


# Leitura do arquivo "autômato.txt"
def lerArquivo(path:str):
    try:
        arquivo = open(path, "r")
        linhas = arquivo.readlines()
        arquivo.close()
        return linhas
    except FileNotFoundError:
        exit(f'''O arquivo "{path}" não foi encontrado. Por favor, verifique-o (ou remova o parâmetro --file para ler o arquivo "automato.txt" na raiz do projeto) e tente novamente.''')


# Função para interpretar os dados do arquivo e armazená-los em um dicionário
def interpretarArquivo(path:str):
    dados = {
    "estados":None,
    "sigma":None,
    "delta":None,
    "estado_inicial":None,
    "estados_finais":None
    }

    for linha in lerArquivo(path):
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


# Transcrição dos dados interpretados em um objeto Autômato
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
    
    return Automato(dados["estados"],dados["sigma"],dados["delta"],dados["estado_inicial"],dados["estados_finais"])


# Criação de um objeto Autômato interpretando os dados do arquivo
def criarautomato(path:str):
    automato = interpretarArquivo(path)
    return automato


# Input da entrada da cadeia do usuário
def inputCadeia():
    return input("Digite a cadeia que deseja testar com o seu autômato: ")

# Recebe o argumento da localização do arquivo-texto.
def getParser():
    parser = argparse.ArgumentParser(
                    prog='Simulador de Autômatos Finitos Determinísticos',
                    description='A partir de um arquivo-texto o usuário pode testar eu autômato finito com a cadeia que deseja.',
                    epilog='Selecione o arquivo que deseja com o -f "nomeArquivo" e depois digite as cadeias que deseja testar!')
    parser.add_argument("-f", "--file", type=str, help='Digite a localização do arquivo que deseja a partir da path do programa. Exemplo: -f automatos.txt para inicializar com o automato.txt que esta na mesma raiz da pasta do programa.')

    return parser.parse_args()

# Bloco executável do programa
if __name__ == "__main__":
    args = getParser()
    sys.tracebacklimit = 0
    automato = criarautomato(args.file if args.file != None else "automato.txt")
    try:
        while True:
            cadeia = inputCadeia()
            if automato.verificarCadeia(cadeia):
                print(f"A cadeia {cadeia} foi aceita pelo autômato!")
            else:
                print(f"A cadeia {cadeia} foi rejeitada pelo autômato!")
    except KeyboardInterrupt:
        print("\nPrograma finalizado pelo usuário!")
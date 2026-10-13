# CP5 Python
# Felipe Luan RM: 569565
# Anderson Macolino RM: 
# Turma: 1EPSPQ

import json

NOME_SISTEMA = "Plantão de TI"
ARQ_OCORRENCIAS = "ocorrencias.json"
ARQ_DIARIO = "diario.txt"
ARQ_PASSAGEM = "passagem.txt"

PRIORIDADES = ["alta", "media", "baixa"]
STATUS = ["aberto", "resolvido"]



# Leitura e gravação do JSON

def carregar_ocorrencias():
    #Retorna a lista salva, [] se o arquivo não existir ou None se o JSON for inválido."""
    try:
        with open(ARQ_OCORRENCIAS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        mostrar_erro_json()
        return None

    if not isinstance(dados, list):
        mostrar_erro_json()
        return None
    return dados


def mostrar_erro_json():
    print("\nERRO: o arquivo " + ARQ_OCORRENCIAS + " está com formato inválido.")
    print("Abra o arquivo, corrija o conteúdo (ele deve ser uma lista JSON, como []) e tente de novo.")
    print("O arquivo não foi alterado. Cadastro, consulta de ocorrências e passagem de plantão")
    print("ficam suspensos até a correção. O diário continua disponível.")


def salvar_ocorrencias(lista):
    with open(ARQ_OCORRENCIAS, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)



# Entrada de dados

def pedir_texto(mensagem):
    texto = input(mensagem).strip()
    while texto == "":
        print("O campo não pode ficar vazio.")
        texto = input(mensagem).strip()
    return texto


def pedir_opcao(mensagem, validas):
    valor = input(mensagem).strip().lower()
    while valor not in validas:
        print("Valor inválido. Use: " + ", ".join(validas) + ".")
        valor = input(mensagem).strip().lower()
    return valor

# Ocorrências

def registrar_ocorrencia():
    lista = carregar_ocorrencias()
    if lista is None:
        return

    print("\n--- Registrar ocorrência ---")
    servico = pedir_texto("Serviço afetado: ")
    descricao = pedir_texto("Descrição (problema e efeito para o usuário): ")
    prioridade = pedir_opcao("Prioridade (alta/media/baixa): ", PRIORIDADES)
    status = pedir_opcao("Status (aberto/resolvido): ", STATUS)

    if status == "resolvido":
        proxima_acao = "nenhuma"
    else:
        proxima_acao = pedir_texto("Próxima ação para a próxima equipe: ")

    ocorrencia = {
        "servico": servico,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": status,
        "proxima_acao": proxima_acao,
    }

    lista.append(ocorrencia)
    salvar_ocorrencias(lista)
    print("Ocorrência registrada com sucesso.")


def consultar_ocorrencias():
    lista = carregar_ocorrencias()
    if lista is None:
        return

    print("\n--- Ocorrências ---")
    if len(lista) == 0:
        print("Não há ocorrências registradas.")
        return

    numero = 1
    for item in lista:
        print("Ocorrência " + str(numero))
        print("  Serviço: " + str(item.get("servico", "")))
        print("  Descrição: " + str(item.get("descricao", "")))
        print("  Prioridade: " + str(item.get("prioridade", "")))
        print("  Status: " + str(item.get("status", "")))
        print("  Próxima ação: " + str(item.get("proxima_acao", "")))
        print("")
        numero += 1



# Diário

def registrar_diario():
    print("\n--- Registrar anotação no diário ---")
    servico = pedir_texto("Serviço: ")
    anotacao = pedir_texto("Anotação: ")

    with open(ARQ_DIARIO, "a", encoding="utf-8") as arquivo:
        arquivo.write(servico + " — " + anotacao + "\n")
    print("Anotação registrada.")

    
def consultar_diario():
    print("\n--- Diário ---")

    try:
        with open(ARQ_DIARIO, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

    except FileNotFoundError:
        print("Nenhuma anotação registrada")
        return

    if conteudo.strip() == "":
        print("Nenhuma anotação registrada")
    else:
        print(conteudo)

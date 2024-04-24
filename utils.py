import os

def criar_pasta(case_name):
    '''
    Função para criar um diretório para armezanar os resultados de uma 
    simulação.

    Parametros
    ----------
    case_name: str
        Nome do caso a ser simulado.

    Returna
    -------
    dir_saida: str
        Endereço do diretório de saída.

    dir_local: str
        Endereço do diretório local da onde se roda a simulação.

    
    Notas:
    ---
    Nenhum.

    '''
    dir_saida = f'./resultados/{case_name}'
    dir_local = os.getcwd()
    if not os.path.exists(dir_saida):
        os.mkdir(dir_saida)
    return dir_saida, dir_local

import os
import datetime
import shutil
import time

def copiar_arquivo_mais_recente(log_file):
    # Obtém a data atual
    data_atual = datetime.datetime.now()
    ano = data_atual.strftime('%Y')
    mes = data_atual.strftime('%m')
    dia = data_atual.strftime('%d')

    # Monta o caminho do diretório com base na data atual
    diretorio_base = r'V:/Dump_TabAuto'
    diretorio_mes = os.path.join(diretorio_base, ano, mes)
    diretorio_dia = os.path.join(diretorio_mes, dia)
    diretorio_destino = os.path.join(diretorio_base, 'Teste')

    # Verifica se o diretório do dia existe
    if os.path.exists(diretorio_dia):
        # Lista todos os arquivos no diretório
        arquivos = [os.path.join(diretorio_dia, f) for f in os.listdir(diretorio_dia) if os.path.isfile(os.path.join(diretorio_dia, f))]
        
        if arquivos:
            # Encontra o arquivo mais recente
            arquivo_mais_recente = max(arquivos, key=os.path.getmtime)
            
            # Copia o arquivo mais recente para o diretório de destino
            if not os.path.exists(diretorio_destino):
                os.makedirs(diretorio_destino)
            
            try:
                shutil.copy2(arquivo_mais_recente, diretorio_destino)
                print(f"{arquivo_mais_recente} copiado para {diretorio_destino}")
                log_file.write(f"{arquivo_mais_recente} copiado para {diretorio_destino}\n")
            except Exception as e:
                print(f"Erro ao copiar {arquivo_mais_recente}: {str(e)}")
                log_file.write(f"Erro ao copiar {arquivo_mais_recente}: {str(e)}\n")
        else:
            print(f"Nenhum arquivo encontrado no diretório '{diretorio_dia}'.")
            log_file.write(f"Nenhum arquivo encontrado no diretório '{diretorio_dia}'.\n")
    else:
        print(f"O diretório '{diretorio_dia}' não existe.")
        log_file.write(f"O diretório '{diretorio_dia}' não existe.\n")

# Função para verificar se é 18:05
def verificar_horario():
    agora = datetime.datetime.now()
    return agora.hour == 18 and agora.minute == 7

# Função para criar um novo arquivo de log diário
def criar_novo_arquivo_log():
    data_atual = datetime.datetime.now()
    nome_arquivo = data_atual.strftime('%Y-%m-%d') + '_log.txt'
    caminho_arquivo = os.path.join(r'L:/ROBOS/ROBO DUMP TAB AUTO/Logs', nome_arquivo)
    return open(caminho_arquivo, 'a')

# Loop principal que verifica a cada minuto se é 18:05
def main():
    while True:
        if verificar_horario():
            print("É 22:15! Copiando arquivo mais recente...")
            with criar_novo_arquivo_log() as log_file:
                log_file.write(f"\n\n--- Início do registro em {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
                copiar_arquivo_mais_recente(log_file)
                log_file.write(f"--- Fim do registro em {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n\n")
            # Aguarda 24 horas para verificar novamente
            time.sleep(86400)  # 24 horas em segundos
        else:
            # print("Esperando dar 22:15...")
            # Aguarda 1 minuto para verificar novamente
            time.sleep(30)

if __name__ == "__main__":
    main()

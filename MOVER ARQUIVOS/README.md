Este repositório contém um script Python desenvolvido para automatizar a cópia do arquivo mais recente de um diretório específico para outro, baseado em um horário agendado. O script utiliza módulos padrão do Python como os, datetime, shutil e time para realizar as operações necessárias.

Funcionalidades Principais:
Cópia Automática: Encontra e copia o arquivo mais recente de um diretório para outro.
Agendamento: Executa a operação de cópia em um horário específico do dia (18:07).
Registro: Cria um arquivo de log diário para registrar as operações realizadas.
Estrutura do Repositório:
script_copia_arquivo.py: Contém o código principal do script.
Logs/: Diretório onde são armazenados os arquivos de log diários.
Uso:
Configuração Inicial: Modifique os diretórios base (diretorio_base e diretorio_destino) conforme necessário.
Execução: Execute o script. Ele verificará a cada minuto se é 18:07 para iniciar a cópia do arquivo mais recente.
Requisitos:
Python 3.x
Módulos padrão do Python (os, datetime, shutil, time)
Autor:
João Victor da Silva

Contribuições:
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests para melhorias ou correções.
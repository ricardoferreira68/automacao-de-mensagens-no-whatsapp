# Porgrama para enviar mensagens via Whatsapp.
# Envia mensagens predefinidas para contatos gravados no arquivo 'mensagem.csv'.
import pandas as pd  # Usado para ler o arquivo csv.
from selenium import webdriver  # Manipular o site do Whatsapp.
from selenium.webdriver.common.keys import Keys  # Usado par simular o pressionamento da tecla <Enter>.
import time  # Usado para provocar pausa no programa.
import urllib.parse  # Usado par converter string como em string no formato de link de site (URL).


# Rotina para ler o arquivo de mensagens com mensagem.
def carregar_mensagens():
    # Lê os dados do arquivo em disco para a memória.
    arquivo_com_mensagens = pd.read_csv('mensagem.csv', sep=';', header=[0])
    return arquivo_com_mensagens


# Abre uma instância do navegador para ser manipulado pelo programa.
def abre_whatsapp_web():
    navegador = webdriver.Chrome()  # Cria um objeto do tipo Chrome.
    navegador.get('https://web.whatsapp.com/')  # Abre o navegador Chrome.
    # Laço para verificar se o site do whatsapp foi devidamente carregado.
    while len(navegador.find_elements_by_id('pane-side')) < 1:
        # Provoca uma pausa de 1 segundo enquanto não for identificado o elemento da página do Whatsapp.
        # Se não foi detectado o componente 'pane-side', significa que a página ainda não foi carreada.
        time.sleep(1)
    # Retorna o objeto do navegador aberto.
    return navegador


# Função para enviar mensagens.
def envia_mensagem(navegador, celular, message):
    # converte o texto da mensagem para o padrão URL.
    # Por exemplo: Se tiver espaço em branco no texto será convertido para %20
    message_url = urllib.parse.quote(message)
    # monta a URL com o site do Whatsapp, o número do celular e a mensagem.
    texto = f'https://web.whatsapp.com/send?phone={celular}&text={message_url}'
    # Abre o navegador com a página de mensagem do Whatsapp.
    navegador.get(texto)
    # Provoca uma pausa de 5 segundo para dar tempo de abertura do navegador.
    time.sleep(5)
    # Laço para verificar se a página de mensagem foi carregada no navegador.
    while len(navegador.find_elements_by_id('pane-side')) < 1:
        # Enquanto não for detectado o componente 'pane-side', será provocada uma pausa de 1 segundo.
        time.sleep(1)
    # Após detectar o carregamento da página, provoca uma pausa de
    # 5 segundo para garantir a finalização do carregamento.
    time.sleep(5)
    # Simular o pressionamento da tecla <Enter> no navegador aberto para enviar a mensagem.
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    # Laço para aguardar a finalização do envio da mensagem.
    while len(navegador.find_elements_by_id('pane-side')) < 1:
        # Enquanto não for detectado o componente 'pane-side', significa que o envio ainda não foi finalizado.
        time.sleep(1)
    # Após detectar o componente, indicando o envio, provoca uma pausa de
    # 5 segundo para garantir a finalização total do envio da mensagem.
    time.sleep(5)


# Início de Execução do programa.
if __name__ == '__main__':
    # Chama a função que lê o arquivo de mensagens em disco.
    mensagens = carregar_mensagens()
    # Chama a função que faz a abertura do navegador.
    secao_navegador = abre_whatsapp_web()
    # Laço para percorrer todas as mensagens lidas do arquivo.
    for i in mensagens.index:
        # Verifica se o número do telefone é difernete de branco.
        if mensagens["contato"][i] != '':
            # Chama a função que envia a mensagem.
            envia_mensagem(secao_navegador, mensagens['contato'][i], mensagens['mensagem'][i])
            print(f'Enviou a {i+1}a mensagem para {mensagens["contato"][i]}.')


# Fim do código.

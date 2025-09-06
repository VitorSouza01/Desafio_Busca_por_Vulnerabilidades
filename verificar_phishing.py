
# Busca por Vulnerabilidades com Desafios de Código em Python

# Detecção de Phishing por Padrões de E-mail


# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):

    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click", "promoção"]

    # TODO: Verifique se alguma palavra suspeita está presente no corpo do e-mail:

    # Verificando cada palavra do e-mail se é phishing
    for n in palavras_suspeitas:

        if n in email_usuario:

            return "Phishing"

    return "Seguro"


# Mensagem de Entrada
email_usuario = input()

email_usuario = email_usuario.strip()

# Execução da Função
resultado = verificar_phishing(email_usuario)

# Retorno da Classificação
print(f"Classificação: {resultado}")

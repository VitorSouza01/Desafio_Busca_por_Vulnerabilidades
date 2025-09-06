
# Busca por Vulnerabilidades com Desafios de Código em Python

# Detecção de Tentativas de Invasão em Logs

# Função para detectar tentativas de invasão em registros de log
def detectar_invasao(registros):

    # Variáveis para rastrear o ID do usuário atual e suas falhas consecutivas
    usuario_atual = None
    tentativas_consecutivas = 0
    invasor_detectado = None

    for registro in registros:
        # Divide cada registro em id_usuario e status
        id_usuario, status = registro.split(":")

        if id_usuario == usuario_atual:
            # Se o mesmo usuário continuar
            if status == "falha":
                tentativas_consecutivas += 1

            else:
                tentativas_consecutivas = 0 # reseta se tiver sucesso

        else:
            # Se trocou de usuário, verifica se o anterior teve mais de 3 falhas
            if tentativas_consecutivas > 3:
                invasor_detectado = usuario_atual
                break

            # Atualizar para o novo usuário
            usuario_atual = id_usuario
            tentativas_consecutivas = 1 if status == "falha" else 0

        # Checa se passou de 3 falhas consecutivas
        if tentativas_consecutivas > 3:
            invasor_detectado = usuario_atual
            break

    # Retorna o resultado final
    return invasor_detectado if invasor_detectado else "Nenhum invasor detectado"


# Função principal para executar o programa
def main():
    # Solicita ao usuário que insira os registros de log
    entrada = input()

    registros = [registro.strip().strip('"') for registro in entrada.split(",")]

    # Chama a função para detectar tentativas de invasão:
    resultado = detectar_invasao(registros)

    # Imprime o resultado
    print(resultado)


# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()
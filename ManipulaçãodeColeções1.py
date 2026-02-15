# Leitura da linha de identificadores de transações
entrada = input()

# Divide a string de entrada em uma lista de transações, separadas por ESPAÇO
# O método split() sem argumentos divide por qualquer espaço em branco
transacoes = entrada.split()

# Lista para armazenar as transações únicas (sem repetição)
transacoes_unicas = []

# Percorre cada transação na lista original
for transacao in transacoes:
    # Verifica se o item JÁ existe na nossa lista de únicos
    if transacao not in transacoes_unicas:
        # Se NÃO existe, adiciona na lista
        transacoes_unicas.append(transacao)

# Imprime a lista final, unindo os itens com um espaço entre eles
print(' '.join(transacoes_unicas))
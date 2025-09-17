import os

# Caminho principal onde estão as pastas
pasta_principal = '/home/victor/Área de Trabalho/Nova pasta/extração'

# Percorre todas as pastas
for raiz, pastas, arquivos in os.walk(pasta_principal):
    for arquivo in arquivos:
        if arquivo == "estoque_inicial.txt":
            caminho_arquivo = os.path.join(raiz, arquivo)
            
            # Abre o arquivo para leitura
            with open(caminho_arquivo, 'r') as f:
                conteudo = f.readline().strip()
            
            # Processa o conteúdo da linha
            if "ESTOQUE INICIAL:" in conteudo:
                partes = conteudo.split(",")
                estoque = partes[2].strip() + " Kg"  # Extrai o valor do estoque
                data = partes[-1].strip()           # Extrai a data
                
                # Novo conteúdo
                novo_conteudo = "ESTOQUE INICIAL, DATA\n"
                novo_conteudo += f"{estoque}, {data}\n"
                
                # Reescreve o arquivo com o novo conteúdo
                with open(caminho_arquivo, 'w') as f:
                    f.write(novo_conteudo)

print("Todos os arquivos foram processados!")

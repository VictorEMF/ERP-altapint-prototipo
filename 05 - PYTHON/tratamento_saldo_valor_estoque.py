import os
import re

# Função para processar um único arquivo
def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    # Inicializa os valores que vamos extrair
    saldo = ""
    tara_caixa = ""
    valor_unit = ""
    valor_estoque = ""

    # Extrai os valores das linhas conforme a lógica descrita
    for linha in linhas:
        if linha.startswith("SALDO"):
            saldo_match = re.search(r"SALDO,\s*([^,]+)", linha)
            if saldo_match:
                saldo = saldo_match.group(1).strip()
        if "TARA CAIXA" in linha:
            tara_caixa_match = re.search(r"TARA CAIXA\s*(-\s*[\d.,]+\s*KG)", linha)
            if tara_caixa_match:
                tara_caixa = tara_caixa_match.group(1).strip().replace(",", ".")
        elif "Valor unit. Do prod." in linha:
            valor_unit_match = re.search(r"Valor unit\. Do prod\.,\s*,\s*([^,]+),", linha)
            if valor_unit_match:
                valor_unit = valor_unit_match.group(1).strip()
        elif "Valor em estoque" in linha:
            valor_estoque_match = re.search(r"Valor em estoque,\s*,\s*([^,]+),", linha)
            if valor_estoque_match:
                valor_estoque = valor_estoque_match.group(1).strip()

    # Formata as linhas conforme o necessário
    header = "SALDO,TARA CAIXA,Valor unit. Do prod.,Valor em estoque\n"
    nova_linha = f"{saldo},{tara_caixa},{valor_unit},{valor_estoque}\n"

    # Escreve o novo conteúdo no arquivo
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(header)
        arquivo.write(nova_linha)

# Caminho base onde as 169 pastas estão localizadas
caminho_base = '/home/victor/Área de Trabalho/Nova pasta/extração'

# Itera sobre todas as pastas e subpastas
for raiz, _, arquivos in os.walk(caminho_base):
    for arquivo in arquivos:
        if arquivo == "saldo_valor_estoque.txt":
            caminho_arquivo = os.path.join(raiz, arquivo)
            print(f"Processando arquivo: {caminho_arquivo}")
            processar_arquivo(caminho_arquivo)

print("Processamento concluído.")

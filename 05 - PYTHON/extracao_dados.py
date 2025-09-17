import os
import pandas as pd

# Função para criar pastas e salvar os textos
def salvar_texto_em_pasta(base_dir, nome_pasta, nome_arquivo, conteudo):
    pasta = os.path.join(base_dir, nome_pasta)
    os.makedirs(pasta, exist_ok=True)
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

# Função para processar cada planilha
def processar_planilha(df, base_dir, nome_planilha):
    # Função auxiliar para incluir linhas vazias
    def processar_linhas_completas(sub_df):
        return '\n'.join(sub_df.apply(lambda row: ', '.join(row.fillna('').astype(str)), axis=1))

    # Extrair texto entre "FABRICA:" e "RESINA:"
    fabrica_linha = df[df[0].astype(str).str.contains('FABRICA:', na=False)].index[0]
    resina_linha = df[df[0].astype(str).str.contains('RESINA:', na=False)].index[0]
    texto_fabrica_resina = processar_linhas_completas(df.iloc[fabrica_linha:resina_linha + 1])
    salvar_texto_em_pasta(base_dir, nome_planilha, 'fabrica_resina.txt', texto_fabrica_resina)

    # Extrair texto onde está "ESTOQUE INICIAL:"
    estoque_inicial_linha = df[df[0].astype(str).str.contains('ESTOQUE INICIAL:', na=False)].index[0]
    texto_estoque_inicial = processar_linhas_completas(df.iloc[estoque_inicial_linha:estoque_inicial_linha + 1])
    salvar_texto_em_pasta(base_dir, nome_planilha, 'estoque_inicial.txt', texto_estoque_inicial)

    # Extrair linhas da linha 13 até uma linha antes de "SALDO"
    saldo_linha = df[df[0].astype(str).str.contains('SALDO', na=False)].index[0]
    texto_entre_13_saldo = processar_linhas_completas(df.iloc[12:saldo_linha])
    salvar_texto_em_pasta(base_dir, nome_planilha, 'entre_13_saldo.txt', texto_entre_13_saldo)

    # Extrair texto entre "SALDO" e "Valor em estoque"
    valor_estoque_linha = df[df[0].astype(str).str.contains('Valor em estoque', na=False)].index[0]
    texto_saldo_valor_estoque = processar_linhas_completas(df.iloc[saldo_linha:valor_estoque_linha + 1])
    salvar_texto_em_pasta(base_dir, nome_planilha, 'saldo_valor_estoque.txt', texto_saldo_valor_estoque)

    print(f"Processamento concluído para: {nome_planilha}")

# Caminho base para o arquivo Excel e onde salvar os resultados
caminho_arquivo_excel = '/home/victor/Área de Trabalho/Nova pasta/excel/Estoque Rev. 3.9.xlsx'
base_dir_resultados = '/home/victor/Área de Trabalho/Nova pasta/extração'
os.makedirs(base_dir_resultados, exist_ok=True)

# Abrir o arquivo Excel com múltiplas planilhas
excel = pd.ExcelFile(caminho_arquivo_excel)

# Processar cada planilha
for nome_planilha in excel.sheet_names:
    df = excel.parse(nome_planilha, header=None)
    processar_planilha(df, base_dir_resultados, nome_planilha)

print("Processamento finalizado!")

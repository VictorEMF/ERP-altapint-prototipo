import os

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Listas para armazenar as primeiras palavras e os dados com ":,"
    first_words = []
    second_words = []

    for line in lines:
        # Dividir a linha pelo delimitador ':'
        parts = line.split(':', 1)  # Limitar a divisão para o primeiro ':'
        if len(parts) > 1:
            first_word = parts[0].strip()
            first_words.append(first_word)

            # Capturar ":," e o primeiro valor após ele (se houver)
            after_colon = parts[1].strip()
            if after_colon.startswith(','):  # Garantir que ":," seja mantido
                second_part = '' + after_colon[1:].split(',', 1)[0].strip()
            else:
                second_part = ':' + after_colon.split(',', 1)[0].strip()

            second_words.append(second_part)

    # Retornar as palavras formatadas
    return ','.join(first_words) + '\n' + ','.join(second_words)

def process_and_update_files(root_dir):
    for folder_name, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'fabrica_resina.txt':
                file_path = os.path.join(folder_name, filename)
                processed_content = process_file(file_path)

                # Substituir o conteúdo do arquivo pelo conteúdo processado
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(processed_content)

# Caminho da pasta raiz contendo as 169 pastas
root_directory = '/home/victor/Área de Trabalho/Nova pasta/extração'

# Processar e atualizar todos os arquivos
process_and_update_files(root_directory)

print('Arquivos "fabrica_resina.txt" atualizados com sucesso!')

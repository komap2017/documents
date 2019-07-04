from src.extractor import get_files
from src.text import extract_text
from src.names import get_names
import os
import argparse


def get_text(path):
    return extract_text(path, lang='rus')


def main():
    parser = argparse.ArgumentParser(description='Извлечение информации о выданных доверенностях')
    parser.add_argument('--keyword', '-k', required=True, type=str, help='Ключевое слово, которое ищется в документах, в указанной папке')
    parser.add_argument('--dir', '-d', required=True, type=str,help='Папка, в которой располагаются документы доверенности')
    args = parser.parse_args()
    path = args.dir
    # path = 'доверенности'
    files = get_files(path)
    # keyword = 'июль'
    keyword = args.keyword
    keyword = keyword.lower()
    for file in files[::-1]:
        text = get_text(file)
        file_name = os.path.basename(file)
        if keyword in text.lower():
            name = get_names(text)
            print('Слово обнаружено в документе!')
            print(f'Название документа: {file_name}')
            output_name = ' '.join(name)
            print(f'На кого выдана доверенность: {output_name}')
        else:
            print(f'В документе {file_name} не было найдено слово {keyword}!')
        print()


if __name__ == '__main__':
    main()

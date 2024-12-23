import os
import logging
from collections import namedtuple
import argparse

# Настройка логирования
logging.basicConfig(
    filename="directory_info.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Определение namedtuple
FileInfo = namedtuple("FileInfo", ["name", "extension", "is_directory", "parent_directory"])

def collect_directory_info(directory_path):
    """
    Собирает информацию о содержимом директории.
    
    :param directory_path: Путь к директории.
    :return: Список объектов FileInfo.
    """
    file_info_list = []

    # Проверка существования директории
    if not os.path.isdir(directory_path):
        logging.error(f"Путь {directory_path} не является директорией.")
        raise ValueError(f"Путь {directory_path} не является директорией.")
    
    # Итерация по содержимому директории
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        parent_dir = os.path.basename(directory_path)
        
        if os.path.isdir(item_path):
            file_info = FileInfo(name=item, extension="", is_directory=True, parent_directory=parent_dir)
        else:
            name, extension = os.path.splitext(item)
            file_info = FileInfo(name=name, extension=extension.lstrip("."), is_directory=False, parent_directory=parent_dir)
        
        file_info_list.append(file_info)
        
        # Логирование информации
        logging.info(f"Объект: {file_info}")
    
    return file_info_list

def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description="Сбор информации о содержимом директории.")
    parser.add_argument("directory", type=str, help="Путь до директории.")
    
    args = parser.parse_args()
    directory_path = args.directory
    
    try:
        directory_info = collect_directory_info(directory_path)
        for info in directory_info:
            print(info)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

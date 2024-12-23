import argparse

def main():
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(description="Скрипт для работы с числами и строками с дополнительными опциями.")
    
    # Добавление обязательных аргументов
    parser.add_argument("number", type=int, help="Число для обработки")
    parser.add_argument("text", type=str, help="Строка для вывода")
    
    # Добавление опций
    parser.add_argument("--verbose", action="store_true", help="Вывод дополнительной информации")
    parser.add_argument("--repeat", type=int, default=1, help="Количество повторений строки в выводе (по умолчанию 1)")
    
    # Разбор аргументов
    args = parser.parse_args()
    
    # Логика обработки
    if args.verbose:
        print(f"Начало выполнения скрипта...")
        print(f"Получено число: {args.number}")
        print(f"Получена строка: {args.text}")
        print(f"Количество повторений: {args.repeat}")
    
    for i in range(args.repeat):
        print(f"({i + 1}) {args.text}")
    
    if args.verbose:
        print("Завершение выполнения скрипта.")

if __name__ == "__main__":
    main()

from datetime import datetime, timedelta

def get_future_date(days_from_now):
    """
    Возвращает дату, которая наступит через указанное количество дней от текущей даты.
    
    :param days_from_now: Количество дней от текущей даты.
    :return: Строка с датой в формате YYYY-MM-DD.
    """
    # Получение текущей даты
    current_date = datetime.now()
    
    # Вычисление будущей даты
    future_date = current_date + timedelta(days=days_from_now)
    
    # Форматирование будущей даты
    formatted_date = future_date.strftime('%Y-%m-%d')
    
    return formatted_date

# Пример использования
days = 10
future_date = get_future_date(days)
print(f"Дата через {days} дней: {future_date}")

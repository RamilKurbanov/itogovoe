from datetime import datetime

# Получение текущей даты и времени
current_datetime = datetime.now()

# Форматирование даты и времени в формате YYYY-MM-DD HH:MM:SS
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Получение полного названия дня недели
day_of_week = current_datetime.strftime('%A')

# Получение номера недели в году
week_number = current_datetime.isocalendar()[1]

# Вывод результатов
print(f"Текущая дата и время: {formatted_datetime}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")

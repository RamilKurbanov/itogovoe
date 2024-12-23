import logging

# Создание логгеров
logger = logging.getLogger("multi_file_logger")
logger.setLevel(logging.DEBUG)

# Создание обработчиков для разных файлов
debug_info_handler = logging.FileHandler("debug_info.log")
debug_info_handler.setLevel(logging.DEBUG)

warnings_errors_handler = logging.FileHandler("warnings_errors.log")
warnings_errors_handler.setLevel(logging.WARNING)

# Создание форматов для логов
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Применение форматов к обработчикам
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Примеры логов
logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")

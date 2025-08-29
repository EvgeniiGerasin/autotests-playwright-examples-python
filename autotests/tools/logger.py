import logging
import functools
from playwright.sync_api import Page


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("test_actions.log", encoding="utf-8"),
        logging.StreamHandler()  # вывод в консоль
    ]
)

logger = logging.getLogger("playwright_actions")

class LoggedPage:
    def __init__(self, page: Page):
        self.page = page

    def __getattr__(self, name):
        # Получаем атрибут из оригинального page
        attr = getattr(self.page, name)

        # Если это метод — оборачиваем его в логгер
        if callable(attr):
            return self._wrap_method(name, attr)
        return attr

    def _wrap_method(self, method_name: str, method):
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            # Логируем вызов
            logger.info(f"Выполняю: {method_name} с аргументами {args}, {kwargs}")

            try:
                result = method(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"Ошибка в {method_name}: {e}")
                raise
        return wrapper
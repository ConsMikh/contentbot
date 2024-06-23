'''Все операции для работы с контентом
'''
import datetime
import os
import logging
import codecs
import string

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class ContentHandler():

    PATH_TO_SAVE = os.getenv("PATH_TO_SAVE")

    def __init__(self, content: str) -> None:
        self.content = content.split('\n')
        self.header = self.content[0]
        self.body = self.content[1:]

    def save_content(self):
        try:
            self._prepare_header()
            file_name = f"{''.join(c for c in self.header if c not in string.punctuation)}.md"
            with codecs.open(os.path.join(ContentHandler.PATH_TO_SAVE, file_name), "w", "utf-8") as f:
                f.write("\n".join(self.full_header + self.body))
                logging.info(f"Save message: {self.header}")
            return 1
        except Exception as e:
            logging.error(e.__repr__())
            return 0

    def _prepare_header(self):

        self.full_header = [f"{datetime.datetime.today().date().strftime('%Y.%m.%d')}\n",
                            f"# {self.header}"]


# Режим сохранения. По умолчанию каждое сообщение - отдельный файл

# Создание маркдаун структуры
# Накопление контента из сообщений
# Сохранение в файл
# Решение проблем с конфликтами имен

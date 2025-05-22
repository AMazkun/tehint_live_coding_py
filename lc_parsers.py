# 1. Розробити функцію `get_int(s: str)`, яка буде отримувати ціле значення з рядка,
# використовуючи ланцюжок парсерів, що настроюються, і повертати `int` або `None`, якщо вилучення неможливо.
# Уніфікація обробки потенційно різнорідних форматів
# - парсер, коли вхідний рядок - це представлений рядком JSON ключ "value" '{"value": 10}'
# - парсер вхідного рядка - plain text

# Зробити реалізацію у парадигмі:
# - pure OOP
# - functional programming


# Вхідні дані:
# - Один аргумент `s:str` - довільний рядок.

# Вихідні дані:
# - Об'єкт типу `int`, якщо значення успішно вилучено.
# - `None`, якщо не вдалося розпізнати допустиме ціле число.

# 2. Зробити тести

import json
from abc import abstractmethod
from typing import Optional, Callable, List


# PURE OOP PARSERS
class Parser:
    @classmethod
    @abstractmethod
    def parse(cls, input_str: str) -> Optional[int]:
        raise NotImplementedError

class JsonParser(Parser):
    @classmethod
    def parse(cls, input_str: str) -> Optional[int]:
        try:
            data = json.loads(input_str)
            value = data.get("value")
            return value if isinstance(value, int) else None
        except:
            return None

class PlainTextParser(Parser):
    @classmethod
    def parse(cls, input_str: str) -> Optional[int]:
        return int(input_str) if input_str.isdigit() else None

def get_int_o(s:str) -> Optional[int]:
    parsers = [JsonParser, PlainTextParser]
    return next((val for parser in parsers if (val := parser.parse(s)) is not None), None)

# FUNCTIONAL
# y = (x+1)**2
# y = (x+1)*(x+1)
# y = x**2 + x + x + 1**2
# y = x**2 + 2*x + 1

def parse_json(s: str) -> Optional[int]:
    try:
        data = json.loads(s)
        value = data.get("value")
        return value if isinstance(value, int) else None
    except:
        return None

def parse_text(s:str) -> Optional[int]:
    return int(s) if s.isdigit() else None

def get_int_f(s:str) -> Optional[int]:
    parsers: List[Callable[[str], Optional[int]]] = [parse_json, parse_text]
    return next((val for parser in parsers if (val := parser(s)) is not None), None)

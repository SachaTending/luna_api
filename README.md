# luna_api
Простой враппер api для LunaStore

Для установки используйте pip
```sh
pip install git+https://github.com/SachaTending/luna_api
```

Пример использования:
```py
from luna_api import LunaInstance

instance = LunaInstance() # Можно указать свой api инстанса LunaStore в параметрах

heartbeat_response = instance.heartbeat() # Вызываем метод heartbeat и получаем ответ в json

print(f"Ответ heartbeat: {heartbeat_response}")
```

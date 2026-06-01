# luna_api
Простой враппер api для LunaStore

Пример использования:
```py
from luna_api import LunaInstance

instance = LunaInstance() # Можно указать свой api инстанса LunaStore в параметрах

heartbeat_response = instance.heartbeat() # Вызываем метод heartbeat и получаем ответ в json

print(f"Ответ heartbeat: {heartbeat_response}")
```

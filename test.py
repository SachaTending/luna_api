from luna_api import LunaInstance, InstanceError
from traceback import print_exception

lunastore = LunaInstance()

print("Тест 1. heartbeat")
try:
    resp = lunastore.heartbeat()
    print(f"Ответ: {resp}")
except InstanceError as e:
    print("Ошибка при выполнении запроса")
    print_exception(e)


print("Тест 2. getAppInfo")
try:
    resp = lunastore.get_app_info(128)
    print(f"Ответ: {resp}")
except InstanceError as e:
    print("Ошибка при выполнении запроса")
    print_exception(e)

print("Тест 3. search")
try:
    resp = lunastore.search("Total")
    print(f"Ответ: {resp}")
except InstanceError as e:
    print("Ошибка при выполнении запроса")
    print_exception(e)

print("Тест 4. getAppList")
try:
    resp = lunastore.get_app_list(1)
    print(f"Ответ слишком большой для консоли")
except InstanceError as e:
    print("Ошибка при выполнении запроса")
    print_exception(e)

print("Тест 5. getDistributionList")
try:
    resp = lunastore.get_dist_list(128)
    print(f"Ответ: {resp}")
except InstanceError as e:
    print("Ошибка при выполнении запроса")
    print_exception(e)

print("Тест 5. kunyakin")
try:
    resp = lunastore.kunyakin()
    print(f"Ответ: {resp}")
except InstanceError as e:
    print("Ошибка при выполнении запроса")
    print_exception(e)

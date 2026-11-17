from google import genai

# Инициализируем клиент, передавая API-ключ прямо в коде
# (замените текст в кавычках на ваш реальный ключ)
client = genai.Client(api_key="ВАШ_РЕАЛЬНЫЙ_API_КЛЮЧ")

print("Список доступных моделей:")
for model in client.models.list():
    # Выводим имя модели и поддерживаемые методы
    print(f"- Имя: {model.name}")
    if hasattr(model, "supported_generation_methods"):
        print(f"  Поддерживаемые методы: {model.supported_generation_methods}")
def get_price_change(product_name, filename):
    import datetime

    # Відкриваємо файл з даними про товари
    with open(filename, 'r') as file:
        # Читаємо кожний рядок файла
        lines = file.readlines()

    # Знаходимо дату, яка була місяць тому
    one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)

    # Створюємо словник для зберігання даних про ціну товару
    prices = {}

    # Проходимося по кожному рядку файла
    for line in lines:
        # Розділяємо рядок на назву товару, дату та ціну
        name, date_str, price_str = line.strip().split(',')

        # Переводимо дату в об'єкт datetime
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

        # Якщо дата більше, ніж місяць тому, і назва товару відповідає вхідному параметру
        if date > one_month_ago and name == product_name:
            # Зберігаємо ціну товару у словнику
            prices[date] = float(price_str)

    # Якщо немає записів про ціну товару за останній місяць
    if not prices:
        return "Немає записів про ціну товару за останній місяць"

    # Знаходимо першу та останню ціну товару за останній місяць
    first_price = min(prices.values())
    last_price = max(prices.values())

    # Обчислюємо зміну ціни
    price_change = last_price - first_price

    # Повертаємо результат
    return f"Ціна товару {product_name} змінилась на {price_change} за останній місяць"

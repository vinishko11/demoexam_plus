def validate_material_data(data):
    errors = []

    for field in ['name', 'price', 'quantity', 'min_quantity', 'quantity_pack', 'measure']:
        if not data.get(field):
            errors.append(f"Поле '{field}' не должно быть пустым")

    try:
        price = round(float(data['price']), 2)
        if price < 0:
            errors.append("Цена не может быть отрицательной")
    except (ValueError, KeyError):
        errors.append("Некорректная цена")

    for field in ['quantity', 'min_quantity', 'quantity_pack']:
        try:
            value = int(data[field])
            if field == 'min_quantity' and value < 0:
                errors.append("Минимальное количество не может быть отрицательным")
        except (ValueError, KeyError):
            errors.append(f"Поле '{field}' должно быть целым числом")

    return errors

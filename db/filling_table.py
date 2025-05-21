import pandas as pd

from db.create_table import connect_db

def filling_material_type(connect):
    try:
        df = pd.read_excel('../excel/Material_type_import.xlsx', engine = 'openpyxl')

        query = 'insert into material_type values (%s, %s)'

        cursor = connect.cursor()

        for row in df.itertuples():
            print(row)
            values = (row._1, row._2)
            cursor.execute(query, values)

        connect.commit()
        cursor.close()

        print('Данные добавлены в типы материалов')

    except Exception as e:
        print(e)

def filling_product_type(connect):
    try:
        df = pd.read_excel('../excel/Product_type_import.xlsx', engine = 'openpyxl')

        query = 'insert into product_type values (%s, %s)'

        cursor = connect.cursor()

        for row in df.itertuples():
            print(row)
            values = (row._1, row._2)
            cursor.execute(query, values)

        connect.commit()
        cursor.close()

        print('Данные добавлены в типы продукции')

    except Exception as e:
        print(e)

def filling_materials(connect):
    try:
        df = pd.read_excel('../excel/Materials_import.xlsx', engine = 'openpyxl')

        query = 'insert into materials values (%s, %s, %s, %s, %s, %s, %s)'

        cursor = connect.cursor()

        for row in df.itertuples():
            print(row)
            values = (row._1, row._2, round(row._3), round(row._4), round(row._5), round(row._6, 2), row._7)
            cursor.execute(query, values)

        connect.commit()
        cursor.close()

        print('Данные добавлены в материалы')

    except Exception as e:
        print(e)

def filling_products(connect):
    try:
        df = pd.read_excel('../excel/Products_import.xlsx', engine = 'openpyxl')

        query = 'insert into products values (%s, %s, %s, %s)'

        cursor = connect.cursor()

        for row in df.itertuples():
            print(row)
            values = (row._1, row._2, row.Артикул, round(row._4, 2))
            cursor.execute(query, values)

        connect.commit()
        cursor.close()

        print('Данные добавлены в продукцию')

    except Exception as e:
        print(e)

def filling_history(connect):
    try:
        df = pd.read_excel('../excel/Material_products__import.xlsx', engine='openpyxl')
        query = 'INSERT INTO history VALUES (%s,%s, %s, %s)'

        cursor = connect.cursor()

        for row in df.itertuples():
            index = row.Index
            original_name = row._1
            product_name = row.Продукция
            quantity = round(row._3, 2)

            # Проверка: существует ли material_name в таблице materials
            cursor.execute("""
                SELECT 1 FROM materials WHERE material_name = %s
            """, (original_name,))
            exists = cursor.fetchone()

            if not exists:
                # Если нет точного совпадения, ищем по первому слову
                first_word = original_name.split()[0]
                cursor.execute("""
                    SELECT material_name FROM materials
                    WHERE material_name ILIKE %s
                    LIMIT 1
                """, (first_word + '%',))
                match = cursor.fetchone()

                if match:
                    corrected_name = match[0]
                    print(f"Заменено: '{original_name}' -> '{corrected_name}'")
                    material_name = corrected_name
                else:
                    print(f"❌ Не найден материал: '{original_name}' — пропущено")
                    continue  # пропускаем вставку, если ничего не найдено
            else:
                material_name = original_name

            cursor.execute(query, (index, material_name, product_name, quantity))

        connect.commit()
        cursor.close()

        print('Данные добавлены в историю')

    except Exception as e:
        print(e)


filling_material_type(connect_db())
filling_product_type(connect_db())
filling_materials(connect_db())
filling_products(connect_db())
filling_history(connect_db())

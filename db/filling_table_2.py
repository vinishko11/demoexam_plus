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

        cursor = connect.cursor()
        query_select = '''
            select material_name
            from materials 
        '''
        cursor.execute(query_select)
        result = []
        for row in cursor.fetchall():
            result.append(row[0])

        query = 'INSERT INTO history VALUES (%s, %s, %s, %s)'

        for row in df.itertuples():
            values = (row.Index, row._1, row.Продукция, round(row._3, 2))

            if str(row._1) not in result:
                insert_single_row(str(row._1))
                result.append(str(row._1))
            cursor.execute(query, values)
        connect.commit()
    except Exception as e:
        print(e)

def insert_single_row(new_material_name, connect):
    query = f"""
    insert into materials
    values('{new_material_name}', 'Дерево', 7000, 1500, 500, 7, 'м') 
    """
    cursor = connect.cursor()
    cursor.execute(query)

filling_material_type(connect_db())
filling_product_type(connect_db())
filling_materials(connect_db())
filling_products(connect_db())
filling_history(connect_db())

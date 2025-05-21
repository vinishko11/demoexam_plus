from db.create_table import connect_db

class Database():
    def __init__(self) :
        self.connect = connect_db()

    def take_all_materials(self):
        query = '''
            select * from materials
        '''
        try:
            cursor = self.connect.cursor()
            cursor.execute(query)

            material_data = []

            for row in cursor.fetchall():
                material_data.append({
                    'name':row[0], 'type':row[1], 'price':row[2], 'quantity':row[3], 'min_quantity':row[4], 'quantity_pack':row[5], 'measure':row[6]
                })
            cursor.close()

            print('Данные по материалам получены', material_data)
            return material_data

        except Exception as e:
            print('Данные по материалам не были получены', e)

    def count_min_quantity(self, material_name):
        try:
            query = f'''
                select sum(min_quantity_material) from history where material_name = '{material_name}'
            '''
            cursor = self.connect.cursor()
            cursor.execute(query)

            count_min_quantity = cursor.fetchone()[0] or 0

            cursor.close()

            print('Данные по минимально требуемым материалам получены')

            return count_min_quantity
        except Exception as e:
            print('Ошибка', e)

    def take_all_material_type(self):
        query = '''
                select material_type from material_type
            '''
        try:
            cursor = self.connect.cursor()
            cursor.execute(query)

            material_type = []

            for row in cursor.fetchall():
                material_type.append(row[0])

            cursor.close()

            print('Данные по типам материалов получены')
            return material_type
        except Exception as e:
            print('Данные по типам материалов не были получены', e)

    def add_material(self, material_data):
        query = '''
            insert into materials values (%s, %s, %s, %s, %s, %s, %s)
        '''
        try:
            values = (
                material_data['name'],
                material_data['type'],
                material_data['price'],
                material_data['quantity'],
                material_data['min_quantity'],
                material_data['quantity_pack'],
                material_data['measure']
            )

            cursor = self.connect.cursor()
            cursor.execute(query, values)
            self.connect.commit()
            cursor.close()
            print('Материал успешно добавлен')
            return True
        except Exception as e:
            print('Материал не был добавлен', e)
            return False

    def take_material_info(self, material_name):
        query = f'''
            select * from materials where material_name = '{material_name}'
        '''
        try:
            cursor = self.connect.cursor()
            cursor.execute(query)

            material_data = []

            for row in cursor.fetchall():
                material_data.append({
                    'name':row[0], 'type':row[1], 'price':row[2], 'quantity':row[3], 'min_quantity':row[4], 'quantity_pack':row[5], 'measure':row[6]
                })
            cursor.close()

            print('Данные по материалам получены')
            return material_data
        except Exception as e:
            print('Данные по материалам не были получены', e)

    def edit_material(self, original_name, material_data):
        query = f'''
            update materials 
            set material_name = %s, material_type = %s, unit_price = %s, quantity = %s, min_quantity = %s, quantity_pack = %s,
            measure = %s where material_name = %s
        '''
        try:
            values = (
                material_data['name'],
                material_data['type'],
                material_data['price'],
                material_data['quantity'],
                material_data['min_quantity'],
                material_data['quantity_pack'],
                material_data['measure'],
                original_name
            )

            cursor = self.connect.cursor()
            cursor.execute(query, values)
            self.connect.commit()
            cursor.close()
            print('Материал успешно отредактирован')
            return True
        except Exception as e:
            print('Материал не был отредактирован', e)
            return False

    def take_products_list(self, material_name):
        try:
            query = f'''
                select p.product_type, p.product_name, p.article, p.min_cost, h.min_quantity_material
                from products p join history h on h.product_name = p.product_name
                where h.material_name = '{material_name}'
            '''
            cursor = self.connect.cursor()
            cursor.execute(query)
            products = []
            for row in cursor.fetchall():
                products.append({
                    'type':row[0],
                    'name':row[1],
                    'article':row[2],
                    'min_cost':row[3],
                    'min_quantity_material':row[4]
                    })
            cursor.close()
            print('Данные по продуктам получены')
            return products
        except Exception as e:
            print('Ошибка', e)



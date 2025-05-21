import psycopg as pg

from db import config

def create_table(connect):
    try:
        query = '''
            create table material_type (
                material_type text not null primary key,
                break_percent text not null
            );
            
            create table materials (
                material_name text not null primary key,
                material_type text not null references material_type(material_type) ON UPDATE CASCADE,
                unit_price int not null,
                quantity int not null,
                min_quantity int not null,
                quantity_pack real not null,
                measure text not null
            );
            
            create table product_type (
                product_type text not null primary key,
                product_index real not null
            );
            
            create table products (
                product_type text not null references product_type(product_type) ON UPDATE CASCADE,
                product_name text not null primary key,
                article text not null,
                min_cost real not null
            );
            
            create table history (
                index int not null primary key,
                material_name text not null references materials(material_name) ON UPDATE CASCADE,
                product_name text not null references products(product_name) ON UPDATE CASCADE,
                min_quantity_material real not null
            )
        '''

        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
        cursor.close()

        print("Таблицы созданы")
    except Exception as e:
        print("Ошибка создания таблиц", e)

def connect_db():
    try:
        connect = pg.connect(host = config.HOST, port = config.PORT, user = config.USER, password = config.PASSWORD, dbname = config.DBNAME)
        if connect:
            print("Подключение к базе данных успешно установлено")
            return connect
    except Exception as e:
        print("Ошибка подключения к базе данных", e)

create_table(connect_db())
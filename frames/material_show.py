from PySide6.QtWidgets import *
from PySide6.QtGui import *

from frames.add_material import AddMaterial
from frames.edit_material import EditMaterial
from frames.products_show import ProductsShow


class MaterialShow(QFrame):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.db = controller.db

        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        title = QLabel('Образ Плюс')
        title.setObjectName('title')
        self.layout.addWidget(title)

        icon = QLabel()
        icon.setPixmap(QPixmap('res/icon.png'))
        icon.setFixedSize(100, 100)
        icon.setScaledContents(True)

        icon_layout = QHBoxLayout()
        icon_layout.addStretch()
        icon_layout.addWidget(icon)
        icon_layout.addStretch()

        self.layout.addLayout(icon_layout)

        self.create_card()

    def create_card(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        cards = QWidget()
        cards_layout = QVBoxLayout(cards)

        for material in self.db.take_all_materials():
            card = QWidget()
            card.setObjectName('card')
            card_layout = QVBoxLayout(card)

            title_type_name = QLabel(f'{material['type']} | {material['name']}')
            title_type_name.setObjectName('title_main')

            medium = QHBoxLayout()
            in_medium = QVBoxLayout()

            title_min_quantity = QLabel(f'Минимальное количество: {material['min_quantity']}')
            title_min_quantity.setObjectName('subtitle')

            title_quantity = QLabel(f'Количество на складе: {material['quantity']}')
            title_quantity.setObjectName('subtitle')

            title_price_measure = QLabel(f'Цена: {material['price']} р / Единица измерения: {material['measure']}')
            title_price_measure.setObjectName('subtitle')

            in_medium.addWidget(title_min_quantity)
            in_medium.addWidget(title_quantity)
            in_medium.addWidget(title_price_measure)

            title_min = QLabel(f'Требуемое количество: {round(self.db.count_min_quantity(material['name']), 2)}')
            title_min.setObjectName('title_right')

            medium.addLayout(in_medium)
            medium.addWidget(title_min)

            card_layout.addWidget(title_type_name)
            card_layout.addLayout(medium)

            btn_suppliers = QPushButton("Список партнеров")
            btn_suppliers.setObjectName("btn")
            btn_suppliers.clicked.connect(lambda event, name=material['name']: self.open_products_list(name))
            card_layout.addWidget(btn_suppliers)

            card.mousePressEvent = lambda event, name=material['name']: self.open_edit_frame(name)
            cards_layout.addWidget(card)

        scroll.setWidget(cards)
        self.layout.addWidget(scroll)

        btn_add = QPushButton('Добавить материал')
        btn_add.setObjectName('btn')
        btn_add.clicked.connect(self.open_create_frame)
        self.layout.addWidget(btn_add)

    def open_edit_frame(self, material_name):
        edit_frame = EditMaterial(self.controller, material_name)
        self.controller.frames_container.addWidget(edit_frame)
        self.controller.frames_container.setCurrentWidget(edit_frame)

    def open_create_frame(self):
        create_frame = AddMaterial(self.controller)
        self.controller.frames_container.addWidget(create_frame)
        self.controller.frames_container.setCurrentWidget(create_frame)

    def open_products_list(self, material_name):
        products_frame = ProductsShow(self.controller, material_name)
        self.controller.frames_container.addWidget(products_frame)
        self.controller.frames_container.setCurrentWidget(products_frame)


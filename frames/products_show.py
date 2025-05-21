from PySide6.QtWidgets import *

class ProductsShow(QFrame):
    def __init__(self, controller, material_name):
        super().__init__()

        self.controller = controller
        self.db = controller.db
        self.material_name = material_name

        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        title = QLabel('Продукция')
        title.setObjectName('title')
        self.layout.addWidget(title)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        container_layout = QVBoxLayout(container)

        products = self.db.take_products_list(self.material_name)

        if products:
            for product in products:
                card = QWidget()
                card.setObjectName("card")
                card_l = QVBoxLayout(card)

                name = QLabel(f"Наименование продукции: {product['name']}")
                name.setObjectName("subtitle")

                type = QLabel(f"Тип продукции: {product['type']}")
                type.setObjectName("subtitle")

                article = QLabel(f"Артикул: {product['article']}")
                article.setObjectName("subtitle")

                min_cost = QLabel(f"Минимальная стоимость: {product['min_cost']}")
                min_cost.setObjectName("subtitle")

                min_quantity_material = QLabel(f"Минимальное количество материала: {product['min_quantity_material']}")
                min_quantity_material.setObjectName("subtitle")

                card_l.addWidget(name)
                card_l.addWidget(type)
                card_l.addWidget(article)
                card_l.addWidget(min_cost)
                card_l.addWidget(min_quantity_material)

                container_layout.addWidget(card)
        else:
            no_suppliers = QLabel("Нет продукции для этого материала")
            no_suppliers.setObjectName("title_main")
            container_layout.addWidget(no_suppliers)

        scroll_area.setWidget(container)
        self.layout.addWidget(scroll_area)

        btn_back = QPushButton("Назад")
        btn_back.setObjectName("btn")
        btn_back.clicked.connect(lambda: self.controller.frames_container.setCurrentWidget(self.controller.frame_start))

        self.layout.addWidget(btn_back)
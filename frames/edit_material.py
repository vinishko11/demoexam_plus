from PySide6.QtWidgets import *

from messages import war_message, info_message, crit_message

class EditMaterial(QFrame):
    def __init__(self, controller, material_name):
        super().__init__()

        self.controller = controller
        self.db = controller.db
        self.original_name = material_name

        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        title = QLabel('Редактирование материала')
        title.setObjectName('title')
        self.layout.addWidget(title)

        material = self.db.take_material_info(self.original_name)[0]
        print(material)

        self.label_pattern('Наименование материала')
        self.material_name_edit = self.edit_pattern(f'{material["name"]}')
        self.layout.addWidget(self.material_name_edit)

        self.label_pattern('Выберите тип материала')
        self.material_type = QComboBox()
        self.material_type.addItems(self.db.take_all_material_type())
        self.layout.addWidget(self.material_type)

        self.label_pattern('Цена единицы материала')
        self.unit_price = self.edit_pattern(f'{material["price"]}')
        self.layout.addWidget(self.unit_price)

        self.label_pattern('Количество на складе')
        self.quantity = self.edit_pattern(f'{material["quantity"]}')
        self.layout.addWidget(self.quantity)

        self.label_pattern('Минимальное количество')
        self.min_quantity = self.edit_pattern(f'{material["min_quantity"]}')
        self.layout.addWidget(self.min_quantity)

        self.label_pattern('Количество в упаковке')
        self.quantity_pack = self.edit_pattern(f'{material["quantity_pack"]}')
        self.layout.addWidget(self.quantity_pack)

        self.label_pattern('Единица измерения')
        self.measure = self.edit_pattern(f'{material["measure"]}')
        self.layout.addWidget(self.measure)

        btn_back = QPushButton('Назад')
        btn_back.setObjectName('btn')
        btn_back.clicked.connect(lambda: self.controller.frames_container.setCurrentWidget(self.controller.frame_start))
        self.layout.addWidget(btn_back)

        btn_add = QPushButton('Редактировать материал')
        btn_add.setObjectName('btn')
        btn_add.clicked.connect(self.edit_material)
        self.layout.addWidget(btn_add)

    def label_pattern(self, text):
        label = QLabel(text)
        label.setObjectName('label_hint')
        self.layout.addWidget(label)

        return label

    def edit_pattern(self, text):
        edit = QLineEdit()
        edit.setText(text)
        edit.setObjectName('edit_hint')
        self.layout.addWidget(edit)

        return edit

    def edit_material(self):
        material_data = {
            'name': self.material_name_edit.text(),
            'type': self.material_type.currentText(),
            'price': self.unit_price.text(),
            'quantity': self.quantity.text(),
            'min_quantity': self.min_quantity.text(),
            'quantity_pack': self.quantity_pack.text(),
            'measure': self.measure.text()
        }

        if war_message('Редактировать материал?'):
            if self.db.edit_material(self.original_name, material_data):
                info_message('Материал отредактирован')
                self.controller.refresh_main_frame()
                self.controller.frames_container.setCurrentWidget(self.controller.frame_start)
            else: crit_message('Ошибка редактирования материала')
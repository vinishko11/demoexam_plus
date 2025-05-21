from PySide6.QtWidgets import *

from messages import war_message, info_message, crit_message
from validate import validate_material_data


class AddMaterial(QFrame):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.db = controller.db

        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        title = QLabel('Добавление нового материала')
        title.setObjectName('title')
        self.layout.addWidget(title)

        self.label_pattern('Наименование материала')
        self.material_name = self.edit_pattern('Введите наименование материала')
        self.layout.addWidget(self.material_name)

        self.label_pattern('Выберите тип материала')
        self.material_type = QComboBox()
        self.material_type.addItems(self.db.take_all_material_type())
        self.layout.addWidget(self.material_type)

        self.label_pattern('Цена единицы материала')
        self.unit_price = self.edit_pattern('Введите цену единицы материала')
        self.layout.addWidget(self.unit_price)

        self.label_pattern('Количество на складе')
        self.quantity = self.edit_pattern('Введите количество на складе')
        self.layout.addWidget(self.quantity)

        self.label_pattern('Минимальное количество')
        self.min_quantity = self.edit_pattern('Введите минимальное количество')
        self.layout.addWidget(self.min_quantity)

        self.label_pattern('Количество в упаковке')
        self.quantity_pack = self.edit_pattern('Введите количество в упаковке')
        self.layout.addWidget(self.quantity_pack)

        self.label_pattern('Единица измерения')
        self.measure = self.edit_pattern('Введите единицу измерения')
        self.layout.addWidget(self.measure)

        btn_back = QPushButton('Назад')
        btn_back.setObjectName('btn')
        btn_back.clicked.connect(lambda: self.controller.frames_container.setCurrentWidget(self.controller.frame_start))
        self.layout.addWidget(btn_back)

        btn_add = QPushButton('Добавить материал')
        btn_add.setObjectName('btn')
        btn_add.clicked.connect(self.add_material)
        self.layout.addWidget(btn_add)

    def label_pattern(self, text):
        label = QLabel(text)
        label.setObjectName('label_hint')
        self.layout.addWidget(label)

        return label

    def edit_pattern(self, text):
        edit = QLineEdit()
        edit.setPlaceholderText(text)
        edit.setObjectName('edit_hint')
        self.layout.addWidget(edit)

        return edit

    def add_material(self):
        material_data = {
            'name': self.material_name.text(),
            'type': self.material_type.currentText(),
            'price': round(float(self.unit_price.text()), 2),
            'quantity': int(self.quantity.text()),
            'min_quantity': int(self.min_quantity.text()),
            'quantity_pack': int(self.quantity_pack.text()),
            'measure': self.measure.text()
        }

        errors = validate_material_data(material_data)
        if errors:
            crit_message("\n".join(errors))
            return

        if war_message('Добавить материал?'):
            if self.db.add_material(material_data):
                info_message('Материал добавлен')
                self.controller.refresh_main_frame()
                self.controller.frames_container.setCurrentWidget(self.controller.frame_start)
            else: crit_message('Ошибка добавления материала')

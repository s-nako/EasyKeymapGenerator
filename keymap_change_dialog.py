# -*- coding: utf-8 -*
from PySide2.QtWidgets import *
from . import config


class MapTypeWidget(QWidget):
    """
    Widget to display KeyMapItem information that change dynamically along with map type combo box
    """

    def __init__(self, map_type="Keyboard", km_item=None, parent=None):
        """
        Create main layout, add items and resize window
        Args:
            map_type (str): map type to display
            km_item (bpy.types.KeyMapItem): initial KeyMapItem to display
            parent (QWidget): parent widget
        """
        super(MapTypeWidget, self).__init__(parent)
        self.main_layout = QGridLayout()
        self.main_layout.setRowMinimumHeight(0, 20)
        self.main_layout.setRowMinimumHeight(1, 20)
        self.main_layout.setRowMinimumHeight(2, 20)
        self.map_type_combobox = None
        self.setLayout(self.main_layout)
        # define ui items
        self.type_button = None
        self.type = None
        self.value_combobox = None
        self.key_buttons = None
        self.map_type_combobox = None
        self.repeat_checkbox = None
        self.reset_button = None

        self.redraw(map_type)
        if km_item:
            self._init_items(map_type, km_item)
        self.setMinimumWidth(300)

    def _init_items(self, map_type, km_item):
        """
        initialize values of ui according to km_item
        Args:
            map_type (str): map type to display
            km_item (bpy.types.KeyMapItem): KeyMapItem
        Returns:
        """

        # type_button
        if map_type in ["Keyboard", "Mouse", "NDOF"]:
            self.type_button.setText(km_item.to_string())

        # type
        if map_type == "Keyboard":
            self.type.setText(config.KEY_TYPES.inverse[km_item.type])
        elif map_type == "Tweak":
            self.value_combobox.setCurrentText(config.TWEAK_VALUES.inverse[km_item.value])
        elif map_type == "Mouse":
            self.type.setCurrentText(config.MOUSE_TYPES.inverse[km_item.type])
        elif map_type == "NDOF":
            self.type.setCurrentText(config.NDOF_TYPES.inverse[km_item.type])
        elif map_type == "Timer":
            self.type.setCurrentText(config.TIMER_TYPES.inverse[km_item.type])

        # value
        if map_type in ["Keyboard", "Mouse", "NDOF"]:
            self.value_combobox.setCurrentText(config.CLICK_VALUES.inverse[km_item.value])
        elif map_type == "Tweak":
            self.value_combobox.setCurrentText(config.TWEAK_VALUES.inverse[km_item.value])

        # key_buttons
        if map_type in ["Keyboard", "Tweak", "Mouse", "NDOF"]:
            for key in self.key_buttons.keys():
                if key == "key_modifier":
                    key_modifier = km_item.key_modifier
                    if key_modifier:
                        self.key_buttons["key_modifier"].setChecked(False)
                        self.key_buttons["key_modifier"].setText("  ")
                    else:
                        self.key_buttons["key_modifier"].setChecked(True)
                    self.key_buttons["key_modifier"].setText(key_modifier)
                else:
                    self.key_buttons[key].setChecked(getattr(km_item, key))

        # repeat button
        if map_type == "Keyboard":
            self.repeat_checkbox.setChecked(km_item.repeat)


    def redraw(self, map_type):
        """
        update and redraw ui
        Args:
            map_type: map type to display
        Returns:
        """
        if map_type == "Keyboard":
            self.draw_keyboard_ui()
        elif map_type == "Tweak":
            self.draw_tweak_ui()
        elif map_type == "Mouse":
            self.draw_mouse_ui()
        elif map_type == "NDOF":
            self.draw_ndof_ui()
        elif map_type == "Text Input":
            self.draw_textinput_ui()
        elif map_type == "Timer":
            self.draw_timer_ui()
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)

    def generate_key_buttons(self):
        """
        return key buttons
        Returns (doct): dictionary of key name and QPushButton object
        """
        return {"any": QPushButton("Any"), "shift": QPushButton("Shift"),
                "ctrl": QPushButton("Ctrl"), "alt": QPushButton("Alt"),
                "oskey": QPushButton("Cmd"), "key_modifier": QPushButton("  ")}

    def draw_keyboard_ui(self):
        self.clear()
        self.map_type_combobox = QComboBox()
        self.map_type_combobox.addItems(config.MAP_TYPES)
        self.main_layout.addWidget(self.map_type_combobox, 0, 1, 1, 2)
        self.type_button = QPushButton("A")
        self.main_layout.addWidget(self.type_button, 0, 3, 1, 2)
        self.reset_button = QPushButton("reset")
        self.reset_button.setFixedWidth(40)
        self.main_layout.addWidget(self.reset_button, 0, 5, 1, 1)
        self.type = QPushButton("A")
        self.main_layout.addWidget(self.type, 1, 0, 1, 2)
        self.value_combobox = QComboBox()
        self.value_combobox.addItems(config.CLICK_VALUES)
        self.main_layout.addWidget(self.value_combobox, 1, 2, 1, 2)
        self.repeat_checkbox = QCheckBox("repeat")
        self.main_layout.addWidget(self.repeat_checkbox, 1, 4, 1, 2)
        self.key_buttons = self.generate_key_buttons()
        for index, button in enumerate(self.key_buttons.values()):
            button.setFixedWidth(50)
            button.setCheckable(True)
            self.main_layout.addWidget(button, 2, index, 1, 1)

    def draw_tweak_ui(self):
        self.clear()
        sub_widget = QWidget()
        sub_layout = QGridLayout()
        sub_widget.setLayout(sub_layout)
        sub_layout.setMargin(0)
        self.main_layout.addWidget(sub_widget, 0, 0, 1, 5)
        self.map_type_combobox = QComboBox()
        self.map_type_combobox.addItems(config.MAP_TYPES)
        self.map_type_combobox.setCurrentIndex(1)
        self.type = QComboBox()
        self.type.addItems(config.TWEAK_TYPES)
        self.value_combobox = QComboBox()
        self.value_combobox.addItems(config.TWEAK_VALUES)
        sub_layout.addWidget(self.map_type_combobox, 0, 1, 1, 1)
        sub_layout.addWidget(self.type, 0, 2, 1, 1)
        sub_layout.addWidget(self.value_combobox, 0, 3, 1, 1)
        self.reset_button = QPushButton("reset")
        self.reset_button.setFixedWidth(40)
        self.main_layout.addWidget(self.reset_button, 0, 5, 1, 1)
        self.key_buttons = self.generate_key_buttons()
        for index, button in enumerate(self.key_buttons.values()):
            button.setFixedWidth(50)
            button.setCheckable(True)
            self.main_layout.addWidget(button, 1, index, 1, 1)

    def draw_mouse_ui(self):
        self.clear()
        self.map_type_combobox = QComboBox()
        self.map_type_combobox.addItems(config.MAP_TYPES)
        self.map_type_combobox.setCurrentIndex(2)
        self.main_layout.addWidget(self.map_type_combobox, 0, 1, 1, 2)
        self.type_button = QPushButton("Left Mouse")
        self.main_layout.addWidget(self.type_button, 0, 3, 1, 2)
        self.reset_button = QPushButton("reset")
        self.reset_button.setFixedWidth(40)
        self.main_layout.addWidget(self.reset_button, 0, 5, 1, 1)
        self.type = QComboBox()
        self.type.addItems(config.MOUSE_TYPES)
        self.main_layout.addWidget(self.type, 1, 0, 1, 3)
        self.value_combobox = QComboBox()
        self.value_combobox.addItems(config.CLICK_VALUES)
        self.main_layout.addWidget(self.value_combobox, 1, 3, 1, 3)
        self.key_buttons = self.generate_key_buttons()
        for index, button in enumerate(self.key_buttons.values()):
            button.setFixedWidth(50)
            button.setCheckable(True)
            self.main_layout.addWidget(button, 2, index, 1, 1)

    def draw_ndof_ui(self):
        self.clear()
        self.map_type_combobox = QComboBox()
        self.map_type_combobox.addItems(config.MAP_TYPES)
        self.map_type_combobox.setCurrentIndex(3)
        self.main_layout.addWidget(self.map_type_combobox, 0, 1, 1, 2)
        self.type_button = QPushButton("NDOF Motion")
        self.main_layout.addWidget(self.type_button, 0, 3, 1, 2)
        self.reset_button = QPushButton("reset")
        self.reset_button.setFixedWidth(40)
        self.main_layout.addWidget(self.reset_button, 0, 5, 1, 1)
        self.type = QComboBox()
        self.type.addItems(config.NDOF_TYPES)
        self.main_layout.addWidget(self.type, 1, 0, 1, 3)
        self.value_combobox = QComboBox()
        self.value_combobox.addItems(config.CLICK_VALUES)
        self.value_combobox.setCurrentText("Nothing")
        self.main_layout.addWidget(self.value_combobox, 1, 3, 1, 3)
        self.key_buttons = self.generate_key_buttons()
        for index, button in enumerate(self.key_buttons.values()):
            button.setFixedWidth(50)
            button.setCheckable(True)
            self.main_layout.addWidget(button, 2, index, 1, 1)

    def draw_textinput_ui(self):
        self.clear()
        self.map_type_combobox = QComboBox()
        self.map_type_combobox.addItems(config.MAP_TYPES)
        self.map_type_combobox.setCurrentIndex(4)
        self.main_layout.addWidget(self.map_type_combobox, 0, 1, 1, 2)
        null_widget = QWidget()
        self.main_layout.addWidget(null_widget, 0, 3, 1, 2)
        self.reset_button = QPushButton("reset")
        self.reset_button.setFixedWidth(40)
        self.main_layout.addWidget(self.reset_button, 0, 5, 1, 1)

    def draw_timer_ui(self):
        self.clear()
        self.map_type_combobox = QComboBox()
        self.map_type_combobox.addItems(config.MAP_TYPES)
        self.map_type_combobox.setCurrentIndex(5)
        self.main_layout.addWidget(self.map_type_combobox, 0, 1, 1, 2)
        self.type = QComboBox()
        self.type.addItems(config.TIMER_TYPES)
        self.main_layout.addWidget(self.type, 0, 3, 1, 2)
        self.reset_button = QPushButton("reset")
        self.reset_button = QPushButton("reset")
        self.reset_button.setFixedWidth(40)
        self.main_layout.addWidget(self.reset_button, 0, 5, 1, 1)

    def clear(self):
        for i in range(self.main_layout.count()):
            child = self.main_layout.itemAt(i)
            child.widget().deleteLater()


class KeymapChangeDialog(QDialog):
    """
    Popup dialog to set keymap, which is displayed When keymap item double clicked
    """
    def __init__(self, km_item, parent=None):
        """
        Create main layout, add items and resize window
        Args:
            km_item (bpy.types.KeyMapItem): initial KeyMapItem to display
            parent (QWidget): parent widget
        """
        super(KeymapChangeDialog, self).__init__(parent)
        self.main_layout = QGridLayout()
        self.main_layout.setRowMinimumHeight(0, 20)
        self.main_layout.setRowMinimumHeight(1, 20)
        self.setLayout(self.main_layout)
        keymap_name = QLabel(km_item.name)
        keymap_name.setFixedHeight(20)
        self.main_layout.addWidget(keymap_name, 0, 0, 1, 3)
        self.map_types_widget = MapTypeWidget(map_type=config.MAP_TYPES.inverse[km_item.map_type], km_item=km_item)
        self.map_types_widget.map_type_combobox.currentTextChanged.connect(self._redraw)
        self.main_layout.addWidget(self.map_types_widget, 0, 4, 3, 6)
        identifier = QLineEdit(km_item.idname)
        self.main_layout.addWidget(identifier, 1, 0, 1, 4)
        self.main_layout.setMargin(5)

    def _redraw(self):
        """
        redraw MapTypeWidget when its map_type_combobox is changed
        Returns:
        """
        map_type = self.map_types_widget.map_type_combobox.currentText()
        self.map_types_widget.deleteLater()
        self.map_types_widget = MapTypeWidget(map_type=map_type)
        self.main_layout.addWidget(self.map_types_widget, 0, 4, 3, 6)
        self.map_types_widget.map_type_combobox.currentTextChanged.connect(self._redraw)

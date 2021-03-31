# -*- coding: utf-8 -*

import sys
from PySide2.QtCore import Qt, QEventLoop
from PySide2.QtWidgets import *
from . import functions
from . import keymap_change_dialog

import bpy

class KeymapLabel(QLabel):
    """ label to display """
    def __init__(self, label, keymap_item, parent=None):
        super(KeymapLabel, self).__init__(label, parent)
        self.keymap_item = keymap_item


class KeymapTree(QWidget):
    """ main keymap_tree widget """
    def __init__(self, parent=None, additional=False):
        super(KeymapTree, self).__init__(parent)
        self.kc_text = ""
        self.additional = additional
        self._generate_ui()
        self._init()

    def _generate_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        header = QWidget()
        header.setFixedHeight(40)
        header_layout = QHBoxLayout()
        header.setLayout(header_layout)
        self.keyconfig_combobox = QComboBox()
        header_layout.addWidget(self.keyconfig_combobox)
        if self.additional:
            close_button = QPushButton("×")
            close_button.setFixedWidth(20)
            close_button.clicked.connect(self._close_tree)
            header_layout.addWidget(close_button)
        main_layout.addWidget(header)
        self.keymap_tree = QTreeWidget()
        self.keymap_tree.setColumnWidth(0, 190)
        self.keymap_tree.itemDoubleClicked.connect(self._double_clicked)
        self.keymap_tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.keymap_tree.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.keymap_tree.setStyleSheet('QTreeView { show-decoration-selected: 1;}')

        self.keymap_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.keymap_tree.customContextMenuRequested.connect(self._show_context_menu)

        main_layout.addWidget(self.keymap_tree)
        main_layout.setMargin(0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def _init(self):
        self._init_keyconfig()

    def _init_keyconfig(self):
        """
        get key config and call addItems()
        Returns:
        """
        self.keyconfig_dict = functions.get_keyconfig_dict()
        self.keyconfig_combobox.currentIndexChanged.connect(self._reset_keymap_tree)
        self.keyconfig_combobox.addItems(self.keyconfig_dict.keys())

    def _add_keymap_tree_item(self, item, parent):
        """
        Add KeyMapItem to keymap_tree
        Args:
            item (bpy.types.KeyMapItems): collection of keymap item
            parent (QTreeWidgetItem): parent widget to add keymap item
        Returns:
        """
        if isinstance(item, list):
            for km_item in item:
                km_item_tree_item = QTreeWidgetItem(["", km_item.to_string()])
                parent.addChild(km_item_tree_item)
                label = KeymapLabel(str(km_item.name), km_item)
                label.setAutoFillBackground(True)
                self.keymap_tree.setItemWidget(km_item_tree_item, 0, label)
        elif isinstance(item, dict):
            for km in item.keys():
                sub_keymap = QTreeWidgetItem([km])
                parent.addChild(sub_keymap)
                self._add_keymap_tree_item(item[km], sub_keymap)

    def _reset_keymap_tree(self):
        """
        reset keymap_tree
        Returns:
        """
        self.keymap_tree.setHeaderLabels(["action", "keymap"])
        self.keymap_tree.clear()
        self.kc_text = self.keyconfig_combobox.currentText()
        kc = functions.get_keyconfig(self.kc_text, self.keyconfig_dict)
        keymap_dict = functions.get_keymap_dict(kc)
        for km in keymap_dict.keys():
            parent_km = QTreeWidgetItem([km])
            self.keymap_tree.addTopLevelItem(parent_km)
            self._add_keymap_tree_item(keymap_dict[km], parent_km)

    def _close_tree(self):
        self.hide()
        self.deleteLater()

    def _double_clicked(self):
        """
        display popup dialog when keymap string is double-clicked
        Returns:
        """
        column = self.keymap_tree.currentColumn()
        if column == 1 and self.keymap_tree.itemWidget(self.keymap_tree.currentItem(), 0):
            item_widget = self.keymap_tree.itemWidget(self.keymap_tree.currentItem(), 0)
            if column == 1 and item_widget:
                dialog = keymap_change_dialog.KeymapChangeDialog(item_widget.keymap_item, parent=self)
                dialog.show()

    def _get_kmi_from_tree_item(self, item_list):
        keymap_item_list = []
        for item in item_list:
            print("key config text", self.kc_text)
            km_text = item.parent().text(0)
            print("key map text", km_text)
            item_widget = self.keymap_tree.itemWidget(item, 0)
            if item_widget:
                kmi = item_widget.keymap_item
                keymap_item_list.append(kmi)
                print("key map item idname", kmi.idname)
            else:
                print("no tree item widget")
        return keymap_item_list

    def _show_context_menu(self, pos):
        """
        display context menu to copy of paste keymap items
        """
        column = self.keymap_tree.currentColumn()
        text = self.keymap_tree.currentItem().text(column)
        if column != 1:
            return

        copy_keymap_action = QAction("Copy Keymap")
        copy_keymap_action.triggered.connect(self._copy_keymap)

        paste_keymap_action = QAction("Paste Keymap")
        paste_keymap_action.triggered.connect(self._paste_keymap)

        menu = QMenu(self.keymap_tree)
        menu.addAction(copy_keymap_action)
        menu.addAction(paste_keymap_action)
        menu.exec_(self.keymap_tree.mapToGlobal(pos))

    def _copy_keymap(self):
        """
        save the selected items as a list of [key str, keymap]
        """
        current_selection = self.keymap_tree.selectedItems()
        print("current_selection", current_selection)
        keymap_item_list = self._get_kmi_from_tree_item(current_selection)
        print("keymap_item_list", keymap_item_list)
        functions.save_keymaps(keymap_item_list)

    def _paste_keymap(self):
        current_selection = self.keymap_tree.selectedItems()
        copied_keymap_items = functions.get_temp()
        copied_length = len(copied_keymap_items)
        for idx, item in enumerate(current_selection):
            item_widget = self.keymap_tree.itemWidget(item, 0)
            if item_widget and idx<copied_length:
                copied_kmi = copied_keymap_items[idx]
                current_kmi = item_widget.keymap_item
                functions.copy_keymap_item(copied_kmi, current_kmi)
                item.setText(1, copied_kmi.to_string())


class EasyKeymapMainWindow(QMainWindow):
    """
    Main window of easy keymap generator
    """
    def __init__(self, parent=None):
        super(EasyKeymapMainWindow, self).__init__(parent)
        self._generate_ui()
        self.setWindowTitle("Easy Keymap Generator")
        self.resize(350, 600)
        self.resize(350, 600)

    def _generate_ui(self):
        self.main_widget = QSplitter()
        self.main_widget.setHandleWidth(5)
        self.setCentralWidget(self.main_widget)
        keymap_tree1 = KeymapTree()
        self.main_widget.addWidget(keymap_tree1)
        add_button = QPushButton("+")
        add_button.setFixedWidth(30)
        add_button.clicked.connect(self._insert_tree)
        self.main_widget.addWidget(add_button)

    def _insert_tree(self):
        """
        Add new keymap_tree when + button is clicked
        Returns:
        """
        keymap_tree2 = KeymapTree(additional=True)
        keymap_tree2.destroyed.connect(self._deleted_tree)
        self.main_widget.insertWidget(self.main_widget.count() - 1, keymap_tree2)
        self.resize(self.width() + 300, self.height())

    def _deleted_tree(self):
        """
        Delete keymap_tree when close button is clicked
        Returns:
        """
        for i in range(5):
            QApplication.processEvents()
        self.resize(self.width() - 300, self.height())

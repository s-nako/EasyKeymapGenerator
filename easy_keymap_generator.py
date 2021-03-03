import bpy
import csv
import sys

from PySide2.QtCore import QEventLoop
from PySide2.QtWidgets import *

from . import ui


class PYSIDE_OT_display_window(bpy.types.Operator):
    bl_idname = 'pyside.display_window'
    bl_label = "Display Window"
    bl_options = {'REGISTER'}

    def execute(self, context):  # eventloop should be here
        self.app = QApplication.instance()
        if not self.app:
            self.app = QApplication(sys.argv)
        self.event_loop = QEventLoop()
        self.widget = ui.EasyKeymapMainWindow()
        self.widget.show()
        # self.app.exec_()  DON'T exec app
        return {'FINISHED'}


class PYSIDE_PT_tools_my_panel(bpy.types.Panel):
    bl_label = "Test Pyside"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.operator('pyside.display_window')


classs = [
    PYSIDE_OT_display_window, PYSIDE_PT_tools_my_panel
]


def register():
    for c in classs:
        bpy.utils.register_class(c)


def unregister():
    for c in classs:
        bpy.utils.unregister_class(c)

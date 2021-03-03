# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Easy Keymap Generator",
    "author": "Nako",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "description": "Compare, Copy and Paste keymaps",
    "doc_url": "",
    "tracker_url": "https://github.com/s-nako/easy_keymap_generator/issues",
    "category": "System",
}

import bpy
from . import easy_keymap_generator

# =========================================================================
# Registration:
# =========================================================================

def register():
    easy_keymap_generator.register()

def unregister():
    easy_keymap_generator.unregister()

if __name__ == "__main__":
    register()

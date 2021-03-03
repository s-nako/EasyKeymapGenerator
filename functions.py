import bpy
import os
from bl_keymap_utils import keymap_hierarchy


def get_keyconfig_dict():
    """
    get dictionary of kerconfig_name(str) and path_to_config_file(str)
    Returns:
        dict: dictionary of kerconfig_name(str) and path_to_config_file(str)
    """

    config_pathes = bpy.utils.preset_paths("keyconfig")
    config_dict = {}
    for config_path in config_pathes:
        for file in os.listdir(config_path):
            name, ext = os.path.splitext(file)
            if ext.lower() in [".py", ".xml"] and not name[0] == ".":
                config_dict[name] = os.path.join(config_path, file)
    return config_dict


def get_keyconfig(keyconfig_name, keyconfig_dict):
    """
    get keyconfig from the dictionary of kerconfig_name and path_to_config_file
    Args:
        keyconfig_name (str): keyconfig name such as "Blender"
        keyconfig_dict (str): keyconfig path such as "blender.py"
    Returns:
        bpy.types.KeyConfig: keyconfig with keyconfig_name
    """
    wm = bpy.context.window_manager
    if keyconfig_name in wm.keyconfigs.keys():
        return wm.keyconfigs[keyconfig_name]
    else:
        keyconfig_path = keyconfig_dict[keyconfig_name]
        current_path = keyconfig_dict[wm.keyconfigs.active.name]
        bpy.ops.preferences.keyconfig_activate(filepath=keyconfig_path)
        kc = wm.keyconfigs.active
        bpy.ops.preferences.keyconfig_activate(filepath=current_path)
        return kc


def get_keymap_dict(keyconfig):
    """
    get dictionary of key_name(str) and path_to_config_file(str)
    Args:
        keyconfig (bpy.types.KeyConfig):
    Returns:
        dict: keymap dict to display
    """
    keymaps = [(km, keyconfig) for km in keyconfig.keymaps]
    keymap_dict = {}
    level = 0
    for entry in keymap_hierarchy.generate():
        add_entry_to_dict(keymaps, entry, keymap_dict, level)
    return keymap_dict


def add_entry_to_dict(keymaps, entry, parent_dict, level):
    idname, spaceid, regionid, children = entry
    for km, kc in keymaps:
        if km.name == idname and km.space_type == spaceid and km.region_type == regionid:
            parent_dict[idname] = add_keymaps_to_dict(keymaps, km, children, level)
        else:
            if idname not in parent_dict:
                parent_dict[idname] = []


def add_keymaps_to_dict(keymaps, km, children, level):
    if children:  # add dict
        parent_dict = {km.name + " (Global)": list(km.keymap_items)}
        for entry in children:
            add_entry_to_dict(keymaps, entry, parent_dict, level + 1)
        return parent_dict
    else:  # add list
        return list(km.keymap_items)

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

# Script copyright (C) Wilhelm Kovatch

bl_info = {
    "name": "km2 City Builder (Midtown Madness 2 core)",
    "author": "SuperSecret",
    "version": (0, 3, 0),
    "blender": (2, 91, 2),
    "location": "File > Export > km2 City Builder (Midtown Madness 2 core)",
    "description": "Import files exported with km2 City Builder using the Midtown Madness 2 core",
    "support": 'COMMUNITY',
    "category": "Import"}

if "bpy" in locals():
    import importlib
    importlib.reload(bin_reader)
    
import bpy, sys
from .bin_reader import BINReader

from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        StringProperty,
        CollectionProperty,
        IntProperty,
        PointerProperty
        )

from bpy_extras.io_utils import (
        ExportHelper, ImportHelper
        )

class ImportBIN(bpy.types.Operator, ImportHelper):
    bl_idname = "import_scene.km2cb_bin_midtownmadness2"
    bl_label = 'Import km2CB BIN'

    filename_ext = ".bin"
    filter_glob: StringProperty(default="*.bin", options={'HIDDEN'})
        
    def execute(self, context):
        reader = BINReader(self.properties.filepath)
        reader.read()
        return {'FINISHED'}

def menu_func_import(self, context):
    self.layout.operator(ImportBIN.bl_idname, text="km2 City Builder BIN - Midtown Madness 2 core (.bin)")

def register():
    bpy.utils.register_class(ImportBIN)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.utils.unregister_class(ImportBIN)

if __name__ == "__main__":
    register()

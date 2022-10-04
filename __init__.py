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
    "name": "Render Image",
    "author": "tintwotin",
    "version": (1, 0),
    "blender": (3, 00, 0),
    "location": "View > Render Current Frame",
    "description": "",
    "warning": "",
    "doc_url": "",
    "category": "Sequencer",
}

import bpy, os
from bpy.types import Operator


class OPERATOR_OT_render_to_file(Operator):
    """Render Current Frame"""

    bl_idname = "sequencer.render_to_file"
    bl_label = "Render Current Frame"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        scene = bpy.context.scene
        fp = scene.render.filepath

        scene.render.image_settings.file_format = "PNG"

        frame_nr = bpy.context.scene.frame_current

        scene.frame_set(frame_nr)

        scene.render.filepath = fp + "Screenshot_" + str(frame_nr)
        bpy.ops.render.opengl(sequencer=True, write_still=True)

        scene.render.filepath = fp

        msg = "Saved: Screenshot_" + str(frame_nr) + ".png"
        self.report({"INFO"}, msg)

        return {"FINISHED"}


def menu_append(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(OPERATOR_OT_render_to_file.bl_idname, icon="FILE_IMAGE")


def register():
    bpy.types.SEQUENCER_MT_view.append(menu_append)


def unregister():
    bpy.types.SEQUENCER_MT_view.remove(menu_append)


if __name__ == "__main__":
    register()

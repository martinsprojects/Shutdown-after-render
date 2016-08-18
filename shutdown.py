# Blender version 2.77

import bpy
import os
import subprocess

def handler(scene):
	try:
		subprocess.call(["shutdown", "/s", "/f"]) # shutdown under windows
	except:
		print("Error can't shutdown")

class shutdown(bpy.types.Operator):
	bl_label = "Shutdown after render"
	bl_idname = "scene.shtdwn"

	def execute(self, context):

		bpy.app.handlers.render_post.append(handler)

		return {'FINISHED'}


class shutdownpanel(bpy.types.Panel):
	bl_label = "Shutdown After Rendering"
	bl_idname = "panel.shttdn"
	bl_space_type = 'VIEW_3D' # change to render panel
	bl_region_type = 'TOOLS' # change
	bl_Category = "vectest" # change

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		col = layout.column()
		layout.operator(shutdown.bl_idname, "Shutdown")

def register():
	bpy.utils.register_class(shutdownpanel)
	bpy.utils.register_class(shutdown)

def unregister():
	bpy.utils.unregister_class(shutdownpanel)
	bpy.utils.unregister_class(shutdown)

if __name__ == "__main__":
	register()

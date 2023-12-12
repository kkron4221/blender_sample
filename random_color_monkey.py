import bpy

import random

def delete_all():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(True)

delete_all()

bpy.ops.mesh.primitive_monkey_add()

monkey = bpy.context.active_object

# generate a random color
red = random.random()
green = random.random()
blue = random.random()
alpha = 1.0
color = (red, green, blue, alpha)

# create a new material
material = bpy.data.materials.new("random_material")
material.diffuse_color = color

# add the material to the object
monkey.data.materials.append(material)

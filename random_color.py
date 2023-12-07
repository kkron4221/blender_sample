# give Python access to Blender's functionality
import bpy

# extend Python's functionality to generate random numbers
import random

# add a plene
bpy.ops.mesh.primitive_plane_add()
plane = bpy.context.active_object

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
plane.data.materials.append(material)

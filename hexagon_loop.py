# give Python access to Blender's functionality
import bpy
# extend Python's math functionality
import math

# create variables used in the loop
radians_step = 0.1
current_radius = 0.1
number_hexagons = 50

z_step = 10

# repeat 50 times
for i in range(number_hexagons):
    # add a triangle mesh into the scene
    current_radius = current_radius +  radians_step
    bpy.ops.mesh.primitive_circle_add(vertices=6, radius=current_radius)

    # get a reference to the currently active object
    hexagon_mesh = bpy.context.active_object 

    # rotate mesh about the x-axis
    degrees = -90
    radians = math.radians(degrees)
    hexagon_mesh.rotation_euler.x = radians
    
    # rotate mesh about the x-axis
    degrees = z_step * i
    radians = math.radians(degrees)
    hexagon_mesh.rotation_euler.z = radians

    # convert mesh into a curve
    bpy.ops.object.convert(target='CURVE')

    # add bevel to curve
    hexagon_mesh.data.bevel_depth = 0.05
    hexagon_mesh.data.bevel_resolution = 16

    # shade smooth
    bpy.ops.object.shade_smooth()
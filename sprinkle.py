# give Python access to Blender's functionality
import bpy

# extend Python's math functionality
import math

import pprint

# initialize paramaters
vert_count = 32
angle_step = 2 * math.tau / vert_count
z_step = 0.1

# create a list of verts
vert_coordinates = list()

# repeat code in a loop
for i in range(vert_count):
    
    # calculate the current angle
    current_angle = i * angle_step

    # calculate coordinate
    x = math.cos(current_angle)
    y = math.sin(current_angle)
    z = z_step * i

    # visualize what we are doing
    bpy.ops.mesh.primitive_ico_sphere_add(radius=0.1, location=(x, y, z))

    vert_coordinates.append((x, y, 0))
    
pprint.pprint(vert_coordinates)
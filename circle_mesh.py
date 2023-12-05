# give Python access to Blender's functionality
import bpy

# extend Python's math functionality
import math

import pprint



def get_circle_vert_coordinates(vert_count, radius):
    angle_step = math.tau / vert_count

    # create a list of verts
    vert_coordinates = list()

    # repeat code in a loop
    for i in range(vert_count):
        
        # calculate the current angle
        current_angle = i * angle_step

        # calculate coordinate
        x = radius * math.cos(current_angle)
        y = radius * math.sin(current_angle)

        # visualize what we are doing
        bpy.ops.mesh.primitive_ico_sphere_add(radius=0.1, location=(x, y, 0))

        vert_coordinates.append((x, y, 0))
        
    pprint.pprint(vert_coordinates)
    
# initialize paramaters
vert_count = 32
radius = 2

vert_coordinates = get_circle_vert_coordinates(vert_count, radius)

# define lists for the verts, edges, adn faces

verts = vert_coordinates

edges = []

faces = []

# create mesh data from the vert, edge, and face data
mesh_data = bpy.data.meshes.new("circle_data")
mesh_data.from_pydata(verts, edges, faces)

# create an object using the mesh data
mesh_obj = bpy.data.objects.new("circle_obj", mesh_data)

# add the object to the scene collection
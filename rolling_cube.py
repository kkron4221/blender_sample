# 
import math

# give Python access to Blender's functionality
import bpy

# create cube
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object
cube.location.x = 1
cube.location.y = -1
cube.location.z = 1

# create a list of locations for the empties
empty_locations = [
    (0, 0, 0),
    (0, 0, cube.dimensions.z),
    (0, -cube.dimensions.y, cube.dimensions.z),
    (0, -cube.dimensions.y, 0)]
    
# create variables for the rotation animation in frames
rotation_animation_length = 15
current_frame = 1
rotation_angle = -90
    
# create a variable to track the previous empty (userd for parenting)
previous_empty = None

# loop over all the empty locations
for loc in empty_locations:
    # creta tan empty and update the location
    bpy.ops.object.empty_add()
    empty = bpy.context.active_object
    empty.location = loc
    
    if previous_empty:
        empty.parent = previous_empty
        # keep the transform when parenting
        empty.matrix_parent_inverse = previous_empty.matrix_world.inverted()
    
    previous_empty = empty
    
    # animate the rotation
    # insert first keyframe
    empty.keyframe_insert("rotation_euler", frame=current_frame)
    
    # rotate cube
    empty.rotation_euler.x = math.radians(rotation_angle)
    
    current_frame += rotation_animation_length
    # insert last keyframe
    empty.keyframe_insert("rotation_euler", frame=current_frame)
    
# parent the cube to the last empty
cube.parent = previous_empty

# move cube into position
cube.location.x = cube.dimensions.x / 2
cube.location.y = cube.dimensions.y / 2
cube.location.z = cube.dimensions.z / 2
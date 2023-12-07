import bpy

count = 10

for i in range(count):
    for j in range(count):
        for k in range(count):
            x = i * 3
            y = j * 3
            z = k * 3
            if k >= 5:
                bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
                
                
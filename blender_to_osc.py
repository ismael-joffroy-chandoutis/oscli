#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
blender_to_osc : chaine Blender -> vecteur -> oscilloscope, en headless.
A lancer avec : blender -b -P blender_to_osc.py -- <sortie.obj>
Cree un objet 3D (Suzanne), le tourne, projette ses aretes en 2D, et ecrit
un OBJ (v + l) que oscli convertit ensuite en WAV XY + image.
"""
import bpy, sys, math

argv = sys.argv
out = argv[argv.index("--") + 1] if "--" in argv else "/tmp/blender_shape.obj"

# scene propre
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

# objet 3D iconique de Blender : Suzanne
bpy.ops.mesh.primitive_monkey_add()
obj = bpy.context.active_object
obj.rotation_euler = (math.radians(12), math.radians(28), 0)

# mesh evalue + matrice monde
dg = bpy.context.evaluated_depsgraph_get()
me = obj.evaluated_get(dg).to_mesh()
mw = obj.matrix_world
verts = [mw @ v.co for v in me.vertices]

# projection : vue de face (x = horizontal, z = vertical)
xs = [v.x for v in verts]
zs = [v.z for v in verts]
edges = [(e.vertices[0], e.vertices[1]) for e in me.edges]

with open(out, "w") as f:
    f.write("# Suzanne projetee 2D pour oscilloscope\n")
    for v in verts:
        f.write("v %.5f %.5f 0\n" % (v.x, v.z))
    for a, b in edges:
        f.write("l %d %d\n" % (a + 1, b + 1))

print("BLENDER_OBJ_OK verts=%d edges=%d -> %s" % (len(verts), len(edges), out))

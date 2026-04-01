
"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# 
cmds.file(new=True, force=True)
#
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)
ground_shader = cmds.shadingNode("lambert", asShader=True, name="GrassMat")
cmds.setAttr(ground_shader + ".color", 0, .3, 0, type="double3")
cmds.select(ground)
cmds.hyperShade(assign=ground_shader)
#
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)
building_shader = cmds.shadingNode("lambert", asShader=True, name="Red01_BuildingMat")
cmds.setAttr(building_shader + ".color", .2, 0, 0, type="double3")
cmds.select(building)
cmds.hyperShade(assign=building_shader)
#
building_b_height = 9
building_b_radius = 2
building_b_x = -10
building_b_z = -5
#Second Building is a Skyscraper, making shape measurements and placement on the plane
building_b = cmds.polyCylinder(name="Building_02",
height=building_b_height, radius=building_b_radius)[0]
cmds.move(building_b_x, building_height / 2.0, building_b_z, building_b)
building_b_shader = cmds.shadingNode("lambert", asShader=True, name="Blue01_BuildingMat")
cmds.setAttr(building_b_shader + ".color", 0, .5, .8, type="double3")
cmds.select(building_b)
cmds.hyperShade(assign=building_b_shader)
#Assigned a light blue shader to my second building & changing name convention for the different color
#
building_height = 4
building_width = 3
building_depth = 2
building_x = -8
building_z = -9
#Exact same as object 1, except I rotated the building and placed values to make it smaller and beside the skyscraper
building = cmds.polyCube(name="Building_02",
width=building_width, height=building_height, depth=building_depth)[0]
cmds.move(building_x, building_height / 2.0, building_z, building)
cmds.rotate(0, 30, 0)

#
road_height = .25
road_width = 50
road_depth = 2
road_x = 0
road_z = 0
#Kept plane length in mind, made measurements for a slim, symmetrical road (& other roads that don't intersect later)
road = cmds.polyCube(name="Road-01",
width=road_width, height=road_height, depth=road_depth)[0]
cmds.move(road_x, road_height / 2.0, road_z, road)

road_shader = cmds.shadingNode("lambert", asShader=True, name="RoadMat")
cmds.setAttr(road_shader + ".color", 0, 0, 0, type="double3")
cmds.select(road)
cmds.hyperShade(assign=road_shader)
#Added no color value for the negative value (black) to result
#
tree1_x = -4.5
tree1_z = 8
trunk_height = 1.82
trunk_radius = 0.25
canopy_radius = 1.1
#Setting overall shape sizes and eng-goal tree placement, as well as linking the trunk to the tree placement
trunk1 = cmds.polyCylinder(name="Trunk_01", radius=trunk_radius, height=trunk_height)[0]
cmds.move(tree1_x, trunk_height / 2.0, tree1_z, trunk1)

canopy1 = cmds.polySphere(name="Canopy_01", radius=canopy_radius)[0]
#Setting up the leaves: assigning size, linking the placement to the trunk while multiplying it with a value that will make it a little lower
canopy_y = trunk_height + canopy_radius * 0.5
cmds.move(tree1_x, canopy_y, tree1_z, canopy1)
canopy_shader = cmds.shadingNode("lambert", asShader=True, name="CanopyMat")
cmds.setAttr(canopy_shader + ".color", 0, .1, 0, type="double3")
for canopy in [canopy1]:
    cmds.select(canopy)
    cmds.hyperShade(assign=canopy_shader)
trunk_shader = cmds.shadingNode("lambert", asShader=True, name="TrunkMat")
cmds.setAttr(trunk_shader + ".color", 0.3, .20, 0.1, type="double3")
for trunk in [trunk1]:
    cmds.select(trunk)
    cmds.hyperShade(assign=trunk_shader)
#Added a shader and applied it to the trunk in the scene, experimenting with color to get brown
#
road_height = .25
road_width = 24
road_depth = 2
road_x = 0
road_z = 13
#Using the same Road code as before but counting values for precise placement
road = cmds.polyCube(name="Road-02",
width=road_width, height=road_height, depth=road_depth)[0]
cmds.move(road_x, road_height / 2.0, road_z, road)
cmds.rotate(0, 90, 0)

road_shader = cmds.shadingNode("lambert", asShader=True, name="RoadMat")
cmds.setAttr(road_shader + ".color", 0, 0, 0, type="double3")
cmds.select(road)
cmds.hyperShade(assign=road_shader)

road_height = .25
road_width = 24
road_depth = 2
road_x = 13
road_z = -13

road = cmds.polyCube(name="Road-03",
width=road_width, height=road_height, depth=road_depth)[0]
cmds.move(road_x, road_height / 2.0, road_z, road)
cmds.rotate(0, 90, 0)

road_shader = cmds.shadingNode("lambert", asShader=True, name="RoadMat")
cmds.setAttr(road_shader + ".color", 0, 0, 0, type="double3")
cmds.select(road)
cmds.hyperShade(assign=road_shader)

road_height = .25
road_width = 24
road_depth = 2
road_x = -14
road_z = -13

road = cmds.polyCube(name="Road-04",
width=road_width, height=road_height, depth=road_depth)[0]
cmds.move(road_x, road_height / 2.0, road_z, road)
cmds.rotate(0, 90, 0)

road_shader = cmds.shadingNode("lambert", asShader=True, name="RoadMat")
cmds.setAttr(road_shader + ".color", 0, 0, 0, type="double3")
cmds.select(road)
cmds.hyperShade(assign=road_shader)
# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
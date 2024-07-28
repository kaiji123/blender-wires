import bpy

def create_geometry_nodes():
    # Create a new node group
    node_group = bpy.data.node_groups.new(type='GeometryNodeTree', name='GeometryNodes')
    node_group.nodes.clear()
    # Create node: Set Position
    Set_Position = node_group.nodes.new(type='GeometryNodeSetPosition')
    Set_Position.location = (1303.2001953125, 25.646800994873047)
    Set_Position.inputs['Selection'].default_value = True
    Set_Position.inputs['Position'].default_value = <bpy_float[3], NodeSocketVector.default_value>

    # Create node: Realize Instances
    Realize_Instances = node_group.nodes.new(type='GeometryNodeRealizeInstances')
    Realize_Instances.location = (732.0, 22.5707950592041)

    # Create node: Group Output
    Group_Output = node_group.nodes.new(type='NodeGroupOutput')
    Group_Output.location = (1973.81103515625, 55.71074295043945)

    # Create node: Curve to Mesh
    Curve_to_Mesh = node_group.nodes.new(type='GeometryNodeCurveToMesh')
    Curve_to_Mesh.location = (1523.6575927734375, 80.03053283691406)
    Curve_to_Mesh.inputs['Fill Caps'].default_value = False

    # Create node: Curve Circle
    Curve_Circle = node_group.nodes.new(type='GeometryNodeCurvePrimitiveCircle')
    Curve_Circle.location = (1261.126708984375, -136.0497589111328)
    Curve_Circle.inputs['Resolution'].default_value = 3
    Curve_Circle.inputs['Point 1'].default_value = <Vector (-1.0000, 0.0000, 0.0000)>
    Curve_Circle.inputs['Point 2'].default_value = <Vector (0.0000, 1.0000, 0.0000)>
    Curve_Circle.inputs['Point 3'].default_value = <Vector (1.0000, 0.0000, 0.0000)>
    Curve_Circle.inputs['Radius'].default_value = 0.15000000596046448

    # Create node: Combine XYZ
    Combine_XYZ = node_group.nodes.new(type='ShaderNodeCombineXYZ')
    Combine_XYZ.location = (1000.2557373046875, -178.83053588867188)
    Combine_XYZ.inputs['X'].default_value = 0.0
    Combine_XYZ.inputs['Y'].default_value = -2.4000000953674316

    # Create node: Math
    Math = node_group.nodes.new(type='ShaderNodeMath')
    Math.location = (834.7337646484375, -228.39187622070312)
    Math.inputs['Value'].default_value = -4.299999237060547
    Math.inputs['Value'].default_value = 0.5

    # Create node: Instance on Points
    Instance_on_Points = node_group.nodes.new(type='GeometryNodeInstanceOnPoints')
    Instance_on_Points.location = (559.7159423828125, 185.07693481445312)
    Instance_on_Points.inputs['Selection'].default_value = True
    Instance_on_Points.inputs['Pick Instance'].default_value = False
    Instance_on_Points.inputs['Instance Index'].default_value = 0
    Instance_on_Points.inputs['Rotation'].default_value = <Euler (x=0.0000, y=-0.0611, z=0.0000), order='XYZ'>
    Instance_on_Points.inputs['Scale'].default_value = <Vector (1.0000, 7.9000, 1.0000)>

    # Create node: Transform Geometry
    Transform_Geometry = node_group.nodes.new(type='GeometryNodeTransform')
    Transform_Geometry.location = (34.71110916137695, 262.9423828125)
    Transform_Geometry.inputs['Translation'].default_value = <Vector (0.0000, 0.0000, 0.0000)>
    Transform_Geometry.inputs['Rotation'].default_value = <Euler (x=0.0000, y=1.5952, z=0.0000), order='XYZ'>
    Transform_Geometry.inputs['Scale'].default_value = <Vector (14.3000, 4.4000, 4.7000)>

    # Create node: Set Position.001
    Set_Position.001 = node_group.nodes.new(type='GeometryNodeSetPosition')
    Set_Position.001.location = (254.40000915527344, 216.7363739013672)
    Set_Position.001.inputs['Selection'].default_value = True
    Set_Position.001.inputs['Offset'].default_value = <Vector (0.0000, 8.9000, 0.0000)>

    # Create node: Quadratic Bezier
    Quadratic_Bezier = node_group.nodes.new(type='GeometryNodeCurveQuadraticBezier')
    Quadratic_Bezier.location = (120.27568054199219, -777.1648559570312)
    Quadratic_Bezier.inputs['Resolution'].default_value = 16
    Quadratic_Bezier.inputs['Start'].default_value = <Vector (0.0000, -10.8000, 0.0000)>
    Quadratic_Bezier.inputs['Middle'].default_value = <Vector (0.0000, 0.0000, 0.0000)>
    Quadratic_Bezier.inputs['End'].default_value = <Vector (0.0000, 0.0000, 0.0000)>

    # Create node: Combine XYZ.001
    Combine_XYZ.001 = node_group.nodes.new(type='ShaderNodeCombineXYZ')
    Combine_XYZ.001.location = (100.5252685546875, -90.55656433105469)
    Combine_XYZ.001.inputs['X'].default_value = 0.0
    Combine_XYZ.001.inputs['Y'].default_value = 1.6999998092651367

    # Create node: Math.001
    Math.001 = node_group.nodes.new(type='ShaderNodeMath')
    Math.001.location = (31.572681427001953, -378.16107177734375)
    Math.001.inputs['Value'].default_value = 54.19999694824219
    Math.001.inputs['Value'].default_value = 0.5

    # Create node: Map Range.001
    Map_Range.001 = node_group.nodes.new(type='ShaderNodeMapRange')
    Map_Range.001.location = (-191.69168090820312, -376.81402587890625)
    Map_Range.001.inputs['From Min'].default_value = 0.0
    Map_Range.001.inputs['From Max'].default_value = 1.0
    Map_Range.001.inputs['To Min'].default_value = -0.30000007152557373
    Map_Range.001.inputs['To Max'].default_value = 1.0
    Map_Range.001.inputs['Steps'].default_value = 4.0
    Map_Range.001.inputs['Vector'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.001.inputs['From Min'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.001.inputs['From Max'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.001.inputs['To Min'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.001.inputs['To Max'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.001.inputs['Steps'].default_value = <bpy_float[3], NodeSocketVector.default_value>

    # Create node: Noise Texture.001
    Noise_Texture.001 = node_group.nodes.new(type='ShaderNodeTexNoise')
    Noise_Texture.001.location = (-502.5765075683594, -430.77862548828125)
    Noise_Texture.001.inputs['Vector'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Noise_Texture.001.inputs['W'].default_value = 3.499999761581421
    Noise_Texture.001.inputs['Scale'].default_value = 5.600000381469727
    Noise_Texture.001.inputs['Detail'].default_value = 2.0
    Noise_Texture.001.inputs['Roughness'].default_value = 1.0
    Noise_Texture.001.inputs['Lacunarity'].default_value = 2.5
    Noise_Texture.001.inputs['Distortion'].default_value = 1.8999998569488525

    # Create node: Noise Texture
    Noise_Texture = node_group.nodes.new(type='ShaderNodeTexNoise')
    Noise_Texture.location = (394.36029052734375, -275.14825439453125)
    Noise_Texture.inputs['Vector'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Noise_Texture.inputs['W'].default_value = 18.799999237060547
    Noise_Texture.inputs['Scale'].default_value = 804.6000366210938
    Noise_Texture.inputs['Detail'].default_value = 6.799999713897705
    Noise_Texture.inputs['Roughness'].default_value = 0.6599999666213989
    Noise_Texture.inputs['Lacunarity'].default_value = 2.5
    Noise_Texture.inputs['Distortion'].default_value = 1.8999998569488525

    # Create node: Map Range
    Map_Range = node_group.nodes.new(type='ShaderNodeMapRange')
    Map_Range.location = (663.3265380859375, -223.3109588623047)
    Map_Range.inputs['From Min'].default_value = 0.0
    Map_Range.inputs['From Max'].default_value = 1.0
    Map_Range.inputs['To Min'].default_value = -1.0
    Map_Range.inputs['To Max'].default_value = 1.0
    Map_Range.inputs['Steps'].default_value = 4.0
    Map_Range.inputs['Vector'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.inputs['From Min'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.inputs['From Max'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.inputs['To Min'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.inputs['To Max'].default_value = <bpy_float[3], NodeSocketVector.default_value>
    Map_Range.inputs['Steps'].default_value = <bpy_float[3], NodeSocketVector.default_value>

    # Create node: Mesh Line
    Mesh_Line = node_group.nodes.new(type='GeometryNodeMeshLine')
    Mesh_Line.location = (-335.3932189941406, 262.69830322265625)
    Mesh_Line.inputs['Count'].default_value = 17
    Mesh_Line.inputs['Resolution'].default_value = 1.0
    Mesh_Line.inputs['Start Location'].default_value = <Vector (-4.0000, -4.1000, 0.0000)>
    Mesh_Line.inputs['Offset'].default_value = <Vector (0.0000, -14.2000, -0.3000)>

    # Create node: Subdivide Mesh
    Subdivide_Mesh = node_group.nodes.new(type='GeometryNodeSubdivideMesh')
    Subdivide_Mesh.location = (87.4834213256836, 104.42533874511719)
    Subdivide_Mesh.inputs['Level'].default_value = 1

    # Create node: Subdivide Curve
    Subdivide_Curve = node_group.nodes.new(type='GeometryNodeSubdivideCurve')
    Subdivide_Curve.location = (339.99993896484375, -411.6866149902344)
    Subdivide_Curve.inputs['Cuts'].default_value = 5

    # Create node: Subdivision Surface
    Subdivision_Surface = node_group.nodes.new(type='GeometryNodeSubdivisionSurface')
    Subdivision_Surface.location = (1743.9998779296875, 82.0166015625)
    Subdivision_Surface.inputs['Level'].default_value = 3
    Subdivision_Surface.inputs['Edge Crease'].default_value = 0.1358024626970291
    Subdivision_Surface.inputs['Vertex Crease'].default_value = 0.006172839552164078

    # Create links
    node_group.links.new(Subdivision_Surface.outputs['Mesh'], Group_Output.inputs['Geometry'])
    node_group.links.new(Subdivide_Curve.outputs['Curve'], Instance_on_Points.inputs['Instance'])
    node_group.links.new(Realize_Instances.outputs['Geometry'], Set_Position.inputs['Geometry'])
    node_group.links.new(Combine_XYZ.outputs['Vector'], Set_Position.inputs['Offset'])
    node_group.links.new(Instance_on_Points.outputs['Instances'], Realize_Instances.inputs['Geometry'])
    node_group.links.new(Map_Range.outputs['Result'], Math.inputs['Value'])
    node_group.links.new(Math.outputs['Value'], Combine_XYZ.inputs['Z'])
    node_group.links.new(Noise_Texture.outputs['Fac'], Map_Range.inputs['Value'])
    node_group.links.new(Set_Position.outputs['Geometry'], Curve_to_Mesh.inputs['Curve'])
    node_group.links.new(Curve_Circle.outputs['Curve'], Curve_to_Mesh.inputs['Profile Curve'])
    node_group.links.new(Mesh_Line.outputs['Mesh'], Transform_Geometry.inputs['Geometry'])
    node_group.links.new(Set_Position.001.outputs['Geometry'], Instance_on_Points.inputs['Points'])
    node_group.links.new(Transform_Geometry.outputs['Geometry'], Set_Position.001.inputs['Geometry'])
    node_group.links.new(Map_Range.001.outputs['Result'], Math.001.inputs['Value'])
    node_group.links.new(Math.001.outputs['Value'], Combine_XYZ.001.inputs['Z'])
    node_group.links.new(Noise_Texture.001.outputs['Fac'], Map_Range.001.inputs['Value'])
    node_group.links.new(Combine_XYZ.001.outputs['Vector'], Set_Position.001.inputs['Position'])
    node_group.links.new(Quadratic_Bezier.outputs['Curve'], Subdivide_Curve.inputs['Curve'])
    node_group.links.new(Curve_to_Mesh.outputs['Mesh'], Subdivision_Surface.inputs['Mesh'])

    return node_group

# Usage example:
node_group = create_geometry_nodes()
obj = bpy.data.objects['Plane']
geom_nodes_modifier = obj.modifiers.new(name='GeometryNodes', type='NODES')
geom_nodes_modifier.node_group = node_group

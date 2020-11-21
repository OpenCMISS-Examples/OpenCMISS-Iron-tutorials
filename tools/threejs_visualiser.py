from ipywidgets import embed
from pythreejs import *
from IPython.display import display
import numpy as np

import mesh_tools

def visualise2(mesh, field):

    # Get mesh topology information.
    num_nodes = mesh_tools.num_nodes_get(mesh, mesh_component=1)
    node_nums = list(range(1, num_nodes + 1))
    num_elements, element_nums = mesh_tools.num_element_get(mesh, mesh_component=1)

    # Convert geometric field to a morphic mesh and export to json
    mesh = mesh_tools.OpenCMISS_to_morphic(
        mesh, field, element_nums, node_nums, dimension=3,
        interpolation='linear')
    vertices, faces = mesh.get_faces(res=8, exterior_only=True)

    vertices = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1]
    ]

    faces = [
        [0, 1, 3],
        [0, 3, 2],
        [0, 2, 4],
        [2, 6, 4],
        [0, 4, 1],
        [1, 4, 5],
        [2, 3, 6],
        [3, 7, 6],
        [1, 5, 3],
        [3, 5, 7],
        [4, 6, 5],
        [5, 6, 7]
    ]

    vertexcolors = ['#000000', '#0000ff', '#00ff00', '#ff0000',
                    '#00ffff', '#ff00ff', '#ffff00', '#ffffff']

    # Map the vertex colors into the 'color' slot of the faces
    faces = [f + [None, [vertexcolors[i] for i in f], None] for f in faces]

    # Create the geometry:
    geometry = Geometry(vertices=vertices,
                            faces=faces,
                            colors=vertexcolors)
    # Calculate normals per face, for nice crisp edges:
    geometry.exec_three_obj_method('computeFaceNormals')

    three_js_mesh = Mesh(
        geometry=geometry,
        material=MeshLambertMaterial(color='green', opacity=0.5, transparent=True),
        position=(0, 0, 0),
    )
    target = (0, 5, 0)
    view_width = 600
    view_height = 400
    camera = CombinedCamera(position=[60, 60, 60], width=view_width,
                            height=view_height)
    camera.mode = 'orthographic'
    lights = [
        PointLight(position=[100, 0, 0], color="#ffffff"),
        PointLight(position=[0, 100, 0], color="#bbbbbb"),
        PointLight(position=[0, 0, 100], color="#888888"),
        AmbientLight(intensity=0.2),
    ]
    orbit = OrbitControls(controlling=camera, target=target)
    camera.lookAt(target)
    scene = Scene(children=[three_js_mesh, camera] + lights)
    renderer = Renderer(scene=scene, camera=camera, controls=[orbit],
                        width=view_width, height=view_height)
    camera.zoom = 4

    embed.embed_minimal_html('export.html', views=renderer, title='Renderer')
    display(renderer)

def colour_map(v):
    colors = ["#084594", "#0F529E", "#1760A8", "#1F6EB3", "#2979B9", "#3484BE", "#3E8EC4",
              "#4A97C9", "#57A0CE", "#64A9D3", "#73B2D7", "#83BBDB", "#93C4DE", "#A2CBE2",
              "#AED1E6", "#BBD6EB", "#C9DCEF", "#DBE8F4", "#EDF3F9", "#FFFFFF"]
    colors = np.array(colors)
    v = ((v-v.min())/(v.max()-v.min())*(len(colors)-1)).astype(np.int16)
    return colors[v]

def visualise(mesh, geometric_field, dependent_field):

    # Get mesh topology information.
    num_nodes = mesh_tools.num_nodes_get(mesh, mesh_component=1)
    node_nums = list(range(1, num_nodes + 1))
    num_elements, element_nums = mesh_tools.num_element_get(mesh, mesh_component=1)

    from opencmiss.iron import iron
    solution = mesh_tools.get_field_values(dependent_field, node_nums, derivative=1, dimension=1,
                     variable=iron.FieldVariableTypes.U)

    node_positions = mesh_tools.get_field_values(geometric_field, node_nums, derivative=1, dimension=3,
                     variable=iron.FieldVariableTypes.U)

    colors = colour_map(np.squeeze(solution))

    import matplotlib
    node_vertexcolors = []
    for value in solution:
        node_vertexcolors.append(matplotlib.colors.to_hex([value[0], value[0], value[0]]))

    # Convert geometric field to a morphic mesh and export to json
    mesh = mesh_tools.OpenCMISS_to_morphic(
        mesh, geometric_field, element_nums, node_nums, dimension=3,
        interpolation='linear')
    vertices, faces = mesh.get_faces(res=1, exterior_only=True)

    vertices = vertices.tolist()
    faces = faces.tolist()

    vertexcolors = []
    for vertex in vertices:
        ##print(np.where((node_positions == vertex).all(axis=1)))
        idx = np.where((node_positions == vertex).all(axis=1))[0][0]
        vertexcolors.append(colors[idx])

    # vertices = [
    #     [0, 0, 0],
    #     [0, 0, 1],
    #     [0, 1, 0],
    #     [0, 1, 1],
    #     [1, 0, 0],
    #     [1, 0, 1],
    #     [1, 1, 0],
    #     [1, 1, 1]
    # ]
    #
    # faces = [
    #     [0, 1, 3],
    #     [0, 3, 2],
    #     [0, 2, 4],
    #     [2, 6, 4],
    #     [0, 4, 1],
    #     [1, 4, 5],
    #     [2, 3, 6],
    #     [3, 7, 6],
    #     [1, 5, 3],
    #     [3, 5, 7],
    #     [4, 6, 5],
    #     [5, 6, 7]
    # ]
    #
    # vertexcolors = ['#000000', '#0000ff', '#00ff00', '#ff0000',
    #                 '#00ffff', '#ff00ff', '#ffff00', '#ffffff']

    # Map the vertex colors into the 'color' slot of the faces
    faces = [f + [None, [vertexcolors[i] for i in f], None] for f in faces]

    # Create the geometry:
    geometry = Geometry(vertices=vertices,
                            faces=faces,
                            colors=vertexcolors)

    # # Create the geometry:
    # geometry = Geometry(vertices=vertices.tolist(),
    #                         faces=faces.tolist())
    # # Calculate normals per face, for nice crisp edges:
    geometry.exec_three_obj_method('computeFaceNormals')

    surf1 = Mesh(geometry=geometry,
                 material=MeshLambertMaterial(vertexColors='VertexColors', side='FrontSide'),
                 position=[-0.5, -0.5, -0.5])# Center the cube,
    surf2 = Mesh(geometry=geometry,
                 material=MeshLambertMaterial(vertexColors='VertexColors', side='BackSide'),
                 position=[-0.5, -0.5, -0.5])# Center the cube,
    surf = Group(children=[surf1, surf2])

    # cube = Mesh(
    #     geometry=geometry,
    #     material=MeshLambertMaterial(vertexColors='VertexColors'),
    #     position=[-0.5, -0.5, -0.5],  # Center the cube,
    # )
    target = (0.0, 0.0, 0.0)
    view_width = 600
    view_height = 400
    camera = CombinedCamera(position=[60, 60, 60], width=view_width,
                            height=view_height)
    camera.mode = 'orthographic'
    lights = [
        PointLight(position=[100, 0, 0], color="#ffffff"),
        PointLight(position=[0, 100, 0], color="#bbbbbb"),
        PointLight(position=[0, 0, 100], color="#888888"),
        PointLight(position=[-100, 0, 0], color="#ffffff"),
        PointLight(position=[0, -100, 0], color="#bbbbbb"),
        PointLight(position=[0, 0, -100], color="#888888"),
        AmbientLight(intensity=0.2),
    ]
    orbit = OrbitControls(controlling=camera, target=target)
    camera.lookAt(target)
    scene = Scene(children=[surf1, surf2] + lights)
    renderer = Renderer(scene=scene, camera=camera, controls=[orbit],
                        width=view_width, height=view_height)
    camera.zoom = 40

    embed.embed_minimal_html('export.html', views=renderer, title='Renderer')
    display(renderer)

def get_faces(self, res=8, exterior_only=True, include_xi=False,
              elements=None):
    self.generate()

    if elements == None:
        Faces = self.faces
    else:
        Faces = []
        for face in self.faces:
            for element_face in face.element_faces:
                if element_face[0] in elements:
                    Faces.append(face)
                    break

    if exterior_only:
        Faces = [face for face in Faces if len(face.element_faces) == 1]

    XiT, TT = xi_grid(shape='tri', res=res)
    XiQ, TQ = xi_grid(shape='quad', res=res)
    NPT, NTT = XiT.shape[0], TT.shape[0]
    NPQ, NTQ = XiQ.shape[0], TQ.shape[0]

    XiQ0 = np.zeros(NPQ)
    XiQ1 = np.ones(NPQ)

    NP, NT = 0, 0
    for face in Faces:
        if face.shape == 'tri':
            NP += NPT
            NT += NTT
        elif face.shape == 'quad':
            NP += NPQ
            NT += NTQ

    X = np.zeros((NP, 3))  #######TODO#####face.nodes[0].num_fields))
    T = np.zeros((NT, 3), dtype='uint32')
    if include_xi:
        Xi = np.zeros((NP, 2))
    np, nt = 0, 0
    for face in Faces:
        if face.shape == 'tri':
            X[np:np + NPT, :] = self._core.evaluate(face.cid, XiT)
            if include_xi:
                Xi[np:np + NPT, :] = XiT
            T[nt:nt + NTT, :] = TT + np
            np += NPT
            nt += NTT
        elif face.shape == 'quad':
            elem = self.elements[face.element_faces[0][0]]
            face_index = face.element_faces[0][1]
            if face_index == 0:
                X[np:np + NPQ, :] = self._core.evaluate(
                    elem.cid,
                    np.array([XiQ[:, 0],
                              XiQ[:, 1],
                              XiQ0]).T)
            elif face_index == 1:
                X[np:np + NPQ, :] = self._core.evaluate(
                    elem.cid,
                    np.array([XiQ[:, 0],
                              XiQ[:, 1],
                              XiQ1]).T)
            elif face_index == 2:
                X[np:np + NPQ, :] = self._core.evaluate(
                    elem.cid,
                    np.array(
                        [XiQ[:, 0], XiQ0,
                         XiQ[:, 1]]).T)
            elif face_index == 3:
                X[np:np + NPQ, :] = self._core.evaluate(
                    elem.cid,
                    np.array(
                        [XiQ[:, 0], XiQ1,
                         XiQ[:, 1]]).T)
            elif face_index == 4:
                X[np:np + NPQ, :] = self._core.evaluate(
                    elem.cid,
                    np.array(
                        [XiQ0, XiQ[:, 0],
                         XiQ[:, 1]]).T)
            elif face_index == 5:
                X[np:np + NPQ, :] = self._core.evaluate(
                    elem.cid,
                    np.array(
                        [XiQ1, XiQ[:, 0],
                         XiQ[:, 1]]).T)

            T[nt:nt + NTQ, :] = TQ + np
            if include_xi:
                Xi[np:np + NPQ, :] = XiQ
            np += NPQ
            nt += NTQ
    if include_xi:
        return X, T, Xi
    return X, T


def xi_grid(shape='quad', res=[8, 8], units='div', method='fit'):
    if units == 'div':
        if isinstance(res, int):
            divs = [res, res]
        else:
            divs = res
    elif units == 'xi':
        raise TypeError('Unimplemented units')

    nx = divs[0] + 1
    dx = 0.5 / nx
    if method == 'fit':
        xi = np.linspace(0, 1, divs[0] + 1)
    elif method == 'center':
        xi = np.linspace(dx, 1 - dx, divs[0] + 1)
    else:
        xi = np.linspace(0, 1, divs[0] + 1)

    if shape == 'quad':
        NPQ = int(nx * nx)
        NTQ = int(2 * (divs[0] * divs[0]))

        xi1, xi2 = np.meshgrid(xi, xi)
        xi1 = xi1.reshape([xi1.size])
        xi2 = xi2.reshape([xi2.size])
        XiQ = np.array([xi1, xi2]).T
        TQ = np.zeros((NTQ, 3), dtype='uint32')
        np = 0
        for row in range(divs[0]):
            for col in range(divs[0]):
                NPPR = row * nx
                TQ[np, :] = [NPPR + col, NPPR + col + 1, NPPR + col + nx]
                np += 1
                TQ[np, :] = [NPPR + col + 1, NPPR + col + nx + 1,
                             NPPR + col + nx]
                np += 1

        return XiQ, TQ

    elif shape == 'tri':
        NPT = int(0.5 * nx * (nx - 1) + nx)
        NTT = int(divs[0] * divs[0])

        XiT = np.zeros([NPT, 2])
        TT = np.zeros((NTT, 3), dtype='uint32')
        NodesPerLine = range(divs[0], 0, -1)
        np = 0
        for row in range(nx):
            for col in range(nx - row):
                XiT[np, 0] = xi[col]
                XiT[np, 1] = xi[row]
                np += 1

        np = 0
        ns = 0
        for row in range(divs[0]):
            for col in range(divs[0] - row):
                TT[np, :] = [ns, ns + 1, ns + nx - row]
                np += 1
                if col != divs[0] - row - 1:
                    TT[np, :] = [ns + 1, ns + nx - row + 1, ns + nx - row]
                    np += 1
                ns += 1
            ns += 1

        return XiT, TT



if __name__ == '__main__':

    #DOC-START imports
    # Intialise OpenCMISS-Iron.
    from opencmiss.iron import iron
    #DOC-END imports

    #DOC-START coordinate system
    # Create coordinate system.
    coordinate_system_user_number = 1
    coordinate_system = iron.CoordinateSystem()
    coordinate_system.CreateStart(coordinate_system_user_number)
    coordinate_system.DimensionSet(3)
    coordinate_system.CreateFinish()
    #DOC-END coordinate system

    #DOC-START region
    # Create region.
    region_user_number = 1
    region = iron.Region()
    region.CreateStart(region_user_number, iron.WorldRegion)
    region.CoordinateSystemSet(coordinate_system)
    region.CreateFinish()
    #DOC-END region

    #DOC-START basis
    # Create basis functions.
    basis_user_number = 1
    basis = iron.Basis()
    basis.CreateStart(basis_user_number)
    basis.CreateFinish()
    #DOC-END basis

    #DOC-START mesh parameters
    # Define mesh parameters.
    number_global_x_elements = 1
    number_global_y_elements = 1
    number_global_z_elements = 1
    height = 1.0
    width = 1.0
    length = 1.0
    #DOC-END mesh parameters

    #DOC-START generated mesh
    # Create mesh.
    generated_mesh_user_number = 1
    generated_mesh = iron.GeneratedMesh()
    generated_mesh.CreateStart(generated_mesh_user_number, region)
    generated_mesh.TypeSet(iron.GeneratedMeshTypes.REGULAR)
    generated_mesh.BasisSet([basis])
    generated_mesh.ExtentSet([width, height, length])
    generated_mesh.NumberOfElementsSet(
        [number_global_x_elements,
         number_global_y_elements,
         number_global_z_elements])
    mesh = iron.Mesh()
    mesh_user_number = 1
    generated_mesh.CreateFinish(mesh_user_number, mesh)
    #DOC-END generated mesh

    #DOC-START decomposition
    # Perform mesh decomposition.
    decomposition_user_number = 1
    decomposition = iron.Decomposition()
    decomposition.CreateStart(decomposition_user_number, mesh)
    decomposition.CreateFinish()
    #DOC-END decomposition

    #DOC-START geometric field
    # Create geometric field.
    geometric_field_user_number = 1
    geometric_field = iron.Field()
    geometric_field.CreateStart(geometric_field_user_number, region)
    geometric_field.MeshDecompositionSet(decomposition)
    geometric_field.CreateFinish()
    #DOC-END geometric field

    #DOC-START update geometric parameters
    # Set geometric field values from the generated mesh.
    generated_mesh.GeometricParametersCalculate(geometric_field)
    #DOC-END update geometric parameters

    fields = iron.Fields()
    fields.CreateRegion(region)
    fields.NodesExport("laplace_equation", "FORTRAN")
    fields.ElementsExport("laplace_equation", "FORTRAN")
    fields.Finalise()

    # DOC-START equation set
    # Create standard Laplace equations set.
    equations_set_user_number = 1
    equations_set_field_user_number = 2
    equations_set_field = iron.Field()
    equations_set = iron.EquationsSet()
    equations_set_specification = [
        iron.EquationsSetClasses.CLASSICAL_FIELD,
        iron.EquationsSetTypes.LAPLACE_EQUATION,
        iron.EquationsSetSubtypes.STANDARD_LAPLACE]
    equations_set.CreateStart(
        equations_set_user_number, region, geometric_field,
        equations_set_specification, equations_set_field_user_number,
        equations_set_field)
    equations_set.CreateFinish()
    # DOC-END equation set

    # DOC-START dependent field
    # Create dependent field.
    dependent_field_user_number = 3
    dependent_field = iron.Field()
    equations_set.DependentCreateStart(
        dependent_field_user_number, dependent_field)
    equations_set.DependentCreateFinish()
    # DOC-END dependent field

    # DOC-START initialise dependent field
    # Initialise dependent field.
    dependent_field.ComponentValuesInitialiseDP(
        iron.FieldVariableTypes.U, iron.FieldParameterSetTypes.VALUES, 1, 0.5)
    # DOC-END initialise dependent field

    # DOC-START equations
    # Create equations.
    equations = iron.Equations()
    equations_set.EquationsCreateStart(equations)
    equations_set.EquationsCreateFinish()
    # DOC-END equations

    # DOC-START problem
    # Create problem.
    problem_user_number = 1
    problem = iron.Problem()
    problem_specification = [
        iron.ProblemClasses.CLASSICAL_FIELD,
        iron.ProblemTypes.LAPLACE_EQUATION,
        iron.ProblemSubtypes.STANDARD_LAPLACE]
    problem.CreateStart(problem_user_number, problem_specification)
    problem.CreateFinish()
    # DOC-END problem

    # DOC-START control loops
    # Create control loops.
    problem.ControlLoopCreateStart()
    problem.ControlLoopCreateFinish()
    # DOC-END control loops

    # DOC-START problem solver
    # Create problem solver.
    solver = iron.Solver()
    problem.SolversCreateStart()
    problem.SolverGet([iron.ControlLoopIdentifiers.NODE], 1, solver)
    solver.OutputTypeSet(iron.SolverOutputTypes.SOLVER)
    problem.SolversCreateFinish()
    # DOC-END problem solver

    # DOC-START solver equations
    # Create solver equations and add equations set to solver equations.
    solver = iron.Solver()
    solver_equations = iron.SolverEquations()
    problem.SolverEquationsCreateStart()
    problem.SolverGet([iron.ControlLoopIdentifiers.NODE], 1, solver)
    solver.SolverEquationsGet(solver_equations)
    solver_equations.EquationsSetAdd(equations_set)
    problem.SolverEquationsCreateFinish()
    # DOC-END solver equations

    # DOC-START boundary condition nodes
    # Identify first and last node number.
    firstNodeNumber = 1
    nodes = iron.Nodes()
    region.NodesGet(nodes)
    lastNodeNumber = nodes.NumberOfNodesGet()
    # DOC-END boundary condition nodes

    # DOC-START boundary conditions
    # Create boundary conditions and set first and last nodes to 0.0 and 1.0
    boundary_conditions = iron.BoundaryConditions()
    solver_equations.BoundaryConditionsCreateStart(boundary_conditions)
    boundary_conditions.SetNode(
        dependent_field, iron.FieldVariableTypes.U, 1, 1, firstNodeNumber,
        1, iron.BoundaryConditionsTypes.FIXED, 0.0)
    boundary_conditions.SetNode(
        dependent_field, iron.FieldVariableTypes.U, 1, 1, lastNodeNumber,
        1, iron.BoundaryConditionsTypes.FIXED, 1.0)
    solver_equations.BoundaryConditionsCreateFinish()
    # DOC-END boundary conditions

    # DOC-START solve
    problem.Solve()
    # DOC-END solve

    import sys
    sys.path.insert(1, '../../tools/')
    import threejs_visualiser
    threejs_visualiser.visualise(mesh, geometric_field, dependent_field)
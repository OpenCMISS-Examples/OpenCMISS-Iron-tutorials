#!/usr/bin/env python

#DOC-START imports
# Intialise OpenCMISS-Iron.
from opencmiss.iron import iron
#DOC-END imports

#DOC-START coordinate system
# Create coordinate system.
coordinate_system_user_number = 1
coordinate_system = iron.CoordinateSystem()
coordinate_system.CreateStart(coordinate_system_user_number)
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
number_global_y_elements = 3
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

#DOC-START equation set
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
#DOC-END equation set

#DOC-START dependent field
# Create dependent field.
dependent_field_user_number = 3
dependent_field = iron.Field()
equations_set.DependentCreateStart(
    dependent_field_user_number, dependent_field)
equations_set.DependentCreateFinish()
#DOC-END dependent field

#DOC-START initialise dependent field
# Initialise dependent field.
dependent_field.ComponentValuesInitialiseDP(
    iron.FieldVariableTypes.U, iron.FieldParameterSetTypes.VALUES, 1, 0.5)
#DOC-END initialise dependent field

#DOC-START equations
# Create equations.
equations = iron.Equations()
equations_set.EquationsCreateStart(equations)
equations_set.EquationsCreateFinish()
#DOC-END equations

#DOC-START problem
# Create problem.
problem_user_number = 1
problem = iron.Problem()
problem_specification = [
    iron.ProblemClasses.CLASSICAL_FIELD,
    iron.ProblemTypes.LAPLACE_EQUATION,
    iron.ProblemSubtypes.STANDARD_LAPLACE]
problem.CreateStart(problem_user_number, problem_specification)
problem.CreateFinish()
#DOC-END problem

#DOC-START control loops
# Create control loops.
problem.ControlLoopCreateStart()
problem.ControlLoopCreateFinish()
#DOC-END control loops

#DOC-START problem solver
# Create problem solver.
solver = iron.Solver()
problem.SolversCreateStart()
problem.SolverGet([iron.ControlLoopIdentifiers.NODE], 1, solver)
solver.OutputTypeSet(iron.SolverOutputTypes.SOLVER)
problem.SolversCreateFinish()
#DOC-END problem solver

#DOC-START solver equations
# Create solver equations and add equations set to solver equations.
solver = iron.Solver()
solver_equations = iron.SolverEquations()
problem.SolverEquationsCreateStart()
problem.SolverGet([iron.ControlLoopIdentifiers.NODE], 1, solver)
solver.SolverEquationsGet(solver_equations)
solver_equations.EquationsSetAdd(equations_set)
problem.SolverEquationsCreateFinish()
#DOC-END solver equations

#DOC-START boundary condition nodes
# Identify first and last node number.
firstNodeNumber = 1
nodes = iron.Nodes()
region.NodesGet(nodes)
lastNodeNumber = nodes.NumberOfNodesGet()
#DOC-END boundary condition nodes

#DOC-START boundary conditions
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
#DOC-END boundary conditions

#DOC-START solve
problem.Solve()
#DOC-END solve

#DOC-START fieldml export
# Export results in FieldML format.
base_name = "laplace_equation"
data_format = "PLAIN_TEXT"

fml = iron.FieldMLIO()
fml.OutputCreate(mesh, "", base_name, data_format)
fml.OutputAddFieldNoType(
    base_name + ".geometric", data_format, geometric_field,
    iron.FieldVariableTypes.U, iron.FieldParameterSetTypes.VALUES)
fml.OutputAddFieldNoType(
    base_name + ".phi", data_format, dependent_field,
    iron.FieldVariableTypes.U, iron.FieldParameterSetTypes.VALUES)
fml.OutputWrite("laplace_equation.xml")
fml.Finalise()
#DOC-END fieldml export

#DOC-START exfile export
# Export results in Exfile format.
fields = iron.Fields()
fields.CreateRegion(region)
fields.NodesExport("laplace_equation", "FORTRAN")
fields.ElementsExport("laplace_equation", "FORTRAN")
fields.Finalise()
#DOC-END exfile export

#DOC-START finalise
# Finalise OpenCMISS-Iron.
iron.Finalise()
#DOC-END finalise

print("Program successfully completed.")

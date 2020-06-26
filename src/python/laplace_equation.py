#!/usr/bin/env python

# Intialise OpenCMISS-Iron.
from opencmiss.iron import iron


def main():
    # Create coordinate system.
    coordinate_system_user_number = 1
    coordinate_system = iron.CoordinateSystem()
    coordinate_system.CreateStart(coordinate_system_user_number)
    coordinate_system.CreateFinish()

    # Create region.
    region_user_number = 1
    region = iron.Region()
    region.CreateStart(region_user_number, iron.WorldRegion)
    region.CoordinateSystemSet(coordinate_system)
    region.CreateFinish()

    # Create basis functions.
    basis_user_number = 1
    basis = iron.Basis()
    basis.CreateStart(basis_user_number)
    basis.CreateFinish()

    # Define mesh parameters.
    number_global_x_elements = 1
    number_global_y_elements = 3
    number_global_z_elements = 1
    height = 1.0
    width = 1.0
    length = 1.0

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

    # Perform mesh decomposition.
    decomposition_user_number = 1
    decomposition = iron.Decomposition()
    decomposition.CreateStart(decomposition_user_number, mesh)
    decomposition.CreateFinish()

    # Create geometric field.
    geometric_field_user_number = 1
    geometric_field = iron.Field()
    geometric_field.CreateStart(geometric_field_user_number, region)
    geometric_field.MeshDecompositionSet(decomposition)
    geometric_field.CreateFinish()

    # Set geometric field values from the generated mesh.
    generated_mesh.GeometricParametersCalculate(geometric_field)

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

    # Create dependent field.
    dependent_field_user_number = 3
    dependent_field = iron.Field()
    equations_set.DependentCreateStart(
        dependent_field_user_number, dependent_field)
    equations_set.DependentCreateFinish()

    # Initialise dependent field.
    dependent_field.ComponentValuesInitialiseDP(
        iron.FieldVariableTypes.U, iron.FieldParameterSetTypes.VALUES, 1, 0.5)

    # Create equations.
    equations = iron.Equations()
    equations_set.EquationsCreateStart(equations)
    equations_set.EquationsCreateFinish()

    # Create problem.
    problem_user_number = 1
    problem = iron.Problem()
    problem_specification = [
        iron.ProblemClasses.CLASSICAL_FIELD,
        iron.ProblemTypes.LAPLACE_EQUATION,
        iron.ProblemSubtypes.STANDARD_LAPLACE]
    problem.CreateStart(problem_user_number, problem_specification)
    problem.CreateFinish()

    # Create control loops.
    problem.ControlLoopCreateStart()
    problem.ControlLoopCreateFinish()

    # Create problem solver.
    solver = iron.Solver()
    problem.SolversCreateStart()
    problem.SolverGet([iron.ControlLoopIdentifiers.NODE], 1, solver)
    solver.OutputTypeSet(iron.SolverOutputTypes.SOLVER)
    problem.SolversCreateFinish()

    # Create solver equations and add equations set to solver equations.
    solver = iron.Solver()
    solver_equations = iron.SolverEquations()
    problem.SolverEquationsCreateStart()
    problem.SolverGet([iron.ControlLoopIdentifiers.NODE], 1, solver)
    solver.SolverEquationsGet(solver_equations)
    solver_equations.EquationsSetAdd(equations_set)
    problem.SolverEquationsCreateFinish()

    # Identify first and last node number.
    firstNodeNumber = 1
    nodes = iron.Nodes()
    region.NodesGet(nodes)
    lastNodeNumber = nodes.NumberOfNodesGet()

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

    problem.Solve()

    # Export results.
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

    fields = iron.Fields()
    fields.CreateRegion(region)
    fields.NodesExport("laplace_equation", "FORTRAN")
    fields.ElementsExport("laplace_equation", "FORTRAN")
    fields.Finalise()

    # Finalise OpenCMISS-Iron.
    iron.Finalise()

    print("Program successfully completed.")

if __name__ == '__main__':
    main()

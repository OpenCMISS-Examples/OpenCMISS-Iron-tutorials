#!/usr/bin/env python

# Intialise OpenCMISS-Iron
from opencmiss.iron import iron


def main():
    
    # Set problem parameters.
    height = 1.0
    width = 1.0
    length = 1.0

    (coordinateSystemUserNumber,
     regionUserNumber,
     basisUserNumber,
     generatedMeshUserNumber,
     meshUserNumber,
     decompositionUserNumber,
     geometricFieldUserNumber,
     equationsSetFieldUserNumber,
     dependentFieldUserNumber,
     equationsSetUserNumber,
     problemUserNumber) = range(1, 12)

    numberGlobalXElements = 1
    numberGlobalYElements = 3
    numberGlobalZElements = 1

    # Get the computational nodes information
    numberOfComputationalNodes = iron.ComputationalNumberOfNodesGet()
    computationalNodeNumber = iron.ComputationalNodeNumberGet()

    # Coordinate system.
    coordinateSystem = iron.CoordinateSystem()
    coordinateSystem.CreateStart(coordinateSystemUserNumber)
    coordinateSystem.CreateFinish()

    # Region.
    region = iron.Region()
    region.CreateStart(regionUserNumber, iron.WorldRegion)
    region.coordinateSystem = coordinateSystem
    region.CreateFinish()

    # Basis creation.
    basis = iron.Basis()
    basis.CreateStart(basisUserNumber)
    basis.type = iron.BasisTypes.LAGRANGE_HERMITE_TP
    basis.numberOfXi = 3
    basis.interpolationXi = [
        iron.BasisInterpolationSpecifications.LINEAR_LAGRANGE] * 3
    basis.quadratureNumberOfGaussXi = [2] * 3
    basis.CreateFinish()

    # Mesh creation.
    generatedMesh = iron.GeneratedMesh()
    generatedMesh.CreateStart(generatedMeshUserNumber, region)
    generatedMesh.type = iron.GeneratedMeshTypes.REGULAR
    generatedMesh.basis = [basis]
    generatedMesh.extent = [width, height, length]
    generatedMesh.numberOfElements = [numberGlobalXElements,
                                      numberGlobalYElements,
                                      numberGlobalZElements]

    mesh = iron.Mesh()
    generatedMesh.CreateFinish(meshUserNumber, mesh)

    # Mesh decomposition.
    decomposition = iron.Decomposition()
    decomposition.CreateStart(decompositionUserNumber, mesh)
    decomposition.type = iron.DecompositionTypes.CALCULATED
    decomposition.numberOfDomains = numberOfComputationalNodes
    decomposition.CreateFinish()

    # Create geometric field.
    geometricField = iron.Field()
    geometricField.CreateStart(geometricFieldUserNumber, region)
    geometricField.meshDecomposition = decomposition
    geometricField.ComponentMeshComponentSet(iron.FieldVariableTypes.U, 1, 1)
    geometricField.ComponentMeshComponentSet(iron.FieldVariableTypes.U, 2, 1)
    geometricField.ComponentMeshComponentSet(iron.FieldVariableTypes.U, 3, 1)
    geometricField.CreateFinish()

    # Set geometry from the generated mesh.
    generatedMesh.GeometricParametersCalculate(geometricField)

    # Create standard Laplace equations set.
    equationsSetField = iron.Field()
    equationsSet = iron.EquationsSet()
    equationsSetSpecification = [iron.EquationsSetClasses.CLASSICAL_FIELD,
                                 iron.EquationsSetTypes.LAPLACE_EQUATION,
                                 iron.EquationsSetSubtypes.STANDARD_LAPLACE]
    equationsSet.CreateStart(equationsSetUserNumber, region, geometricField,
                             equationsSetSpecification,
                             equationsSetFieldUserNumber, equationsSetField)
    equationsSet.CreateFinish()

    # Create dependent field.
    dependentField = iron.Field()
    equationsSet.DependentCreateStart(dependentFieldUserNumber, dependentField)
    dependentField.DOFOrderTypeSet(iron.FieldVariableTypes.U,
                                   iron.FieldDOFOrderTypes.SEPARATED)
    dependentField.DOFOrderTypeSet(iron.FieldVariableTypes.DELUDELN,
                                   iron.FieldDOFOrderTypes.SEPARATED)
    equationsSet.DependentCreateFinish()

    # Initialise dependent field.
    dependentField.ComponentValuesInitialiseDP(
        iron.FieldVariableTypes.U, iron.FieldParameterSetTypes.VALUES, 1, 0.5)

    # Create equations.
    equations = iron.Equations()
    equationsSet.EquationsCreateStart(equations)
    equations.sparsityType = iron.EquationsSparsityTypes.SPARSE
    equations.outputType = iron.EquationsOutputTypes.NONE
    equationsSet.EquationsCreateFinish()

    # Create problem.
    problem = iron.Problem()
    problemSpecification = [iron.ProblemClasses.CLASSICAL_FIELD,
                            iron.ProblemTypes.LAPLACE_EQUATION,
                            iron.ProblemSubtypes.STANDARD_LAPLACE]
    problem.CreateStart(problemUserNumber, problemSpecification)
    problem.CreateFinish()

    # Create control loops.
    problem.ControlLoopCreateStart()
    problem.ControlLoopCreateFinish()

    # Create problem solver.
    solver = iron.Solver()
    problem.SolversCreateStart()
    problem.SolverGet([iron.ControlLoopIdentifiers.NODE], 1, solver)
    solver.outputType = iron.SolverOutputTypes.SOLVER
    solver.linearType = iron.LinearSolverTypes.ITERATIVE
    solver.linearIterativeAbsoluteTolerance = 1.0E-12
    solver.linearIterativeRelativeTolerance = 1.0E-12
    problem.SolversCreateFinish()

    # Create solver equations and add equations set to solver equations.
    solver = iron.Solver()
    solverEquations = iron.SolverEquations()
    problem.SolverEquationsCreateStart()
    problem.SolverGet([iron.ControlLoopIdentifiers.NODE], 1, solver)
    solver.SolverEquationsGet(solverEquations)
    solverEquations.sparsityType = iron.SolverEquationsSparsityTypes.SPARSE
    equationsSetIndex = solverEquations.EquationsSetAdd(equationsSet)
    problem.SolverEquationsCreateFinish()

    # Create boundary conditions and set first and last nodes to 0.0 and 1.0
    boundaryConditions = iron.BoundaryConditions()
    solverEquations.BoundaryConditionsCreateStart(boundaryConditions)
    firstNodeNumber = 1
    nodes = iron.Nodes()
    region.NodesGet(nodes)
    lastNodeNumber = nodes.numberOfNodes
    firstNodeDomain = decomposition.NodeDomainGet(firstNodeNumber, 1)
    lastNodeDomain = decomposition.NodeDomainGet(lastNodeNumber, 1)
    if firstNodeDomain == computationalNodeNumber:
        boundaryConditions.SetNode(
            dependentField, iron.FieldVariableTypes.U, 1, 1, firstNodeNumber,
            1, iron.BoundaryConditionsTypes.FIXED, 0.0)
    if lastNodeDomain == computationalNodeNumber:
        boundaryConditions.SetNode(
            dependentField, iron.FieldVariableTypes.U, 1, 1, lastNodeNumber,
            1, iron.BoundaryConditionsTypes.FIXED, 1.0)
    solverEquations.BoundaryConditionsCreateFinish()

    problem.Solve()

    # Export results.
    baseName = "laplace_equation"
    dataFormat = "PLAIN_TEXT"

    fml = iron.FieldMLIO()
    fml.OutputCreate(mesh, "", baseName, dataFormat)
    fml.OutputAddFieldNoType(
        baseName + ".geometric", dataFormat, geometricField,
        iron.FieldVariableTypes.U, iron.FieldParameterSetTypes.VALUES)
    fml.OutputAddFieldNoType(
        baseName + ".phi", dataFormat, dependentField,
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


if __name__ == '__main__':
    main()

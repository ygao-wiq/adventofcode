from ortools.linear_solver import pywraplp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data["constraint_coeffs"] = [
        [5, 7, 9, 2, 1],
        [18, 4, -9, 10, 12],
        [4, 7, 3, 8, 5],
        [5, 13, 16, 3, -7],
    ]
    data["bounds"] = [250, 285, 211, 315]
    data["obj_coeffs"] = [7, 8, 2, 9, 6]
    data["num_vars"] = 5
    data["num_constraints"] = 4
    return data



def entry():
    """entry is the function to show how to solve a mixed integer optimization problem with SCIP(https://www.scipopt.org/)
    This example makes use of the array to define the constraints and object
    
    Problem:
    Maximize 7*x1 + 8*x2 + 2*x3 + 9*x4 + 6*x5 with constraints:

    - 5*x1 + 7*x2 + 9*x3 + 2*x4 + 1*x5 ≤ 250
    - 18*x1 + 4*x2 - 9*x3 + 10*x4 + 12*x5 ≤ 285
    - 4*x1 + 7*x2 + 3*x3 + 8*x4 + 5*x5 ≤ 211
    - 5*x1 + 13*x2 + 16*x3 + 3*x4 - 7*x5 ≤ 315
    - x1~x5 must be integers
    """
    data = create_data_model()
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        return

    infinity = solver.infinity()
    x = {}
    for j in range(data["num_vars"]):
        x[j] = solver.IntVar(0, infinity, "x[%i]" % j)
    print("Number of variables =", solver.NumVariables())

    for i in range(data["num_constraints"]):
        constraint = solver.RowConstraint(0, data["bounds"][i], "")
        for j in range(data["num_vars"]):
            constraint.SetCoefficient(x[j], data["constraint_coeffs"][i][j])
    print("Number of constraints =", solver.NumConstraints())
    # In Python, you can also set the constraints as follows.
    # for i in range(data['num_constraints']):
    #  constraint_expr = \
    # [data['constraint_coeffs'][i][j] * x[j] for j in range(data['num_vars'])]
    #  solver.Add(sum(constraint_expr) <= data['bounds'][i])

    objective = solver.Objective()
    for j in range(data["num_vars"]):
        objective.SetCoefficient(x[j], data["obj_coeffs"][j])
    objective.SetMaximization()
    # In Python, you can also set the objective as follows.
    # obj_expr = [data['obj_coeffs'][j] * x[j] for j in range(data['num_vars'])]
    # solver.Maximize(solver.Sum(obj_expr))

    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Objective value =", solver.Objective().Value())
        for j in range(data["num_vars"]):
            print(x[j].name(), " = ", x[j].solution_value())
        print()
        print(f"Problem solved in {solver.wall_time():d} milliseconds")
        print(f"Problem solved in {solver.iterations():d} iterations")
        print(f"Problem solved in {solver.nodes():d} branch-and-bound nodes")
    else:
        print("The problem does not have an optimal solution.")


if __name__ == "__main__":
    entry()
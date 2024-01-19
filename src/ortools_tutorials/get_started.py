from ortools.linear_solver import pywraplp


def entry():
    """entry is the function to show how to solve a optimization problem with GLOP(Google Linear Optimization Progragmming)
    Problem:
    Maximize x+3y with constraints:
    - 0 <= x <= 1
    - 0 <= y <= 2
    - 0 <= x+y <= 2
    """
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return
    
    x = solver.NumVar(0, 1, "x")
    y = solver.NumVar(0, 2, "y")
    print("Number of variables =", solver.NumVariables())
    
    # Create a linear constraint, 0 <= x + y <= 2.
    ct = solver.Constraint(0, 2, "ct")
    ct.SetCoefficient(x, 1)
    ct.SetCoefficient(y, 1)
    print("Number of constraints =", solver.NumConstraints())
    
    # Create the objective function, 3 * x + y.
    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 1)
    objective.SetMaximization()

    print(f"Solving with {solver.SolverVersion()}")
    solver.Solve()
    print("Solution:")
    print("Objective value =", objective.Value())
    print("x =", x.solution_value())
    print("y =", y.solution_value())

if __name__ == "__main__":
    entry()

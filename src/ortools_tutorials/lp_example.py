from ortools.linear_solver import pywraplp

def entry():
    """entry is the function to show how to solve a LP optimization problem with GLOP(Google Linear Optimization Progragmming)
    This example makes use of the explicit expression to define the constraints and object and check the returned status for
    convergence detection.
    
    Problem:
    Maximize 3x+4y with constraints:
    - x+2y <= 14
    - 3x-y >= 0
    - x-y <= 0
    """
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), "x")
    y = solver.NumVar(0, solver.infinity(), "y")
    print("Number of variables =", solver.NumVariables())
    
    # Constraint 0: x + 2y <= 14.
    solver.Add(x + 2 * y <= 14.0)

    # Constraint 1: 3x - y >= 0.
    solver.Add(3 * x - y >= 0.0)

    # Constraint 2: x - y <= 2.
    solver.Add(x - y <= 2.0)

    print("Number of constraints =", solver.NumConstraints())
    
    # Objective function: 3x + 4y.
    solver.Maximize(3 * x + 4 * y)
    
    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print(f"Objective value = {solver.Objective().Value():0.1f}")
        print(f"x = {x.solution_value():0.1f}")
        print(f"y = {y.solution_value():0.1f}")
    else:
        print("The problem does not have an optimal solution.")
    
if __name__ == "__main__":
    entry()
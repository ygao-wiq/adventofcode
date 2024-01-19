from ortools.sat.python import cp_model

def cp_sat_single_solution_entry():
    """cp_sat_single_solution_entry is the function to show how to solve a castraint programming problem with SAT(Satisfied)
    It returns a single solution if any would be found
    Problem:
    Find a feasible solution with the constraint:
    - x != y
    """
    model = cp_model.CpModel()
    num_vals = 3
    x = model.NewIntVar(0, num_vals - 1, "x")
    y = model.NewIntVar(0, num_vals - 1, "y")
    z = model.NewIntVar(0, num_vals - 1, "z")
    
    model.Add(x != y)
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"solver status: {solver.StatusName(status)}")
        print(f"x = {solver.Value(x)}")
        print(f"y = {solver.Value(y)}")
        print(f"z = {solver.Value(z)}")
    else:
        print("No solution found.")
        
if __name__ == "__main__":
    cp_sat_single_solution_entry()
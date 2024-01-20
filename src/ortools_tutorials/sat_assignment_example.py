import io

import pandas as pd

from ortools.sat.python import cp_model


def sat_assignment_entry():
    """scip_assignment_entry is the entry function to solve a combinational problem with optimal object and linear constraints
    
    It uses SAT CP solver
    The problem is to assign tasks across workers, with constraints:
    - each worker is assigned with at most one task
    - each task must be assigned to a single worker
    - Get the assignment result with lowest cost
    """
    # Data
    data_str = """
  worker  task  cost
      w1    t1    90
      w1    t2    80
      w1    t3    75
      w1    t4    70
      w2    t1    35
      w2    t2    85
      w2    t3    55
      w2    t4    65
      w3    t1   125
      w3    t2    95
      w3    t3    90
      w3    t4    95
      w4    t1    45
      w4    t2   110
      w4    t3    95
      w4    t4   115
      w5    t1    50
      w5    t2   110
      w5    t3    90
      w5    t4   100
  """

    data = pd.read_table(io.StringIO(data_str), sep=r"\s+")

    # Model
    model = cp_model.CpModel()

    # Variables
    x = model.NewBoolVarSeries(name="x", index=data.index)

    # Constraints
    # Each worker is assigned to at most one task.
    for unused_name, tasks in data.groupby("worker"):
        model.AddAtMostOne(x[tasks.index])

    # Each task is assigned to exactly one worker.
    for unused_name, workers in data.groupby("task"):
        model.AddExactlyOne(x[workers.index])

    # Objective
    model.Minimize(data.cost.dot(x))

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print solution.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Total cost = {solver.ObjectiveValue()}\n")
        selected = data.loc[solver.BooleanValues(x).loc[lambda x: x].index]
        for unused_index, row in selected.iterrows():
            print(f"{row.task} assigned to {row.worker} with a cost of {row.cost}")
    elif status == cp_model.INFEASIBLE:
        print("No solution found")
    else:
        print("Something is wrong, check the status and the log of the solve")


if __name__ == "__main__":
    sat_assignment_entry()
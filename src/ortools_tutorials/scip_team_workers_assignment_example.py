from ortools.linear_solver import pywraplp


def scip_team_assignment_entry():
    """scip_team_assignment_entry is the entry function to solve a combinational problem with optimal object and linear constraints
    
    It uses SCIP MIP solver
    The problem is to assign tasks across workers, with constraints:
    - each worker is assigned with at most one task
    - each task must be assigned to a single worker
    - The workers are grouped into two groups and each group must only be assigned at most two tasks
    - Get the assignment result with lowest cost
    """
    # Data
    costs = [
        [90, 76, 75, 70],
        [35, 85, 55, 65],
        [125, 95, 90, 105],
        [45, 110, 95, 115],
        [60, 105, 80, 75],
        [45, 65, 110, 95],
    ]
    num_workers = len(costs)
    num_tasks = len(costs[0])

    team1 = [0, 2, 4]
    team2 = [1, 3, 5]
    # Maximum total of tasks for any team
    team_max = 2

    # Solver
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        return

    # Variables
    # x[i, j] is an array of 0-1 variables, which will be 1
    # if worker i is assigned to task j.
    x = {}
    for worker in range(num_workers):
        for task in range(num_tasks):
            x[worker, task] = solver.BoolVar(f"x[{worker},{task}]")

    # Constraints
    # Each worker is assigned at most 1 task.
    for worker in range(num_workers):
        solver.Add(solver.Sum([x[worker, task] for task in range(num_tasks)]) <= 1)

    # Each task is assigned to exactly one worker.
    for task in range(num_tasks):
        solver.Add(solver.Sum([x[worker, task] for worker in range(num_workers)]) == 1)

    # Each team takes at most two tasks.
    team1_tasks = []
    for worker in team1:
        for task in range(num_tasks):
            team1_tasks.append(x[worker, task])
    solver.Add(solver.Sum(team1_tasks) <= team_max)

    team2_tasks = []
    for worker in team2:
        for task in range(num_tasks):
            team2_tasks.append(x[worker, task])
    solver.Add(solver.Sum(team2_tasks) <= team_max)

    # Objective
    objective_terms = []
    for worker in range(num_workers):
        for task in range(num_tasks):
            objective_terms.append(costs[worker][task] * x[worker, task])
    solver.Minimize(solver.Sum(objective_terms))

    # Solve
    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print(f"Total cost = {solver.Objective().Value()}\n")
        for worker in range(num_workers):
            for task in range(num_tasks):
                if x[worker, task].solution_value() > 0.5:
                    print(
                        f"Worker {worker} assigned to task {task}."
                        + f" Cost = {costs[worker][task]}"
                    )
    else:
        print("No solution found.")
    print(f"Time = {solver.WallTime()} ms")


if __name__ == "__main__":
    scip_team_assignment_entry()
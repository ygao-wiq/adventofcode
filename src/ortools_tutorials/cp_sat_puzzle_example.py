from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}={self.Value(v)}", end=" ")
        print()

    def solution_count(self):
        return self.__solution_count


def cp_sat_puzzle_entry():
    """Solve the CP+IS+FUN==TRUE cryptarithm."""
    # Constraint programming engine
    model = cp_model.CpModel()

    base = 10

    c = model.NewIntVar(1, base - 1, "C")
    p = model.NewIntVar(0, base - 1, "P")
    i = model.NewIntVar(1, base - 1, "I")
    s = model.NewIntVar(0, base - 1, "S")
    f = model.NewIntVar(1, base - 1, "F")
    u = model.NewIntVar(0, base - 1, "U")
    n = model.NewIntVar(0, base - 1, "N")
    t = model.NewIntVar(1, base - 1, "T")
    r = model.NewIntVar(0, base - 1, "R")
    e = model.NewIntVar(0, base - 1, "E")

    # We need to group variables in a list to use the constraint AllDifferent.
    letters = [c, p, i, s, f, u, n, t, r, e]

    # Verify that we have enough digits.
    assert base >= len(letters)

    # Define constraints.
    model.AddAllDifferent(letters)

    # CP + IS + FUN = TRUE
    model.Add(
        c * base + p + i * base + s + f * base * base + u * base + n
        == t * base * base * base + r * base * base + u * base + e
    )

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(letters)
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True
    # Solve.
    status = solver.Solve(model, solution_printer)

    # Statistics.
    print("\nStatistics")
    print(f"  status   : {solver.StatusName(status)}")
    print(f"  conflicts: {solver.NumConflicts()}")
    print(f"  branches : {solver.NumBranches()}")
    print(f"  wall time: {solver.WallTime()} s")
    print(f"  sol found: {solution_printer.solution_count()}")


if __name__ == "__main__":
    cp_sat_puzzle_entry()
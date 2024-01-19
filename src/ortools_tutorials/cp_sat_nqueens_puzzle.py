import sys
import time
from ortools.sat.python import cp_model
from ortools.constraint_solver import pywrapcp

class NQueenSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, queens):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__queens = queens
        self.__solution_count = 0
        self.__start_time = time.time()

    def solution_count(self):
        return self.__solution_count

    def on_solution_callback(self):
        current_time = time.time()
        print(
            f"Solution {self.__solution_count}, "
            f"time = {current_time - self.__start_time} s"
        )
        self.__solution_count += 1

        all_queens = range(len(self.__queens))
        for i in all_queens:
            for j in all_queens:
                if self.Value(self.__queens[j]) == i:
                    # There is a queen in column j, row i.
                    print("Q", end=" ")
                else:
                    print("_", end=" ")
            print()
        print()


def cp_sat_nqueens_puzzle_cp_entry(board_size):
    # Creates the solver.
    model = cp_model.CpModel()

    # Creates the variables.
    # There are `board_size` number of variables, one for a queen in each column
    # of the board. The value of each variable is the row that the queen is in.
    queens = [model.NewIntVar(0, board_size - 1, f"x_{i}") for i in range(board_size)]

    # Creates the constraints.
    # All rows must be different.
    model.AddAllDifferent(queens)

    # No two queens can be on the same diagonal.
    model.AddAllDifferent(queens[i] + i for i in range(board_size))
    model.AddAllDifferent(queens[i] - i for i in range(board_size))

    # Solve the model.
    solver = cp_model.CpSolver()
    solution_printer = NQueenSolutionPrinter(queens)
    solver.parameters.enumerate_all_solutions = True
    solver.Solve(model, solution_printer)

    # Statistics.
    print("\nStatistics")
    print(f"  conflicts      : {solver.NumConflicts()}")
    print(f"  branches       : {solver.NumBranches()}")
    print(f"  wall time      : {solver.WallTime()} s")
    print(f"  solutions found: {solution_printer.solution_count()}")


def cp_sat_nqueens_puzzle_original_solver_entry(board_size):
    # Creates the solver.
    solver = pywrapcp.Solver("n-queens")

    # Creates the variables.
    # The array index is the column, and the value is the row.
    queens = [solver.IntVar(0, board_size - 1, f"x{i}") for i in range(board_size)]

    # Creates the constraints.
    # All rows must be different.
    solver.Add(solver.AllDifferent(queens))

    # No two queens can be on the same diagonal.
    solver.Add(solver.AllDifferent([queens[i] + i for i in range(board_size)]))
    solver.Add(solver.AllDifferent([queens[i] - i for i in range(board_size)]))

    db = solver.Phase(queens, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)

    # Iterates through the solutions, displaying each.
    num_solutions = 0
    solver.NewSearch(db)
    while solver.NextSolution():
        # Displays the solution just computed.
        for i in range(board_size):
            for j in range(board_size):
                if queens[j].Value() == i:
                    # There is a queen in column j, row i.
                    print("Q", end=" ")
                else:
                    print("_", end=" ")
            print()
        print()
        num_solutions += 1
    solver.EndSearch()

    # Statistics.
    print("\nStatistics")
    print(f"  failures: {solver.Failures()}")
    print(f"  branches: {solver.Branches()}")
    print(f"  wall time: {solver.WallTime()} ms")
    print(f"  Solutions found: {num_solutions}")


if __name__ == "__main__":
    # By default, solve the 8x8 problem.
    size = 8
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    cp_sat_nqueens_puzzle_cp_entry(size)
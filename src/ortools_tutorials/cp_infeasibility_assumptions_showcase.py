#!/usr/bin/env python3
"""Code sample that solves a model and gets the infeasibility assumptions."""
from ortools.sat.python import cp_model


def main():
    """Showcases assumptions."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    x = model.NewIntVar(0, 10, "x")
    y = model.NewIntVar(0, 10, "y")
    z = model.NewIntVar(0, 10, "z")
    a = model.NewBoolVar("a")
    b = model.NewBoolVar("b")
    c = model.NewBoolVar("c")
    d = model.NewBoolVar("d")

    # Creates the constraints.
    model.Add(x > y).OnlyEnforceIf(a)
    model.Add(y > z).OnlyEnforceIf(b)
    model.Add(z > x).OnlyEnforceIf(c)
    model.Add(z < x).OnlyEnforceIf(c.Not())

    # Add assumptions
    model.AddAssumptions([a, b, c])

    # Creates a solver and solves.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print solution.
    print(f"Status = {solver.StatusName(status)}")
    if status == cp_model.INFEASIBLE:
        print(
            "SufficientAssumptionsForInfeasibility = "
            f"{solver.SufficientAssumptionsForInfeasibility()}"
        )
        print("Infeasible variables:")
        for i in solver.SufficientAssumptionsForInfeasibility():
            print(model.GetBoolVarFromProtoIndex(i))


if __name__ == "__main__":
    main()
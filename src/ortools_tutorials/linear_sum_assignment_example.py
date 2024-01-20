import numpy as np

from ortools.graph.python import linear_sum_assignment


def linear_sum_assignment_entry():
    """linear_sum_assignment_entry is the entry function to solve a combinational problem with optimal object and linear constraints
    
    It uses Linear Sum solver
    The problem is to assign tasks across workers, with constraints:
    - each worker is assigned with at most one task
    - each task must be assigned to a single worker
    - Get the assignment result with lowest cost
    """
    assignment = linear_sum_assignment.SimpleLinearSumAssignment()

    costs = np.array(
        [
            [90, 76, 75, 70],
            [35, 85, 55, 65],
            [125, 95, 90, 105],
            [45, 110, 95, 115],
        ]
    )

    # Let's transform this into 3 parallel vectors (start_nodes, end_nodes,
    # arc_costs)
    end_nodes_unraveled, start_nodes_unraveled = np.meshgrid(
        np.arange(costs.shape[1]), np.arange(costs.shape[0])
    )
    start_nodes = start_nodes_unraveled.ravel()
    end_nodes = end_nodes_unraveled.ravel()
    arc_costs = costs.ravel()

    assignment.add_arcs_with_cost(start_nodes, end_nodes, arc_costs)

    status = assignment.solve()

    if status == assignment.OPTIMAL:
        print(f"Total cost = {assignment.optimal_cost()}\n")
        for i in range(0, assignment.num_nodes()):
            print(
                f"Worker {i} assigned to task {assignment.right_mate(i)}."
                + f"  Cost = {assignment.assignment_cost(i)}"
            )
    elif status == assignment.INFEASIBLE:
        print("No assignment is possible.")
    elif status == assignment.POSSIBLE_OVERFLOW:
        print("Some input costs are too large and may cause an integer overflow.")


if __name__ == "__main__":
    linear_sum_assignment_entry()

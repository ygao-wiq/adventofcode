from ortools.graph.python import min_cost_flow


def network_team_assignment_as_min_cost_entry():
    """network_team_assignment_as_min_cost_entry is the entry function solving an assignment with teams of worker."""
    smcf = min_cost_flow.SimpleMinCostFlow()

    # Define the directed graph for the flow.
    team_a = [1, 3, 5]
    team_b = [2, 4, 6]

    start_nodes = (
        # fmt: off
      [0, 0]
      + [11, 11, 11]
      + [12, 12, 12]
      + [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]
      + [7, 8, 9, 10]
        # fmt: on
    )
    end_nodes = (
        # fmt: off
      [11, 12]
      + team_a
      + team_b
      + [7, 8, 9, 10, 7, 8, 9, 10, 7, 8, 9, 10, 7, 8, 9, 10, 7, 8, 9, 10, 7, 8, 9, 10]
      + [13, 13, 13, 13]
        # fmt: on
    )
    capacities = (
        # fmt: off
      [2, 2]
      + [1, 1, 1]
      + [1, 1, 1]
      + [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      + [1, 1, 1, 1]
        # fmt: on
    )
    costs = (
        # fmt: off
      [0, 0]
      + [0, 0, 0]
      + [0, 0, 0]
      + [90, 76, 75, 70, 35, 85, 55, 65, 125, 95, 90, 105, 45, 110, 95, 115, 60, 105, 80, 75, 45, 65, 110, 95]
      + [0, 0, 0, 0]
        # fmt: on
    )

    source = 0
    sink = 13
    tasks = 4
    # Define an array of supplies at each node.
    supplies = [tasks, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -tasks]

    # Add each arc.
    for i in range(0, len(start_nodes)):
        smcf.add_arc_with_capacity_and_unit_cost(
            start_nodes[i], end_nodes[i], capacities[i], costs[i]
        )

    # Add node supplies.
    for i in range(0, len(supplies)):
        smcf.set_node_supply(i, supplies[i])

    # Find the minimum cost flow between node 0 and node 10.
    status = smcf.solve()

    if status == smcf.OPTIMAL:
        print("Total cost = ", smcf.optimal_cost())
        print()
        for arc in range(smcf.num_arcs()):
            # Can ignore arcs leading out of source or intermediate, or into sink.
            if (
                smcf.tail(arc) != source
                and smcf.tail(arc) != 11
                and smcf.tail(arc) != 12
                and smcf.head(arc) != sink
            ):
                # Arcs in the solution will have a flow value of 1.
                # There start and end nodes give an assignment of worker to task.
                if smcf.flow(arc) > 0:
                    print(
                        "Worker %d assigned to task %d.  Cost = %d"
                        % (smcf.tail(arc), smcf.head(arc), smcf.unit_cost(arc))
                    )
    else:
        print("There was an issue with the min cost flow input.")
        print(f"Status: {status}")


if __name__ == "__main__":
    network_team_assignment_as_min_cost_entry()
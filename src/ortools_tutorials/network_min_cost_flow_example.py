"""From """
import numpy as np

from ortools.graph.python import min_cost_flow


def network_min_cost_flow_entry():
    """network_min_cost_flow_entry is the entry function for the problem defined in Bradley, Hax and Maganti, 'Applied Mathematical Programming', figure 8.1.
    
    It is to solve the flow of minimum cost between two arbitrary vertices within a weighted directed graph
    - There are two special categories of nods: supply and demand
    - Supply nodes add onto the flow while the demand nodes take away from the flow
    - Other nodes are assumed with zero addings and take-ways
    - At each node, the total flow leading out of the node minus the total flow leading in to the node equals the supply (or demand) at that node
    - Each edge has a capacity and a cost associated
    """
    # Instantiate a SimpleMinCostFlow solver.
    smcf = min_cost_flow.SimpleMinCostFlow()

    # Define four parallel arrays: sources, destinations, capacities,
    # and unit costs between each pair. For instance, the arc from node 0
    # to node 1 has a capacity of 15.
    start_nodes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 4])
    end_nodes = np.array([1, 2, 2, 3, 4, 3, 4, 4, 2])
    capacities = np.array([15, 8, 20, 4, 10, 15, 4, 20, 5])
    unit_costs = np.array([4, 4, 2, 2, 6, 1, 3, 2, 3])

    # Define an array of supplies at each node.
    supplies = [20, 0, 0, -5, -15]

    # Add arcs, capacities and costs in bulk using numpy.
    all_arcs = smcf.add_arcs_with_capacity_and_unit_cost(
        start_nodes, end_nodes, capacities, unit_costs
    )

    # Add supply for each nodes.
    smcf.set_nodes_supplies(np.arange(0, len(supplies)), supplies)

    # Find the min cost flow.
    status = smcf.solve()

    if status != smcf.OPTIMAL:
        print("There was an issue with the min cost flow input.")
        print(f"Status: {status}")
        exit(1)
    print(f"Minimum cost: {smcf.optimal_cost()}")
    print("")
    print(" Arc    Flow / Capacity Cost")
    solution_flows = smcf.flows(all_arcs)
    costs = solution_flows * unit_costs
    for arc, flow, cost in zip(all_arcs, solution_flows, costs):
        print(
            f"{smcf.tail(arc):1} -> {smcf.head(arc)}  {flow:3}  / {smcf.capacity(arc):3}       {cost}"
        )


if __name__ == "__main__":
    network_min_cost_flow_entry()
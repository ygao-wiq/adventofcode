import numpy as np

from ortools.graph.python import max_flow


def network_max_flow_entry():
    """network_max_flow_entry is the entry function for the problem defined in Taha 'Introduction to Operations Research', example 6.4-2.
    
    It is to solve the maximum flow between two arbitrary vertices within a weighted directed graph
    """
    # Instantiate a SimpleMaxFlow solver.
    smf = max_flow.SimpleMaxFlow()

    # Define three parallel arrays: start_nodes, end_nodes, and the capacities
    # between each pair. For instance, the arc from node 0 to node 1 has a
    # capacity of 20.
    start_nodes = np.array([0, 0, 0, 1, 1, 2, 2, 3, 3])
    end_nodes = np.array([1, 2, 3, 2, 4, 3, 4, 2, 4])
    capacities = np.array([20, 30, 10, 40, 30, 10, 20, 5, 20])

    # Add arcs in bulk.
    #   note: we could have used add_arc_with_capacity(start, end, capacity)
    all_arcs = smf.add_arcs_with_capacity(start_nodes, end_nodes, capacities)

    # Find the maximum flow between node 0 and node 4.
    status = smf.solve(0, 4)

    if status != smf.OPTIMAL:
        print("There was an issue with the max flow input.")
        print(f"Status: {status}")
        exit(1)
    print("Max flow:", smf.optimal_flow())
    print("")
    print(" Arc    Flow / Capacity")
    solution_flows = smf.flows(all_arcs)
    for arc, flow, capacity in zip(all_arcs, solution_flows, capacities):
        print(f"{smf.tail(arc)} / {smf.head(arc)}   {flow:3}  / {capacity:3}")
    print("Source side min-cut:", smf.get_source_side_min_cut())
    print("Sink side min-cut:", smf.get_sink_side_min_cut())


if __name__ == "__main__":
    network_max_flow_entry()
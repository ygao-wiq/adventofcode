## Summary
This directory contains the examples created to learn about programming with [ortools](https://developers.google.com/optimization/introduction).  
The examples are developed with Python programmng language. 

## Installation `ortools`
Run following commands:
> pip install -U --user ortools

## Examples

#### LP Problem
| sample code | description |
|:------------|:------------|
|[get_started.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/get_started.py)| A simple one with CPP style interface by GLOP|
|[lp_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/lp_example.py)| A simple one with expression styoe interface by GLOP|
|[lp_various_solvers.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/lp_various_solvers.py)| A simple one with mixed solvers for a same LP problem|
|[mip_array_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/mip_array_example.py) | An example of LP expressed in arrays and solved by SCIP |
|[mip_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/mip_example.py) | An example of LP expressed in arrays and solved by SCIP |

#### CP Problem
| sample code | description |
|:------------|:------------|
|[cp_infeasibility_assumptions_showcase.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/cp_infeasibility_assumptions_showcase.py)| A showcase of troubleshooting CP-SAT with assumptions|
|[cp_original_solver_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/cp_original_solver_example.py)| An example to use legacy CP problem solver |
|[cp_sat_all_solutions_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/cp_sat_all_solutions_example.py) | An example to list all feasibile solutions by SAT |
|[cp_sat_nqueens_puzzle.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/cp_sat_nqueens_puzzle.py)| An example to solve N-queeens problem with SAT |
|[cp_sat_optimal_solution_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/cp_sat_optimal_solution_example.py)| An example to solve an optimal CP problem with SAT |
|[cp_sat_puzzle_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/cp_sat_puzzle_example.py)| An example to solve a character algebra CP probelm with SAT |
|[cp_sat_single_solution_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/cp_sat_single_solution_example.py)| An example to find a single feasible solution for CP problem by SAT |
|

#### Assignment Problem
| sample code | description |
|:------------|:------------|
|[scip_assignment_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/scip_assignment_example.py)| A sample one using SCIP to solve a tasks assignment problem |
|[scip_sized_task_assignment_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/scip_sized_task_assignment_example.py)| A sample one using SCIP to solve a sized tasks assignment problem |
|[scip_allowed_group_assignment_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/scip_allowed_group_assignment_example.py)| A sample one using SCIP to solve a tasks assignment problem with grouping constraint |
|[scip_team_workers_assignment_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/scip_team_workers_assignment_example.py)| A sample one using SCIP to solve a tasks assignment problem with team capacity constraint |
|[sat_assignment_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/sat_assignment_example.py)| A sample one using SAT to solve a tasks assignment problem |
|[sat_sized_task_assignment_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/sat_sized_task_assignment_example.py)| A sample one using SAT to solve a sized tasks assignment problem |
|[sat_allowed_group_assignment_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/sat_allowed_group_assignment_example.py)| A sample one using SAT to solve a tasks assignment problem with grouping constraint |
|[sat_team_works_assignment_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/sat_team_works_assignment_example.py)| A sample one using SAT to solve a tasks assignment problem with team capacity constraint |

#### Schedule Problem
| sample code | description |
|:------------|:------------|
|[scheduling_sat_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/scheduling_sat_example.py)| Use SAT to solve a simple scheduling problem |
|[scheduling_sat_max_requests_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/scheduling_sat_max_requests_example.py) | Use SAT to solve a scheduling problem with a soft constraint to meet desired shifts as many as possible |
|[scheduling_job_shop_example.py](https://github.com/ygao-wiq/adventofcode/blob/main/src/ortools_tutorials/scheduling_job_shop_example.py)| A schedule problem with hard constraints of inter-dependencies|
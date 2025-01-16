<h1> Github advents calendar House Grid</h1> <br>
<h2>Code that solves the advents calendar for connected houses inside of a matrix</h2>

This code is intended to solve the problem of the connected houses with christmas decoration in a Neighbourhood. 
The problem was formulated in github as the advents calendar programming challenges of the year 2024.
Description of the problem:
```
Write a function `largest_cluster(grid: List[List[int]]) -> int` that returns the size of
the largest contiguous cluster of decorated houses.
A cluster is defined as a set of '1' cells that are connected horizontally or vertically (but not diagonally).
For example:
Given the grid:<br>
[<br>
    [1, 1, 0], <br>
    [1, 0, 0],<br>
    [0, 1, 1]<br>
]<br>
There are three clusters:
- Cluster A: The top-left corner (3 houses) → positions: (0,0), (0,1), (1,0)
- Cluster B: The bottom row from (2,1) to (2,2) (2 houses)
- The cell at (0,2) is a '0' so it's not decorated and doesn't form a cluster.
The largest cluster size here is 3.
Your function should return 3 for the above input.
```
<h2> Technical Requirements to run this code</h2>
This code has no special requirements regarding the Python version. The tests are written in pytest. 
For installing and setting up the environment, please do the following:

```bash
python -m venv .env
source .env/bin/activate
pip install requirements.txt
```

In case you see this after pointing out personally the previous lack of Readme.md and the error for constants... 
You will make me smile :-)

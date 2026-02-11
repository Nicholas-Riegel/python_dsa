# Graphs

## What is a Graph?
A **graph** is a data structure consisting of a collection of vertices (nodes) connected by edges. Graphs are used to model relationships between objects, such as:
- Social networks (users and friendships)
- Road networks (cities and roads)
- Computer networks (devices and connections)
- Dependencies (tasks and prerequisites)

## Basic Components

### Vertices (Nodes)
- **Vertices** (also called nodes) are the fundamental units of a graph
- They represent entities or objects in the system
- Each vertex can store data/value
- In a graph with V vertices, vertices are typically numbered 0 to V-1

### Edges
- **Edges** are connections between vertices
- They represent relationships or links between entities
- An edge connects exactly two vertices
- In a graph with E edges, each edge can be represented as a pair (u, v)

## Graph Types

### Directed vs Undirected

#### Undirected Graph
- Edges have **no direction**
- If there's an edge between vertex A and B, you can travel both A→B and B→A
- Represented as unordered pairs: {A, B}
- Example: Facebook friendships (mutual relationship)

#### Directed Graph (Digraph)
- Edges have **direction** (arrows)
- An edge from A to B doesn't imply an edge from B to A
- Represented as ordered pairs: (A, B) where A→B
- Example: Twitter follows (A follows B doesn't mean B follows A)

### Weighted vs Unweighted

#### Unweighted Graph
- All edges are considered **equal**
- No additional cost/weight associated with edges
- Only connection matters, not the "strength" of connection
- Example: Simple friendship network

#### Weighted Graph
- Each edge has an associated **weight/cost**
- Weight represents distance, cost, time, or any numeric value
- Used when the relationship strength/cost matters
- Example: Road network with distances, flight routes with costs

## Graph Representations

### Adjacency Matrix

#### Structure
- **2D array** of size V × V (where V = number of vertices)
- `matrix[i][j] = 1` if edge exists from vertex i to vertex j
- `matrix[i][j] = 0` if no edge exists
- For weighted graphs: `matrix[i][j] = weight` instead of 1

#### Example (Undirected)
```
Vertices: 0, 1, 2
Edges: (0,1), (1,2), (0,2)

   0  1  2
0 [0  1  1]
1 [1  0  1]  
2 [1  1  0]
```

#### Big O Complexity
- **Space**: O(V²) - regardless of number of edges
- **Edge lookup**: O(1) - direct array access
- **Add vertex**: O(V²) - need to resize matrix
- **Add edge**: O(1) - set array element
- **Get all neighbors**: O(V) - scan entire row

### Adjacency List

#### Structure
- **Array/List of lists** or **HashMap/Dictionary**
- Each vertex has a list of its connected vertices
- `adj_list[i]` contains all vertices connected to vertex i
- For weighted graphs: store (vertex, weight) pairs

#### Example (Undirected)
```
Vertices: 0, 1, 2
Edges: (0,1), (1,2), (0,2)

0: [1, 2]
1: [0, 2]
2: [0, 1]
```

#### Big O Complexity
- **Space**: O(V + E) - space proportional to vertices and edges
- **Edge lookup**: O(degree of vertex) - scan neighbor list
- **Add vertex**: O(1) - add new empty list
- **Add edge**: O(1) - append to list
- **Get all neighbors**: O(degree of vertex) - return the list

## Choosing the Right Representation

### Use Adjacency Matrix when:
- Graph is **dense** (many edges)
- Need **fast edge lookups** O(1)
- Performing matrix operations
- Graph size is small and fixed

### Use Adjacency List when:
- Graph is **sparse** (few edges)
- Need **memory efficiency**
- Frequently adding/removing vertices
- Need to iterate through neighbors often

## Summary
- **Dense graphs**: |E| ≈ |V|² → Adjacency Matrix
- **Sparse graphs**: |E| << |V|² → Adjacency List
- **Space trade-off**: Matrix O(V²) vs List O(V + E)
- **Time trade-off**: Matrix O(1) edge lookup vs List O(degree) lookup

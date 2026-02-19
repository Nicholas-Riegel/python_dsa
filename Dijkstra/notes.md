One of the most famous and widely used algorithms around!

Finds the shortest path between two vertices on a graph

"What's the fastest way to get from point A to point B?"

Approach:
1. Every time we look to visit a new node, we note the previous and the distance from the origin to each of our neighbors. 
2. We pick the node with the smallest known distance from the origin to visit next.
2. Once we’ve moved to that node, we add it to visited, and look at each of its neighbors
3. For each neighboring node, we marke the previous and calculate the distance from the origin by summing the total edges that led to that node. 
4. If the new total distance to a node is less than the previous total, we store the new shorter distance for that node, and update the previous. 
5. Then look at the known distances of all the unvisited nodes from the origin and pick the smallest one to visit next


FIND THE SHORTEST PATH

FROM A TO E

Vertex | Shortest Dist From A
-----------------------------
   A   |    0
   B   |
   C   |
   D   |
   E   |
   F   |

Visited = []

Previous = {
    A: null,
    B: null,
    C: null,
    D: null,
    E: null,
    F: null
}

Dijkstra's Pseudocode

1. This function should accept a starting and ending vertex
2. Create an object (we'll call it distances) and set each key to be every vertex in the adjacency list with a value of infinity, except for the starting vertex which should have a value of 0.
3. After setting a value in the distances object, add each vertex with a priority of Infinity to the priority queue, except the starting vertex, which should have a priority of 0 because that's where we begin.
4. Create another object called previous and set each key to be every vertex in the adjacency list with a value of null
5. Start looping as long as there is anything in the priority queue
    dequeue a vertex from the priority queue
    If that vertex is the same as the ending vertex - we are done!
    Otherwise loop through each value in the adjacency list at that vertex
        Calculate the distance to that vertex from the starting vertex
        if the distance is less than what is currently stored in our distances object
            update the distances object with new lower distance
            update the previous object to contain that vertex
            enqueue the vertex with the total distance from the start node



Graph Connections:
A: [B(4), C(2)]
B: [A(4), E(3)]
C: [A(2), D(2), F(4)]
D: [C(2), E(3), F(1)]
E: [B(3), D(3), F(1)]
F: [C(4), D(1), E(1)]

Distance:
vertext | Shortest Dist From A
-----------------------------
   A   | 0
   B   | inf   
   C   | inf   
   D   | inf   
   E   | inf   
   F   | inf   

Previous:
{
    A: null,
    B: null,
    C: null,
    D: null,
    E: null,
    F: null
}
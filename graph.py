# graph.py
# From Classic Computer Science Problems in Python Chapter 4
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TypeVar, Generic, List, Optional
from edge import Edge


V = TypeVar('V') # type of the vertices in the graph


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices) # Number of vertices

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges)) # Number of edges

    # Add a vertex to the graph and return its index
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([]) # add empty list for containing edges
        return self.vertex_count - 1 # return index of added vertex

    # This is an undirected graph,
    # so we always add edges in both directions
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # Add an edge using vertex indices (convenience method)
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    # Add an edge by looking up vertex indices (convenience method)
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # Find the vertex at a specific index
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    # Find the index of a vertex in the graph
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    # Find the vertices that a vertex at some index is connected to
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # Lookup a vertice's index and find its neighbors (convenience method)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    # Return all of the edges associated with a vertex at some index
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    # Lookup the index of a vertex and return its edges (convenience method)
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    # Make it easy to pretty-print a Graph
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc


if __name__ == "__main__":
    # test basic Graph construction
    city_graph: Graph[str] = Graph(["Mombasa", "Voi", "Emali", "Mlolongo", "Athiriver", "Nairobi", "Nakuru", "Eldoret", "Kitale", "Webuye", "Amagoro", "Malaba", "Molo", "Mandera", "Embu"])
    city_graph.add_edge_by_vertices("Mombasa", "Nairobi")
    city_graph.add_edge_by_vertices("Mombasa", "Voi")
    city_graph.add_edge_by_vertices("Voi", "Mlolongo")
    city_graph.add_edge_by_vertices("Voi", "Emali")
    city_graph.add_edge_by_vertices("Emali", "Mlolongo")
    city_graph.add_edge_by_vertices("Emali", "Athiriver")
    city_graph.add_edge_by_vertices("Mlolongo", "Athiriver")
    city_graph.add_edge_by_vertices("Mlolongo", "Nairobi")
    city_graph.add_edge_by_vertices("Athiriver", "Amagoro")
    city_graph.add_edge_by_vertices("Athiriver", "Malaba")
    city_graph.add_edge_by_vertices("Amagoro", "Nairobi")
    city_graph.add_edge_by_vertices("Amagoro", "Kitale")
    city_graph.add_edge_by_vertices("Amagoro", "Malaba")
    city_graph.add_edge_by_vertices("Malaba", "Kitale")
    city_graph.add_edge_by_vertices("Malaba", "Webuye")
    city_graph.add_edge_by_vertices("Kitale", "Nairobi")
    city_graph.add_edge_by_vertices("Kitale", "Embu")
    city_graph.add_edge_by_vertices("Kitale", "Webuye")
    city_graph.add_edge_by_vertices("Webuye", "Embu")
    city_graph.add_edge_by_vertices("Nairobi", "Molo")
    city_graph.add_edge_by_vertices("Molo", "Nakuru")
    city_graph.add_edge_by_vertices("Molo", "Embu")
    city_graph.add_edge_by_vertices("Molo", "Eldoret")
    city_graph.add_edge_by_vertices("Nakuru", "Eldoret")
    city_graph.add_edge_by_vertices("Eldoret", "Mandera")
    city_graph.add_edge_by_vertices("Mandera", "Embu")
    print(city_graph)

    # Reuse BFS from Chapter 2 on city_graph
    import sys
    sys.path.insert(0, '..') # so we can access the Chapter2 package in the parent directory
    from Chapter2.generic_search import bfs, Node, node_to_path

    bfs_result: Optional[Node[V]] = bfs("Boston", lambda x: x == "Miami", city_graph.neighbors_for_vertex)
    if bfs_result is None:
        print("No solution found using breadth-first search!")
    else:
        path: List[V] = node_to_path(bfs_result)
        print("Path from Boston to Miami:")
        print(path)


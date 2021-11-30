# weighted_graph.py
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
from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('V') # type of the vertices in the graph


class WeightedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]

    def add_edge_by_indices(self, u: int, v: int, weight: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge) # call superclass version

    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
        return desc


if __name__ == "__main__":
    city_graph2: WeightedGraph[str] = WeightedGraph(["Mombasa", "Voi", "Emali", "Mlolongo", "Athiriver", "Nairobi", "Nakuru", "Eldoret", "Kitale", "Webuye", "Amagoro", "Malaba", "Molo", "Mandera", "Embu"])

    city_graph2.add_edge_by_vertices("Mombasa", "Nairobi", 1737)
    city_graph2.add_edge_by_vertices("Mombasa", "Voi", 678)
    city_graph2.add_edge_by_vertices("Voi", "Mlolongo", 386)
    city_graph2.add_edge_by_vertices("Voi", "Emali", 348)
    city_graph2.add_edge_by_vertices("Emali", "Mlolongo", 50)
    city_graph2.add_edge_by_vertices("Emali", "Athiriver", 357)
    city_graph2.add_edge_by_vertices("Mlolongo", "Athiriver", 307)
    city_graph2.add_edge_by_vertices("Mlolongo", "Nairobi", 1704)
    city_graph2.add_edge_by_vertices("Athiriver", "Amagoro", 887)
    city_graph2.add_edge_by_vertices("Athiriver", "Malaba", 1015)
    city_graph2.add_edge_by_vertices("Amagoro", "Nairobi", 805)
    city_graph2.add_edge_by_vertices("Amagoro", "Kitale", 721)
    city_graph2.add_edge_by_vertices("Amagoro", "Malaba", 225)
    city_graph2.add_edge_by_vertices("Malaba", "Kitale", 702)
    city_graph2.add_edge_by_vertices("Malaba", "Webuye", 968)
    city_graph2.add_edge_by_vertices("Kitale", "Nairobi", 588)
    city_graph2.add_edge_by_vertices("Kitale", "Embu", 543)
    city_graph2.add_edge_by_vertices("Kitale", "Webuye", 604)
    city_graph2.add_edge_by_vertices("Webuye", "Embu", 923)
    city_graph2.add_edge_by_vertices("Nairobi", "Molo", 238)
    city_graph2.add_edge_by_vertices("Molo", "Nakuru", 613)
    city_graph2.add_edge_by_vertices("Molo", "Embu", 396)
    city_graph2.add_edge_by_vertices("Molo", "Eldoret", 482)
    city_graph2.add_edge_by_vertices("Nakuru", "Eldoret", 190)
    city_graph2.add_edge_by_vertices("Eldoret", "Mandera", 81)
    city_graph2.add_edge_by_vertices("Mandera", "Embu", 123)

    print(city_graph2)

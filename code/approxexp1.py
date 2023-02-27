from experiment1 import create_random_graph, add_random_edge
from graph import approx1, approx2, approx3, MVC, is_connected, Graph
from plotting import PlotGroup
import matplotlib.pyplot as plot
import copy
import random

GRAPH_LIMIT = 1000
NODE_LIMIT = 25
EDGE_LIMIT = 196


def generate_random_tree(n):
    graph = Graph(n)

    if n == 1:
        return graph

    root = random.randint(0, n-1)
    unvisited = [i for i in range(n) if i != root]
    visited = set([root])

    while unvisited:
        node = random.choice(unvisited)
        parent = random.choice(list(visited))
        graph.add_edge(node, parent)
        unvisited.remove(node)
        visited.add(node)

    return graph


def approximation_performance_by_node_tests():
    approx1_performance = PlotGroup("Approximation 1", "#359cff")
    approx2_performance = PlotGroup("Approximation 2", "#b4daff")
    approx3_performance = PlotGroup("Approximation 3", "#d4b4ff")
    mvc_performance = PlotGroup("MVC", "#ff4d4d")
    for nodes in range(1, NODE_LIMIT):
        print(f"Running Tests for {nodes} nodes")
        sum1, sum2, sum3 = 0, 0, 0
        G = create_random_graph(nodes, int(nodes * (nodes - 1) / 2))
        mvcsum = len(MVC(G)) * GRAPH_LIMIT
        for trial in range(GRAPH_LIMIT):
            print(f"Running Trial {trial} for {nodes} nodes")
            G1 = copy.deepcopy(G)
            G2 = copy.deepcopy(G)
            G3 = copy.deepcopy(G)
            G4 = copy.deepcopy(G)
            sum1 += len(approx1(G1))
            sum2 += len(approx2(G2))
            sum3 += len(approx3(G3))
        if mvcsum == 0:
            mvcsum = 1
            sum1 = 1
            sum2 = 1
            sum3 = 1
        approx1_performance.add_point(nodes, sum1 / mvcsum)
        approx2_performance.add_point(nodes, sum2 / mvcsum)
        approx3_performance.add_point(nodes, sum3 / mvcsum)
        mvc_performance.add_point(nodes, 1)

    name = "Performance of Approximations vs. MVC for Random Graphs with Node Count 1 to 20"
    plot.title(name)
    plot.xlabel("Node Count")
    plot.ylabel("Approximation / MVC")

    approx1_performance.plot()
    approx2_performance.plot()
    approx3_performance.plot()
    mvc_performance.plot()

    plot.legend()
    plot.show()


def approximation_performance_by_edges_tests():
    approx1_performance = PlotGroup("Approximation 1", "#359cff")
    approx2_performance = PlotGroup("Approximation 2", "#b4daff")
    approx3_performance = PlotGroup("Approximation 3", "#d4b4ff")
    mvc_performance = PlotGroup("MVC", "#ff4d4d")
    for edges in range(1, EDGE_LIMIT, 5):
        sum1, sum2, sum3 = 0, 0, 0
        G = create_random_graph(NODE_LIMIT, edges + 10)
        mvcsum = len(MVC(G)) * GRAPH_LIMIT
        for trial in range(GRAPH_LIMIT):
            print(f"Running Trial {trial} for {edges} edges")
            G1 = copy.deepcopy(G)
            G2 = copy.deepcopy(G)
            G3 = copy.deepcopy(G)
            G4 = copy.deepcopy(G)
            sum1 += len(approx1(G1))
            sum2 += len(approx2(G2))
            sum3 += len(approx3(G3))

        approx1_performance.add_point(edges, sum1 / mvcsum)
        approx2_performance.add_point(edges, sum2 / mvcsum)
        approx3_performance.add_point(edges, sum3 / mvcsum)
        mvc_performance.add_point(edges, 1)

    name = "Performance of Approximations vs. MVC for Random Graphs with Node Count 20 and Edge Count 1 to 200"
    plot.title(name)
    plot.xlabel("Edge Count")
    plot.ylabel("Approximation / MVC")

    approx1_performance.plot()
    approx2_performance.plot()
    approx3_performance.plot()
    mvc_performance.plot()

    plot.legend()
    plot.show()


def approximation_performance_by_trees(nodes):
    approx1_performance = PlotGroup("Approximation 1", "#359cff")
    approx2_performance = PlotGroup("Approximation 2", "#b4daff")
    approx3_performance = PlotGroup("Approximation 3", "#d4b4ff")
    mvc_performance = PlotGroup("MVC", "#ff4d4d")
    for nodes in range(1, nodes):
        sum1, sum2, sum3 = 0, 0, 0
        G = generate_random_tree(nodes + 1)
        mvcsum = len(MVC(G)) * GRAPH_LIMIT
        for trial in range(GRAPH_LIMIT):
            print(f"Running Trial {trial} for {nodes} nodes")
            G1 = copy.deepcopy(G)
            G2 = copy.deepcopy(G)
            G3 = copy.deepcopy(G)
            G4 = copy.deepcopy(G)
            sum1 += len(approx1(G1))
            sum2 += len(approx2(G2))
            sum3 += len(approx3(G3))

        if mvcsum == 0:
            mvcsum = 1
            sum1 = 1
            sum2 = 1
            sum3 = 1

        approx1_performance.add_point(nodes, sum1 / mvcsum)
        approx2_performance.add_point(nodes, sum2 / mvcsum)
        approx3_performance.add_point(nodes, sum3 / mvcsum)
        mvc_performance.add_point(nodes, 1)

    name = "Performance of Approximations vs. MVC for Random Trees with Node Count 1 to 20"
    plot.title(name)
    plot.xlabel("Node Count")
    plot.ylabel("Approximation / MVC")

    approx1_performance.plot()
    approx2_performance.plot()
    approx3_performance.plot()
    mvc_performance.plot()

    plot.legend()
    plot.show()


if __name__ == "__main__":
    # approximation_performance_by_edges_tests()
    approximation_performance_by_node_tests()
    # approximation_performance_by_trees(23)

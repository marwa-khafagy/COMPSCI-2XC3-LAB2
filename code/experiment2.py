
from graph import is_connected, Graph
from plotting import PlotGroup
import matplotlib.pyplot as plot
import random

from experiment1 import create_random_graph

#
def proportionality_test(const_node_count, max_edge_count, trial_count, skip_count = 1):
    
    #Plot
    amount = PlotGroup("Average Number of Cyclical Graphs")
    amount.placelineAtFirstY1 = True

    #How many Edges to create? (X axis)
    for e in range(0, max_edge_count, skip_count):

        cyclicalGraphCount = 0

        # Generate X Graphs
        for _ in range(trial_count):

            #Generate Random Graph
            sampleGraph = create_random_graph(const_node_count, e);

            #Increment Count
            if is_connected(sampleGraph):
                cyclicalGraphCount += 1

        #Get Proportion
        cyclicalAverageCount = cyclicalGraphCount / trial_count
        amount.add_point(e, cyclicalAverageCount)

        print(f"Plotted Point ({e},{cyclicalAverageCount}). ({e}/{max_edge_count})")

    # Plot Here
    name = f"Percentage of Cyclical Graphs out of {trial_count} Graphs with Node Count {const_node_count}"
    plot.title(name)

    plot.xlabel("Random Graph Edge Count")
    plot.ylabel("Percentage of Cyclical Graphs")

    amount.plot()

    plot.legend()
    plot.show()

#
def max_proportionality_test(const_node_count, trial_count):

    edgeCount = int((const_node_count*(const_node_count + 1)) / 2)
    proportionality_test(const_node_count, edgeCount, trial_count)

#
# TESTS
#

if (__name__ == "__main__"):

    # Proportionality For small(ish) graphs
    # test1 = max_proportionality_test(5, 1000) # Edges = 15
    # test2 = max_proportionality_test(10, 1000) # edges = 55
    # test3 = proportionality_test(30, 250, 1000) #instead of 465

    #At this point the amount of possible graphs become crazy
    test4 = proportionality_test(1000, 1000, 100, 50)

    test5 = proportionality_test(1000, 10000, 100, 100)
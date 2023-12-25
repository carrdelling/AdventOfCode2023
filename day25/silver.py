from itertools import combinations
import matplotlib.pyplot as plt
import networkx as nx


def get_connected(subgraph, start):

    reverse = {}
    for k, v in subgraph.items():
        for vv in v:
            if vv not in reverse:
                reverse[vv] = set()
            reverse[vv].add(k)

    visited = set()
    states = [start]

    while states:
        current = states.pop()
        visited.add(current)
        for dest in subgraph.get(current, []):
            if dest not in visited:
                states.append(dest)
        for dest in reverse.get(current, []):
            if dest not in visited:
                states.append(dest)

    return visited


def plot_graph(graph):

    G = nx.Graph()
    for k, v in graph.items():
        for vv in v:
            G.add_edge(k, vv)

    # Uncomment the following two lines to see what edges are to be removed
    nx.draw(G, with_labels=True)
    plt.show()


def solve(data):

    graph = {}
    seen = set()
    all_nodes = set()

    as_list = []
    for row in data:
        h, l = row.split(': ')
        all_nodes.add(h)

        graph[h] = l.split(' ')
        seen |= set(l.split(' '))
        for p in l.split(' '):
            as_list.append((h, p))
            all_nodes.add(p)

    for n in seen:
        if n not in graph:
            graph[n] = []

    # plot the graph
    PLOT = False
    if PLOT:
        plot_graph(graph)
        return "Disable plot to calculate solution"
    else:
        # from the plot we can manually see three weak links in the middle
        # pzc <-> vps
        # cvx <-> dph
        # sgc <-> xvk

        # remove them
        def _remove(graph, src, dst):
            if src in graph:
                graph[src] = [x for x in graph[src] if x != dst]

        for a, b in [('pzc', 'vps'), ('cvx', 'dph'), ('sgc', 'xvk')]:
            _remove(graph, a, b)
            _remove(graph, b, a)

        g1 = get_connected(graph, 'pzc')
        g2 = get_connected(graph, 'vps')

        assert len(g1) + len(g2) == len(all_nodes)

        solution = len(g1) * len(g2)

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row.strip()
            input_.append(v)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()



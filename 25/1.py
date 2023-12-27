import networkx

G = networkx.Graph()
with open('input.txt') as data:
    for line in data:
        component, others = line.split(': ')
        for other in others.split():
            G.add_edge(component, other)

cuts, (side1, side2) = networkx.algorithms.connectivity.stoerwagner.stoer_wagner(G)
assert cuts == 3
print(len(side1) * len(side2))

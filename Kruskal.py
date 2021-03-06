from AdaptableHeapPriorityQueue import HeapPriorityQueue
from Partition import Partition


def MST_Kruskal(g):

    tree = []
    pq = HeapPriorityQueue()
    forest = Partition()
    position = {}

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)

    size = g.vertex_count()

    while len(tree) != size - 1 and not pq.is_empty():
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])

        if a != b:
            tree.append(edge)
            forest.union(a, b)

    return tree



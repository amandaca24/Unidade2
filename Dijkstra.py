from AdaptableHeapPriorityQueue import AdaptableHeapPriorityQueue


def SPL_Dijkstra(g, src):
    d = {}
    cloud = {}
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')

        pqlocator[v] = pq.add(d[v], v)

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key
        del pqlocator[u]

        for e in g.incident_edges(u):
            v = e.opposite

            if v not in cloud:
                wgt = e.element()

                if d[u] + wgt < d[v]:
                    d[v] = wgt + d[u]
                    pq.update(pqlocator[v], d[v], v)

    return cloud

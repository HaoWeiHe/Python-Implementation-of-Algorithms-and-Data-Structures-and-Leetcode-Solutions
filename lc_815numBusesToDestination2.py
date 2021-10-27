class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
         [[1,2,7],[3,6,7]],
        1 
        6
        {stop: [group_id1, group_id2,..]}
        {1:[0], 7:[0,
        stop   num_tran color_visted
        1     |   0    |   {}
        2,7   |   1    |    {0}
        7      | 1,3,6



        """
        g = defaultdict(set)
        for stop, lst in enumerate(routes):
            for e in lst:
                g[e].add(stop)

        group_visited, stop_visited = set(), set()

        q = deque([(source,0)])
        while q:
            cur, lvl = q.popleft()
            if cur == target:
                return lvl

            for bus in g[cur]:
                if bus in group_visited:
                    continue
                for stop in routes[bus]:
                    if stop in stop_visited:
                        continue
                    if stop == target:
                        return lvl +1 if bus not in group_visited else lvl 
                    stop_visited.add(stop)
                    q.append((stop, lvl +1 if bus not in group_visited else lvl ))
                group_visited.add(bus)

        return -1
        
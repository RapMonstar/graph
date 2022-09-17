graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}


class Graph:

    def StartOfTheCrawl(self, visited, graph, node):
        pass

    def EndOfTheTour(self):
        pass

    def VisitNodeV(self, visited, graph, node, vnode):
        pass

    def VisitRibE(self, fnode, snode):
        pass

    def start(self):
        self.StartOfTheCrawl(visited, graph, 'A')
        self.EndOfTheTour()
        self.VisitNodeV(visited, graph, 'A', 'A')
        self.VisitRibE('A', 'B')


visited = []
queue = []
a1 = []


class BFS(Graph):

    def StartOfTheCrawl(self, visited, graph, node):
        print('Начальный элемент', node)
        visited.append(node)
        queue.append(node)

        while queue:
            m = queue.pop(0)
            a1.append(m)
            print(m, end=" ")

            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    def EndOfTheTour(self):
        print('Последний элемент', a1[-1])

    def VisitNodeV(self, visited, graph, node, vnode):

        visited = []
        queue = []
        visited.append(node)
        queue.append(node)
        s = 1
        # print('Начальный элемент', node)
        while queue:
            m = queue.pop(0)
            # print(m, end=" ")

            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        for i in visited:
            if i == vnode:
                print(vnode, 'На значении', s)
            else:
                s += 1

    def VisitRibE(self, fnode, snode):
        s = 0
        s1 = 0
        for i in a1:
            if i == fnode:
                s = a1.index(i)
            if i == snode:
                s1 = a1.index(i)
        print('Ребро между', fnode, snode, 'под индексом', s1 - s)


a2 = []


class DFS(Graph):
    def StartOfTheCrawl(self, visited, graph, node):
        visited = set()
        print('Начальный элемент', node)

        def dfs(visited, graph, node):
            if node not in visited:
                print(node)
                a2.append(node)
                visited.add(node)
                for neighbour in graph[node]:
                    dfs(visited, graph, neighbour)

        dfs(visited, graph, node)

    def EndOfTheTour(self):
        print('Последний элемент', a2[-1])

    def VisitNodeV(self, visited, graph, node, vnode):
        visited = set()

        def dfs(visited, graph, node):
            if node not in visited:
                # print(node)
                s = 1
                if node == vnode:
                    print(node, 'На значении', s)
                else:
                    s += 1
                a2.append(node)
                visited.add(node)
                for neighbour in graph[node]:
                    dfs(visited, graph, neighbour)

        dfs(visited, graph, node)

    def VisitRibE(self, fnode, snode):
        s = 0
        s1 = 0
        for i in a2:
            if i == fnode:
                s = a2.index(i)
            if i == snode:
                s1 = a2.index(i)
        print('Ребро между', fnode, snode, 'под индексом', s1 - s)


if __name__ == '__main__':
    print('BFS:')
    bfs = BFS()
    bfs.start()
    print()
    print('DFS:')
    dfs = DFS()
    dfs.start()
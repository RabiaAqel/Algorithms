from collections import deque
import pytest


def bfs(graph, start):
    def bfs_util(visited, queue):

        while queue:
            vertex = queue.pop()
            for node in graph[vertex]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        return visited

    return bfs_util(set([start]), deque([start]))


def test_bfs():
    graph = {
        'A': ['B', 'S'],
        'B': ['A'],
        'C': ['D', 'E', 'F', 'S'],
        'D': ['C'],
        'E': ['C', 'H'],
        'F': ['C', 'G'],
        'G': ['F', 'S'],
        'H': ['E', 'G'],
        'S': ['A', 'C', 'G']
    }
    print(bfs(graph, 'A'))

    assert bfs(graph, 'A') == {'A', 'B', 'S', 'C', 'D', 'E', 'H', 'G', 'F'}


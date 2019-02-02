from typing import Dict
import pytest


def dfs(graph: Dict, start: chr):
    def dfs_util(node, visited):
        if node not in visited:
            visited.add(node)

            for node in graph[node]:
                dfs_util(node, visited)
        return visited

    return dfs_util(start, set())


def test_dfs():
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
    print(dfs(graph, 'A'))

    assert dfs(graph, 'A') == {'A', 'B', 'S', 'C', 'D', 'E', 'H', 'G', 'F'}


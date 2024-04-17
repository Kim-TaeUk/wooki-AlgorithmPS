"""
input
5
7
3 1
2 3
4 1
5 2
5 4
3 5
2 4
"""
import sys

V = int(sys.stdin.readline().rstrip())  # vertex (정점)
E = int(sys.stdin.readline().rstrip())  # edge (간선)
adjacent_matrix = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, sys.stdin.readline().split())
    adjacent_matrix[start][end] = 1

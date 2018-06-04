import unittest
from graph import graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graphObj = graph.Graph()
        for i in range(10):
            self.graphObj.add_vertex(i)

        for i in range(9):
            self.graphObj.add_edge(i, i + 1)

    def test_add_vertices_and_edges(self):
        self.assertEqual(self.graphObj.get_vertices(), [i for i in range(10)])
        self.assertEqual(self.graphObj.get_edges(), [
                         {i, i + 1} for i in range(9)])

    def test_bfs(self):
        self.assertTrue(self.graphObj.bfs(5))
        self.assertFalse(self.graphObj.bfs(100))

    def test_dfs(self):
        self.assertTrue(self.graphObj.dfs(5))
        self.assertFalse(self.graphObj.dfs(100))

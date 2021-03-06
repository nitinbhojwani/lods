def test():
    import unittest
    from avl_tree.test_avl_tree import TestAvlTree
    from binary_search_tree.test_binary_search_tree import TestBinarySearchTree
    from binary_tree.test_binary_tree import TestBinaryTree
    from doubly_linked_list.test_doubly_linked_list import TestDoublyLinkedList
    from graph.test_graph import TestGraph
    from linked_list.test_linked_list import TestLinkedList
    from max_heap.test_max_heap import TestMaxHeap
    from min_heap.test_min_heap import TestMinHeap
    from pyqueue.test_queue import TestQueue
    from stack.test_stack import TestStack
    from trie.test_trie import TestTrie

    test_cases = [
        TestAvlTree,
        TestBinarySearchTree,
        TestBinaryTree,
        TestDoublyLinkedList,
        TestGraph,
        TestLinkedList,
        TestMaxHeap,
        TestMinHeap,
        TestQueue,
        TestStack,
        TestTrie
    ]

    suites = [unittest.defaultTestLoader.loadTestsFromTestCase(
        test_case) for test_case in test_cases]
    all_tests_suite = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner()
    runner.run(all_tests_suite)


test()

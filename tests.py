def test():
    import unittest
    from graph.test_graph import TestGraph
    from pyqueue.test_queue import TestQueue
    from stack.test_stack import TestStack

    test_cases = [
        TestGraph,
        TestQueue,
        TestStack
    ]

    suites = [unittest.defaultTestLoader.loadTestsFromTestCase(
        test_case) for test_case in test_cases]
    all_tests_suite = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner()
    runner.run(all_tests_suite)


test()
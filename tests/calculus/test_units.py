# Python code to unittest the methods and agents
import unittest 
import os

import nbimporter
import notebooks.bqplot as eg

class TestAgent(unittest.TestCase): 

    def setUp(self): 
        print("Initialised unit test")

    def test_chain_rule(self):
        self.assertAlmostEqual(eg.get_change_rate(10),699,0)
        self.assertEqual(eg.cal_units().units,'pascal / second')

if __name__ == '__main__':
    main = TestAgent()

    # This executes the unit test/(itself)
    import sys
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAgent)
    unittest.TextTestRunner(verbosity=4,stream=sys.stderr).run(suite)
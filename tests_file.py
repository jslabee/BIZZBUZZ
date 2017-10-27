

class TestSumab(unittest.TestCase):
    def testing_numbers_sum():
        self.assertEqual(sum_sum(2, 3), 1)

    def test_generate_list(self):
        new_list = generate_list(1, 4, 6, 10)
        self.assIsInstance(new_list, int)
        self.assertIn(4, new_list)
        self.assertisnot(newlist, none)
        self.assertgreter(len(new_list), 0)

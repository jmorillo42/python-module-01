import sys
import unittest
from io import StringIO

from game import Stark


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.arya = Stark("Arya")

    def test_dict(self):
        self.assertEqual(self.arya.__dict__, {'first_name': 'Arya', 'is_alive': True, 'family_name': 'Stark',
                                              'house_words': 'Winter is Coming'})
        print(self.arya.__dict__)

    def test_print_house_words(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.arya.print_house_words()
            output = out.getvalue().strip()
            self.assertEqual(output, 'Winter is Coming')
        finally:
            sys.stdout = saved_stdout

    def test_is_alive(self):
        self.assertEqual(self.arya.is_alive, True)
        print(f'Arya is alive? {self.arya.is_alive}')

    def test_die(self):
        self.arya.die()
        self.assertEqual(self.arya.is_alive, False)
        print(f'Arya is alive? {self.arya.is_alive}')


if __name__ == '__main__':
    unittest.main()

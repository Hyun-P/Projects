import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def test_string_cleaner(self):
        self.assertEqual(challenge.id_cleaner("1=.&^%uif381"), '1381')
        self.assertEqual(challenge.id_cleaner("8 2.qerf3dsgf 5"), '8235')
        self.assertEqual(challenge.id_cleaner("3-=_+=--_~``4  3 4"), '3434')
        self.assertEqual(challenge.id_cleaner("7/?.F>,<=+-_)(&*(^&$623"), '7623')

        # check the datatype
        self.assertIsInstance(challenge.id_cleaner("7/?.F>,<=+-_)(&*(^&$623"), str)

    def test_duplicate_remover(self):
        self.assertEqual(challenge.duplicate_remover([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(challenge.duplicate_remover([1, 3, 3, 2]), [1, 3, 2])
        self.assertEqual(challenge.duplicate_remover(['a', 'b', 'b', 'c']), ['a', 'b', 'c'])
        self.assertEqual(challenge.duplicate_remover(['a', 'c', 'c', 'b']), ['a', 'c', 'b'])

        # check the datatype
        self.assertIsInstance(challenge.duplicate_remover([1, 2, 2, 3]), list)
        self.assertIsInstance(challenge.duplicate_remover([1, 2, 2, 3])[0], int)
        self.assertIsInstance(challenge.duplicate_remover(['1', '2', '2', '3'])[0], str)
        self.assertIsInstance(challenge.duplicate_remover([1.0, 2.0, 2.0, 3.0])[0], float)


if __name__ == '__main__':
    unittest.main()

__author__ = 'cashsun'

import unittest

class StringPlay(unittest.TestCase):
    """Test driven string playground"""

    def testStringAttributes(self):
        self.assertEqual(len("random"), 6)

    def testStringSplit(self):
        self.assertEqual('random words'.split(' '), ['random', 'words'])

    def testStringSlice(self):
        self.assertEqual('random'[2:], 'ndom')
        self.assertEqual('random'[:5], 'rando')
        self.assertEqual('random'[2:5], 'ndo')

    def testCapitalize(self):
        fullname = ', '.join(map(str.capitalize, 'cash sun'.split(' ')))
        self.assertEqual(fullname, 'Cash, Sun')

__author__ = 'cashsun'

import unittest


class DictAndArray(unittest.TestCase):

    def testDictBasic(self):
        myDict = {
            'a': 'cash',
            'b': 'Sun'
        }

        self.assertEqual(myDict['a'], 'cash')
        self.assertEqual(myDict['b'], 'Sun')

    def testDictConstruct(self):
        citiesAndTemps = [('Wenzhou', -5), ('London', 5), ('Shanghai', 10)]
        d = dict(citiesAndTemps)

        self.assertEqual(d['Wenzhou'], -5)
        self.assertEqual(d['London'], 5)
        self.assertEqual(d['Shanghai'], 10)
        with self.assertRaises(KeyError):
            return d['Hangzhou']

    def testDictConstruct2(self):
        d = dict(a='cash', b='sun')
        self.assertEqual(d['a'], 'cash')
        self.assertEqual(d['b'], 'sun')

    def testUpdate(self):
        d = dict(a='cash', b='sun')
        d.update(a='money')
        self.assertEqual(d['a'], 'money')
        self.assertEqual(d['b'], 'sun')

    def testIteration(self):
        d = dict(a='cash', b='sun')
        for key, val in d.items():
            print('{}:{}'.format(key, val))

        self.assertTrue('a' in d)
        self.assertTrue('b' in d)

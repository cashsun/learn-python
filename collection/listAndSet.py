__author__ = 'cashsun'

import unittest


class ListTest(unittest.TestCase):
    def testListBasic(self):
        myList = [11, 22, 33, 55, '6']

        self.assertEqual(myList[0], 11)
        self.assertEqual(myList[1], 22)
        self.assertEqual(myList[2], 33)
        self.assertEqual(myList[3], 55)
        self.assertEqual(myList[4], '6')

        self.assertEqual(myList[-1], '6')
        self.assertEqual(myList[-3], 33)

    def testSlice(self):
        myList = [11, 22, 33, 55, '6']

        myCopy = myList[:]
        self.assertEqual(myList, myCopy)
        self.assertEqual(myList[:3], [11, 22, 33])

    def testRepetition(self):
        myList = [11, 22]
        myRep = myList * 2
        myList.append(33)
        self.assertEqual(myRep, [11, 22, 11, 22])
        self.assertEqual(myList, [11, 22, 33])

    def testModifyMethods(self):
        myList = ['cash', 'sun', 'cash', 'money']
        self.assertEqual(myList.index('cash'), 0)
        self.assertEqual(myList.count('cash'), 2)

        self.assertTrue('sun' in myList)

        myList.remove('cash')
        # only removes first matching one
        self.assertEqual(myList, ['sun', 'cash', 'money'])

        myList += ['coin']
        self.assertEqual(myList, ['sun', 'cash', 'money', 'coin'])

    def testSortMethods(self):
        myList = ['cash', 'sun', 'cash', 'money']
        myList.sort()
        self.assertEqual(myList, ['cash', 'cash', 'money', 'sun'])

import unittest
from router import route
class Tests(unittest.TestCase):
    def test_route(self):
        r=route([{"id":1,"text":"team meeting"}],{"work":["meeting"]})
        self.assertEqual(r["routes"][0]["category"],"work")
    def test_unmatched(self):
        self.assertEqual(route([{"text":"hello"}],{"work":["meeting"]})["routes"][0]["category"],"uncategorized")
    def test_frequency(self):
        r=route([{"text":"meeting meeting grocery"}],{"work":["meeting"],"home":["grocery"]})
        self.assertEqual(r["routes"][0]["category"],"work")
    def test_empty(self):
        self.assertEqual(route([],{})["total"],0)
    def test_bad_note(self):
        with self.assertRaises(ValueError): route(["text"],{})
if __name__=="__main__": unittest.main()

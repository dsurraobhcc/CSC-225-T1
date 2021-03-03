import unittest
from recently_used_list import RecentlyUsedList

class TestRecentlyUsedList(unittest.TestCase):
    
    def test_inserted(self):
        r = RecentlyUsedList()
        r.add_used_item('shoes')
        r.add_used_item('clothes')
        r.add_used_item('shoes')
        r.add_used_item('accessories')
        self.assertTrue(len(r.recently_used) > 0)

    def test_most_recent(self):
        #TODO: your code here to test get_recently_used_item()
        pass

    def test_duplicates(self):
        #TODO: your code here to test that duplicate insertions are moved rather than added.
        pass

if __name__ == '__main__':
    unittest.main()
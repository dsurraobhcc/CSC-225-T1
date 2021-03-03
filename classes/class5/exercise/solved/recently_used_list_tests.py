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
        r = RecentlyUsedList()
        r.add_used_item('shoes')
        r.add_used_item('clothes')
        r.add_used_item('shoes')
        r.add_used_item('accessories')
        self.assertEquals(r.get_recently_used_item(), 'accessories')

    def test_duplicates(self):
        r = RecentlyUsedList()
        r.add_used_item('shoes')
        r.add_used_item('clothes')
        r.add_used_item('shoes')
        r.add_used_item('accessories')
        self.assertEquals(len(r.recently_used), 3)

if __name__ == '__main__':
    unittest.main()
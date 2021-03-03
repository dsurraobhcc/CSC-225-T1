'''
Problem source: cyber-dojo.org

Develop a recently-used-list class to hold strings uniquely in 
Last-In-First-Out order.

o) A recently-used-list is initially empty.
o) The most recently added item is first, the least recently added item is last.
o) Items can be looked up by index, which counts from zero.
o) Items in the list are unique, so duplicate insertions are moved rather than added.
Optional extras
o) Null insertions (empty strings) are not allowed.
o) A bounded capacity can be specified at construction, so there is an upper 
limit to the number of items contained, with the least recently added items dropped on overflow.
'''

from collections import deque

class RecentlyUsedList():
    recently_used = deque([])

    def add_used_item(self, item):
        '''
        Record a used item
        '''
        if item in RecentlyUsedList.recently_used:
            RecentlyUsedList.recently_used.remove(item)
        RecentlyUsedList.recently_used.appendleft(item)

    def get_recently_used_item(self, index=0):
        '''
        Get the recently used item, optionally passing in an index
        '''
        return RecentlyUsedList.recently_used[index]

    def __str__(self):
        '''
        user friendly printout
        '''
        st = ''
        for i in range(len(RecentlyUsedList.recently_used)):
            st += RecentlyUsedList.recently_used[i]
            if i < len(RecentlyUsedList.recently_used) - 1:
                st += ', '
        return st


if __name__ == '__main__':
    r = RecentlyUsedList()
    r.add_used_item('shoes')
    r.add_used_item('clothes')
    r.add_used_item('shoes')
    r.add_used_item('accessories')

    print(r)
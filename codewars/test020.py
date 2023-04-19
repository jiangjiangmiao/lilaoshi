# For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.
#
# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.
#
# The following are some examples of how this class is used:
#
# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0)  # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid
#
# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid

class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.col_new = list(collection)
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        item_count = len(self.col_new)
        return item_count

    # returns the number of pages
    def page_count(self):
        page_count_remainder = len(self.col_new) % self.items_per_page
        page_count = len(self.col_new) / self.items_per_page
        if page_count_remainder == 0:
            return int(page_count)
        else:
            return int(page_count) + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        page_count = self.page_count()
        item_count = self.item_count()
        if page_index > page_count - 1:
            return -1
        if page_index < page_count - 1:
            page_item_count = (page_index + 1) * self.items_per_page
            return page_item_count
        else:
            page_item_count = item_count - page_index * self.items_per_page
            return page_item_count

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        item_count = self.item_count()
        item_index_new = item_index + 1
        if item_index_new > item_count:
            return -1
        if item_index_new % self.items_per_page == 0:
            return int(item_index_new / self.items_per_page) - 1
        else:
            return int(item_index_new / self.items_per_page)


collection = range(1, 25)
helper = PaginationHelper(collection, 10)
print(helper.item_count())
print(helper.page_count())
print(helper.page_item_count(1))
print(helper.page_index(23))
print(helper.item_count())

helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print(helper.page_count())  # should == 2
print(helper.item_count())  # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1))  # last page - should == 2
print(helper.page_item_count(2))  # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5))  # should == 1 (zero based index)
print(helper.page_index(2))  # should == 0
print(helper.page_index(20))  # should == -1
print(helper.page_index(-10))  # should == -1 because negative indexes are invalid

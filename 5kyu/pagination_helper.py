import math

class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        # returns the number of items within the entire collection
        return len(self.collection)

    def page_count(self):
        # returns the number of pages
        return math.ceil(float(self.item_count()) / self.items_per_page)

    def page_item_count(self, page_index):
        # returns the number of items on the current page. page_index is zero based
        # this method should return -1 for page_index values that are out of range
        page_index += 1
        if page_index > self.page_count() or page_index < 0:
            return -1
        elif page_index != self.page_count():
            return self.items_per_page
        else:
            return self.item_count() % self.items_per_page

    def page_index(self, item_index):
        # determines what page an item is on. Zero based indexes.
        # this method should return -1 for item_index values that are out of range
        if item_index >= len(self.collection) or item_index < 0:
            return -1
        else:
            return item_index / self.items_per_page



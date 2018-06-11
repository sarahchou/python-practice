def take(count, iterable):
    """Take items from the front of an iterable.

    Args: 
        count: The maximum number of items to retrieve. 
        iterable: The source of the items. 

    Yields: 
        At most 'count' items from 'iterable'.
    """


    counter = 0
    for item in iterable: 
        if counter == count: 
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)

def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args: 
        iterable: The source of the items.

    Yields: 
        Unique elements in order from 'iterable'.
    """
    seen = set()
    for item in iterable: 
        if item in seen: 
            continue
        yield item
        seen.add(item)

def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)

# Fetch the first three unique items from a collection 
def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)




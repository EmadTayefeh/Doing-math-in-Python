'''
Creating a grouped frequency table
'''

def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)

    # Width of each class
    width = (high - low)/n
    classes = []
    a = low
    b = low + width
    classes = []
    while a < (high-width):
        classes.append((a, b))
        a = b
        b = a + width

    # The last class may be of a size that is less than width
    classes.append((a, high+1))
    return classes

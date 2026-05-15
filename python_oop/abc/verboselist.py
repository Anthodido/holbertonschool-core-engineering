#!/usr/bin/env python3

class VerboseList(list):

    """A list that prints the type of objects being added to it."""

    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, iterable):
        print("Extended the list with [{}] items.".format(len(iterable)))
        super().extend(iterable)

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

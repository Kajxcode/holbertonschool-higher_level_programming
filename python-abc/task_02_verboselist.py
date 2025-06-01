#!/usr/bin/python3
"""this module defines a class"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Appended {item!r} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended list with {len(iterable)} items: {list(iterable)!r}")

    def remove(self, item):
        super().remove(item)
        print(f"Removed {item!r} from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped {item!r} from index {index}.")
        return item

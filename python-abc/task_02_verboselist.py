#!/usr/bin/env python3
"""IS DOCUMENTED"""


class VerboseList(list):
    """IS DOCUMENTED"""
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item=-1):
        print(f"Popped [{self[item]}] from the list.")
        super().pop(item)

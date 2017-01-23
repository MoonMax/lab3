# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = list(items)
        self.max_size = len(self.items)
        self.index = 0
        self.set = set()
        try:
            self.ignore_case = kwargs['ignore_case']
        except:
            self.ignore_case = False

    def __next__(self):
        if self.index == self.max_size:
            raise StopIteration
        item = self.items[self.index]
        if self.ignore_case is True:
            item = item.lower()

        while item in self.set:
            self.index = self.index + 1
            if self.index == self.max_size:
                raise StopIteration
            item = self.items[self.index]
            if self.ignore_case is True:
                item = item.lower()

        self.set.add(item)
        return item

    def __iter__(self):
        return self
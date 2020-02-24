from copy import copy
from random import randint


class SortAndShuffle:
    def __init__(self):
        self.CUTOFF = 7

    @staticmethod
    def _exchange(data: list, i: int, j: int):
        temp = data[i]
        data[i] = data[j]
        data[j] = temp

    def knuth_shuffle(self, data: list):

        for i in range(len(data)):
            j = randint(0, len(data) - 1)
            self._exchange(data, i, j)

        return data

    def _insertion_sort(self, data: list, low: int, high: int):
        for i in range(low, high + 1):
            j = i

            while j > low:

                if data[j] < data[j-1]:
                    self._exchange(data, j, j-1)

                j -= 1

    def insertion_sort(self, data: list):
        self._insertion_sort(data, low=0, high=len(data) - 1)

    def shell_sort(self, data: list):
        h = 1

        while h < len(data) // 3:
            h = 3 * h + 1

        while h >= 1:

            for i in range(h, len(data)):
                j = i

                while (j >= h) and (data[j] < data[j-h]):
                    self._exchange(data, j, j-h)
                    j -= h

            h = h // 3

    @staticmethod
    def _merge(data: list, low: int, mid: int, high: int):
        temp_data = data[low: high+1]
        i = 0
        j = mid - low + 1

        for k in range(len(temp_data)):
            item_index = low + k

            if i > mid - low:
                data[item_index: high+1] = temp_data[j:]
                return
            elif j > high - low:
                data[item_index: high+1] = temp_data[i: mid - low + 1]
                return
            elif temp_data[i] < temp_data[j]:
                data[item_index] = temp_data[i]
                i += 1
            else:
                data[item_index] = temp_data[j]
                j += 1

    def _merge_sort(self, data: list, low: int, high: int):
        if high <= low:
            return

        if high - low <= self.CUTOFF:
            self._insertion_sort(data, low, high)
            return

        mid = low + (high - low) // 2
        self._merge_sort(data, low=low, high=mid)
        self._merge_sort(data, low=mid + 1, high=high)

        if data[mid] < data[mid + 1]:
            return

        self._merge(data, low=low, mid=mid, high=high)

    def merge_sort(self, data: list):
        self._merge_sort(data, 0, len(data) - 1)

    def merge_sort_bottom_up(self, data: list):
        size = 1

        while size < len(data):
            low = 0

            while low < len(data) - size:
                self._merge(data, low=low, mid=low + size - 1, high=min(low + size * 2 + 1, len(data) - 1))
                low += size * 2

            size *= 2

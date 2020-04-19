from random import randint


class SortAndShuffle:
    def __init__(self):
        self.CUTOFF_MERGE_SORT = 7
        self.CUTOFF_QUICK_SORT = 9

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

        if high - low <= self.CUTOFF_MERGE_SORT:
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
                self._merge(data, low=low, mid=low + size - 1, high=min(low + size * 2 - 1, len(data) - 1))
                low += size * 2

            size *= 2

    def _partitioning(self, data: list, low: int, high: int):
        key_item = data[low]
        i = low + 1
        j = high

        while True:

            while True:
                if data[i] > key_item:
                    break
                if i == high:
                    break
                i += 1

            while True:
                if data[j] < key_item:
                    break
                if j == low:
                    break
                j -= 1

            if i >= j:
                break

            self._exchange(data, i, j)

        self._exchange(data, low, j)
        return j

    def _quick_sort(self, data: list, low: int, high: int):
        if high <= low:
            return

        if high - low <= self.CUTOFF_QUICK_SORT:
            self._insertion_sort(data, low, high)
            return

        j = self._partitioning(data, low, high)
        self._quick_sort(data, low, j-1)
        self._quick_sort(data, j+1, high)

    def quick_sort(self, data: list):
        self.knuth_shuffle(data)  # shuffle needed for performance guarantee
        self._quick_sort(data, 0, len(data) - 1)

    def _three_way_quick_sort(self, data: list, low: int, high: int):
        if high <= low:
            return

        i, lt, gt = low, low, high
        key_item = data[low]

        while i <= gt:
            if data[i] < key_item:
                self._exchange(data, lt, i)
                i += 1
                lt += 1

            elif data[i] > key_item:
                self._exchange(data, i, gt)
                gt -= 1

            else:
                i += 1

        self._three_way_quick_sort(data, low, lt - 1)
        self._three_way_quick_sort(data, gt + 1, high)

    def three_way_quick_sort(self, data: list):
        self._three_way_quick_sort(data, 0, len(data) - 1)


if __name__ == '__main__':
    from copy import deepcopy

    from education_part.common import time_it


    def sort_scenario_1(a: int):
        """
        Make list of dimension 'a' shuffle it and then sort it using insertion sort algorithm.
        Print shuffled list and then sorted list.
        :param a: list dimension
        :return: None
        """
        worker = SortAndShuffle()
        b = worker.knuth_shuffle(list(range(a)))

        print('--- ' * 22)
        print(f'Sort with {worker.insertion_sort.__name__}')
        print(b)
        worker.insertion_sort(b)
        print(b)
        print('--- ' * 22)


    def sort_scenario_2(a: int):
        """
        Make list of dimension 'a' shuffle it and then sort it using shell sort algorithm.
        Print shuffled list and then sorted list.
        :param a: list dimension
        :return: None
        """
        worker = SortAndShuffle()
        b = worker.knuth_shuffle(list(range(a)))

        print('--- ' * 22)
        print(f'Sort with {worker.shell_sort.__name__}')
        print(b)
        worker.shell_sort(b)
        print(b)
        print('--- ' * 22)


    def sort_scenario_3(a: int):
        """
        Make list of dimension 'a' shuffle it and then sort it using merge sort algorithm.
        Print shuffled list and then sorted list.
        :param a: list dimension
        :return: None
        """
        worker = SortAndShuffle()
        b = worker.knuth_shuffle(list(range(a)))

        print('--- ' * 22)
        print(f'Sort with {worker.merge_sort.__name__}')
        print(b)
        worker.merge_sort(b)
        print(b)
        print('--- ' * 22)


    def sort_scenario_4(a: int):
        """
        Make list of dimension 'a' shuffle it and then sort it using merge sort algorithm.
        Print shuffled list and then sorted list.
        :param a: list dimension
        :return: None
        """
        worker = SortAndShuffle()
        b = worker.knuth_shuffle(list(range(a)))

        print('--- ' * 22)
        print(f'Sort with {worker.merge_sort_bottom_up.__name__}')
        print(b)
        worker.merge_sort_bottom_up(b)
        print(b)
        print('--- ' * 22)


    def sort_scenario_5(a: int):
        """
        Make list of dimension 'a' shuffle it and then sort it using quick sort algorithm.
        Print shuffled list and then sorted list.
        :param a: list dimension
        :return: None
        """
        worker = SortAndShuffle()
        b = worker.knuth_shuffle(list(range(a)))

        print('--- ' * 22)
        print(f'Sort with {worker.quick_sort.__name__}')
        print(b)
        worker.quick_sort(b)
        print(b)
        print('--- ' * 22)


    def sort_scenario_6(a: int):
        """
        Make list of dimension 'a' shuffle it and then sort it using 3-way quick sort algorithm.
        Print shuffled list and then sorted list.
        :param a: list dimension
        :return: None
        """
        worker = SortAndShuffle()
        b = worker.knuth_shuffle(list(range(a)))

        print('--- ' * 22)
        print(f'Sort with {worker.three_way_quick_sort.__name__}')
        print(b)
        worker.three_way_quick_sort(b)
        print(b)
        print('--- ' * 22)


    def sort_comparison():
        """
        Compare time of different methods for 3_000 unique keys and 100 repeated keys randomly repeated 3_000 times.
        """

        lists = [
            SortAndShuffle().knuth_shuffle(list(range(3_000))),
            [randint(1, 100) for _ in range(3_000)]
        ]
        funcs = [
            SortAndShuffle().insertion_sort,
            SortAndShuffle().shell_sort,
            SortAndShuffle().merge_sort,
            SortAndShuffle().merge_sort_bottom_up,
            SortAndShuffle().quick_sort,
            SortAndShuffle().three_way_quick_sort,
        ]

        print('Compare time of sort methods for 3000 unique keys and 100 unique keys randomly repeated 3000 times.')
        for list_to_sort in lists:
            print('--- ' * 22)
            for func in funcs:
                data = deepcopy(list_to_sort)
                time_it(func, data)
        print('--- ' * 22)


    sort_scenario_1(17)
    sort_scenario_2(17)
    sort_scenario_3(17)
    sort_scenario_4(17)
    sort_scenario_5(17)
    sort_scenario_6(17)
    sort_comparison()

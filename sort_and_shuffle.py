from random import randint


class SortAndShuffle:

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

        return data

    @staticmethod
    def _merge(data):
        low = 0
        high = len(data) - 1
        mid = len(data) // 2

        temp_data = []
        i, j = low, mid

        for k in range(len(data)):

            if i >= mid:
                temp_data += data[j:]
                return temp_data
            elif j > high:
                temp_data += data[i: mid]
                return temp_data
            elif data[i] < data[j]:
                temp_data.append(data[i])
                i += 1
            else:
                temp_data.append(data[j])
                j += 1

        return temp_data

    def merge_sort(self, data: list):
        length = len(data)

        if length <= 1:
            return data

        mid = length // 2
        left = self.merge_sort(data[:mid])
        right = self.merge_sort(data[mid:])
        return self._merge(left + right)

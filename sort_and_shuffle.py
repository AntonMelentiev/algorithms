from random import randint


class SortAndShuffle:

    @staticmethod
    def exchange(data: list, i: int, j: int):
        temp = data[i]
        data[i] = data[j]
        data[j] = temp

    def shell_sort(self, data: list):
        h = 1

        while h < len(data) // 3:
            h = 3 * h + 1

        while h >= 1:

            for i in range(h, len(data)):
                j = i

                while (j >= h) and (data[j] < data[j-h]):
                    self.exchange(data, j, j-h)
                    j -= h

            h = h // 3

        return data

    def knuth_shuffle(self, data: list):

        for i in range(len(data)):
            j = randint(0, len(data) - 1)
            self.exchange(data, i, j)

        return data


shell_sort = SortAndShuffle()
a = 1000
b = shell_sort.knuth_shuffle(list(range(a)))

print(b)
print(shell_sort.shell_sort(b))

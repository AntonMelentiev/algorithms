class KeyIndexSort:
    """
    Get a list of strings.
    Sort them in alphabetic sequence.
    """
    def __init__(self, arr):
        self.arr = arr

        self.unique_first_letters_count = {}
        for string in self.arr:
            if string[0] not in self.unique_first_letters_count:
                self.unique_first_letters_count[string[0]] = 1
            else:
                self.unique_first_letters_count[string[0]] += 1

        self.unique_first_letters_offset = {}
        previous_letter = None
        for letter in sorted(self.unique_first_letters_count.keys()):
            previous_offset = self.unique_first_letters_offset.get(previous_letter, 0)
            previous_letter_count = self.unique_first_letters_count.get(previous_letter, 0)
            self.unique_first_letters_offset[letter] = previous_offset + previous_letter_count
            previous_letter = letter

        self.aux = [None for _ in range(len(self.arr))]
        for i in range(len(self.arr)):
            first_letter = self.arr[i][0]
            self.aux[self.unique_first_letters_offset[first_letter]] = self.arr[i]
            self.unique_first_letters_offset[first_letter] += 1

        for i in range(len(self.arr)):
            self.arr[i] = self.aux[i]


if __name__ == '__main__':
    import random
    import string
    from copy import deepcopy

    from education_part.common import time_it

    new_arr = ['foo', 'bar', 'test', 'alpha', 'best', 'floor', 'feed']
    KeyIndexSort(new_arr)
    print(new_arr)

    print('\n' + '--- ' * 22)
    print('Compare time of sort methods for 3000 unique keys and 100 unique keys randomly repeated 3000 times.')
    letters = string.ascii_lowercase
    string_length = 5

    unique_items = []
    for _ in range(3000):
        unique_items.append(''.join(random.choice(letters) for i in range(string_length)))

    repeated_items = []
    items_to_repeat = []
    for _ in range(100):
        items_to_repeat.append(''.join(random.choice(letters) for i in range(string_length)))
    for _ in range(3000):
        repeated_items.append(random.choice(items_to_repeat))

    lists = {
        'Unique items': unique_items,
        'Repeated items': repeated_items,
    }
    funcs = [KeyIndexSort]

    for list_to_sort in lists:
        print('--- ' * 22)
        print(list_to_sort + ':')
        for func in funcs:
            data = deepcopy(lists[list_to_sort])
            time_it(func, data, check_sort=False, check_alphabetic=True)
    print('--- ' * 22)

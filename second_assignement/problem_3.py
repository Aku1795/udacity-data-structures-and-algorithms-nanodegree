class Node:

    def __init__(self, freq, letter=None):
        self.left=None
        self.right=None
        self.freq = freq
        self.letter = letter

class Tree:

    def __init__(self, root):
        self.root = root

class PriorityQueue:

    def __init__(self):
        return 

def calc_freq(string):

    freq_dict = {}

    for char in string:
        if freq_dict.get(char):
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    return freq_dict

def build_priority_queue(freq_dict):

    priority_queue = [(key, val) for key, val in freq_dict.items()]
    priority_queue_sorted = sorted(priority_queue, key=lambda tup: tup[1], reverse=False)

    return priority_queue_sorted

def build_huffman_tree(priority_queue):
    return 

def test_calc_freq():
    string = "AAAABBBB"
    assert(calc_freq(string) == {"A": 4, "B": 4})

def test_build_priority_queue():
    string = "AAAABBBBB"
    freq_dict = calc_freq(string)
    priority_queue = build_priority_queue(freq_dict)
    assert priority_queue == [("A", 4), ("B", 5)]

def test():
    test_calc_freq()
    test_build_priority_queue()

test()
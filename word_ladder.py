"""
# Translate

- "Shortest" makes me think BFS
- "Transformation Sequence" makes me think BFS Path
- "Word" a graph vertex / node
- "One Letter Change" Edge

# Build
- Vertex List -> word list
- thinking about how to get all edges (???)

"""

# open the words.txt file
f = open("words.txt", "r")
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

# list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'w', 'x', 'y', 'z']

def get_neighbors(word):
    neighbors = []
    # TODO: the logic for getting neighbors
    return neighbors

def find_word_ladder(begin_word, end_word):
    pass


print(find_word_ladder("sail", "boat"))

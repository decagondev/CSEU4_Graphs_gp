"""
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4

remember to talk through a possible approach to the problem with your group

"""


def island_counter(matrix):
    pass

if __name__ == "__main__":
    islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

    island_counter(islands)  # 4

    islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

    island_counter(islands)  # 13
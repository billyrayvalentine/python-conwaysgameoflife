# Copywright (c) 2017 Ben Sampson
# A Conway's game of life implementation
"""
An implementation of Conway's game of life that captures just the state in an
array
"""
class ConwaysGameOfLife():
    """Implement Conway's Game of life as a Python class"""

    # RULES
    MIN_NEIGHBOURS = 2
    IDEAL_NEIGHBOURS = (2, 3)
    MAX_NEIGHBOURS = 3
    BORN_NEIGHBOURS = 3


    def __init__(self, universe):
        """"""
        self.universe = universe
        self.generation = 0

    def __str__(self):
        """Print the universe"""
        out = ''
        width, height = self.get_size()

        # count up the width and down the height
        for y in range(height -1, -1, -1):
            for x in range(width):
                if self.universe[x][y]:
                    out += ' o'
                else:
                    out += ' .'
            out += '\n'

        return(out)


    def get_size(self):
        """Return the size of the universe"""
        width = len(self.universe)
        height = len(self.universe[0])
        return width, height


    def next(self):
        """Calculate and create and set the next generation"""
        # create a new universe which will be the next generation
        width, height = self.get_size()
        new_universe = [[ 0 for _ in range(height)] for _ in range(width)]

        # Iterate the current universe and test
        for y in range(height):
            for x in range(width):

                new_universe[x][y] = self._lives_or_born(x, y)

        self.universe = new_universe
        self.generation += 1

    def _lives_or_born(self, x, y):
        """Return true is the cell at x, y lives or is born"""
        neighbours = self._neighbours(x, y)

        # Rules for alive cells
        if self.universe[x][y]:
            if neighbours < self.MIN_NEIGHBOURS or neighbours > self.MAX_NEIGHBOURS:
                return False
            #elif neighbours in self.IDEAL_NEIGHBOURS:
            else:
                return True

        # Rules for dead cells
        else:
            if neighbours == self.BORN_NEIGHBOURS:
                return True
            else:
                return False


    def _neighbours(self, x, y):
        """Return the number of neighbours"""
        count = 0
        neighbourhood = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

        try:
            for pos in neighbourhood:
                if self.universe[x - pos[0]][y - pos[1]]:
                    count += 1
        except IndexError:
            pass

        return(count)


if __name__ == "__main__":

    blinker = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
    block = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    toad = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]

    #a = ConwaysGameOfLife(block)
    #a = ConwaysGameOfLife(tub)
    a = ConwaysGameOfLife(toad)
    print('Size of universe is w,h {0}'.format(a.get_size()))

    for _ in range(5):
        print('Generation ' + str(a.generation))
        print(a)
        a.next()

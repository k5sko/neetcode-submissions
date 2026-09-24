class CountSquares:
    # maybe keep two hashmaps; one to keep track of the x coordinate and one to keep track of the y coordinate. then we can look for points with the same x and y coordinate as the point in count
    def __init__(self):
        self.x = dict()
        self.y = dict()

    # why not a counter dict as the value

    def add(self, point: List[int]) -> None:
        coord1, coord2 = point

        if coord1 not in self.x:
            self.x[coord1] = []

        self.x[coord1] += [coord2]

        if coord2 not in self.y:
            self.y[coord2] = {}
        if coord1 not in self.y[coord2]:
            self.y[coord2][coord1] = 0

        self.y[coord2][coord1] += 1

    # x = {1: [1, 2], 2: [2]}
    # y = {1: [1], 2: [2, 1]}

    # num_ways = 0
    # x1, y1 = 2, 1
    # same_x = [2]
    # same_y = [1]

    # y2 = 2
    # x2 = 

    def count(self, point: List[int]) -> int:
        num_ways = 0
        x1, y1 = point

        if x1 in self.x:
            same_x = self.x[x1] # y value of all points with the same x value
        else:
            return 0

        if y1 in self.y:
            same_y = self.y[y1] # y value of all points with the same x value
        else: 
            return 0

        # what if the inner loop only runs over points which have square lengths anyways?
        # meaning only over points such that abs(x2 - x1) == abs(y2 - y1)

        for vert in same_x:
            # points with the same x value; vertically displaced
            y2 = vert

            if y1 == y2:
                continue

            # x2 - x1 = y2 - y1 or x2 - x1 = y1 - y2
            x = [y2 - y1 + x1, y1 - y2 + x1]

            for x2 in x:
                if x2 in self.y[y2]:
                    num_ways += self.y[y2][x2]

        return num_ways
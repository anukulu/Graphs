

class CoordinateChanger:

    @staticmethod
    def GridToArray(n, m, columnSize):
        return (n + 1 + (m * columnSize))

    @staticmethod
    def ArrayToGRid(arrayIndex, columnSize):
        # returns the actual grid coordinates + 1
        if columnSize > arrayIndex:
            return
        r = (arrayIndex % columnSize)
        q = int(arrayIndex / columnSize)
        return [q, r]


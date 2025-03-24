class Structure:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def compare(self, ob):
        if self.size == ob.size: return 0
        return -1 if self.size < ob.size else 1

nuts = [
    Structure("nut", 9),
    Structure("nut", 5),
    Structure("nut", 0),
    Structure("nut", 2),
    Structure("nut", 7),
    ]

bolts = [
    Structure("bolt", "7"),
    Structure("bolt", "9"),
    Structure("bolt", "0"),
    Structure("bolt", "5"),
    Structure("bolt", "2"),
]


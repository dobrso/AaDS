from typing import List, Tuple


def buildPolyline(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    points.sort()
    return points


points = [(1, 2), (3, 1), (2, 2), (0, 0)]
print(buildPolyline(points))

from math import sqrt


def checkCircleIntersections(circles) -> bool:
    events = []

    for i, (xi, yi, ri) in enumerate(circles):
        events.append((xi-ri, "start", i))
        events.append((xi+ri, "end", i))

    events.sort(key=lambda x: x[0])

    active = []

    for event in events:
        x, type, i = event
        xi, yi, ri = circles[i]

        if type == "start":
            for (yj, j) in active:
                xj, yj, rj = circles[j]

                if abs(yi - yj) > (ri + rj):
                    continue

                d = sqrt((xi - xj) **2 + (yi - yj) **2)
                if d <= (ri + rj):
                    return True

            active.append((yi, i))
            active.sort(key=lambda x: x[0])

        elif type == "end":
            active.pop(i)

    return False

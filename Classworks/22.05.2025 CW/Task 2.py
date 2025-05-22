from typing import List, Tuple


def canAccommodate(bookings: List[Tuple[int, int]], K: int) -> bool:
    events = []

    for booking in bookings:
        start, end = booking
        events.append((start, 1))
        events.append((end, -1))

    events.sort()

    currentRooms = 0

    for event in events:
        day, change = event
        currentRooms += change
        if currentRooms > K:
            return False

    return True


K = 2
bookings = [(1, 4), (2, 6), (4, 7)]
print(canAccommodate(bookings, K))

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        SeatsToAdd = [0] * (n + 1)

        for start, last, seats in bookings:
            SeatsToAdd[start - 1] += seats
            SeatsToAdd[last] -= seats
        SeatsToAdd = list(accumulate(SeatsToAdd))

        return SeatsToAdd[:-1]
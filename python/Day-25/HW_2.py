class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        # Create Registries of guest entry and exit
        # Registry has two inputs, date of event,
        # and status (1 for arrival, -1 for departure)

        hotel_registry = [(date, 1) for date in arrive]
        hotel_registry += [(date, -1) for date in depart]

        # Sort Registry w.r.t Dates for same dates, exits come first
        hotel_registry.sort(key=lambda x: (x[0], -x[-1]))

        overlap_count = 0

        # Count number of overlaps in sequential manner,
        # and return answer if crosses room count
        for _, action in hotel_registry:
            overlap_count += action
            if overlap_count > K:
                return 0

        return 1

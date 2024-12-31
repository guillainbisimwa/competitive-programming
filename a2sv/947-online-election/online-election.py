class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.votes = [0] * len(persons)
        self.freq = [0] * (max(persons) + 1)
        max_votes = 0
        max_person = 0

        for i in range(len(persons)):
            self.freq[persons[i]] += 1
            if self.freq[persons[i]] >= max_votes:
                max_votes = self.freq[persons[i]]
                max_person = persons[i]
            self.votes[i] = max_person

    def q(self, t: int) -> int:
        closest_index = self.closest(t)
        return self.votes[closest_index]
    def closest(self, target):
        start, end = 0, len(self.times) - 1
        idx = end
        while start <= end:
            mid = start + (end - start) // 2
            if self.times[mid] == target:
                return mid
            elif self.times[mid] > target:
                end = mid - 1
            else:
                idx = mid
                start = mid + 1
        return idx


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
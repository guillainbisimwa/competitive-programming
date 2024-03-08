class FrequencyTracker:

    def __init__(self):
        self.map = {}
        self.freq = {}
        

    def add(self, number: int) -> None:
        if number not in self.map:
            self.freq[1] = self.freq.get(1, 0) + 1
        else:
            self.freq[self.map[number]] -= 1
            if self.freq[self.map[number]] == 0:
                del self.freq[self.map[number]]
            self.freq[self.map[number] + 1] = self.freq.get(self.map[number] + 1, 0) + 1
        self.map[number] = self.map.get(number, 0) + 1
        

    def deleteOne(self, number: int) -> None:
        if number in self.map:
            self.freq[self.map[number]] -= 1
            if self.freq[self.map[number]] == 0:
                del self.freq[self.map[number]]
            self.freq[self.map[number] - 1] = self.freq.get(self.map[number] - 1, 0) + 1
            self.map[number] -= 1
            if self.map[number] == 0:
                del self.map[number]
        

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
        
        
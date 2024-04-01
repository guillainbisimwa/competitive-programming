class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        element_counts = [[key, freq[key]] for key in freq.keys()]

        element_counts.sort(key=lambda x: x[1], reverse=True)

        top_k_elements = [element for element, _ in element_counts[:k]]

        return top_k_elements

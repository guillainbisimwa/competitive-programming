class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        listDict_1 = {}
        res = {}
        ans = []

        for i, restaurant in enumerate(list1):
            listDict_1[restaurant] = i

        for j, restaurant in enumerate(list2):
            if restaurant in listDict_1:
                res[restaurant] = j + listDict_1[restaurant]

        min_value = float('inf')
        for value in res.values():
            min_value = min(min_value, value)

        for key, value in res.items():
            if value == min_value:
                ans.append(key)

        return ans
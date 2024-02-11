class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        map = {}
        n = len(matches)

        for i in range(n):
            if matches[i][0] not in map:
                map[matches[i][0]] = 0

            if matches[i][1] in map:
                map[matches[i][1]] += 1
            else:
                map[matches[i][1]] = 1

        res = []
        list1 = []
        list2 = []

        for key in map:
            if map[key] == 0:
                list1.append(key)
            if map[key] == 1:
                list2.append(key)

        list1.sort()
        list2.sort()
        res.append(list1)
        res.append(list2)
        return res
        
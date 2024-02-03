class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        finalValue = 0

        for operation in operations:
            if "++X" in operation or "X++" in operation:
                finalValue += 1
            elif "--X" in operation or "X--" in operation:
                finalValue -= 1

        return finalValue

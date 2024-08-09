class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = {}
        queue = deque([(0, 0, 0, "")])
        while queue:
            index, prev_operand, current_evaluation, expression_path = queue.popleft()

            if index == len(num):
                if current_evaluation == target:
                    result[expression_path] = current_evaluation
                continue

            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i > index and num[index] == '0':
                    break
                current_string = num[index:i + 1]
                current_value = int(current_string)

                if index == 0:
                    queue.append((i + 1, current_value, current_value, current_string))
                else:
                    queue.append((i + 1, current_value, current_evaluation + current_value, expression_path + '+' + current_string))
                    queue.append((i + 1, -current_value, current_evaluation - current_value, expression_path + '-' + current_string))
                    queue.append((i + 1, prev_operand * current_value, current_evaluation - prev_operand + prev_operand * current_value, expression_path + '*' + current_string))

        return result

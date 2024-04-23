class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log.startswith('../'):
                if stack:
                    stack.pop()
            elif log.startswith('./'):
                continue
            else:
                stack.append(log)
        return len(stack)

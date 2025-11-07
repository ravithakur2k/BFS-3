# O(2^n) as we have to traverse through each level to find the valid parentheses.
# O(2^n * n) for visit set

# The intuition here is to do BFS and at each level check if we have a valid parentheses, if yes then get all the results at that level and stop further iterations

class Solution:
    def removeInvalidParenthesesBFS(self,s: str) -> List[str]:
        queue = deque()
        queue.append(s)
        resultSet = set()
        visit = set()
        flag = False
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if self.isValid(curr):
                    flag = True
                    resultSet.add(curr)
                for j in range(len(curr)):
                    if curr[j] not in ("(", ")"):
                        continue
                    newStr = curr[0:j] + curr[j + 1:]
                    if newStr not in visit:
                        visit.add(newStr)
                        queue.append(newStr)

            if flag:
                break

        return list(resultSet)

    # The same can be achieved using DFS as well. The time and space is the same. Only caveat is we have to clear the result whenever we find the next max string.
    def removeInvalidParenthesesDFS(self, s: str) -> List[str]:
        visit = set()
        visit.add(s)
        maxLen = 0
        result = []

        def dfs(strS):
            nonlocal maxLen
            if maxLen > len(strS): return

            if isValid(strS):
                if len(strS) > maxLen:
                    maxLen = len(strS)
                    result.clear()

                result.append(strS)
                return

            for k in range(len(strS)):
                if strS[k].isalpha(): continue
                curr = strS[0:k] + strS[k + 1:]
                if curr not in visit:
                    visit.add(curr)
                    dfs(curr)

            dfs(s)
            return result

    def isValid(self, strS):
        count = 0
        for c in strS:
            if c == "(":
                count += 1
            elif c == ")":
                if count == 0: return False
                count -= 1

        if count == 0:
            return True
        return False
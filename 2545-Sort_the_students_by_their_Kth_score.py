# 2545. Leetcode - Sort the students by their Kth score

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x:x[k], reverse=True)
        return score
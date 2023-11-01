class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        print(len(word1),len(word2))
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        #dp = [ [0 for j in range(len2)] ] * len1 
        dp = [[0] * (len2) for _ in range(len1)]
        for i in xrange(len1):
            dp[i][0] = i
        for j in xrange(len2):
            dp[0][j] =j
        for i in xrange(1, len1):
            for j in xrange(1, len2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    #print("i=%d|j=%d|dpij=%s" % (i,j,dp[i][j]))
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
                    #print("i=%d|j=%d|dpij=%s" % (i,j,dp[i][j]))
        return dp[len1-1][len2-1]

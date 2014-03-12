'''
Analysis:
Be careful with the question, for [1,2,2], [2,2] is needed.
Here we use another way different from the previous problem to solve this problem.

First, consider there is no duplicates, how to generate the subsets?
Say n is the # of the elements,
when n=1, subsets :  {}, {"1"},  "i" means the ith element.
when n=2, subsets:   {}, {"1"}, {"2"}, {"1", "2"}
when n=3, subsets:   {}, {"1"}, {"2"}, {"1", "2"}, {"3"}, {"1","3"}, {"2","3"}, {"1", "2","3"}
So, the way of generating subsets is:
From 2 to n, COPY the previous subsets, add the current element, push back to the subsets list.

Then we take the duplicates into account, the same example:
when n=1, subsets :  {}, {"1"},  "i" means the ith element.
when n=2, subsets:   {}, {"1"}, {"2"}, {"1", "2"}
when n=3, but "2"=="3" subsets: 
   {}, {"1"}, {"2"}, {"1", "2"}, {"3"}, {"1","3"}, {"2","3"}, {"1", "2","3"}
since "2"=="3", which truly is:
   {}, {"1"}, {"2"}, {"1", "2"}, {"2"}, {"1","2"}, {"2","2"}, {"1", "2","2"}
where the bold ones are not needed.
So, how these two subsets are generated? They are from the subsets of n=1.

In sum up, when meet the same element as previous one, then generate new subsets ONLY from the subsets generated from previous iteration, other than the whole subsets list.

See code below for more details.
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S = sorted(S)
        rt = [[]]
        prev_rec = 0
        for i in xrange(len(S)):
            prev_leng = len(rt)
            start_with = 0
            if i != 0 and S[i] == S[i - 1]:
                start_with = prev_rec
            rt += [item + [S[i]] for item in rt[start_with:]]
            prev_rec = prev_leng
        return rt

s = Solution()
print s.subsetsWithDup([1,2,2])

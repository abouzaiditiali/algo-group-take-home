from typing import List

"""
Implementations 1 and 2 assume that the input has been provided exactly as 
described in the instructions.
"""

#Solution 1
def findDuplicate1(input: List[int]) -> int:
    for i, element in enumerate(input): 
        if element in input[i+1:]:
            return element

"""
This solution has a time complexity of O(N^2). Line 10 iterates through the
entire input list O(N). Line 11 performs a linear search over the remaining 
elements which can take O(N) in the worst case.

For space complexity, since each sublist (input[i+1:]) is created one at a time 
and doesn't persist after each iteration, the space used is at most proportional 
to the size of the input list. Thus, space complexity is O(N).
"""

#Solution2
def findDuplicate2(input: List[int]) -> int:
    input.sort()
    for i, element in enumerate(input): 
        if element == input[i+1]:
            return element
        
"""
Sorting the list takes O(N log N) time (I looked up on internet the time 
complexity of the Python sort method), where N is the size of the input list.
After sorting, I perform a single linear scan of the sorted list, which takes 
O(N) time. Thus, the overall time complexity is dominated by the sorting step, 
O(N log N).

For space complexity, I found that Python does in-place sorting, O(1).
"""
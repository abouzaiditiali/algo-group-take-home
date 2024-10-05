# algo-group-take-home

I answered option 1.

I came up with two solutions. The first one consisted of a nested for-loop
where time complexity was O(N^2). In the second solution, I thought of sorting 
the list first and then performing a linear search seeing that the duplicates
will be next to each other. This solution had a time complexity of O(N log N).
More details about the solutions are found within the implementation file
itself, named option1.py.

Tests can be found in the file test_option1.py. Pytest was used to run the tests.
100% of the tests have passed.
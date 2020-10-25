**Anagram Checker**

An anagram is a word or phrase formed by rearranging the letters of
a different word or phrase. In other words, both strings must contain
the same exact letters in the same exact frequency.

Write a python script that reads 2 strings from command line and finds
out whether they are anagrams or not.
If they are not anagrams, then the script should find and print the
minimum number of character deletions required to make the two strings
anagrams. Otherwise, just print that they are anagrams.

**Input Format**

- The first line contains a single string, **a**.
- The second line contains a single string, **b**.

Expected input and output:
```
$ python3 solution.py
a: Tom Marvolo Riddle
b: I Am Lord Voldemort
remove 7 characters from 'Tom Marvolo Riddle' and 8 characters from 'I Am Lord Voldemort'

$ python3 solution.py
a: tom marvolo riddle
b: i am lord voldemort
remove 0 characters from 'tom marvolo riddle' and 1 characters from 'i am lord voldemort'

$ python3 solution.py
a: tom marvolo riddle
b: i am lordvoldemort
they are anagrams

$ python3 solution.py
a: tom riddle
b: voldemort
remove 3 characters from 'tom riddle' and 2 characters from 'voldemort'
```

### **Implementation**
The example is done using Python 3 programming language, and tested using the standard `unittest` module shipped with the default version.
The solution is based on the idea that when two anagram strings' characters are sorted, then they can be directly compared with a simple equality operation.

### **Performance Analysis**
The algorithm implemented in `solution.py`, the approach intended to be as efficient as possible.
The soring operation of the `sorted()` function in python is `O(n log n)` which is a good time complexity to achieve.
Since we have two strings with different length, the overall complexity will sum up to `O(n log n) + O(m log m)`, and the additional hashmap checking done in the final false report (when both strings are not anagram) does not have a complexity more than `O(n + m)`. A trivial lookup operation is done in the in-hashmap check, since the number of distinct character is limited.
Speaking about space complexity, the algorithm is space efficient of complexity of `O(n + m)`

### **Usage**
The prepared solution can be directly called as any simple python script through the command: `python3 solution.py`. 
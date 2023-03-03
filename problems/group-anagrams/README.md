## Group Anagrams

Given an array of strings `strings`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

### Example 1
```
Input: strings = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

### Example 2
```
Input: strings = [""]
Output: [[""]]
```

### Example 3
```
Input: strings = ["a"]
Output: [["a"]]
```

### Constraints
- `1 <= strings.length <= 10^4`
- `0 <= strings[i].length <= 100`
- `strings[i]` consists of lowercase English letters.

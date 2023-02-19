## 3Sum

Given an integer array `numbers`, return all the triplets `[numbers[i], numbers[j], numbers[k]]` such that `i != j`, `i != k`, and `j != k`, and `numbers[i] + numbers[j] + numbers[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1
```
Input: numbers = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
numbers[0] + numbers[1] + numbers[2] = (-1) + 0 + 1 = 0.
numbers[1] + numbers[2] + numbers[4] = 0 + 1 + (-1) = 0.
numbers[0] + numbers[3] + numbers[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

### Example 2
```
Input: numbers = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

### Example 3
```
Input: numbers = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

### Constraints
- `3 <= numbers.length <= 3000`
- `-10^5 <= numbers[i] <= 10^5`

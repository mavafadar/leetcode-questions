## Valid Parentheses

Given a string `string` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

## Examples

### Example 1
```
Input: string = "()"
Output: true
```

### Example 2
```
Input: string = "()[]{}"
Output: true
```

### Example 3
```
Input: s = "(]"
Output: false
```

### Constraints
- `1 <= string.length <= 10^4`
- `string` consists of parentheses only `'()[]{}'`.

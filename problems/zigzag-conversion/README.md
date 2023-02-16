## Zigzag Conversion
The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

`string convert(string string, int row_number);`

## Examples

### Example 1
```
Input: string = "PAYPALISHIRING", row_number = 3
Output: "PAHNAPLSIIGYIR"
```

### Example 2
```
Input: string = "PAYPALISHIRING", row_number = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

### Example 3
```
Input: string = "A", row_number = 1
Output: "A"
```

### Constraints
 - `1 <= string.length <= 1000`
 - `string` consists of English letters (lower-case and upper-case), `,` and `.`.
 - `1 <= row_number <= 1000`

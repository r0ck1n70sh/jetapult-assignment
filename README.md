# jetapult-assignment

### Run
```shell
$ python main.py
```

### Time Complexity
```
T = O (( r*r + r*c + c*c ) * l)
where,
  r -> no. of rows
  c -> no. fo cols
  l -> length of longest word, in words
```

### Space Complexity
```
S = O (r + c + W)
where,
  r -> no. of rows
  c -> no. fo cols
  W -> total no. of characters in words
```

### Explaination
as we know, we can use trie data structure to check whether a sub-string `s', where s' = S[i:j], 0 <= i < j < len(S)` is present in list of words in `O(len(S) * L) time, where L is length of longest word in words`. ex.
```
in order of check whether string "CD", is present in words, we have 
S = "ABCDE"
s = [ "ABCDE", "BCDE", "CDE", "DE", "E" ]

by using sub-string "CDE", we can check in time
T = O (L)

therefore, to check all sub-string s', we'll have use all elements in s. so time is,
T = O ( Time to check one element of s * no. of elements in s )
  = O ( L * len(S) )
```

therefore, in order check whether a word, is present in a grid, we can divide grid as follows:
```
grid = [
  [ 'A', 'B', 'C' ],
  [ 'E', 'F', 'G' ],
  [ 'H', 'I', 'J' ],
]

row_str = [ 'ABC', 'EFG', 'HIJ' ]
col_str = [ 'AEH', 'BFI', 'CGJ' ]
diagonal_str = [ 'AFJ', 'BG', 'C', 'A', 'BE', 'CFH', 'GI', 'J' ]
```
so, any word present in grid would be sub-string of element in `row_str`, `col_str`, `diagonal_str`, so have
```
T (grid) = T (row_str) + T (col_str) + T (diagonal_str)

now,
T (row_str) = r * T (elem in row_str)

we know,
len(elem in row_str) = c
therefore,
T (elem in row_str) = O (c * L)

hence,
T (row_str) = O (r * c * L)

similarily,
T (col_str) = O (r * c * L)
T (diagonal_str) = O ( min (r , c) * (r + c) * L ), // max. length of diagonal = min(r , c), no of. diagonals = order of ( r + c ) 

T (grid_ = O ( (r*r + r*c + c*c) * L )
```
for space complexity, at any instance we'll be working with any element of `row_str`, `col_str`, or `diagoal_str`, and also a trie of words.
```
S (grid) = max( S (row_str), S (col_str), S (diagonal_str) ) + S (trie of words)

S (trie of words) =  W // since, trie is a overlapping tree of characters, in words 

S (row_str) = len (elem in row_str = c

similarily,
S (col_str) = r
S (diagonal_str) = min (r, c)

therefore,

S (grid) = S ( r + c + W )
```

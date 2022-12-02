## Decode algorithm 
1. initially known : 1,4,7,8
2. find char_f, only char in all but 1 signal
3. Known :  1,4,7,8 + 2,  2 is the only without f
4. find char_c using 1 : 1    
5. Known : 1,2,4,7,8 + 5, 6 because 5 and 6 are the only one without c
6. find 3 because it's the last of size 5
7. find 9 because it's intersection with 4 is 4
8. find 0 because it's the last

# Using set theory can minimize confusion and is one of the easy ways to get the answer very fast, best of all it is very understandable even for beginners.

The only digits which has a length of 6 are 0, 6 and 9

I used algebra set theory to create an intersection of 
+ digits 5 and 9 which has a length of 4
+ digits 1 and 0 has a length of 2 (if you can exclude 9)
then the only remaining six segment piece is digit 6

then, the only digits which have a length of 5 2, 3, and 5 
+ An intersection of digits 1 and 3 has 2
+ An intersection of digits 0 and 5 has len 5
the only five segment left is two


### Another excellent approach using match in python 3.10

```python
s = 0
for x,y in [x.split('|') for x in open(0)]:  # split signal and output
  l = {len(s): set(s) for s in x.split()}    # get number of segments

  n = ''
  for o in map(set, y.split()):              # loop over output digits
    match len(o), len(o&l[4]), len(o&l[2]):  # mask with known digits
      case 2,_,_: n += '1'
      case 3,_,_: n += '7'
      case 4,_,_: n += '4'
      case 7,_,_: n += '8'
      case 5,2,_: n += '2'
      case 5,3,1: n += '5'
      case 5,3,2: n += '3'
      case 6,4,_: n += '9'
      case 6,3,1: n += '6'
      case 6,3,2: n += '0'
  s += int(n)
print(s)
```

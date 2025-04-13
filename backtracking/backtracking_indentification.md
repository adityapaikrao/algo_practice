Backtracking is basically 'controlled recursion' +  'pass by reference'

Identification:

1. We have to make a choice/decision at each step
2. need to permute 'all combinations'
3. controlled recursion -> at each step save yourself the trouble by only recursing for a 'good' choice. Ex: if you know your house is in south-west, there's no point going north or east
4. number of choices at each step is large, hence the need for 'controlled' recursion
5. constraints are usually small n < 20 etc. i.e expected time complexity is $O(2^{n})$ or $O(n!)$

Generalization:

1. Base Condition: On hitting base condiition -> either print or save the answer and terminate recursion
2. Use a for loop to recurse through choices
3. Controlled recursion -> think about the valid choices and recurse for it. remove value added by this choice immediately after its called
4. 

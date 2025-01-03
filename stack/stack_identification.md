## How to identify?

1. Given an array
2. Brute force solution is usually O($n^2$) with the inner loop $j$ dependent on the outer loop $i$. Ex: $j$ varies from 
   
   i. $0 \text{ to } i$ Ex: Nearest smallest/largest to Left\
   ii. $i \text{ to } n$ \
   iii. $n \text{ to } i$ Ex: Nearest smallest/largest to right \
   iv. $i \text{ to } 0$

Start from j and store elements in stack according to the condiition. The idea is that the popped elements would never be used again, hence safe to pop them. Classic

Sometimes, we may also need to vary $j$ both ways ($0$ to $i$) and ($i$ to $n$) within the same problem and then do *some* operations using these values. Ex: Max Area Histogram, max area binary matrix, <a href='https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/description/'> 2334. Subarray With Elements Greater Than Varying Threshold </a>
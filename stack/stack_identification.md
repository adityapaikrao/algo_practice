## How to identify?

1. Given an array
2. Brute force solution is usually O($n^2$) with the inner loop $j$ dependent on the outer loop $i$. Ex: $j$ varies from 
   
   i. $0 \text{ to } i$ \
   ii. $i \text{ to } n$ \
   iii. $n \text{ to } i$ \
   iv. $i \text{ to } 0$

Start from j and store elements in stack according to the condiition. The idea is that the popped elements would never be used again, hence safe to pop them.
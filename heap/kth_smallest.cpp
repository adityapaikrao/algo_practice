#include<iostream>
#include<queue>

using namespace std;

int main()
{
    vector<int> arr = {10, 2, 4, 8, 6, 9};
    int n = arr.size();
    int k = 3;
    

    // kth smallest
    priority_queue<int> maxheap;
    for(int i =0; i < n; i++)
    {
        maxheap.push(arr[i]);
        if(maxheap.size() > k){maxheap.pop();}
    }

    cout << maxheap.top() << endl;

    // kth largest
    priority_queue<int, vector<int>, greater<int>> minheap;
    for(int i=0; i <n; i++)
    {
        minheap.push(arr[i]);
        if(minheap.size() > k)
        {
            minheap.pop();
        }
    }
    cout << minheap.top() << endl;
    
}


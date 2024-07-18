#include<iostream>
#include<vector>
#include<queue>

using namespace std;

void sort_arr(vector<int> arr, int n, int k)
{
    priority_queue<int, vector<int>, greater<int>> minheap;
    vector<int> out;
    for(int i =0; i < n; i++)
    {
        minheap.push(arr[i]);
        if(minheap.size() > k)
        {
            out.push_back(minheap.top());
            minheap.pop();
        }
    }
    for(int j =0; j < minheap.size(); j++)
    {
        out.push_back(minheap.top());
        minheap.pop();
    }
    
    for(int i=0; i < out.size(); i++)
    {
        cout << out[i] << " ";
    }
    cout << endl;
}

int main()
{
    vector<int> arr = {6, 5, 3, 2, 8, 10, 9};
    int n = arr.size();
    int k = 3;
    sort_arr(arr, n, k);
}
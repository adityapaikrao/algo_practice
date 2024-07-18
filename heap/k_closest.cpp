#include<iostream>
#include<vector>
#include<queue>
#include<utility>

using namespace std;

vector<int> k_closest(vector<int> arr, int n, int k, int x)
{
    priority_queue<pair<int, int>> maxheap; // sorts on the basis of pair.first
    vector<int> op;

    for(int i =0; i< n; i++)
    {
        pair<int, int> p = make_pair(abs(x - arr[i]), arr[i]);
        maxheap.push(p);
        while(maxheap.size() > k)
        {
            maxheap.pop();
        }
    }
    while(!maxheap.empty())
    {
        op.push_back(maxheap.top().second);
        maxheap.pop();
    }

    return op;
}


int main()
{
    vector<int> arr = {5,6,7,8,9};
    int n = arr.size();
    int k = 3;
    int x = 7; // find k closest elements to x

    vector<int> op = k_closest(arr, n, k, x);

    for(int i =0; i < k; i++)
    {
        cout << op[i] << " ";
    }
    cout << endl;
}
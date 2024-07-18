#include<iostream>
#include<vector>
#include<utility>
#include<queue>
#include<unordered_map>

using namespace std;
using dtype = pair<int, int>;

vector<int> top_k(vector<int> arr, int n, int k)
{
    priority_queue<dtype, vector<dtype>, greater<dtype>> minh;
    vector<int> op;
    unordered_map<int, int> map;

    for(int i =0; i < n; i++)
    {
        map[arr[i]]++;
    }

    for(auto x : map)
    {
        dtype p = make_pair(x.second, x.first);
        minh.push(p);
        while(minh.size() > k)
        {
            minh.pop();
        }
    }

    while(!minh.empty())
    {
        op.push_back(minh.top().first);
        minh.pop();
    }

    return op;
}

int main()
{
    vector<int> arr = {1, 1, 1, 3, 2, 4};
    int n = arr.size();
    int k = 2;

    vector<int> op = top_k(arr, n, k);

    for(int i=0; i < k; i++)
    {
        cout << op[i] << " ";
    }
    cout << endl;
}
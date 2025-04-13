#include<iostream>
#include<vector>
#include<utility>
#include<queue>
#include<cmath>

using namespace std;
using dtype = pair<int, pair<int, int>>;

vector<pair<int, int>> closest_to_origin(vector<vector<int>> arr, int n, int k)
{
    priority_queue<dtype> maxh;

    for(int i =0; i < n; i++)
    {
        int d = pow(arr[i][0], 2) + pow(arr[i][1], 2);
        dtype p = make_pair(d, make_pair(arr[i][0], arr[i][1]));
        maxh.push(p);
        if(maxh.size() > k)
        {
            maxh.pop();
        }
    }
    
    vector<pair<int, int>> op;
    while(!maxh.empty())
    {
        op.push_back(maxh.top().second);
        maxh.pop();
    }

    return op;

}

int main()
{
    vector<vector<int>> arr = {{1,3}, {-2,2}, {5,8}, {0,1}};
    int n = arr.size();
    int k = 2;

    vector<pair<int, int>> op = closest_to_origin(arr, n, k);
    for(int i =0; i < op.size(); i++)
    {
        cout << "(" << op[i].first << ", " << op[i].second << ") ";
    }
    cout << endl;
}
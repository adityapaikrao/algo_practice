#include<iostream>
#include<vector>
#include<stack>
#include<utility>
#include<algorithm>

using namespace std;

vector<int> max_to_right(vector<int> arr, int n)
{
    stack<int> s;
    vector<int> right;

    for(int i = n-1; i >=0; i--)
    {
        if(s.empty())
        {
            right.push_back(0);
            s.push(arr[i]);
        }
        else if (s.top() > arr[i])
        {
            right.push_back(s.top());
        }
        else
        {
            s.pop();
            s.push(arr[i]);
            right.push_back(0);
        }
        
    }
    reverse(right.begin(), right.end());
    return right;
}

vector<int> max_to_left(vector<int> arr, int n)
{
    stack<int> s;
    vector<int> left;

    for(int i = 0; i < n; i++)
    {
        if(s.empty())
        {
            left.push_back(0);
            s.push(arr[i]);
        }
        else if (s.top() > arr[i])
        {
            left.push_back(s.top());
        }
        else
        {
            s.pop();
            s.push(arr[i]);
            left.push_back(0);
        }
        
    }
    return left;
}

int total_area(vector<int> arr, int n)
{
    vector<int> maxr = max_to_right(arr, n);
    vector<int> maxl = max_to_left(arr, n);

    for(int i =0; i < n; i++)
    {
        cout << maxl[i] << " ";
    }
    cout << endl;

    for(int i =0; i < n; i++)
    {
        cout << maxr[i] << " ";
    }
    cout << endl;

    int area = 0;
    for(int i=0; i < n; i++)
    {
        area += max((min(maxr[i], maxl[i]) - arr[i]), 0);
    }
    return area;
}


int main()
{
    vector<int> arr = {2, 1, 0, 3, 1, 2};
    int n = arr.size(); 

    int area = total_area(arr, n);

    cout << "area trapped: " << area << endl;
}
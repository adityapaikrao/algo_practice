#include<iostream>
#include<vector>
#include<stack>
#include<utility>
#include<algorithm>

using namespace std;

vector<int> nearest_smaller_left(vector<int> arr, int n)
{
    stack <pair<int, int>> stack; // index, value
    vector<int> nsl;
    for(int i =0; i < n; i++)
    {
        if(stack.empty()){nsl.push_back(-1);}
        else if (stack.top().second < arr[i])
        {
            /* code */
            
            nsl.push_back(stack.top().first);
        }
        else{
            while(!stack.empty() && stack.top().second > arr[i]){stack.pop();}
            if(stack.empty()){nsl.push_back(-1);}
            else{nsl.push_back(stack.top().first);}
        }
        pair<int, int> p = make_pair(i, arr[i]);
        stack.push(p);
    }
    return nsl;
}

vector<int> nearest_smaller_right(vector<int> arr, int n)
{
    stack <pair<int, int>> stack; // index, value
    vector<int> nsr;
    for(int i = n-1; i >= 0; i--)
    {
        if(stack.empty()){nsr.push_back(7);}
        else if (stack.top().second < arr[i])
        {
            /* code */
            
            nsr.push_back(stack.top().first);
        }
        else{
            while(!stack.empty() && stack.top().second > arr[i]){stack.pop();}
            if(stack.empty()){nsr.push_back(7);}
            else{nsr.push_back(stack.top().first);}
        }
        pair<int, int> p = make_pair(i, arr[i]);
        stack.push(p);
    }
    reverse(nsr.begin(), nsr.end());
    return nsr;
}

int max_area(vector<int> arr, int n)
{   
    // iterate through array, for each element find its NSL & NSR
    vector<int> nsl = nearest_smaller_left(arr, n);
    vector<int> nsr = nearest_smaller_right(arr, n);
    for(int i =0; i < n; i++){
        cout << nsl[i] << " ";
    }
    cout << endl;

    for(int i =0; i < n; i++){
        cout << nsr[i] << " ";
    }
    cout << endl;

    int max = 0;
    for(int i =0; i < n; i++){
        int curr = (nsr[i] -nsl[i] -1) * arr[i];
        if(curr > max)
        {
            max = curr;
        }
    }
    cout << "max area is: " << max <<endl;

    return 0;
}

int main()
{
    vector<int> arr = {6, 2, 5, 4, 5, 1, 6};
    int n = arr.size();

    int area = max_area(arr, n);
}
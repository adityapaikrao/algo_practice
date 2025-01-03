#include<iostream>
#include<vector>
#include<queue>
#include<utility>

using namespace std;

vector<int> first_negative(vector<int> arr, int k)
// idea is to maintain a queue of negative elements within a window
// using queue because we want a FIFO operation on negative numbers 
{
    queue<pair<int, int>> q;
    vector<int> out;
    int i =0;
    int j =0;
    while(j< arr.size()) // until valid window
    {
        if(arr[j] < 0)
        // only push negative numbers in the queue
        {
            pair<int,int> p = make_pair(j, arr[j]);
            q.push(p);
        }
        
        if(j-i+1 < k)
        {
            j++;
        }
        else
        {
            if(q.empty())
            // no negative number in the window
            {
                out.push_back(0);
                j++;
            }
            else
            // there is negative number in the window
            {
                out.push_back(q.front().second);
                i++;j++;
                // remove all negative numbers outside the next window 
                while(!q.empty() && q.front().first < i)
                {
                    q.pop();
                }
            }
        }
    }
    return out;
}

int main()
{
    vector<int> arr = {2, -1, 0, 3, 4, -4, -6};
    int k = 3;

    vector<int> out = first_negative(arr, k);
    for(int i =0; i < out.size(); i++)
    {
        cout << out[i] << " ";
    }
    cout << endl;
}
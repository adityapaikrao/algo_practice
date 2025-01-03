#include<iostream>
#include<vector>

using namespace std;

int largest_subarray(vector<int> arr, int k)
{
    int i = 0;
    int j = 0;
    int sum = 0;
    int maxlen = 0;

    while(j < arr.size())
    {
        sum += arr[j];
        // after adding the jth element there can be three possibilities w.r.t sum:
        if(sum < k)
        {
            // increment j and add the next element
            j++;
        }
        else if (sum==k)
        {
            //compute max size and increment j
            maxlen = max(maxlen, j-i+1);
            j++;
        }
        else
        {
            while(sum>k)
            {
                sum -= arr[i];
                i++;
            }
            if(sum==k)
            {
                maxlen = max(maxlen, j-i+1);
            }
            j++;
        }
    }
    return maxlen;
}

int main()
{
    vector<int> arr = {4, 1, 1, 0, 2, 3, 5};
    int k = 5;
    // find largest subrray with sum 5

    cout << "size of largest subarray: " << largest_subarray(arr, k) << endl;
}
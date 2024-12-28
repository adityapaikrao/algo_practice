#include<iostream>
#include<vector>

using namespace std;

int max_sum(vector<int> arr, int k)
{
    int i = 0;
    int j = 0;
    int sum = 0;
    int maxsum = 0;
    while(j < arr.size())
    {
        sum += arr[j];
        if(j-i + 1 < k)
        {
            j++;
        }
        else if (j-i+1==k)
        {
            maxsum = max(maxsum, sum);
            i++;j++;
            sum -= arr[i-1];
        }
    }
    return maxsum;
}

int main()
{
    vector<int> arr = {2, 5, 7, 1, 0, 3, 12};
    int k = 3;

    int sum = max_sum(arr, k);

    cout << "max sum subrarray of size "<< k << " is " << sum << endl;
}
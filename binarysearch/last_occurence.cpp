#include<iostream>
#include<vector>

using namespace std;

int last_occurence(vector<int> arr, int n, int el)
{
    int start = 0;
    int end = n-1;
    int idx = -1;

    while(start <= end)
    {
        int mid = start + (end-start)/2;
        
        if(arr[mid] == el)
        {
            idx = mid;
            start = mid +1;
        }
        else if(arr[mid] > el)
        {
            if(arr[start] <= arr[end]){end = mid-1;}
            else{start = mid +1;}
        }
        else{
            if(arr[start] <= arr[end]){start = mid+1;}
            else{end = mid -1;}
        }
    }
    return idx;
}

int main()
{   
    vector<int> arr = {6, 5, 4, 4, 4, 3, 3, 1};
    int n = arr.size();
    int el = 4;
    int idx = last_occurence(arr, n, el);

    cout << "Last occurence of is at: " << idx << endl;


}
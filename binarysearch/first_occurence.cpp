#include<iostream>
#include<vector>

using namespace std;

int first_occurence(vector<int> arr, int n, int el){
    int start = 0;
    int end = n -1;
    int idx = -1;
    while(start <= end){
        int mid = (start + end) /2; // addition of two ints could overflow, use mid = start + (end-start)/2
        mid  = start + (end-start)/2;

        if(arr[mid] == el){
            idx = mid;
            end = mid-1;
        }
        else if (arr[mid] > el)
        {
            /* code */
            if(arr[start] <= arr[end]){end = mid - 1;}
            else{start = mid + 1;}
            
        }
        else{
            if(arr[start] <= arr[end]){start = mid + 1;}
            else{end = mid - 1;}
        }
    }
    return idx;
}

int main()
{
    vector<int> arr = {12, 10, 10, 10, 10};
    int n = arr.size();

    int index = first_occurence(arr, n, 10);

    cout << "first occurence at index: " << index << endl;
}
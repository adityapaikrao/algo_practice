#include<iostream>
#include<vector>

using namespace std;

int bs(vector<int> arr, int n, int el){
    int start = 0;
    int end = n -1;
    while(start <= end){
        int mid = (start + end) /2; // addition of two ints could overflow, use mid = start + (end-start)/2
        mid  = start + (end-start)/2;
        if(arr[mid] == el){
            return mid;
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
    return -1;
}

int main()
{
    vector<int> arr = {10, 8, 6, 5, 4, 1};
    int n = arr.size();

    int index = bs(arr, n, 40);

    cout << "element present at index: " << index << endl;
}
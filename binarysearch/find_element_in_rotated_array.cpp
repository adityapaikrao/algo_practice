#include<iostream>
#include<vector>

using namespace std;

int bs(vector<int> arr, int n, int start, int end, int el)
{
    while(start<=end)
    {
        int mid = start + (end-start)/2;
        cout << "start, end: " << start << ", " << end << endl;
        cout << "mid: " << mid << endl;
        if(arr[mid] == el)
        {
            cout << "a" << endl;
            return mid;
        }
        else if (arr[mid] > el)
        {
            cout << "b" << endl;
            end = mid -1;
        }
        else
        {
            cout << "b" << endl;
            start = mid + 1;
        }
        
    }
    return -1;

}

int find_minimum(vector<int> arr, int n)
{
    int start = 0;
    int end = n-1;
    while(start <=end)
    {
        int mid = start + (end-start)/2;
        int left = (n + mid -1) % n;
        int right = (mid+1)%n;
        cout << "start, end: " << start << ", " << end << endl;
        cout << "mid: " << mid << endl;

        if(arr[mid] < arr[left] && arr[mid] < arr[right])
        {
            return mid;
        }
        else if (arr[mid] < arr[start])
        {
            end = mid-1;
        }
        else
        {
            start = mid +1;
        }   
    }
    return -1;
}

int find_element(vector<int> arr, int n, int el)
{
    int min = find_minimum(arr, n);
    int start, end, idx;

    cout << "min: " << min <<endl;
    if(arr[min] == el)
    {
        return min;
    }
    else if(el < arr[n-1])
    {
        start = min;
        end = n-1;
        
    }
    else
    {
        start = 0;
        end = min;
    }

    cout << "intial: start, end " << start << ", " << end << endl;
    return bs(arr, n, start, end, el);
}

int main(){
    vector<int> arr = {5, 1, 2, 3, 4};
    int n = arr.size();
    int el = 7;

    int idx = find_element(arr, n, el);

    cout << "index: " << idx <<endl;

}
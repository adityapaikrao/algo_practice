#include<iostream>
#include<vector>

// using namespace std;

int find_pivot(std::vector<int> arr, int n)
{
    int start = 0;
    int end = n-1;

    while(start<=end)
    {
        int mid  = start + (end-start)/2;
        int left = (n + mid -1) % n;
        int right = (mid+1) % n;

        if(arr[mid] < arr[left] && arr[mid] < arr[right])
        {
            return mid;
        }
        else if(arr[mid] < arr[start])
        {
            end = mid -1;
        }
        else
        {
            start = mid +1;
        }
    }
    return 0;
}

int main()
{
    std::vector<int> arr = {7, 8, 1, 2, 3, 4};
    int n = arr.size();

    int k = find_pivot(arr, n);

    std::cout << "Array is pivoted at index: " << k << std::endl; 
}
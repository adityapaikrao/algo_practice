#include<iostream>
#include<vector>

using namespace std;

int first_ocurrence(vector<int> arr, int n, int el)
{
    int start = 0;
    int end = n-1;
    int idx = -1;

    while(start<=end)
    {
        int mid = start  + (end-start)/2;
        if(arr[mid] == el)
        {
            idx = mid;
            end = mid -1;
        }
        else if (arr[mid] > el)
        {
            if(arr[start] <= arr[mid]){end = mid-1;}
            else{start = mid +1;}
        }
        else
        {
            if(arr[start] <= arr[mid]){start = start+1;}
            else{end = end -1;}
        }
        
    }
    return idx;

}

int last_ocurrence(vector<int> arr, int n, int el)
{
    int start = 0;
    int end = n-1;
    int idx = -1;

    while(start<=end)
    {
        int mid = start  + (end-start)/2;
        if(arr[mid] == el)
        {
            idx = mid;
            start = mid +1;
        }
        else if (arr[mid] > el)
        {
            if(arr[start] <= arr[mid]){end = mid-1;}
            else{start = mid +1;}
        }
        else
        {
            if(arr[start] <= arr[mid]){start = start+1;}
            else{end = end -1;}
        }
        
    }
    return idx;

}

int count_occurence(vector<int> arr, int n, int el)
{
    int count  = 0;
    int first_idx = first_ocurrence(arr, n, el);
    int last_idx = last_ocurrence(arr, n, el);

    if(first_idx == 0 || last_idx == 0){return count;} // ||, && are logical operators; |, & are bitwise operators

    return last_idx - first_idx + 1;


}

int main()
{
    vector<int> arr = {6,5,4,4,4,1};
    int n = arr.size();
    int el = 4;

    int count = count_occurence(arr, n, el);

    cout << "Count of given element: " << count << endl;
}
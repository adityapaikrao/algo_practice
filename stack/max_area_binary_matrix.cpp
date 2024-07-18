#include<iostream>
#include<vector>
#include<stack>
#include<utility>
#include<algorithm>

using namespace std;

vector<int> nsl(vector<int> arr, int m){
    stack<int> stack;
    vector<int> idx;
    for(int i=0; i < m; i++)
    {
        if(stack.empty()){idx.push_back(-1);}
        else if (arr[stack.top()] < arr[i])
        {
            /* code */
            idx.push_back(stack.top());
        }
        else
        {
            while(!stack.empty() && arr[stack.top()] >= arr[i])
            {
                stack.pop();
            }
            if(stack.empty()){idx.push_back(-1);}
            else{
                idx.push_back(stack.top());
            }
        }
        stack.push(i);
    }
    return idx;
}

vector<int> nsr(vector<int> arr, int m){
    stack<int> stack;
    vector<int> idx;
    for(int i=m; i >= 0; i--)
    {
        if(stack.empty()){idx.push_back(m);}
        else if (arr[stack.top()] < arr[i])
        {
            /* code */
            idx.push_back(stack.top());
        }
        else
        {
            while(!stack.empty() && arr[stack.top()] >= arr[i])
            {
                stack.pop();
            }
            if(stack.empty()){idx.push_back(m);}
            else{
                idx.push_back(stack.top());
            }
        }
        stack.push(i);
    }
    reverse(idx.begin(), idx.end());
    return idx;

}

int max_area_1d(vector<int> arr, int m)
{
    vector<int> left = nsl(arr, m); // get index of nearest smallest to left
    vector<int> right = nsr(arr, m); // get index of nearest smallest to right

    // cout << "nsl: " << endl;
    // for(int i =0; i <m; i++)
    // {
    //     cout << left[i] << " ";
    // }
    // cout << endl;

    // cout << "nsr: " << endl;
    // for(int i =0; i <m; i++)
    // {
    //     cout << right[i] << " ";
    // }
    // cout << endl;
    
    int max = 0;
    for(int i =0; i< m; i++){
        int curr = arr[i]*(right[i]-left[i]-1); 
        if(max < curr)
        {
            max = curr;
        };
    }

    return max;
}

int max_area(vector<vector<int>> arr, int n, int m){
    int max = 0;
    vector<int> height;
    for(int i =0; i < n; i++)
    {
        // cout << "int i: " << i <<endl;
        for(int j =0; j<m; j++)
        {
            // cout<< "    int j:" << j <<endl;
            if(i==0){height.push_back(arr[i][j]);}
            else
            {
                if(arr[i][j] == 0)
                {
                    height[j] = 0;
                }
                else
                {
                    height[j] += 1;
                }
            }
        // for(int k =0; k<m; k++)
        // {
        //     cout << height[k] << " ";
        // }
        // cout << endl;
        }
        int max_area = max_area_1d(height, m);
        cout << "the max area for row " << i <<" is "<< max_area << endl;
        if(max_area > max){max = max_area;}
    }
    return max;
}


int main()
{
    vector<vector<int>> arr = {{0,1,1,0},
                               {1,1,1,1},
                               {1,1,1,1},
                               {1,1,0,0}};
    int n = arr.size(); // rows
    int m = arr[0].size(); // cols

    int area = max_area(arr, n, m);

    cout << "max area in binary matrix is: " << area << endl;
}
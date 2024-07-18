#include<iostream>
#include<vector>
#include<stack>
#include<utility>

using namespace std;

vector<int> stock_span(vector<int> arr, int n){
        stack <pair<int, int> > stack; // (idx, value)
        vector<int> span;
        for(int i = 0; i <n; i++)
        {
            if(stack.empty())
            {
                cout << "case1"<<endl;
                span.push_back(1);
            }
            else if (stack.top().second > arr[i])
            {
                /* code */
                cout << "case2"<<endl;
                span.push_back(1);
            }
            else
            {
                cout << "case3"<<endl;
                while(!stack.empty() && stack.top().second < arr[i])
                {
                    cout << "3a" <<endl;
                    stack.pop();
                }
                if(stack.empty()){
                    span.push_back(i+1);
                }
                else{
                    span.push_back(i -stack.top().first);
                }
            }
            pair <int, int> p = make_pair(i, arr[i]);
            stack.push(p);
        }
    return span;

}

int main()
{
    vector<int> arr = {10, 4, 5, 90, 120, 80};
    int n = arr.size();

    vector<int> span = stock_span(arr, n);
    for(int i = 0; i < n; i++)
    {
        cout << span[i]<< " ";

    }
    cout << endl;
}
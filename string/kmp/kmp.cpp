#include<iostream>
#include<vector>
#include<string>

using namespace std;


vector<int> getLPS(string& P){
    vector<int> lps = {0};
    int i = 1;
    int length = 0;

    while (i < P.length()){
        if(P[i] == P[length]){
            i++, length++;
            lps.push_back(length);
        }
        else{
            if(length != 0) length = lps[length - 1]; // try to match for smaller length prefix
            else {
                lps.push_back(length); // cant match anymore, chain breaks
                i++;
            }
        }
    }
    return lps;
}

bool KMP(string& P, string& T, vector<int>& lps){
    int i = 0, j = 0;
    int N = T.length(), M = P.length();
    
    while(i < N && j < M){
        if (P[j] == T[i]){
            i++;
            j++;

            if (j == M) return true;
        }
        else{
            if(j != 0) j = lps[j-1];
            else{
                i++;
            }
        }
    }

    return false;
}

int main(){
    string T = "ABABABD";
    string P = "ABABD";

    vector<int> lps = getLPS(P);
    for(int i: lps){
        cout << i << " ";
    }
    cout << endl;
    cout << P << " present in " << T << " " << KMP(P, T, lps) << endl;
}
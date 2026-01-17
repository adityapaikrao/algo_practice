/**
 * @file kmp.cpp
 * @brief Implementation of the Knuth-Morris-Pratt (KMP) string searching algorithm.
 * 
 * This program demonstrates the KMP algorithm, which efficiently searches for occurrences of a pattern string (P) within a text string (T).
 * The algorithm achieves O(N + M) time complexity, where N is the length of the text and M is the length of the pattern, by preprocessing the pattern
 * to build a Longest Prefix Suffix (LPS) array. This array helps in skipping unnecessary character comparisons during the search phase.
 * 
 * Algorithm Intuition:
 * - The naive string search checks every possible alignment of P in T, leading to O(N*M) in the worst case (e.g., when many partial matches occur).
 * - KMP improves this by using the LPS array to "remember" how much of the pattern has already been matched. When a mismatch happens, instead of resetting
 *   the pattern pointer to the start, it shifts the pattern by the amount indicated by the LPS value, effectively reusing the knowledge of previous matches.
 * - This avoids backtracking in the text string, making the algorithm linear time. The LPS array is built by iterating through the pattern and tracking
 *   the longest prefix that is also a suffix for each substring, which informs how to handle mismatches efficiently.
 * - In the search phase, the algorithm aligns the pattern with the text, advancing both pointers on matches. On mismatch, it uses the LPS to jump ahead
 *   in the pattern without losing progress.
 * 
 * Key Benefits:
 * - Efficient for large texts and patterns.
 * - Useful in scenarios like text editors, DNA sequence matching, or any substring search where speed matters.
 * 
 * Example Usage:
 * - Input: Text "ABABABD", Pattern "ABABD"
 * - LPS for "ABABD": [0, 0, 1, 2, 0]
 * - Search result: Pattern is found in the text.
 */

/**
 * Computes the Longest Prefix Suffix (LPS) array for the given pattern string P.
 * 
 * The LPS array is a preprocessing step where each index i in the array stores the length of the longest proper prefix of P[0..i] that is also a suffix.
 * This array is crucial for the KMP search to determine how far to shift the pattern when a mismatch occurs.
 * 
 * Algorithm Intuition for LPS Construction:
 * - Start with LPS[0] = 0 (no proper prefix for a single character).
 * - Use two pointers: i for the current position in P, and length for the length of the current prefix match.
 * - If P[i] matches P[length], extend the match (increment both i and length, set LPS[i] = length).
 * - If not, fall back to the previous LPS value (length = LPS[length-1]) to find a shorter prefix that matches, or set LPS[i] = 0 and move i forward.
 * - This builds the array in linear time by reusing previously computed LPS values, avoiding redundant checks.
 * 
 * @param P The pattern string for which to compute the LPS array.
 * @return A vector of integers where each element LPS[i] represents the longest prefix suffix length for P[0..i].
 */
vector<int> getLPS(string& P);

/**
 * Performs the KMP string search to determine if the pattern P exists within the text T, using the precomputed LPS array.
 * 
 * This function iterates through the text and pattern simultaneously, using the LPS array to handle mismatches by shifting the pattern appropriately.
 * 
 * Algorithm Intuition for Search:
 * - Use two pointers: i for the text position, j for the pattern position.
 * - On a match (P[j] == T[i]), advance both pointers. If j reaches M (pattern length), a match is found.
 * - On mismatch, if j > 0, shift j to LPS[j-1] (the next possible match position based on prefix-suffix overlap).
 * - If j == 0, just advance i in the text (no overlap to leverage).
 * - This ensures no backtracking in T, maintaining linear time, as each character in T and P is processed a constant number of times.
 * 
 * @param P The pattern string to search for.
 * @param T The text string in which to search.
 * @param lps The LPS array for P, computed by getLPS.
 * @return True if P is found as a substring in T, false otherwise.
 */
bool KMP(string& P, string& T, vector<int>& lps);
#include<iostream>
#include<vector>
#include<string>

using namespace std;

/**/
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
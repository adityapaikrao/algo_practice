/**/

package main

import "fmt"

// Rabin-Karp algorithm for string pattern matching.
// Intuition: Instead of comparing the pattern with every substring of the text character by character,
// which would be O((n-m+1)*m) in the worst case, we use hashing to quickly check for potential matches.
// Compute a hash for the pattern and for each substring of the text of the same length.
// If hashes match, perform a full string comparison to confirm (to handle hash collisions).
// This makes the algorithm efficient in practice.
// Expected time complexity: O(n + m), where n is the length of the text and m is the length of the pattern.
// Calculation: Hashing the pattern takes O(m), and sliding through the text with rolling hash updates takes O(n).
// String comparisons are only done when hashes match, and with a good hash function, collisions are rare,
// so the total time remains linear. Worst case (many collisions) could degrade to O(n*m), but expected is O(n+m).
// The expectation is O(n + m + #matches * m) guaranteed when hashes match with probability less than 1/|m|.
func isPatternPresent(s, p string) bool {
	n := len(s)
	m := len(p)

	// pattern length greater than query
	if m > n {
		return false
	}

	hashP := NewRollingHash()
	for _, ch := range p {
		hashP.AddChar(ch)
	}

	hashS := NewRollingHash()
	for i, ch := range s {
		hashS.AddChar(ch)
		if hashS.Len() == hashP.Len() {
			if hashS.Hash() == hashP.Hash() && s[i-m+1:i+1] == p {
				return true
			}
			hashS.RemoveChar()
		}
	}

	return false
}

func main() {
	s := "butsad"
	p := "sad"

	fmt.Printf("pattern %s present in %s : %t", p, s, isPatternPresent(s, p))

}

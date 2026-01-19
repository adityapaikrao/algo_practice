package main

// RollingHash implements a rolling hash for efficient substring hashing in algorithms like Rabin-Karp.
// It maintains a deque for the sliding window and updates the hash incrementally.
//
// Implementation details:
// - Hash is computed as: hash = (hash * power + int(ch)) % mod when adding a character.
// - When removing a character, subtract its contribution: hash = (hash - (int(ch) * power^(len-1)) % mod + mod) % mod.
// - The deque ensures O(1) additions and removals, with hash updates in O(1) amortized (but O(n) in worst case for power calculation in RemoveChar; optimize by precomputing powers if needed).
//
// Suggestions for power and mod:
// - Power: Choose a prime > number of distinct characters in the alphabet (e.g., 31 for lowercase ASCII, 37 for mixed case, 101 for larger sets). This minimizes collisions.
// - Mod: Use a large prime like 1e9+7 or 1e9+9 to reduce hash collisions. Ensure it's > max possible hash (e.g., for strings up to length 1e5, mod > 31^1e5 is impractical, so rely on mod for wrapping).

import (
	"github.com/gammazero/deque"
)

type RollingHash struct {
	rollinghash int
	power       int
	mod         int
	q           deque.Deque[rune]
}

func NewRollingHash() *RollingHash {
	return &RollingHash{
		rollinghash: 0,
		power:       31,
		mod:         int(1e9 + 7),
		q:           deque.Deque[rune]{},
	}
}

func (rh *RollingHash) AddChar(ch rune) {
	rh.rollinghash = (rh.rollinghash*rh.power + int(ch)) % rh.mod
	rh.q.PushBack(ch)
}

func (rh *RollingHash) RemoveChar() {
	ch := rh.q.PopFront()

	p := 1
	for range rh.q.Len() {
		p *= rh.power
	}
	rh.rollinghash = (rh.rollinghash - (int(ch)*p+rh.mod)%rh.mod) % rh.mod
}

func (rh *RollingHash) Hash() int {
	return rh.rollinghash
}

func (rh *RollingHash) Len() int {
	return rh.q.Len()
}

'''
Problem statement
Given two strings, 'S' and 'T' with lengths 'M' and 'N', find the length of the 'Longest Common Subsequence'.

For a string 'str'(per se) of length K, the subsequences are the strings containing characters in the same relative order as they are present in 'str,'
 but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to K.

Example :
Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= M <= 10 ^ 3
0 <= N <= 10 ^ 3

Time Limit: 1 sec
Sample Input 1 :
adebc
dcadb
Sample Output 1 :
3
Explanation of the Sample Output 1 :
Both the strings contain a common subsequence 'adb', which is the longest common subsequence with length 3. 
Sample Input 2 :
ab
defg
Sample Output 2 :
0
Explanation of the Sample Output 2 :
The only subsequence that is common to both the given strings is an empty string("") of length 0.
'''

dp = []

# f(n, m) --->> LCS in (n ele of S, m ele of T)
def f(n, m, S, T):
    global dp
    if n != 0 and m == 0 or m != 0 and n == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    # if two chars are equal, LCS should inc by 1
    if S[n-1] == T[m-1]:
        dp[n][m] = f(n-1, m-1, S, T) + 1
    # else we have two possibilities
    # 1. leave char of S and make subsequence with T
    # 2. leave char of T and make Subsequence with S
    # Take max of it
    else:
        dp[n][m] = max(f(n-1, m, S, T), f(n, m-1, S, T))
    return dp[n][m]


def longest_common_subsequence(S, T):
    global dp
    n, m = len(S), len(T)
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    return f(n, m, S, T)

# Main function to handle input/output
def main():
    S = input().strip()
    T = input().strip()
    print(longest_common_subsequence(S, T))

if __name__ == "__main__":
    main()

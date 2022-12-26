def fib(n):
    global dp
    if dp[n] == -1:
        dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]


def main():
    global dp
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    fib(n)

    print(dp[n])
    return dp[n]


if __name__ == "__main__":
    main()

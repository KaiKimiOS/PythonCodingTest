# answer = ["" for _ in range(13)]
# answer[0] = "-"

# for i in range(1,13):
#     answer[i] = answer[i-1] + (" " * (3 ** (i-1))) + answer[i-1]


# while True:
#     try:
#         N = int(input())
#         print(answer[N])
#     except:
#         break


def func(k):
    if k == 0:
        print("-", end="")
        return
    func(k-1)
    print(" " * (3 ** (k-1)), end="")
    func(k-1)

while True:
    try:
        N = int(input())
        func(N)
        print()
    except:
        break
        
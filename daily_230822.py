

# 5177. 이진 힙

# import sys
# sys.stdin = open('input_5177.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     tree = list(map(int, input().split()))
#     result = 0
#
#     heap = [0] * (N+1)
#     root = 1
#
#     for idx in range(N):
#         if heap[root] == 0:
#             heap[root] = tree[idx]
#         else:
#             root += 1
#             heap[root] = tree[idx]
#
#         parent = root // 2
#         child = root
#
#         while heap[parent] > heap[child]:
#             heap[parent], heap[child] = heap[child], heap[parent]
#             child = parent
#             parent //= 2
#
#     end = N
#     while end != 1:
#         end //= 2
#         result += heap[end]
#
#     print(f'#{tc} {result}')



# 1232. 사칙연산

# import sys
# sys.stdin = open('input_1232.txt', 'r')
#
#
# def mid_rot(n):
#     if n:
#         mid_rot(c_left[n])
#         mid_rot(c_right[n])
#         if tree[n] not in '+-/*':
#             calc.append(int(tree[n]))
#         else:
#             if tree[n] == '+':
#                 B = calc.pop()
#                 A = calc.pop()
#                 calc.append(A+B)
#             elif tree[n] == '-':
#                 B = calc.pop()
#                 A = calc.pop()
#                 calc.append(A-B)
#             elif tree[n] == '*':
#                 B = calc.pop()
#                 A = calc.pop()
#                 calc.append(A*B)
#             elif tree[n] == '/':
#                 B = calc.pop()
#                 A = calc.pop()
#                 calc.append(A/B)
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [0] * (N+1)
#     c_left = [0] * (N+1)
#     c_right = [0] * (N+1)
#     calc = []
#
#     for _ in range(N):
#         arr = input().split()
#         tree[int(arr[0])] = arr[1]
#         if len(arr) == 4:
#             c_left[int(arr[0])] = int(arr[2])
#             c_right[int(arr[0])] = int(arr[3])
#
#     mid_rot(1)
#     print(f'#{tc} {int(calc[0])}')



# 18528. 노드의 합

# import sys
# sys.stdin = open('input_18528.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#     tree = [0] * (N+1)
#     for _ in range(M):
#         idx, val = map(int, input().split())
#         tree[idx] = val
#
#     if N % 2 == 1:
#         for i in range(N, 2, -2):
#             tree[i//2] = tree[i-1] + tree[i]
#     else:
#         tree[N//2] = tree[N]
#         for i in range(N-1, 2, -2):
#             tree[i//2] = tree[i-1] + tree[i]
#
#     print(f'#{tc} {tree[L]}')



# 4615. 노드의 합

import sys
sys.stdin = open('input_4615.txt', 'r')

def check(y, x):
    global board
    eight = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    center = board[x][y]
    for di, dj in eight:
        ni = x + di
        nj = y + dj
        if 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj] != center:
                stack.append([ni, nj])
                while board[ni][nj] != center:
                    ni += di
                    nj += dj
                    if 0 <= ni < N and 0 <= nj < N:
                        continue
                    else:
                        break


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    white = 0
    black = 0
    board = [[0] * N for _ in range(N)]
    board[N//2][N//2] = 2         # white = 2, black = 1
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1

    for _ in range(M):
        row, col, color = map(int, input().split())
        stack = []
        if color == 1:
            board[col-1][row-1] = 1
            check(row-1, col-1)
            while len(stack) != 0:
                stack.pop()
        else:
            pass

    for row1 in range(N):
        for col1 in range(N):
            if board[row1][col1] == 2:
                white += 1
            elif board[row1][col1] == 1:
                black += 1

    print(f'#{tc} {white} {black}')

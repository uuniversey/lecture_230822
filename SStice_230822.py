
#       4
#     2   1
#       3

# 참외밭

# import sys
# sys.stdin = open('test.txt', 'r')
#
# K = int(input())        # 참외의 개수
# l_list = []             # 길이의 리스트
# select = []             # 가장 큰 모서리를 알아내기 위한 리스트
#
# for _ in range(6):
#     direction, length = map(int, input().split())
#     l_list.append(length)       # 길이들을 리스트에 담음
#
# area = 0          # 제일 큰 모서리, 즉 큰 사각형의 넓이 초기값
# idx = 0           # 제일 큰 모서리일때의 인덱스
# for i in range(6):
#     if i == 5:    # 마지막 인덱스라면 리스트의 맨 앞이 붙어있는 선이므로
#         select.append(l_list[i] * l_list[0])
#     else:         # 그 밖에는 인접한 선과의 넓이 구하기
#         select.append(l_list[i] * l_list[i + 1])
#
#     if area < select[-1]:     # 가장 큰 모서리 알아내고 그 때의 인덱스 값 저장
#         area = select[-1]
#         idx = i
#
# result = area - select[(idx + 3) % 6]
# # 가장 큰 모서리에서 가장 먼 모서리 넓이 빼기 인덱스가 6개이므로 인덱스 3개 차이이다.
#
# print(result * K)





# 최소 힙 삽입

# data = [3, 7, 9, 2, 1, 5]   # 삽입할 데이터 하나씩 반복문으로 넣을 예정
# N = 6   # 데이터의 길이
#
# heap = [0] * (N+1)      # 0번 idx는 사용 x
# last_idx = 1            # 가장 마지막 위치 (초기화 root idx)
#
# # heap에 넣어 보자
# for idx in range(N):
#     if heap[last_idx] == 0:     # root 인덱스
#         heap[last_idx] = data[idx]
#     else:
#         last_idx += 1   # 들어갈 인덱스 마지막 위치
#         heap[last_idx] = data[idx]  # 마지막 위치에 값을 삽입
#
#         # 우선순위 비교를 위한 준비
#         parent = last_idx // 2      # 부모 노드 인덱스
#         child = last_idx           # 알아보기 쉽게 변수명 지정 (안해도 상관 x)
#
#         while heap[parent] > heap[child]:
#             # 부모 노드와 자식 노드를 교체
#             heap[parent], heap[child] = heap[child], heap[parent]
#             # 다음 부모노드와 자식 노드를 지정
#             child = parent
#             parent = child // 2
#
# print(heap)


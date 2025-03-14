# [Bronze III] 행렬 덧셈 - 2738 

[문제 링크](https://www.acmicpc.net/problem/2738) 

### 성능 요약

메모리: 33432 KB, 시간: 48 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2025년 3월 14일 18:03:12

### 문제 설명

<p>N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.</p>

### 출력 

 <p>첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.</p>

### Memo
#### Question:
import sys 

N, M = map(int, sys.stdin.readline().split())
A, B, sum_arr = [0]*N, [0]*N, [[0]*M]*N
for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    B[i] = list(map(int, sys.stdin.readline().split()))
for n in range(N):
    for m in range(M):
        sum_arr[n][m] = A[n][m] + B[n][m]

이 코드에 

3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

이걸 입력으로 줬을 때, 왜 sum_arr[0][0]가 4가 아닌 5야? 

#### Answer:
ChatGPT

코드에서 sum_arr = [[0]*M]*N 이 부분이 문제입니다.
이렇게 하면 sum_arr의 모든 행이 같은 리스트 객체를 참조하게 됩니다.

즉, sum_arr의 모든 행이 하나의 리스트를 공유하므로,
어떤 한 원소를 변경하면 모든 행에서 동일한 인덱스의 값이 함께 변경됩니다.

초기화된 sum_arr:
sum_arr = [[0, 0, 0],  # 이 리스트가 모든 행에 공유됨
           [0, 0, 0],
           [0, 0, 0]]

sum_arr[n][m] = A[n][m] + B[n][m] 연산이 실행되면,
모든 행이 같은 리스트를 참조하므로 한 곳이 바뀌면 다른 곳도 함께 바뀝니다.

해결 방법
다음과 같이 sum_arr를 각각의 독립적인 리스트로 초기화하면 해결됩니다.

sum_arr = [[0] * M for _ in range(N)]

이렇게 하면 sum_arr의 각 행이 서로 다른 리스트가 되어 문제가 발생하지 않습니다.

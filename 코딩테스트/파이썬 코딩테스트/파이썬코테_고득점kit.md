---
title: "python"
date: 
category: "코딩테스트"
tags: [Python, 코딩테스트]
---

# python

> 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

---

```python
베스트앨범
문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.

입출력 예
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]


from collections import Counter

def solution(genres, plays):
    answer = []
    songs = {}
    genre_total_plays = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in songs:
            songs[genre] = [(i, play)]
            genre_total_plays[genre] = play
        else:
            songs[genre].append((i, play))
            genre_total_plays[genre] += play

    sorted_genres = sorted(genre_total_plays, key=lambda x: genre_total_plays[x], reverse=True)

    for genre in sorted_genres:
        songs[genre].sort(key=lambda x: (x[1], -x[0]), reverse=True)
        selected_songs = songs[genre][:2]
        for song in selected_songs:
            answer.append(song[0])

    return answer


스택/큐

다리를 지나는 트럭
문제 설명
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

제한 조건
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = deque()
    trucks_waiting = deque(truck_weights)
    current_weight = 0
    
    while trucks_waiting or trucks_on_bridge:
        answer += 1
        
        if trucks_on_bridge:
            time, truck_weight = trucks_on_bridge[0]
            if answer - time >= bridge_length:
                current_weight -= truck_weight
                trucks_on_bridge.popleft()

        if trucks_waiting:
            if current_weight + trucks_waiting[0] <= weight:
                truck_weight = trucks_waiting.popleft()
                current_weight += truck_weight
                trucks_on_bridge.append((answer, truck_weight))

    return answer


주식가격
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = n - j - 1

    return answer


더 맵게
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) 
    
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            break

        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville) 
        new_scoville = min1 + (min2 * 2) 
        heapq.heappush(scoville, new_scoville)
        answer += 1

    return answer


디스크 컨트롤러
문제 설명
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

예를들어

- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청
와 같은 요청이 들어왔습니다. 이를 그림으로 표현하면 아래와 같습니다.
한 번에 하나의 요청만을 수행할 수 있기 때문에 각각의 작업을 요청받은 순서대로 처리하면 다음과 같이 처리 됩니다.

- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

하지만 A → C → B 순서대로 처리하면
- A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
- C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
- B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한 사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

import heapq

def solution(jobs):
    total_time = 0 
    elapsed_time = 0  
    job_count = len(jobs) 

    jobs.sort() 

    waiting_jobs = [] 

    while jobs or waiting_jobs:
        while jobs and jobs[0][0] <= elapsed_time:
            start_time, job_time = jobs.pop(0)
            heapq.heappush(waiting_jobs, (job_time, start_time))

        if waiting_jobs:
            job_time, start_time = heapq.heappop(waiting_jobs)
            elapsed_time += job_time
            total_time += elapsed_time - start_time
        else:
            elapsed_time += 1

    answer = total_time // job_count
    return answer


가장 큰 수
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    answer = ''.join(numbers)

    if answer[0] == '0':
        return '0'
    else:
        return answer


전력망을 둘로 나누기
문제 설명
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 2 이상 100 이하인 자연수입니다.
wires는 길이가 n-1인 정수형 2차원 배열입니다.
wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
1 ≤ v1 < v2 ≤ n 입니다.
전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

def solution(n, wires):
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    min_diff = float('inf')  # 최소 차이값 초기화
    
    def dfs(v, parent):
        nonlocal min_diff
        
        # 서브 그래프의 송전탑 개수 계산
        count = 1
        for neighbor in graph[v]:
            if neighbor != parent:
                count += dfs(neighbor, v)
        
        # 송전탑 개수의 차이 갱신
        diff = abs(n - 2 * count)
        min_diff = min(min_diff, diff)
        
        return count
    
    dfs(1, 0)  # DFS 탐색 시작
    
    return min_diff


모음 사전
문제 설명
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

제한사항
word의 길이는 1 이상 5 이하입니다.
word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
입출력 예
word	result
"AAAAE"	6
"AAAE"	10
"I"	1563
"EIO"	1189
입출력 예 설명
입출력 예 #1

사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA", "AAA", "AAAA", "AAAAA", "AAAAE", ... 와 같습니다. "AAAAE"는 사전에서 6번째 단어입니다.

입출력 예 #2

"AAAE"는 "A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", "AAAAU"의 다음인 10번째 단어입니다.

입출력 예 #3

"I"는 1563번째 단어입니다.

입출력 예 #4

"EIO"는 1189번째 단어입니다.

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']  # 알파벳 모음
    word_dict = {}  # 사전을 저장할 딕셔너리
    count = 0  # 단어의 순서 카운트
    
    def generate_words(curr_word):
        nonlocal count
        
        # 단어를 사전에 추가하고 카운트 증가
        word_dict[curr_word] = count
        count += 1
        
        # 단어의 길이가 5 이하일 때, 다음 글자를 추가하여 단어 생성
        if len(curr_word) < 5:
            for vowel in vowels:
                generate_words(curr_word + vowel)
    
    generate_words('')  # 빈 문자열부터 시작
    return word_dict[word]  # 주어진 단어의 순서 반환

조이스틱
문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer

# alphabet_to_num(char) 함수:

# 알파벳 문자를 숫자로 변환하는 함수입니다.
# 알파벳 'A'부터 'M'까지는 0부터 13까지의 숫자로 변환하고, 알파벳 'N'부터 'Z'까지는 12부터 1까지의 숫자로 변환합니다.
# 이는 알파벳 조작 시 위/아래로 조작하는 횟수를 나타내기 위한 변환입니다.
# for ch in name:

# 주어진 이름의 각 문자에 대해 반복합니다.
# alphabet_to_num 함수를 통해 각 문자를 숫자로 변환하고, answer에 더합니다.
# 이를 통해 이름을 완성하기 위해 필요한 위/아래 조작 횟수를 계산합니다.
# move = n - 1:

# move 변수를 초기화합니다. 이는 이름을 완성하기 위해 필요한 좌/우 이동 횟수를 나타냅니다.
# 초기값으로 n - 1을 설정하는 이유는 첫 글자는 조작하지 않아도 되기 때문입니다.
# for idx in range(n):

# 0부터 n-1까지의 인덱스에 대해 반복합니다. 각 인덱스는 현재 조작할 문자의 위치를 나타냅니다.
# next_idx = idx + 1:

# 다음 인덱스를 idx의 다음 위치로 설정합니다.
# while (next_idx < n) and (name[next_idx] == 'A'):

# 다음 인덱스가 이름의 범위 내에 있고, 해당 인덱스의 문자가 'A'인 동안 반복합니다.
# 연속된 'A' 문자의 개수를 확인하기 위한 과정입니다.
# distance = min(idx, n - next_idx):

# 현재 위치(idx)와 나머지 이름의 끝과의 거리 중 작은 값을 선택합니다.
# 이는 현재 위치에서 역으로 이동하여 이름의 끝까지 이동하는 경우를 고려하기 위한 값입니다.
# move = min(move, idx + n - next_idx + distance):

# move 값과 현재까지 계산된 좌/우 이동 횟수(idx + n - next_idx + distance) 중 작은 값을 선택하여 업데이트합니다.
# answer += move:

# answer에 좌/우 이동 횟수(move)를 더합니다.
# 이를 통해 이름을 완성하기 위해 필요한 좌/우 조작 횟수를 계산합니다.
# 최종적으로 answer를 반환합니다.


큰 수 만들기
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.

def solution(number, k):
    stack = [number[0]]  # 첫 번째 숫자를 스택에 넣어 시작
    for num in number[1:]:  # 두 번째 숫자부터 탐색
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 스택의 가장 위에 있는 숫자가 현재 숫자보다 작으면 스택에서 제거하고 k 감소
            stack.pop()
            k -= 1
        stack.append(num)  # 현재 숫자를 스택에 추가
    
    # k가 남아있는 경우 남은 k만큼 스택에서 숫자 제거
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)  # 스택에 남은 숫자들을 문자열로 결합하여 반환


게임 맵 최단거리
문제 설명
ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

지금부터 당신은 한 팀의 팀원이 되어 게임을 진행하려고 합니다. 다음은 5 x 5 크기의 맵에, 당신의 캐릭터가 (행: 1, 열: 1) 위치에 있고, 상대 팀 진영은 (행: 5, 열: 5) 위치에 있는 경우의 예시입니다.

위 그림에서 검은색 부분은 벽으로 막혀있어 갈 수 없는 길이며, 흰색 부분은 갈 수 있는 길입니다. 캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 게임 맵을 벗어난 길은 갈 수 없습니다.
아래 예시는 캐릭터가 상대 팀 진영으로 가는 두 가지 방법을 나타내고 있습니다.

첫 번째 방법은 11개의 칸을 지나서 상대 팀 진영에 도착했습니다.

두 번째 방법은 15개의 칸을 지나서 상대팀 진영에 도착했습니다.

위 예시에서는 첫 번째 방법보다 더 빠르게 상대팀 진영에 도착하는 방법은 없으므로, 이 방법이 상대 팀 진영으로 가는 가장 빠른 방법입니다.

만약, 상대 팀이 자신의 팀 진영 주위에 벽을 세워두었다면 상대 팀 진영에 도착하지 못할 수도 있습니다. 예를 들어, 다음과 같은 경우에 당신의 캐릭터는 상대 팀 진영에 도착할 수 없습니다.


게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

제한사항
maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

입출력 예
maps	answer
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1

from collections import deque

def solution(maps):
    # 게임 맵의 크기를 구함
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]
    
    # BFS를 위한 큐와 방문 체크 배열 초기화
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    
    # 시작 지점 (0, 0)을 큐에 넣고 방문 체크
    queue.append((0, 0))
    visited[0][0] = True
    
    # BFS 탐색 시작
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치가 상대 팀 진영인 경우 최단 거리를 반환
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        
        # 상하좌우 인접한 위치를 확인하며 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 게임 맵을 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽이 있는 경우 무시
            if maps[nx][ny] == 0:
                continue
            
            # 방문하지 않은 위치라면 큐에 넣고 방문 체크
            if not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                
                # 이전 위치까지의 최단 거리 + 1을 현재 위치에 저장
                maps[nx][ny] = maps[x][y] + 1
    
    # BFS를 마친 후에도 상대 팀 진영에 도착하지 못한 경우 -1 반환
    return -1


# 진법에 맞게 숫자를 표현 -> A 는 10 ~~~ F는 15
def convert_base(number, base):
    # 주어진 진법에 맞게 숫자를 표현하는 함수
    if number == 0:
        return '0'
    digits = []
    while number:
        if number % base >= 10:
            digits.append(chr(ord('A') + (number % base) - 10))
        else:
            digits.append(str(number % base))
        number //= base
    return ''.join(reversed(digits))

def solution(n, t, m, p):
    answer = ''
    numbers = ''
    current_number = 0

    while len(numbers) < t * m:
        numbers += convert_base(current_number, n)
        current_number += 1

    for i in range(p-1, t * m, m):
        answer += numbers[i]

    return answer

타겟 넘버
문제 설명
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.


def solution(numbers, target):
    count = 0
    queue = [(0, 0)]  # 현재까지의 합과 인덱스를 저장하는 큐
    
    while queue:
        current_sum, idx = queue.pop(0)
        
        if idx == len(numbers):
            if current_sum == target:
                count += 1
        else:
            queue.append((current_sum + numbers[idx], idx + 1))
            queue.append((current_sum - numbers[idx], idx + 1))
    
    return count

최소직사각형
문제 설명
명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

명함 번호	가로 길이	세로 길이
1	60	50
2	30	70
3	60	30
4	80	40
가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다. 하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다. 이때의 지갑 크기는 4000(=80 x 50)입니다.

모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

class Solution {
    public int solution(int[][] sizes) {
        int maxWidth = 0; // 가장 긴 가로 길이
        int maxHeight = 0; // 가장 긴 세로 길이
        
        for (int[] size : sizes) {
            int width = size[0];
            int height = size[1];
            
            if (width > height) {
                int temp = width;
                width = height;
                height = temp;
            }
            
            if (width > maxWidth) {
                maxWidth = width;
            }
            if (height > maxHeight) {
                maxHeight = height;
            }
        }
        
        return maxWidth * maxHeight;
    }
}


소수 찾기
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

from itertools import permutations as pe


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = set()
    for i in range(1, len(numbers) + 1):
        perms = pe(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            nums.add(num)
    
    for num in nums:
        if is_prime(num):
            answer += 1
    
    return answer


피로도
문제 설명
XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다. "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, "소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다. 예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 위해서는 유저의 현재 남은 피로도는 80 이상 이어야 하며, 던전을 탐험한 후에는 피로도 20이 소모됩니다.

이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다. 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
k는 1 이상 5,000 이하인 자연수입니다.
dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.
dungeons의 가로(열) 길이는 2 입니다.
dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.
"최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다.
"최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다.
서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.

from itertools import permutations
def solution(k, dungeons):
    clears = []
    dungeons_permutaions = list(permutations(dungeons, len(dungeons)))
    
    for case in dungeons_permutaions:
        clear = 0
        stamina = k
        
        for dungeon in case:
            if stamina >= dungeon[0]:
                stamina -= dungeon[1]
                clear += 1

        clears.append(clear)
    return max(clears)

전력망을 둘로 나누기
문제 설명
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 2 이상 100 이하인 자연수입니다.
wires는 길이가 n-1인 정수형 2차원 배열입니다.
wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
1 ≤ v1 < v2 ≤ n 입니다.
전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    min_diff = float('inf') 
    
    def dfs(v, parent):
        nonlocal min_diff
        
        count = 1
        for neighbor in graph[v]:
            if neighbor != parent:
                count += dfs(neighbor, v)
        
        diff = abs(n - 2 * count)
        min_diff = min(min_diff, diff)
        
        return count
    
    dfs(1, 0) 
    
    return min_diff

모음 사전
문제 설명
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

제한사항
word의 길이는 1 이상 5 이하입니다.
word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']  
    word_dict = {}  
    count = 0  
    
    def generate_words(curr_word):
        nonlocal count
        
        word_dict[curr_word] = count
        count += 1
        
        if len(curr_word) < 5:
            for vowel in vowels:
                generate_words(curr_word + vowel)
    
    generate_words('')  
    return word_dict[word] 

H-Index
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.


def solution(citations):
    citations.sort(reverse=True) 
    
    print(citations)
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i  
    
    return len(citations) 

문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
입출력 예
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

def solution(progresses, speeds):
    answer = []
    plist = [x+y for x,y in zip(progresses, speeds)]
    count = 0
    for i in range(len(plist)):
        if len(plist) == 0:
            break
        while plist[0] < 100:
            plist = [x + y for x, y in zip(plist, speeds)]
        while len(plist) > 0 and plist[0] >= 100:
            plist.pop(0)
            speeds.pop(0)
            count += 1
        
        answer.append(count)
        count = 0
    return answer

문제 설명
운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

def solution(n, lost, reserve):
    clothes = [1] * n  
    
    for i in lost:
        clothes[i-1] -= 1  
    
    for i in reserve:
        clothes[i-1] += 1  
    
    for i in range(n):
        if clothes[i] == 0:  
            if i > 0 and clothes[i-1] == 2: 
                clothes[i] += 1
                clothes[i-1] -= 1
            elif i < n-1 and clothes[i+1] == 2:  
                clothes[i] += 1
                clothes[i+1] -= 1
    count = 0 
    for c in clothes:
        if c > 0:
            count += 1
    
    return count

구명보트
문제 설명
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

def solution(people, limit):
    people.sort()  
    left = 0  
    right = len(people) - 1  
    count = 0  

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  
        right -= 1  
        count += 1  

    return count

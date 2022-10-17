N,M = map(int,input().split())
# N : 행
# M : 얄
cards = [] # 카드 배열
# 카드 숫자 입력받기
for i in range(N): # 각 행에 대해서 
    row_list = list(map(int,input().split())) # 리스트로 입력받아
    cards.append(row_list) # 2차원 배열로 저장
row_min = 0 # 행의 최소값 저장 변수

for i in range(N):
    tmp = min(cards[i])
    if tmp>row_min:
        row_min = tmp
print(row_min)
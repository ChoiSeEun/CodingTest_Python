N,M,K = list(map(int,input().split()))
# N : 배열의 전체 개수
# M : 더할 개수 
# K : 연속해서 더할 수 있는 인덱스 개수
num_list = list(map(int,input().split())) # 리스트 입력받기
num_list = sorted(num_list,reverse=True) # 리스트 내림차순 정렬
cnt = 0 # 최대값 반복 인덱스
total_cnt = 0 # 전체 횟수
sum = 0  # 결과값
while(total_cnt!=M): 
    if cnt<3: # 최대 연속 갯수 이하인 경우
        sum += num_list[0] # 최대값 더하기
        # print(sum)
        cnt += 1 # 최대값 반복 인덱스 증가
        total_cnt += 1 # 전체 횟수 증가
    else: # 최대 연속 갯수를 넘은 경우
        sum += num_list[1] # 두번째 최대값 더하기
        # print(sum)
        cnt = 0 # 최대값 반복 인덱스 초기화
        total_cnt += 1 # 전체 횟수 증가 
print(sum)


 # ----------------------------- 230104 답안 ------------------------------------


# ----------------------------- 예시 답안 ------------------------------------
def possible(answer): # 현재 설치된 구조물이 가능한 구조물인지 확인 
    for x,y,stuff in answer:
        if stuff == 0: # 설치된 것이 기둥인 경우 
            # 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위
            if y ==0 or [x-1,y-1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False # 정상이 아니면 거짓 반환
        elif stuff ==1 : # 설치된 것이 보인 경우 
            # 한 쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시에 연결 
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y-1] in answer and [x+1,y,1] in answer):
                continue
            return False 
        return True 

def solution(n,build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate ==0: #삭제하는 경우
            answer.remove([x,y,stuff]) # 삭제를 해서
            if not possible(answer): # 가능한 구조물이 아니라면 
                answer.append([x,y,stuff]) # 다시 설치 
        if operate ==1: # 설치하는 경우 
            answer.append([x,y,stuff]) # 설치를 해서
            if not possible(answer): # 가능한 구조물이 아니라면 
                answer.remove([x,y,stuff]) # 다시 제거 
    return sorted(answer)
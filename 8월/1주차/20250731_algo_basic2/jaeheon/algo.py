# 계란 내구도, 무게가 정해져있다
# 상대 계란의 무게만큼 내구도가 깎이게 된다.
# 0 이하가 되는 순간 계란이 깨지게 된다.
# 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제


# 가장 왼족읜 계란을 든다
# 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다
# 단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다
# 이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다
# 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다
# 단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 치는 과정을 종료한다


def beat(eggs,n):
  count = 0
  current_idx = 0
  
  while True:
    if current_idx >n:
      break
    if eggs[next_idx][s] == 0:
      current_idx = next_idx

    next_idx = current_idx + 1

    
    current_eggs = eggs[current_idx][0]-eggs[next_idx][1]
    next_eggs = eggs[next_idx][0]-eggs[current_idx][1]
    current_eggs = current_eggs if current_eggs > 0 else 0
    next_eggs = next_eggs if next_eggs>0 else 0

    if current_eggs == 0:
      count+=1
    if next_eggs == 0:
      count += 1
    
    eggs[next_idx][0] = next_eggs
  
  return count
  


n = int(input())
eggs = []
for _ in range(n):
  s,w = map(int,input().split())
  eggs.append((s,w))

result = beat(eggs,n)

print(result)
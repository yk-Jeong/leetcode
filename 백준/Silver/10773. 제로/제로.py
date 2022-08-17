K = int(input())

num_list = []
for _ in range(K):
  a = int(input())
  if a == 0:
    num_list.pop()
    # remove: 지정한 위치 값과 같은 값을 검색한 다음 '처음 값'을 삭제하므로, 원하지 않는 값이 삭제될 수 있음 - 따라서 사용하면 안 됨 
  else:
    num_list.append(a)

print(sum(num_list))
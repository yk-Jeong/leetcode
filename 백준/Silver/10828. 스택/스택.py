import sys 
input = sys.stdin.readline

N = int(input())

# command: push, pop, size, empty, top 
def stack(command):
  # 1. push 
  if command.startswith('push'):
    test_stack.append(order[1])
  
  # 2. pop
  elif command == 'pop':
    if not test_stack:
      print(-1)
    else: 
      print(test_stack.pop())

  # 3. skze
  elif command == 'size':
    print(len(test_stack))

  # 4. empty
  elif command == 'empty':
    if not test_stack:
      print(1)
    else: 
      print(0)

  # 5. top
  elif command == 'top': 
    if not test_stack:
      print(-1)
    else: 
      print(test_stack[-1])
      
test_stack = []
for _ in range(N):
  order = input().split()
  command = order[0]
  stack(command)

import sys 
N = int(sys.stdin.readline())

test_stack = []
for _ in range(N):
  word = sys.stdin.readline().split()
  command = word[0]

  # 1. push 
  if command == 'push':
    num = word[1]
    test_stack.append(num)
  
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
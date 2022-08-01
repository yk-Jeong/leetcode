H, M = map(int, input().split())
if H != 0:
  if M >= 45:
    print(f'{H} {M - 45}')
  else:
    print(f'{H - 1} {15 + M}')
else:
  if M >= 45:
    print(f'{H} {M - 45}')
  else: 
    print(f'23 {15 + M}')
num_list = [int(input()) for _ in range(10)]
num_mod_list = [num_list[i] % 42 for i in range(len(num_list))]
print(len(set(num_mod_list)))
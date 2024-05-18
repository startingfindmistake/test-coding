T = int(input())
for i in range(1, T+1):
N = int(input())
print(f"#{i}")
print("1")
prev_list = [1]
for j in range(0, N-1):
cur_list = [1]
for k in range(len(prev_list)-1):
cur_list.append(prev_list[k] + prev_list[k+1])
cur_list.append(1)
prev_list = cur_list.copy()
result = " ".join(list(map(str, cur_list)))
print(result)
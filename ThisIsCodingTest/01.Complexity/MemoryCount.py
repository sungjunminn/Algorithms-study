from random import randint
import time

array = []
for _ in range(10000): #
    array.append(randint(1, 100))

start_time = time.time() #

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index > array[j]]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
print('선택 정렬 시간 측정:', end_time - start_time)

sort_start_time = time.time()

array.sort()

sort_end_time = time.time()

print("sort 시간:", sort_end_time - sort_start_time)

# 선택 정렬 시간측정 : 8.62038803100586
# Sort 정렬 시간측정 : 0.0010328292846679688
def TwoPointer1(data, m, n):
    interval_sum = 0
    count = 0
    end = 0
    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += data[end]
            end += 1
        if interval_sum == m:
            count += 1
        interval_sum -= data[start]
    return count

print(TwoPointer1([1,2,3,2,5], 5, 5))

def TwoPointer2(a, b, n, m):
    result = [0] * (n + m)
    i, j, k = 0, 0, 0
    while i < n or j < m:
        if j >= m or (i < n and a[i] <= b[j]):
            result[k] = a[i]
            i += 1
        else:
            result[k] = b[j]
            j += 1
        k += 1
    return result

print(TwoPointer2([1, 3, 5], [2, 4, 6, 8], 3, 4))
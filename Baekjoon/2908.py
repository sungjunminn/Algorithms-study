a, b = map(str, input().split())
sangsu_a = list(a)[::-1]
sangsu_b = list(b)[::-1]

sangsu_A = sangsu_a[0] + sangsu_a[1] + sangsu_a[2]
sangsu_B = sangsu_b[0] + sangsu_b[1] + sangsu_b[2]

if sangsu_A > sangsu_B:
    print(sangsu_A)
elif sangsu_A < sangsu_B:
    print(sangsu_B)
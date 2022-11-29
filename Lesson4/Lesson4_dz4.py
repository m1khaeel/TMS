

x = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
y = [(3, 3, 3), (2, 2, 2), (1, 1, 1)]
z = [(2, 2, 2), (3, 3, 3), (4, 4, 4)]

res = [(a[i] * b[i] * c[i]) for i, (a, b, c) in enumerate(((x[0], y[0], z[0]), (x[1], y[1], z[1]), (x[2], y[2], z[2])), 0)]
# res = [(x[i][0] * y[i][1] * z[i][2]) for i in range(len(x))]
print(res, '\n', len(res))



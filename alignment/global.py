f, s = input().split(' ')
n = len(f) + 1
m = len(s) + 1
def_value = 28
# 1 - up, 0 - diag, -1 - left, 28 - start
a = [[(0, def_value) for i in range(m)] for j in range(n)]
for i in range(1, n):
    a[i][0] = (-i, 1)
for i in range(1, m):
    a[0][i] = (-i, -1)
for i in range(1, n):
    for j in range(1, m):
        best = (-n - m, 0)
        if a[i - 1][j - 1][0] > best[0]:
            best = (a[i - 1][j - 1][0], 0)
        if a[i - 1][j][0] > best[0]:
            best = (a[i - 1][j][0], 1)
        if a[i][j - 1][0] > best[0]:
            best = (a[i][j - 1][0], -1)
        if (f[i - 1] == s[j - 1]) and (best[1] == 0):
            a[i][j] = (best[0] + 1, best[1])
        else:
            a[i][j] = (best[0] - 1, best[1])

f_ans, s_ans = "", ""
cur_i = n - 1
cur_j = m - 1
while a[cur_i][cur_j][1] != def_value:
    new_cur_i, new_cur_j = cur_i, cur_j
    if a[cur_i][cur_j][1] == 0:
        f_ans += f[cur_i - 1]
        s_ans += s[cur_j - 1]
        new_cur_i = cur_i - 1
        new_cur_j = cur_j - 1
    if a[cur_i][cur_j][1] == -1:
        f_ans += '_'
        s_ans += s[cur_j - 1]
        new_cur_j = cur_j - 1
    if a[cur_i][cur_j][1] == 1:
        f_ans += f[cur_i - 1]
        s_ans += '_'
        new_cur_i = cur_i - 1
    cur_i = new_cur_i
    cur_j = new_cur_j
f_ans = f_ans[::-1]
s_ans = s_ans[::-1]

print(f_ans, s_ans)


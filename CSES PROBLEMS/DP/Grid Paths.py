import sys
n = int(input())
MOD = 10**9 + 7

vals = []
fal = True

# First row
output = list(input().strip())
for i in range(n):
    if output[i] == "." and fal:
        output[i] = 1
    else:
        fal = False
        output[i] = 0
vals.append(output)

if n == 1:
    print(vals[-1][-1] % MOD)
    sys.exit()

for _ in range(1, n):
    row = input().strip()
    out = []
    for j in range(n):
        if row[j] == "*":
            out.append(0)
        elif j == 0:
            out.append(1 if vals[-1][j] == 1 else 0)
        else:
            out.append((vals[-1][j] + out[j - 1]) % MOD)
    vals.append(out)

print(vals[-1][-1] % MOD)

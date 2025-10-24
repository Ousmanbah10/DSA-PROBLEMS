def query(l, r):
    """Return True if subarray arr[l:r+1] contains any 1."""
    return any(arr[l:r + 1])


def find_ones(l, r):
    # If no 1 in this entire range, stop early
    if not query(l, r):
        return

    # Base case: single element
    if l == r:
        result.append(l)
        return

    mid = (l + r) // 2

    # Check left half
    find_ones(l, mid)

    # Check right half
    find_ones(mid + 1, r)


# --- Input handling ---
n = int(input().strip())
arr = list(map(int, input().strip().split()))

result = []
find_ones(0, n - 1)

# --- Output ---
print(" ".join(map(str, result)))



# SECOND
def query(l, r):
    """Return True if subarray arr[l:r+1] contains any 1."""
    return any(arr[l:r + 1])


# --- Input handling ---
n = int(input().strip())
arr = list(map(int, input().strip().split()))

result = []

# --- Linear search for 1s ---
for i in range(n):
    if query(i, i):   # check single element
        result.append(i)

# --- Output ---
print(" ".join(map(str, result)))

import sys

def query(r, c):
    print(f"? {r} {c}")
    sys.stdout.flush()
    response = int(input())
    if response == -1:
        sys.exit()
    return response

def answer(r, c):
    print(f"! {r} {c}")
    sys.stdout.flush()
    sys.exit()

def solve():
    col2_result = query(3, 2)
    col4_result = query(3, 4)
    
    if col2_result == 1:
        row2_result = query(2, 2)
        row4_result = query(4, 2)
        
        if row2_result == 1:
            treasure_row = 1
        elif row4_result == 1:
            treasure_row = 3
        else:
            treasure_row = 4
        
        col1_result = query(treasure_row, 1)
        if col1_result == 1:
            treasure_col = 1
        else:
            treasure_col = 2
    
    elif col4_result == 1:
        row2_result = query(2, 4)
        row4_result = query(4, 4)
        
        if row2_result == 1:
            treasure_row = 1
        elif row4_result == 1:
            treasure_row = 3
        else:
            treasure_row = 4
        
        col3_result = query(treasure_row, 3)
        if col3_result == 1:
            treasure_col = 3
        else:
            treasure_col = 4
    
    else:
        treasure_col = 4
        
        row2_result = query(2, 5)
        row4_result = query(4, 5)
        
        if row2_result == 1:
            treasure_row = 1
        elif row4_result == 1:
            treasure_row = 3
        else:
            treasure_row = 4
    
    answer(treasure_row, treasure_col)

if __name__ == "__main__":
    solve()
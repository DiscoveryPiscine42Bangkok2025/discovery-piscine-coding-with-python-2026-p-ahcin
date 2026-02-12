#!/usr/bin/env python3

def checkmate(board):
    rows = board.strip().split('\n')
    size = len(rows)
    
    for row in rows:
        if len(row) != size:
            # print("not square")
            return
    
    king_position = (-1, -1)
    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                if king_position != (-1, -1):
                    # print("more than 1 king")
                    return
                king_position = (r, c)
                
    if king_position == (-1, -1):
        # print("0 king")
        return
    
    if is_check(king_position, rows, size):
        print("Success")
    else:
        print("Fail")
    
def is_check(king_position, rows, size):
    kr, kc = king_position
    
    # R, Q
    straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            target = rows[r][c]
            if target in ('R', 'Q'): return True
            if target != '.': break
            r, c = r + dr, c + dc
            
    diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal:
        r, c = kr + dr, kc + dc
        
        if 0 <= r < size and 0 <= c < size:
            if rows[r][c] == 'P' and r == kr + 1:
                return True
            
        while 0 <= r < size and 0 <= c < size:
            target = rows[r][c]
            if target in ('B', 'Q'): return True
            if target != '.': break
            r, c = r + dr, c + dc

    return False
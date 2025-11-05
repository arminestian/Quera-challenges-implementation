king, queen, bishop, knight, rook, pawn = map(int, input().split())
print(1 - king, 1 - queen, 2 - bishop, 2 - knight, 2 - rook, 8 - pawn)
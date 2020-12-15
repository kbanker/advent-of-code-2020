f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def find_seat_ID(seat):
    row_binary = seat[:7]
    col_binary = seat[7:]

    row = list(range(128))
    col = list(range(8))

    for x in row_binary:
        mid = int(len(row) / 2)
        if x == 'F':
            row = row[:mid]
        elif x == 'B':
            row = row[mid:]

    for x in col_binary:
        mid = int(len(col) / 2)
        if x == 'L':
            col = col[:mid]
        elif x == 'R':
            col = col[mid:]

    return row[0] * 8 + col[0]

sid = 0
seats = []
for line in lines:
    s = find_seat_ID(line)
    seats.append(s)
    if s > sid:
        sid = s

for i in range(sid):
    if i not in seats:
        if i+1 in seats and i-1 in seats:
            print(i)

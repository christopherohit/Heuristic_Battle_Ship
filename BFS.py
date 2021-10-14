do_thi = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : [],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

diem_qua = []
hang_cho = []

def bfs(diem_qua , do_thi , diem):
    diem_qua.append(diem)
    hang_cho.append(diem)

    while hang_cho:
        m = hang_cho.pop(0)
        print(m, end=" ")

        for i in do_thi[m]:
            if i not in diem_qua:
                diem_qua.append(i)
                hang_cho.append(i)

print("BFS:" ,end= " ")
bfs(diem_qua, do_thi , '5')
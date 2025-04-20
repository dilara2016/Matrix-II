x = [[2,3,7],
    [9,1,5],
    [6,5,9]]

answer = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j] = answer + x[i][j]

for r in answer:
    print(r)

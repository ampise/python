m1 = [[0, 2], [-2, -5]]
m2 = [[6, -6], [3, 0]]
m3 = []

if len(m1[0]) == len(m2):
    m1Row = 0
    while m1Row < len(m1):
        m3.append([])
        m2Column = 0
        while m2Column < len(m2[m1Row]):
            mm = 0
            for i in range(len(m1[m1Row])):
                m1Element = m1[m1Row][i]
                m2Element = m2[i][m2Column]
                mm += m1Element * m2Element
            m3[m1Row].append(mm)
            m2Column += 1
        m1Row += 1
    print(m3)
else:
    print("Sorry! The dimensions of the matrices don't match.")

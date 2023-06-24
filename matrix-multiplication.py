import os
os.system("clear")

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[7, 8], [9, 10], [11, 12]]
# m3 = [[58, 64], [139, 154]]

# Define result matrix
m3 = []
for i in range(len(m1)):
    m = []
    for j in range(len(m2[0])):
        m.append(0)
    m3.append(m)

# Perform matrix multiplication
    for rM1 in range(len(m1)):
        for cM1 in range(len(m1[0])):
            m1_element = m1[rM1][rM1]
            mm_element = 0
            for cM2 in range(len(m2[0])):
                m2_element = m2[cM1][rM1]
                mm_element += m1_element * m2_element
            print(m1_element, m2_element,
                  m1_element * m2_element, mm_element)

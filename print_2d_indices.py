r = [[9,5,4], [4,5,2], [7,6,3]]
def print_indices(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print("[" + str(i) + "]" + "[" + str(j) + "]", end = ' ')
        print()
print_indices(r)
'''
[0][0] [0][1] [0][2] 
[1][0] [1][1] [1][2] 
[2][0] [2][1] [2][2]
'''

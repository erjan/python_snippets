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

#better more fully covering function
def print_indices(x):
    print("the matrix, size: " + str(width) + "x" + str(height))    
    if height == 1:
        print("one liner")
        for i in range(width):
            for j in range(height):            
                print("[" + str(i) + "]" + "[" + str(j) + "]", end='\t')    
    elif width ==1:
        print("column")
        for i in range(width):
            for j in range(height):            
                print("[" + str(i) + "]" + "[" + str(j) + "]")    
    else:
        print("random nxm matrix")
        print("width: " + str(width) + " ,height: " + str(height))
        for i in range(height):
            for j in range(width):            
                print("[" + str(i) + "]" + "[" + str(j) + "]",end= '\t')
            print()

import csv
with open('data1.csv') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))
data = [[int(y) for y in x] for x in data]

#Converting the quoted arrays to digits

import numpy
data = numpy.array(data)                                     #Converting to a matrix form for easy view

a = [0,3,6]                                                  #Array will be used in looping for Sudoku Regions
zeros = [1,2,3]                                              #Array initiating While loop
while len(zeros) > 0:                                        #Loop continued till all the zeros are filled

    for r in a:                                              #r & c are the Loops run for getting 9 regions in each while loop 
        for c in a:
            
                loop = [0,1,2]                               #variable will be used in getting 9 elements of each region 
                for i in loop:
                    for j in loop:
                        region=[[data[r,c],data[r,c+1],data[r,c+2]],            #generating region from r & c
                          [data[r+1,c],data[r+1,c+1],data[r+1,c+2]],
                          [data[r+2,c],data[r+2,c+1],data[r+2,c+2]]]
                        
                        if region[i][j] == 0:                                   #Check whether the element is filled or not
                            x = r+i                                             #Getting the actual row and column co-ordinates
                            y = c+j
                            
                            cols = data.transpose()                             #Generating the column matrix for getting columns
                            arr = numpy.concatenate((region[0],region[1],region[2],data[x],cols[y]))                #getting all digits that comes in the region, row and column of the element to be filled
                            total = [1,2,3,4,5,6,7,8,9]                                                             #array of 1-9 digits
                            ans = list(set(total) - set(arr))                                                       #getting the digits not present in the row,column or region of the element
                            
                            if len(ans) == 1:                                   #filling the place only if one digit is present in 'ans' to avoid wrong filling
                                data[x][y] = ans[0]                             #filling the data

    zeros = []                                                                  #initiating variables to get remaining zeros
    temp = []
    for t in range(0,8):
        temp = [i for i, x in enumerate(data[t]) if x == 0]                     #getting zeros row-wise
        if len(temp) > 0:                                                       #if zeros present
            zeros.insert(len(zeros),temp)                                       #filling the variable checked in while loop

final = []                                                                      #converting matrix to a csv array
data_list = list(data)
for l in range(0,8):
    test = list(data_list[l])
    final.insert(len(final),test)
    print(final[l])

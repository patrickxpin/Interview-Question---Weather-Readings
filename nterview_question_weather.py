# used islice fucntion to make an iterator that returns selected elements from the iterable object
from itertools import islice

with open("weather.dat", "r") as datafile: 
    
    # read the rest of the file lines, slicing off the 1st, 2nd and last(33) columns (i.e unwanted lines)
    myDataList = (line.split() for line in islice(datafile, 2,32)) 
    
    # store months and spreads values into a myDataList tupple, removing any occurences of * character
    spreads = [(int(col[0]),int(col[1].replace("*", ""))-int(col[2].replace("*", ""))) for col in myDataList] 

    # print the month with the highest spread
    
    print '{}, {}'.format(*(max(spreads, key = lambda i : i[1]))) #A little formating of the value returned to remove the brackets
    
datafile.close() 

# Interview-Question---Weather-Readings
Task response to JUMOw technical assessment

The task was done in Python Language

# Task Description

Write a program to find the row with the maximum spread in the weather.dat file, where spread is defined as the difference between MxT and MnT. For example, the spread for day 2 was (79 - 63) = 16.

Your program should print the day of the month and spread to standard output

# Problem Understanding

The problem is to print the month with the highest spread. From the weather dat file, the 1st, 2nd and 3rd columns are all we need.

The file needs cleaning to discard unwanted rows of data like the 1st, 2nd, and last (33) before processing to avoid errors.

To reduce memory requirements by assigning variables, I decided to read the required columns (1,2,3) for the right rows (3 - 32) into a list, then calculate the spreads for each row into a tupple from which i derived the maximum spread for output. 


# Steps Followed - Algorithm

Step 1. Read the file in reading mode into memory

Step 2. Read line by line into a list data variable 

Step 3. Slice off unwanted lines; lines 1,2 and 33.

Step 4. for each line in the sliced datafile:

Step 5.   Read the first 3 columns of each line

Step 6.   Remove unwanted characters from the data values

Step 7.   Calculate spread by subtracting 3rd from 2nd column

Step 8.   Store the month and its spread into a tupple data structure

Step 9. Return the month and spread with the maximum value on using the second index; i[1] as the key. 

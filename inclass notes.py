# 9/13/23
'''
list1 = [1,2,3,4,5]
list2 = ["milk", 'frog', 'toad', 'cow']

for i in list1:
    print(i)
    
for h in list2:
    print(h)
    
average = 0
count = 0

#range function
n = 4
for i in range(n):
    print(i)
    #going to stop at right before the number listed there
    #use the break function to break out of the code loop
'''
#delete '''
'''
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print("done!")
'''
'''
        #finish statement ends with the current iteration and jobs to the top of the loop and starts the net iteration'

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("done!")
    #can rewrite a for loop using a while loop
    
    #range(0,3) can be used like this or range(2,5)

#roth IRA practice

maxcontribution = 6500
total_invested = 0
balance = 0
#invest max every year for 40 years
for i in range(40):
    if i%3 == 0:
        maxcontribution += 500
    total_invested += maxcontribution
    balance += maxcontribution
    #assume 1.1 roi
    balance = balance*1.1

print("you invested $", total_invested)
print("you have a balance of ", balance)
'''
#9/18/23 - new stuff -formatting text for output
'''
int_var = 3
float_var = 2.3523
print('%2d%4.2f' % (int_var, float_var))
#• d – integer
#• f – float
#• .xxxxx number of digits after decimal
#• xxxx. Character spaces for the output

'''


#9/20/23  -formatting text for output
'''
int1 = 1000
float2 = 17.389058
print("%2d and %10.3f" %(int1, float2)) 

'''
# counting in python
#range(x,y,z - what to count up by )
'''
for i in range(1,11,2):
    print(i)
for i in range(11,1,-2):
    print(i)
'''
#handle = open(filename, mode)
#mode input is optional and should be ‘r’ (default) if we are
#planning to read the file and 'w' if we are going to write to the
#file
#handle = open(filename, mode)
'''
fh = open('fightsong.txt')
count = 0
for line in fh:
    count += 1
    print(line)

print("there are", count, "line" )
'''
#9/25/23 indexing
'''
fruit = 'bananas are great'
print(fruit[0:17:2])
print(len(fruit))
handle = open('mbox-short.txt')
for i in handle:
    print(i)

fs = open('fightsong.txt')
num_line = 0
fight_line = 0
for l in fs:
    num_line +=1
    if "Fight!" in l:
        fight_line += 1
print("Percent Fight:", fight_line/num_line)
'''
#10/2/23
'''
fh = open('fightsong.txt')
count = 0
for i in fh:
    count += 1
    if count == 8:
        print(i)
   '''     
#there are find and rfind string functions, replace functions
#parsing and extracting
#read() function
    # 'a'- append to the end of file
    # 'w' - overwrite any exisiting content, w, or make a new file
    # 'x' - if there exist a file, give an error, or else will create a new file to write
'''       
fh = open('fightsong.txt', 'a')
fh.write("\nGood thing for special teams.")
fh.close()
        
fh = open('fightsong copy.txt', 'w')
fh.write("\nGood thing for special teams.")
fh.write("\nGood thing for dee!")
#you have to use close medthod to save data
fh.close()

fh = open('fightsong copy2.txt', 'x')

'''
'''
fh = open('fightsong.txt', 'r')
#print(len(fh))
#doesn't have this length
#use read() to read the entire thing as a string
fight_song = fh.read()
print(len(fight_song)) 
print(fight_song[-20:])

#to delete a file, os.remove()
'''
'''
import os
os.remove("234")

   '''     
'''   
'''
#10/11/23
#extend just adds the element to it
#append a list nests it. [23,3,4, [3,4,5]]

#the syntax of simple function definitions
#def square(x):
    #return x*x
    
#main serves as the entry point for a scrip
#usually expects no arguments and returns no value
#definition of main and other functions
'''
def main():
    number = float(input("enter a number: "))
    result = square(number)
    print("the square of ", number, "is", result)
def square(x):
    
    return x*x
#wtf is this part???
if __name__ == "__main__":
    main()
    
'''
#lists are mutable, strings are immutable, to change from  upper to lower string.lower()
#list methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
'''
list3 = [1,3,4,5,7,9,11,13,15]
#insert(position, number)
list3.insert(1,2)
btw = ["wisconsin", "iowa", "minn"]
btw2 ="iowa,will,win, this,"
#split = btw2.split(",") how to split with a comma
print(list3)
'''
#remove dublicates
'''
list1 = [10,20,30,20,10,50,60,40,80,50,40]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
'''

#mindtap is very tricky
'''
phrase = "MindTap is very picky!"
l = phrase[16]
print(phrase[0:22])
print(l)

s = "6.00 is 6.0001 and 6.0002"
new_str = ""
new_str += s[-3]
new_str += s[1]
new_str += s[5::25]
new_str += s[15:12:-1]
print(new_str)
print(s[5::25])
'''
'''
mysum = 0
for i in range(2, 11, 2):
    mysum += i
    print(mysum)
    if mysum == 8:
        break
        mysum += 1
print(mysum)

'''
'''
l1 = ["n"]
l2 = ["y"]
l3 = l1+l2
print(l3)
l3.append(['x','z'])
print(l3)

'''
'''
L1 = ["bacon", "eggs"]
L2 = ["toast", "jam"]
brunch = L1
#print(1)
#L2.extend(brunch)
#print(L2)
L1.append("juice")
print(brunch)
L2.extend(brunch)
print(L2)

for x in range(6):
    
    print(x)

'''
'''
L = list("asdfdsaf")
print(L)

'''
'''
string = "racecare"
reverse = string[::-1]
for h in reverse:
    print(h)
if string == reverse:
    print("Yes, the string is a palindrome.")
else:
    print("No, it is not.")


'''

#text to list, use split
#mind tap 10/18/23
'''
def main():
    list1 = [4,3,5,1]
    print(median(list1))
    #call the median function
    
def median(list_num):
    numbers = []
    for x in list_num:
        numbers.append(x)
    #making a copy of our list number
    #list are mutable, so if we sort the list here it would've been sorted 
    #in other parts of our code
    #// means divide and round down
    # % means divide and check remainder
    numbers.sort()
    if len(numbers)%2 == 1:
        #odd case
        midpoint = len(numbers) //2
        median_val = numbers[midpoint]
        return median_val
    else:
        midpoint = len(numbers)//2
        median_val = (numbers[midpoint] + numbers[midpoint - 1]) / 2
        return median_val
    
main()

'''
#dictionaries - key value pairs, numbers - perfume, numbers moeny
#key must be immutable 
'''
dictionary1 = dict()
dictionary1['perfume'] = 'chanel'
dictionary1['apple'] = 'food'
print(dictionary1)
'''
'''
tackle = dict()
fh = open("first_half_tackles.txt", "r")
for line in fh:
     names = line.split()
     for name in names:
         if name not in tackle:
             tackle[name] = 1
         else:
                tackle[name] += 1
print(tackle)
'''
# get method gives you the value 
'''
tackles = {}
fh = open("first_half_tackles.txt")
for line in fh:
    names = line.split()
    for name in names:
        tackles[name] = tackles.get(name, 0) +1
            #0 means default if that name isn't in the dicitonary yet 
print(tackles)
            
'''
'''
text1 = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"
words = text1.split()
freq = {}
for word in words:
    #is that word there yet?
    freq[word] = freq.get(word, 0) + 1 #each time add 1 to the value 
print(freq)
            
            
     '''
#def power
'''
def pow(a,b)       :
    result = a**b
    return result, a

answer, orginal = pow(2,4)
print(answer)
print(orginal)
            
'''
            
#dictionary exercise
'''
dic1 = {3:4, 7:5}
#get the value of key 3, add 6
dic1[3] = dic1.get(3) + 6
dic1[3] = dic1.get(7)
#so you just get the value from the key, 
#if you type dic1.get(15) they won't find the key of 15 set a default with a ,0
dic1[3] = dic1.get(15,0)+6
print(dic1)
       
#dict.keys, dict.values, .items will give you pair of your key and value tuple

'''
#pract 1 safe int input

'''
def main():
    string1 = input("give an integer")
    integer1 = int_input(string1)
    print(integer1)

def int_input(message):
    while True:
        #try this if you run into an error, then default to go to the except
        try:
            val = int((message))
            return val
        except:
            print("invalid input")
            #return False
            break
 #the none that prints out is just going to return a none   
if __name__ == "__main__":
    main()
    
 '''

#variable scope 
#there are global and local variables 
# What is in the entire python or in a function
#the one that is in a function is local 
'''
x = "awesome"
y = 10
   
def myfunct():
    
    global y 
    global x
    print("inside: python is", x)
    
myfunct()
print("y is ", )
print("main: python is ",x )
    '''
#practice  Statefacts.csv 
'''
def main():
    
    fh = open("state_facts.csv")
    state_dict = {}
    for line in fh:
        state_data = line.split(",")
        state_dict[state_data[0]] = state_data
    print(state_dict)
    
    state = "Iowa"
    print(getbird(state_dict,state))
    print(getcapital(state_dict,state))

def getbird(dictionary1, name):
    
    return dictionary1[name][3]
def getcapital(dictionary1, name):
    
    return dictionary1[name][1]

main()
'''
#keyword arguments 
#10/30/23 - tuples 

#sets are unique items not in a particular order, just a list and dictionary
'''
days = set(["mon", "mon", "tues", "weds", "thurs", "fri", "sat", "sun", "sat"])
days.remove("mon")
print(days)
'''
#so you can turn it back into a list with all unique values

# & - intersection, | combine 
#tuples cannot be changed, but are ordered 
#tuples good for assignments 
#you can have tuples as keys

# numbers and pandas 
# so you will have to send a default value 
#lab quiz list, dictionary, and functions
#line.split()

#dictionary - similar to list, but 
#freq.get(name,0) + 1 when you are looping through a file 
#numpy and pandas
#basic linear algebra functions
#sophiaisted fast numbericans


#module 6 - pandas 
#numpy array - looks like psythin lis t


#import numpy as np
#import pandas as pd

'''
a = np.array([1,2,3,4,5,6])
# no more commas
print(type(a))
#basically the same as infexting as a list but in 2 dimensions
#arrays are helpfuck when imagine processing
#pandas backbone is the dataframe 

'''
#figure this out 
'''
actors_dict = {
    'First Name': ['Tom', 'Leonardo', 'Nicole', 'Tom', 'Meryl'],
    'Last Name': ['Cruise', 'DiCaprio', 'Kidman', 'Hanks', 'Streep'],
    'Age': [60, 48, 55, 66, 73],
    'Oscars Nominated': [4, 6, 5, 6, 21],
    'Oscars Won': [0, 1, 1, 2, 3]}
actors_df = pd.DataFrame(actors_dict)
print(actors_df['Oscars Won'].mean())


'''
'''

import numpy as np
import pandas as pd
'''

#dataframe titanic
'''
df_titanic = pd.read_csv("titanic.csv")
print(df_titanic)
df_survival = df_titanic[["Age","Survived"]]
df_survivalOLD = df_survival[df_survival["Age"]>60]
print(df_survival.mean())
'''
#new data frame DF survival 

#delays 
'''
df_delays = pd.read_csv("July23_Flight_Delays.csv")
print(df_delays)
df_average_delay = df_delays["Delay"].median()
print(df_average_delay)
df_delta = df_delays[df_delays['Airline'] == 'DL']
print(df_delta.mean())

'''
#11/6 challenge question 
#how to filter with panda data frame 
'''
import pandas as pd
actors_dict = {
'First Name': ['Tom', 'Leonardo', 'Nicole', 'Tom', 'Meryl'],
'Last Name': ['Cruise', 'DiCaprio', 'Kidman', 'Hanks', 'Streep'],
'Age': [60, 48, 55, 66, 73],
'Oscars Nominated': [4, 6, 5, 6, 21],
'Oscars Won': [0, 1, 1, 2, 3]}
actors_df = pd.DataFrame(actors_dict)
actors_df['Years per Nomination'] = actors_df['Age'] /actors_df['Oscars Nominated']
print(actors_df[actors_df['Years per Nomination']<10])


'''

#numpy arrays
#going into dimensions with low computing time
#separate dimension with a comma, 
# A[0, 3:5] row zero, collumn 3,4, stop at 5
#A[4:,4:] row 5 to the end, column 5 to the end 
    #returns array([44,55],[54,55])
    
#a[2::2, ::2] start at row 3, step by 2, start at column 0 and start by 2

#pandas summary 
# read files pandas
'''
df = pd.read_csv("student.csv")
pd.read_excel('myfile.xlsx',sheet_name='Sheet1', index_col=None, na_values=['NA'])
pd.read_stata('myfile.dta')
pd.read_sas('myfile.sas7bdat')
pd.read_hdf('myfile.h5','df’)
            # hdf is Hierarchical Data Format from NCSA
# used in super-computing
Note: The above command has many optional arguments to fine-tune the data import
process.

'''

#look at panda participation for use of pandas like lab ativity 3 
#data frame is like a key:value dictionary, name of datafram[column name]
'''
import pandas as pd
actors_dict = {
'First Name': ['Tom', 'Leonardo', 'Nicole', 'Tom', 'Meryl'],
'Last Name': ['Cruise', 'DiCaprio', 'Kidman', 'Hanks', 'Streep'],
'Age': [60, 48, 55, 66, 73],
'Oscars Nominated': [4, 6, 5, 6, 21],
'Oscars Won': [0, 1, 1, 2, 3]}
actors_df = pd.DataFrame(actors_dict)
actors_df['Years per Nomination'] = actors_df['Age'] / actors_df['Oscars Nominated']
'''
#use double square backetss 
#slicing by column
'''
actors_df[['Oscars Nominated', 'Oscars Won']]

print(actors_df)
print(actors_df.Age)


'''
#filter by rows 
'''
print(actors_df[1:4])

    '''
    
    
#Module 7 - Image processing 
    #each individual pixel has a color Red Green Blue, each is represented by a tuple
    # number for each of those value is in range of 255 black(0,0,0)
    #pixels on a 2 dimensional grid, (0,0) top left, to the range of (width -1, height -1 )
    #because width starts at 0 height starts at 0

#smokey.gif
'''
from images import Image
image1 = Image("smokey.gif")
#image1.draw()

image = Image(150, 150)

blue = (255, 255, 0)
y = image.getHeight() // 2
for x in range(image.getWidth()):
    image.setPixel(x, y - 1, blue)
    image.setPixel(x, y, blue)
    image.setPixel(x, y + 1, blue)
image.draw()
'''
'''
print(image1.getHeight())
print(image1.getWidth())
print(image1.getPixel(0,0))

'''

#Module 7 - image
'''
from images import Image 
    
image = Image(150, 150)
purple = (255, 0, 150)

for y in range(image.getHeight()): #goes down the picture
    for x in range(image.getWidth()): #goes across the picture 
        image.setPixel(x, y, purple)
image.draw()
'''
#image save
'''

from images import Image 
image = Image("smokey.gif")
print(image.getHeight())
print(image.getWidth())
red,green,blue = image.getPixel(40,50)
print(red)
print(green)
print(blue)
'''
#image.save("") - whatever you want to save it as 
    
#converting image to black and white 
#from images import Image 
'''

def main():
    image = Image("smokey.gif")
    blackandWhite(image)
    image.draw()

def blackandWhite(image):
    blackPixel = (0,0,0)
    whitePixel = (255,255,255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b, = image.getPixel(x,y)
            average = (r+g+b)//3 
            if average < 128:
                image.setPixel(x,y,blackPixel)
            else:
                image.setPixel(x, y, whitePixel)
        
main()  

'''


#shrink function 11/13/23 
'''

def shrink(image, factor):
    width = image.getWidth()
    height = image.getHeight()
    new = Image(width // factor, height //
    factor)
    oldY = 0
    newY = 0
    while oldY < height - factor:
        oldX = 0
        newX = 0
        while oldX < width - factor:
            oldP = image.getPixel(oldX, oldY)
            new.setPixel(newX, newY, oldP)
            oldX += factor
            newX += 1
            oldY += factor
            newY += 1
    return new
'''

# add in average function 
'''
def detectEdges(image, amount):
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    new = image.clone()
    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            if abs(oldLum - leftLum) > amount or abs(oldLum -
            bottomLum) > amount:
                new.setPixel(x, y, blackPixel)
            else:
                new.setPixel(x, y, whitePixel)
        return new


'''
#11/13/23 - practice
'''
import mymodule as mm
print(mm.root(4,2))
print(mm.constants)

'''

#11/27/23 - init.py, modules
'''
dictio1 = {"a":1, "b":2}
print(dir(dictio1))
print(dictio1['a'])
print(dictio1.items())
'''

#11/27/23 - matplotlib 
'''
import matplotlib.pyplot as plt
import numpy as np

objects = ('Python', 'C++', 'Java', 'R', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()
'''

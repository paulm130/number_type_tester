import random
import time

def time_elapsed(end_time, start_time): #function for calculating time elapsed
    end_time = int(end_time)
    start_time = int(start_time)
    time_elapsed = end_time-start_time
    return time_elapsed

def words_per_minute(characters, seconds): #function for calculating words per minute
    characters = int(characters)
    seconds = int(seconds)
    words_per_minute = int((characters/5)/(seconds/60))
    return words_per_minute

string = "" 
correct = 0 

length = int(input("how many characters long do you want the typing test to be: "))

count = 0
while count < length: #creating random number sequence and printing it out
    char = str(random.randint(0,9))
    print(char, end = '')
    string = string + char
    count +=1

print()

start_time = time.time()
typing = input("type out the string: ")
end_time = time.time()
elapsed_time = time_elapsed(end_time, start_time)
wpm = words_per_minute(length,elapsed_time)

for i in range(length):
    if string[i] == typing[i]:
        correct +=1

print('correct: ', correct,'/',length)
print('time elapsed: ', elapsed_time, ' sec')
print('wpm: ', wpm)
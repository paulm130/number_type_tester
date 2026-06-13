import random
import time

#function for calculating time elapsed
def time_elapsed(end_time, start_time): 
    end_time = int(end_time)
    start_time = int(start_time)
    time_elapsed = end_time-start_time
    return time_elapsed

#function for calculating words per minute
def words_per_minute(characters, seconds): 
    characters = int(characters)
    seconds = int(seconds)
    words_per_minute = int((characters/5)/(seconds/60))
    return words_per_minute

string = "" 
correct = 0 

letter_input = 0
while letter_input == 0:
    try:
        length = int(input("how many characters long do you want the typing test to be: "))
        letter_input = 1
    except ValueError:
        print("must input a number for length")

count = 0
while count < length: #creating random number sequence and printing it out
    char = str(random.randint(0,9))
    print(char, end = "")
    string = string + char
    count +=1

print()

start_time = time.time()

letter_input = 0
typing = input("type out the string: ")

is_valid = False
while is_valid == False:
    if len(typing) < length:
        print("you typed too few characters. Try again.")
        typing = input("type out the string: ")
        continue
    is_valid = True
    for i in range(length):
        if(typing[i] < "0" or typing[i] > "9"):
            is_valid = False
            print("you typed in something that is not a number. Try again.")
            typing = input("type out the string: ")

end_time = time.time()
elapsed_time = time_elapsed(end_time, start_time)
wpm = words_per_minute(length,elapsed_time)

for i in range(length):
    if string[i] == typing[i]:
        correct +=1

typed_length = len(typing)
if typed_length > length:
    print(f"you typed too many characters the last {typed_length-length}" 
          f" characters were cut off")

percent_correct = round((correct/length)*100,2)
print("correct: ", correct,"/",length)
print("correct", percent_correct,"%") 
print("time elapsed: ", elapsed_time, " sec")
print("wpm: ", wpm)

if wpm < 20 or percent_correct < 95:
    print("Ranking: beginner :(")
elif wpm < 50:
    print("Ranking: Intermediate :|")
else:
    print("Ranking: Advanced :)") 
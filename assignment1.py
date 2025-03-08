#1
fib = [1, 1]     # control+? is multi lines comment
for i in range(8): 
    fib.append(fib[i]+fib[i+1])
print(fib)

fib2 = [1,1]
for _ in range(8):
    fib2.append(fib2[-1]+fib2[-2])
print(fib2)
 
#2
for i in range(len(fib2)):
    if i % 2 != 0:
        print(fib2[i])

for i in range(1, len(fib2),2):
    print(fib2[i])

#3
string = """

I have provided this text to provide tips on creating interesting paragraphs.

First, start with a clear topic sentence that introduces the main idea.

Then, support the topic sentence with specific details, examples, and evidence.

Vary the sentence length and structure to keep the reader engaged.

Finally, end with a strong concluding sentence that summarizes the main points.

Remember, practice makes perfect!

"""
string = set(string.lower().replace(",","").replace(".","").replace("!","").strip().split()) #set no order, generating different words order each time I run
# string = string.replace(",","")
# string = string.replace(".","")
# string = string.replace("!","")
# words_array = string.strip().split()
# my_set = set(string)       
print(string)

#4
my_word = "Victor"
count = 0
for i in range(len(my_word)):
    if my_word[i] in ["a","e","i","o","u"]:
        count+=1
print(count)

#5
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for a in animals:
    print(a.upper())

#6
for i in range(1,21):
    if i % 2 ==0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")

for i in range(1,21):
    if i % 2 ==0:
        print(f"{i} is even.")
        continue
    print(f"{i} is odd.")

#7
def sum_of_integers(a, b):
    return a + b

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

result = sum_of_integers(a, b)
print("The sum is:", result)
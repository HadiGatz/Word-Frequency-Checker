import sys

# assigning input from sys.argv into variables
user_file = sys.argv[1]
N = int(sys.argv[2])

# reading the content of the file
try:
  with open(user_file, "r") as file:
      data = file.read()
      file.close()
except FileNotFoundError:
    print("The file you entered was not found in the directory.")
except Exception:
    print("Unexpected error.")

# removing unwanted spaces and characters, and lowering all words 
data = data.strip("., ").split()
data = [word.lower() for word in data]

# checking for frequency
words_in_file = {}
try:
  for word in data:
      if word not in words_in_file:
          words_in_file[word] = 1
      else:
          words_in_file[word] += 1
except TypeError: 
    print("TypeError: the file was not in the right format.")
except Exception:
    print("Unexpected error.")

# sorting by descending frequency
sorted_items = sorted(words_in_file.items(), key=lambda item: item[1], reverse=True)

# printing the results 
for i in sorted_items[0:N]:
    print(f"{i[0]} : {i[1]}")
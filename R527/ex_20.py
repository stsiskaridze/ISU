from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file, encoding="utf8")

print("მოდით ჯერ დავბეჭდოთ ფაილი მთლიანად:\n")

print_all(current_file)

print("მოდით ახლა გადავახვიოთ ფაილი უკან, ერთგვარი ლენტური კასეტასავით.")

rewind(current_file)

print("და სათითაოდ დავბეჭდოთ ფაილის ყოველივე სტრიქონი:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
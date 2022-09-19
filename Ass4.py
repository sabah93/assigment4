def findmin(list):
    min= list[0]
    for i in range(len(list)):
        if list[i] <= list[0]:
            min= list[i]
            i+=1
    print("the min  in your list = ", min)

sum=0
list = []
length = 0
positive= 0
negative= 0
print("inter your list if you wanna to exit press 0")

while (True) :
    item = int(input("inter the element"))
    if item == 0:
        break
    if item < 0:
        negative += 1
    if item > 0:
        positive += 1
    sum+=item
    list.append(item)
    length += 1

print("your list = ", list, " the length of your list = ", length)
print("there is  ", positive," positive nu in your list")
print("there is  ", negative," negative nu in your list")
print("the sum of list is = ",sum)
print("the avr of list is = ",sum/length)

t = 0
for i in range(len(list)):
    for j in range(len(list)):
        if list[j] == list[i] and i != j:
           t+= 1
if t == 0:
    print("all nu is UNIQUE in list")
else:
    print(" there is  DUPLICATES nu in list")

findmin(list)
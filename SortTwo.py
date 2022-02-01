numbers = [2,3,4,7,14,1,4]
length = len(numbers)
targetn = 8
calc = 0
array_index = 0

print("Number of items in array:",length)
print("Numbers in list")
for sample in numbers:
    print(sample)

for n in numbers:
    print("Testing list item #:",array_index,"/",length," Value:",n)
    array_index += 1
    array_index2 = 1
    
    for n2 in numbers:
        if array_index == array_index2:
            break
        calc = n+n2
        if calc == targetn:
            break
        else:
            array_index2 += 1

    if calc == targetn:
        print("Sought number was found by combining values",n,"and",n2,"from array item",array_index,"and",array_index2)
        break

if calc != targetn:
    print("No 2 values from the list added up to",targetn)
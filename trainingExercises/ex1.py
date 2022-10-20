#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers = list(range(2000, 3201))

result = []

for i in numbers:
    if(i%7 == 0):
        result.append(str(i))

ans = ",".join(result)

print(len(ans), "\n")
print(ans)

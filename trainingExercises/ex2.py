#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

#n(n-1)

#Get the input from the commandline

n = int(input("Pleae enter a number .. "));

def fact(n):

    print(n)

    if n == 0:
        return 1

    return n * fact(n - 1);

print(fact(n))

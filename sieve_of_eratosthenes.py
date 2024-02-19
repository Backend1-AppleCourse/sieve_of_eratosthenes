# iterate over number in array from 4-150
# iterate over prime list
# for each prime check if current number divides by it
# if it divides i would delete it from numbers array
# if it doesnt divide, add it to prime numbers 
# delete all its multiplications from numbers array
import time

a = 4
N = 151
numbers = [i for i in range(a,N)]
prime_numbers = [2,3]

i=0
runtime = 0

while len(numbers) > i:
    print(numbers[i])

    is_prime = True
    for prime in prime_numbers:
        runtime += 1
        if numbers[i] % prime == 0:
            is_prime = False
            numbers.remove(numbers[i])
            i -= 1
            break
    if is_prime:
        prime_numbers.append(numbers[i])
        numbers.remove(numbers[i])
        i -= 1
        j=0
        while j < len(numbers):
            if numbers[j] == 0:
                numbers.remove(numbers[j])
                j -= 1
            j+=1
    i += 1
        

print(runtime) 
print(numbers)
print(prime_numbers)



def digit_count_and_sum(n):
    n = abs(n)   # convert negative number to positive
    digit_count = 0
    digit_sum = 0

    if n == 0:          # special case
        return 1, 0

    while n > 0:
        digit_sum += n % 10
        digit_count += 1
        n //= 10

    return digit_count, digit_sum


# Main program
num = int(input("Enter an integer: "))
count, total = digit_count_and_sum(num)

print("Total number of digits:", count)
print("Sum of digits:", total)

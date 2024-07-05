def digit_frequency(num):
    digit_freq= {}
    for digit in num:
        if digit.isdigit():
            if digit in digit_freq:
                digit_freq[digit] += 1
            else:
                digit_freq[digit] = 1

    for digit, frequency in digit_freq.items():
        print(f"The frequency of the digit{digit} is {frequency}")

num = input("Enter the numbers: ")
digit_frequency(num)
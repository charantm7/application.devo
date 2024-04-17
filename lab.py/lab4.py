def count_digit_frequency(number):
    digit_frequency={}
    for digit in number:
        if digit.isdigit():
            if digit in digit_frequency:
                digit_frequency[digit]+=1
            else:
                digit_frequency[digit]=1
    for digit, frequency in digit_frequency.items():
        print(f"Frequency of digit {digit}:{frequency}")
number=input("Enter the multi-digit number:")
count_digit_frequency(number)
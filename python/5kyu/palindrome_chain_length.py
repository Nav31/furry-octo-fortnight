def palindrome_chain_length(n):
    # 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884

    def reverse_num(some_number):
        # A function to reverse a number
        return int(str(some_number)[::-1])

    def is_palindrome(some_number):
        # This checks if a number is a palindrome
        return str(some_number) == str(reverse_num(some_number))

    counter = 0
    current_number = n
    if is_palindrome(n):
        return 0
    while True:
        new_sum = current_number + reverse_num(current_number)
        if is_palindrome(new_sum):
            return counter + 1
        else:
            current_number = new_sum
            counter += 1

print palindrome_chain_length(87)


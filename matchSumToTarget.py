# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def matchSumToTarget(inputArr, target):
    required = []

    for num in inputArr:
        match = target - num
        if match in required:
            return True 
        required.append(num)
    return False


assert matchSumToTarget([10, 15, 3, 7], 17) == True
assert matchSumToTarget([10, 15, 3, 12], 17) == False
assert matchSumToTarget([], 50) == False
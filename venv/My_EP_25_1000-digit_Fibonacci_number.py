''' 1000-digit Fibonacci number - Problem 25
INPUT: The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

n_1 = 1
n_2 = 1
count = 2

while len(str(n_2)) < 1000:
    n_1, n_2 = n_2, n_1 + n_2
    count += 1

print(count)


input_sequence = [1, 2, 5, 10]

def fibonacci(n):
    first, second = 0, 1
    for _ in range(n):
        yield first
        first, second = second, first + second
        
    
    
for i in input_sequence:
    print(list(fibonacci(i)))
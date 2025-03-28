class Calculate:
    """
    Collatz Conjecture
    Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
    # If n is even, divide it by 2. 
    # If n is odd, multiply it by 3 and add 1.

    input parameters:
        user input (n)
    
    methods: 
        even_or_odd()
            take n and check if even or odd recursively
    """
    def __init__(self, n):
        self.n = n

    # take n and check if even or odd recursively
    def even_or_odd(self):
        # base case
        if self.n < 2:
            print("success!!!! n is", self.n)
            return self.n
        
        if self.n % 2 == 0:
            print("n is even: ", self.n)
            self.n = int(self.n / 2)
            return self.even_or_odd()
        else:
            print("n is odd: ", self.n)
            self.n = int((self.n * 3) + 1)
            return self.even_or_odd()

        

# Get user input
# TODO: try and make user input nicer looking
n = int(input( "Enter a number"))
c = Calculate(n)
n = c.even_or_odd()
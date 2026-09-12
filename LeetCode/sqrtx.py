class Solution:
    def mySqrt(self, number: int) -> int:
        if number == 0:
            return 0

    # Start with an initial guess
        guess = number / 2.0
        tolerance = 1e-10
    
    # Repeatedly improve the guess until it is accurate enough
        while True:
            better_guess = 0.5 * (guess + number / guess)
            if abs(guess - better_guess) < tolerance:
                return int(better_guess)
            guess = better_guess
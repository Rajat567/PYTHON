import sys

class AdvancedCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def power(self, x, y):
        return x ** y

    def square(self, x):
        return x ** 2

    def cube(self, x):
        return x ** 3

    def sqrt(self, x):
        return x ** 0.5

    def inverse(self, x):
        if x == 0:
            raise ValueError("Cannot find inverse of zero")
        return 1 / x

    def factorial(self, x):
        if x < 0:
            raise ValueError("Cannot find factorial of negative number")
        if x == 0:
            return 1
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    def sin(self, x):
        x = x % (2 * self.pi())
        term = x
        result = x
        n = 1
        while abs(term) > 1e-15:
            term *= -x * x / (2 * n * (2 * n + 1))
            result += term
            n += 1
        return result

    def cos(self, x):
        x = x % (2 * self.pi())
        term = 1
        result = 1
        n = 1
        while abs(term) > 1e-15:
            term *= -x * x / (2 * n * (2 * n - 1))
            result += term
            n += 1
        return result

    def tan(self, x):
        return self.sin(x) / self.cos(x)

    def log(self, x, base=10):
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        if base <= 0:
            raise ValueError("Logarithm base must be positive")
        result = 0
        while x < 1:
            x *= base
            result -= 1
        while x >= base:
            x /= base
            result += 1
        term = (x - 1) / (x + 1)
        term_squared = term * term
        n = 1
        while term > 1e-15:
            result += 2 * term / (2 * n - 1)
            term *= term_squared
            n += 1
        return result

    def pi(self):
        return 3.141592653589793

if __name__ == "__main__":
    calc = AdvancedCalculator()
    print("Advanced Calculator")
    while True:
        try:
            expr = input("Enter expression (or 'exit' to quit): ")
            if expr.lower() == 'exit':
                break
            print("Result:", eval(expr))
        except Exception as e:
            print("Error:", e)
            class AdvancedCalculator:
                def add(self, x, y):
                    return x + y

                def subtract(self, x, y):
                    return x - y

                def multiply(self, x, y):
                    return x * y

                def divide(self, x, y):
                    if y == 0:
                        raise ValueError("Cannot divide by zero")
                    return x / y

                def power(self, x, y):
                    return x ** y

                def square(self, x):
                    return x ** 2

                def cube(self, x):
                    return x ** 3

                def sqrt(self, x):
                    return x ** 0.5

                def inverse(self, x):
                    if x == 0:
                        raise ValueError("Cannot find inverse of zero")
                    return 1 / x

                def factorial(self, x):
                    if x < 0:
                        raise ValueError("Cannot find factorial of negative number")
                    if x == 0:
                        return 1
                    result = 1
                    for i in range(1, x + 1):
                        result *= i
                    return result

                def sin(self, x):
                    x = x % (2 * self.pi())
                    term = x
                    result = x
                    n = 1
                    while abs(term) > 1e-15:
                        term *= -x * x / (2 * n * (2 * n + 1))
                        result += term
                        n += 1
                    return result

                def cos(self, x):
                    x = x % (2 * self.pi())
                    term = 1
                    result = 1
                    n = 1
                    while abs(term) > 1e-15:
                        term *= -x * x / (2 * n * (2 * n - 1))
                        result += term
                        n += 1
                    return result

                def tan(self, x):
                    return self.sin(x) / self.cos(x)

                def log(self, x, base=10):
                    if x <= 0:
                        raise ValueError("Logarithm undefined for non-positive values")
                    if base <= 0:
                        raise ValueError("Logarithm base must be positive")
                    result = 0
                    while x < 1:
                        x *= base
                        result -= 1
                    while x >= base:
                        x /= base
                        result += 1
                    term = (x - 1) / (x + 1)
                    term_squared = term * term
                    n = 1
                    while term > 1e-15:
                        result += 2 * term / (2 * n - 1)
                        term *= term_squared
                        n += 1
                    return result

                def pi(self):
                    return 3.141592653589793

                def exp(self, x):
                    term = 1
                    result = 1
                    n = 1
                    while term > 1e-15:
                        term *= x / n
                        result += term
                        n += 1
                    return result

                def sinh(self, x):
                    return (self.exp(x) - self.exp(-x)) / 2

                def cosh(self, x):
                    return (self.exp(x) + self.exp(-x)) / 2

                def tanh(self, x):
                    return self.sinh(x) / self.cosh(x)

            if __name__ == "__main__":
                calc = AdvancedCalculator()
                print("Advanced Calculator")
                while True:
                    try:
                        expr = input("Enter expression (or 'exit' to quit): ")
                        if expr.lower() == 'exit':
                            break
                        print("Result:", eval(expr))
                    except Exception as e:
                        print("Error:", e)
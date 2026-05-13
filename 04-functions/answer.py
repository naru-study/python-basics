### `greet(name, lang="ja")`
def greet(name,lang="ja"):
    if lang == "ja":
        return f"こんにちは、{name}さん!"
    elif lang == "en":
        return f"Hello,{name}!"

### `is_prime(n)`
def is_prime(n):
    if n <= 1:
        return False
    for x in range(2,int(n**0.5) + 1 ):
        if n % x == 0:
            return False
    return True

### `fizzbuzz(n)`
def fizzbuzz(n):
    result = []
    for i in range(1,n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

if __name__ == "__main__":
    print(greet("なるみ"))
    print(greet("Narumi",lang="en"))
    print(is_prime(7))
    print(fizzbuzz(10))
#prime number checker
def check_prime(n: int) -> str:
    data = []
    if n <= 1: return "is not prime"
    for i in range(1,n+1):
        if n % i == 0:
            data.append(i)
    if len(data) <= 2: return "is prime"
    else: return "is not prime"

print(check_prime(17))
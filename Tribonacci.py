def modsum(a,b,c):
    mod = 10**9 + 7
    return (a%mod +b%mod +c%mod)%mod

def tribonacci(n):
    sum =0
    if (n==0 or n==1):
        sum = 0

    if (n==2 ):
        sum =  1
    if n > 2:
        sum = sum + modsum(tribonacci(n-1), tribonacci(n-2),tribonacci(n-3))
    return sum
if  __name__ == "__main__":
    tests = int(input().strip())

    for z in range(tests):
        p = int(input().strip())
        trib = tribonacci(p)
        print(trib)
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
dic={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    cal=True
    n1 = float(input("What's the first number:"))
    while cal:

        for syb in dic:
            print(syb)
        op = input("Choose the operation: ")
        n2 = float(input("What's the next number: "))
        ans=dic[op](n1,n2)
        print(f"{n1} {op} {n2} = {ans}")
        choice=input("Type 'Y' if you want to continue otherwise 'N' to exit:").lower()
        if choice=='y':
            n1=ans
            cal=True
        else:
            cal=False
            print("\n"*50)
            calculator()
calculator()
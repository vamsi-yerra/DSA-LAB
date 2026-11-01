# Week 1 - A: Countdown from n to 1, followed by "launch"
def launch(n):
    for i in range(n, -1, -1):
        if i == 0:
            print("launch")
        else:
            print(i)

n = int(input("Enter no. of seconds to launch: "))

launch(n)

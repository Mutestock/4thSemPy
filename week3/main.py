import cli

if __name__ == "__main__":
    cli.manager()


"""
CLI commands:

main.py student --write N
where N is the amount of students you want in your output file

main.py student --read all 
writes the info of all students (8)

main.py student --read avg
sorted avg list of all students (8 a+b)

main.py student --graph avg
ex1 - 8C

main.py student --graph pct
ex1 - 10

main.py student --graph pct3
ex2 - 1

main.py student --write pct3
ex2 - 3

main.py student --graph pie
ex3 - 1

main.py student --graph count
ex3 - 2

main.py student --graph count2
ex3 - 3


"""

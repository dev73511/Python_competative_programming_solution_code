# Question 1) There was a teacher in a small town who loves coding and he wants to create a program which prints out the whole multiplaction table of an entered numbered for his students can you help him to write a program in python?

def table(tableof, upto):
    for i in range(1, upto + 1):
        print(tableof, "*", i, "=", (i*tableof))
    return


table(2, 10)

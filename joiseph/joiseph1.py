def peopls(n):
    center = 0
    for i in range(len(n)):
        if n[i] != 0:
            center += 1
        if center > 1:
            center = 0
            return True
    return False

def output(n):
    for i in range(len(n)):
        if n[i] != 0:
            return n[i]


if __name__ == "__main__":
    n, k = map(int, input('Введите значения n и k через пробел: ').split())
    people = []
    ind = 1
    for i in range(1, n + 1):
        people.append(i)
    while peopls(people) == True:
         for i in range(len(people)):  
             if ind == k and people[i] != 0:
                if peopls(people) == False:
                     break
                people[i] = 0
                ind = 1 
             elif people[i] != 0:
                 ind += 1
    print(output(people))
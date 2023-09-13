lines = []

with open('engmix.txt', encoding='utf8') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)

  
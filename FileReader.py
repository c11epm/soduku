def readfile(path):

    file = open(path, 'r')
    cont = file.readlines()
    rows = []

    for line in cont:
        line = line.strip("\n")
        if "," in line:
            chars = line.split(",")
            for i in range(len(chars)):
                if chars[i] == "":
                    chars[i] = '0'
            rows.append(chars)
        else:
            rows.append(line)
    file.close()
    return rows


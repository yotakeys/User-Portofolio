def connectDB():
    fileconfig = open("config.txt",'r')
    val = []
    for line in fileconfig:
        val.append(line)

    fileconfig.close()

    config = {
        "db" : val[1][:-1],
        "user" : val[3][:-1],
        "passwd" : val[5][:-1],
        "host" : val[7][:-1],
    }
    return config
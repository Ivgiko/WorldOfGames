def add_score(difficulty):
    file = open('Utils.py', "r")
    read = file.read()
    for line in read.splitlines():
        if 'SCORES_FILE_NAME' in line:
            scoresfile = line.split('=',1)[1]
    try:
        with open(scoresfile, 'x') as file:
            file.write(str((difficulty * 3) + 5))
    except FileExistsError:
        with open(scoresfile, 'r') as file:
            data = file.read()
        with open(scoresfile, 'w') as file:
            file.write(str(int((data if (data != '') else '0')) + (difficulty * 3) + 5))
    file.close()



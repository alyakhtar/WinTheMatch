from math import ceil
import MySQLdb as mdb

# connection to database


def database():
    global newlist
    newlist = []
    con = mdb.connect('localhost', 'root', '123456', 'cricket')
    sql = "SELECT * from bowling_statistics"
    cur = con.cursor()

    cur.execute(sql)

    mt = cur.fetchall()

    for row in mt:
        newlist.append(row)


# Percentage based on economy of bowler
def win_economy(params):
    economy = 0.0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'

    for name in newlist:
        if name[13] == params: # player name
            # char = '-'
            economy = name[6]
            # if economy.find(char) > -1:
            #     economy = economy.replace("-", "")

            if economy != '-':
                if int(economy) <= param: # economy
                    res = name[12]
                    if res.find(strng) > -1:
                        win += 1
                    elif res.find(strng2) > -1:
                        nr += 1
                    else:
                        lost += 1

    percentage = (win*100/(win+lost))

    print 'Matches Won : ' + str(int(win))
    print 'Matches Lost : ' + str(int(lost))
    print 'No Result : ' + str(int(nr))
    print 'Win Percentage : %.2f ' % (ceil(percentage))

    return str(int(win)), str(int(lost)), str(int(nr)), ceil(percentage)


# Percentage based on runs conceded by the bowler
def win_runs():
    runs = 0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'

    for name in newlist:
        if name[13] == 'Mohammed Shami':
            runs = name[3]
            if runs != '-':
                if int(runs) <= 40:  #take as param
                    res = name[12]
                    if res.find(strng) > -1:
                        win += 1
                    elif res.find(strng2) > -1:
                        nr += 1
                    else:
                        lost += 1

    percentage = (win*100/(win+lost))

    print 'Matches Won : ' + str(int(win))
    print 'Matches Lost : ' + str(int(lost))
    print 'No Result : ' + str(int(nr))
    print 'Win Percentage : %.2f ' % (percentage)


# searching in a list
# def search(list, ground):
#     for (i, v) in enumerate(list):
#         if v == ground:
#             return i
#     return -1


# Spinners combined wickets
def win_spinners():
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'
    Type = "Spinner"
    total = 0

    con = mdb.connect('localhost', 'root', '123456', 'cricket')
    sql = 'SELECT DISTINCT ODI_NO FROM bowling_statistics'
    cur = con.cursor()

    cur.execute(sql)

    mt = cur.fetchall()

    for row in mt:
        for match in row:
            cur.execute(
                """SELECT Wickets FROM bowling_statistics where ODI_NO = %s and Type = %s""", (str(match), Type))

            wi = cur.fetchall()

            for row in wi:
                for wicket in row:
                    if wicket != "-":
                        total += int(wicket)

            if total >= 4: # take params
                cur.execute(
                    """SELECT DISTINCT Result FROM bowling_statistics WHERE ODI_NO = %s""", (str(match)))
                res = cur.fetchone()

                for a in res:
                    rest = a
                if rest.find(strng) > -1:
                    win += 1
                elif rest.find(strng2) > -1:
                    nr += 1
                else:
                    lost += 1

    percentage = ((win*100)/(win+lost))

    print 'Win Percentage : %.2f%% ' % (percentage)


# seamers combined wickets
def win_seamer():
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'
    Type = "Seamer"
    total = 0

    con = mdb.connect('localhost', 'root', '123456', 'cricket')
    sql = 'SELECT DISTINCT ODI_NO FROM bowling_statistics'
    cur = con.cursor()

    cur.execute(sql)

    mt = cur.fetchall()

    for row in mt:
        for match in row:
            cur.execute(
                """SELECT Wickets FROM bowling_statistics where ODI_NO = %s and Type = %s""", (str(match), Type))

            wi = cur.fetchall()

            for row in wi:
                for wicket in row:
                    if wicket != "-":
                        total += int(wicket)

            if total >= 4: # take paramas
                cur.execute(
                    """SELECT DISTINCT Result FROM bowling_statistics WHERE ODI_NO = %s""", (str(match)))
                res = cur.fetchone()

                for a in res:
                    rest = a
                if rest.find(strng) > -1:
                    win += 1
                elif rest.find(strng2) > -1:
                    nr += 1
                else:
                    lost += 1

    percentage = ((win*100)/(win+lost))

    print 'Win Percentage : %.2f%% ' % (percentage)

# Two bowlers taking more than 3 wickets together


def two_bowlers():
    char = '*'
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'

    for wickt in newlist:
        wicket = wickt[4]
        if wicket != "-":
            player1 = wickt[13]
            match = wickt[10]
            wicketnew = check_combined(player1, match, wicket)
            if wicketnew == 1:
                res = wickt[12]
                if res.find(strng) > -1:
                    win += 1
                elif res.find(strng2) > -1:
                    nr += 1
                else:
                    lost += 1

    percentage = ((win*100)/(win+lost))

    print 'Win Percentage : %.2f%% ' % (percentage)


def check_combined(player, match, wicket):
    char = '*'
    total = 0

    for name in newlist:
        if name[13] != player:
            if name[10] == match:
                wicketnew = name[4]
                if wicketnew != "-":
                    total = int(wicket)+int(wicketnew)
                    if total > 3: # total wicket
                        return 1
                        break
    return 0


if __name__ == '__main__':
    database()
    # print '\n***ECONOMY CASE***\n'
    # win_economy()
    # print '\n***RUNS CONCEDED CASE***\n'
    # win_runs()
    print '\n***WICKETS TAKEN BY SPINNERS CASE***\n'
    win_spinners()
    print '\n***WICKETS TAKEN BY SEAMERS CASE***\n'
    win_seamer()
    print '\n***2 BOWLERS COMBINED CASE***\n'
    two_bowlers()

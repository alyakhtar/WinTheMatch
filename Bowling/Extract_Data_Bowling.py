from bs4 import BeautifulSoup
import sys
from math import ceil


def display(list):
    newlist.append(list)


def win_economy():
    economy = 0.0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'

    for stats in newlist:
        for name in stats:
            if name[12] == 'R Ashwin':
                # char = '-'
                economy = name[5]
                # if economy.find(char) > -1:
                #     economy = economy.replace("-", "")

                if economy != '-':
                    if int(economy) <= 4.0:
                        res = name[11]
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


def win_runs():
    runs = 0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'

    for stats in newlist:
        for name in stats:
            if name[12] == 'Mohammed Shami':
                runs = name[2]
                if runs != '-':
                    if int(runs) <= 40:
                        res = name[11]
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


def search(list, ground):
    for (i, v) in enumerate(list):
        if v == ground:
            return i
    return -1


def win_spinners():
    runs = 0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'
    odi_no = []

    for stats in newlist:
        for name in stats:
            if name[12] == 'R Ashwin':
                odi_no.append(name[9])

    print odi_no
    # if name[12] == 'RA Jadeja':

    # percentage = (win*100/(win+lost))

    # print 'Matches Won : ' + str(int(win))
    # print 'Matches Lost : ' + str(int(lost))
    # print 'No Result : ' + str(int(nr))
    # print 'Win Percentage : %.2f ' % (percentage)


if __name__ == '__main__':
    win_economy()
    win_runs()

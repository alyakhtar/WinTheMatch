import MySQLdb as mdb
import sys, glob, os
from warnings import filterwarnings

filterwarnings('ignore', category = mdb.Warning)



def database():
    global newlist
    newlist = []
    con = mdb.connect('localhost', 'root', 'samuraii', 'cricket')
    sql = "SELECT * from statistics"
    cur = con.cursor()

    cur.execute(sql)

    mt = cur.fetchall()


    for row in mt:
        newlist.append(row)       
   


def win_count():
    runs = 0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'


    for name in newlist :
        if name[15] == 'V Kohli':
            char = '*'
            runs = name[1]
            if runs.find(char) > -1:
                runs = runs.replace("*", "")

            if runs != 'DNB' and runs != 'TDNB':
                if int(runs) >= 30:
                    res = name[14]
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


def win_location():
    win_home = 0.0
    nr_home = 0.0
    lost_home = 0.0
    win_away = 0.0
    nr_away = 0.0
    lost_away = 0.0
    percentage_home = 0.0
    percentage_away = 0.0
    strng = 'India won'
    strng2 = 'No result'
    grounds = ['Mumbai', 'Nagpur', 'Trivandrum', 'Lucknow', 'Srinagar', 'Chandigarh', 'Jaipur', 'Rajkot', 'Ahmedabad', 'Vadodara',
               'Hyderabad (Deccan)', 'Pune', 'Madras', 'Kochi', 'Indore', 'Guwahati', 'Margao', 'Faridabad', 'Jammu', 'Patna', 'Chennai', 'Bangalore', 'Jamshedpur', 'Ranchi', 'Delhi', 'Visakhapatnam', 'Vijayawada', 'Dharamsala', 'Kanpur', 'Jalandhar', 'Amritsar', 'Kolkata', 'Gwalior', 'Jodhpur', 'Cuttack']

    
    for ground in newlist:
        if ground[15] == 'V Kohli':
            char = '*'
            runs = ground[1]
            if runs.find(char) > -1:
                runs = runs.replace("*", "")

            if runs != 'DNB' and runs != 'TDNB':
                if int(runs) >= 30 and int(runs) < 100:
                    flag = search(grounds, ground[10])
                    if flag >= 0:
                        res = ground[14]
                        if res.find(strng) > -1:
                            win_home += 1
                        elif res.find(strng2) > -1:
                            nr_home += 1
                        else:
                            lost_home += 1
                    else:
                        res = ground[14]
                        if res.find(strng) > -1:
                            win_away += 1
                        elif res.find(strng2) > -1:
                            nr_away += 1
                        else:
                            lost_away += 1

    percentage_home = (win_home*100/(win_home+lost_home))
    percentage_away = (win_away*100/(win_away+lost_away))

    print 'Matches Won at home : ' + str(int(win_home))
    print 'Matches Won away : ' + str(int(win_away))
    print 'Matches Lost at home : ' + str(int(lost_home))
    print 'Matches Lost away : ' + str(int(lost_away))
    print 'No Result at home : ' + str(int(nr_home))
    print 'No Result away : ' + str(int(nr_away))
    print 'Home Win Percentage : %.2f%%' % (percentage_home)
    print 'Away Win Percentage : %.2f%%' % (percentage_away)


def win_against():
    runs = 0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'

    
    for name in newlist:
        if name[15] == 'V Kohli':
            if name[13] == 'Australia':
                char = '*'
                runs = name[1]
                if runs.find(char) > -1:
                    runs = runs.replace("*", "")

                if runs != 'DNB' and runs != 'TDNB':
                    if int(runs) >= 50 and int(runs) < 100:
                        res = name[14]
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
    print 'Win Percentage : %.2f%% ' % (percentage)


def win_combined():
    win_home = 0.0
    nr_home = 0.0
    lost_home = 0.0
    win_away = 0.0
    nr_away = 0.0
    lost_away = 0.0
    percentage_home = 0.0
    percentage_away = 0.0
    strng = 'India won'
    strng2 = 'No result'
    grounds = ['Mumbai', 'Nagpur', 'Trivandrum', 'Lucknow', 'Srinagar', 'Chandigarh', 'Jaipur', 'Rajkot', 'Ahmedabad', 'Vadodara',
               'Hyderabad (Deccan)', 'Pune', 'Madras', 'Kochi', 'Indore', 'Guwahati', 'Margao', 'Faridabad', 'Jammu', 'Patna', 'Chennai', 'Bangalore', 'Jamshedpur', 'Ranchi', 'Delhi', 'Visakhapatnam', 'Vijayawada', 'Dharamsala', 'Kanpur', 'Jalandhar', 'Amritsar', 'Kolkata', 'Gwalior', 'Jodhpur', 'Cuttack']


    for ground in newlist:
        if ground[15] == 'V Kohli':
            if ground[13] == 'Australia':
                char = '*'
                runs = ground[1]
                if runs.find(char) > -1:
                    runs = runs.replace("*", "")

                if runs != 'DNB' and runs != 'TDNB':
                    if int(runs) >= 50 and int(runs) < 100:
                        flag = search(grounds, ground[10])
                        if flag >= 0:
                            res = ground[14]
                            if res.find(strng) > -1:
                                win_home += 1
                            elif res.find(strng2) > -1:
                                nr_home += 1
                            else:
                                lost_home += 1
                        else:
                            res = ground[14]
                            if res.find(strng) > -1:
                                win_away += 1
                            elif res.find(strng2) > -1:
                                nr_away += 1
                            else:
                                lost_away += 1

    percentage_home = (win_home*100/(win_home+lost_home))
    percentage_away = (win_away*100/(win_away+lost_away))

    print 'Matches Won at home : ' + str(int(win_home))
    print 'Matches Won away : ' + str(int(win_away))
    print 'Matches Lost at home : ' + str(int(lost_home))
    print 'Matches Lost away : ' + str(int(lost_away))
    print 'No Result at home : ' + str(int(nr_home))
    print 'No Result away : ' + str(int(nr_away))
    print 'Home Win Percentage : %.2f%%' % (percentage_home)
    print 'Away Win Percentage : %.2f%%' % (percentage_away)

def double_half_century():
  char = '*'
  win = 0.0
  nr = 0.0
  lost = 0.0
  percentage = 0.0
  strng = 'India won'
  strng2 = 'No result'


  
  for ground in newlist:
      runs = ground[1]
      if runs.find(char) > -1:
          runs = runs.replace("*", "")
      if runs != 'DNB' and runs != 'TDNB':
          if int(runs) >= 50 and int(runs) < 100:
              player1 = ground[15]
              match = ground[12]
              runsnew = check_50(player1,match)
              if runsnew == 1:
                res = ground[14]
                if res.find(strng) > -1:
                    win += 1
                elif res.find(strng2) > -1:
                    nr += 1
                else:
                    lost += 1

  percentage = ((win*100)/(win+lost))

  print 'Win Percentage : %.2f%% ' % (percentage)
                         

def check_50(player,match):
  char = '*'
  
  for name in newlist:
      if name[15]!= player:
          if name[12] == match:
              runsnew = name[1] 
              if runsnew.find(char) > -1:
                runsnew = runsnew.replace("*", "")                   
              if runsnew != 'DNB' and runsnew != 'TDNB':                         
                if int(runsnew) >= 50 and int(runsnew) < 100:
                  return 1
  return 0


def search(list, ground):
    for (i, v) in enumerate(list):
        if v == ground:
            return i
    return -1


if __name__ == '__main__':
    database()
    print '\n***GENERAL CASE***\n'
    win_count()
    print '\n***HOME OR AWAY CASE***\n'
    win_location()
    print '\n***VERSUS CASE***\n'
    print '\nOPPONENT - AUSTRALIA\n'
    win_against()
    print '\n***COMBINED CASE***\n'
    win_combined()
    print '\n***DOUBLE FIFTIES***\n'
    double_half_century()

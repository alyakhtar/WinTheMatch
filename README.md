# WinTheMatch

Minor Project

### Title

Predict Winning Percentage in One Day Cricket on basis of Individual Player Performance


### Abstract 

Millions of dollars are wagered on the outcome of one day international (ODI) cricket matches, with a large percentage of bets occurring after the game has commenced. Using match information gathered from  ODI matches played after January 2011, a range of variables that could independently explain statistically significant proportions of variation associated with the match outcomes are created.

Such variables include home ground advantage (vice versa disadvantage if match is being played away from home),  past performances such as runs scored by the batsmen,  batting strike rate,  total runs conceded by the bowler, bowler economy, performance against the specific opposition. Using a multiple linear regression model, prediction variables will be  numerically weighted according to statistical significance and used to predict the match outcome.

From the data available we perform data mining to exclusively obtain the data relevant to us, and  eventually storing that data in the DB consequently we’ll be performing query on our DB to have an idea of what is the impact of an individual player performance on the winning chances of the team in one day cricket,


### Introduction

The first official one day international (ODI) match was played in 1971 between Australia and England at the Melbourne Cricket Ground. Whilst ODI cricket has developed immensely over the past 44 years, the general principles have remained the same. Both sides bat once for a limited time (maximum 50 overs) with the aim in the first innings to score as many runs as possible, and in the second innings to score more than the target set in the first innings. The game also has powerplay overs, where there is restriction of setting no more than 2 fielders outside the inner circle and thus is usually the period where a cluster of runs are scored.  Each over has six legal deliveries, with commonly illegal deliveries- wide and no ball. 
Our Main focus will be on Team India, since their playing XI have almost remained same from the year 2011 onwards and more importantly they have a young pool of players as a result our result will sustain for a longer period of time. Batting and bowling statistics are provided on espncricinfo.com, which will be our source of data collection. The model is based on team India taking on other 9 international teams and then further dividing the scenario into the home and away fixtures. The percentage based prediction is then taken into account after understanding the past trends of the current batsmen or the bowler from the previous data collected. 



#### Proposed Method

Let us assume that India has played 100 ODI’s from 01 January, 2011 to 01 January 2015. And let us assume that in India won 60 out of 100 matches. 

In these 100 matches, let us say that Shikhar Dhawan has scored half century in 20 matches, now considering only these 20 matches we assume he has scored 15 times India has won and rest of the time India has lost ( here we do not consider the matches that were tied or had no result.).

SO essentially it all boils down to the following -

                V. Kohli - Matches-100
                            





![alt tag](http://i.imgur.com/rtOmP8p.png)  ![alt tag](http://i.imgur.com/Mewns6Z.png)  
![alt tag](http://i.imgur.com/Sn7Foja.png)
![alt tag](http://i.imgur.com/SWzC9xH.png)  ![alt tag](http://i.imgur.com/eO04wyz.png) 
![alt tag](http://i.imgur.com/xjPcCde.png)









### Programming Environment & Tools Used

* Programming Language - Python
* MySQL Database
* Data Warehouse ( as suggested by Tanvir sir) 
* Winning and Score Predicting(WASP)




### References

* ESPN cricinfo
* ICC
* Wikipedia
* Michael Bailey and Stephen R. Clarke, Predicting the Match Outcome in One Day International Cricket Matches, while the Game is in Progress, The 8th Australasian Conference on Mathematics and Computers in Sport, J Sports Sci Med. 2006 Dec; 5(4): 480–487



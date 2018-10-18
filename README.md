# Fantasy Premier League mini-league viewer

Code which imports mini-league data from the fantasy premier league and tabulates it using "prettytable".

The FPL websites limits the number of teams on a single page to 50. The advantage of this code is that you can select how many pages you want to view at once, with detailed information.

## Requirements

* An IDE for those who can or already have one installed. 

**OR**

* A web browser to visit the site https://repl.it/@fez09/FPLMiniLeague to run the code and view data within the browser.

## Imported Data

* Rank
* Last Rank
* Team Name
* Gameweek Points
* Bench Points
* Gameweek Transfers
* Cost (Transfer Hits)
* Total Transfers
* Team Value
* In The Bank
* Total Value
* Captain
* Vice Captain
* What chips have been used
* Team ID

## Modules used

* requests
* prettytable

## Instructions

* Run the code, it will ask for your mini-league ID. To identify your mini-league ID, go to your mini-league page and take note of the number in the link.

for example

https://fantasy.premierleague.com/a/leagues/standings/499/classic 

Here, *499* is the mini-league ID. 

* After you enter the mini-league ID, it will ask you for the pages you wish to view. If your mini-league has just 1 page, simply enter 1 in the 'from' and 'to' prompts.

If you want to check how many pages your mini-league has, uncomment the sections marked in the code. 

**Be aware that while you can use this code for all mini-leagues, using this on the overall league or a large league which has many pages will take a LOT of time to fetch the data. Do not exceed the number of pages by 8 or 10**


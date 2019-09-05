# PyMeUp - Python
Data Analytics BootCamp Assignment 03 

## Background
In this assignment, Python is used to complete 2 scripting challenges.

Inside this local git repository, each challenge is stored in a different directory. Each directory corresponds to each challenge by the names: PyBank and  PyPoll.

Inside of each folder a file called main.py is created. The main script to run for each analysis.

## PyBank Challenge
* In this challenge, the Python script is used to analyze the financial records of a company. The given set of financial data used is called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`.

* The Python script analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, the analysis looks similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, the final script prints the analysis to the terminal and export a text file with the results.


## PyPoll Challenge
* In this challenge, the task is to help a small, rural town modernize its vote-counting process. 

* A given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv) is used. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

* The Python script created analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, the analysis looks similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, the final script prints the analysis to the terminal and export a text file with the results.

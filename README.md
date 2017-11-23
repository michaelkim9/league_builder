# League Builder
## Terminal Application for Building a Soccer League

### Running the program

To run the code, please run the following in Bash.

```bash
$ python3 league_builder.py
```

### The Task

You have volunteered to be the Coordinator for your town’s youth soccer league. As part of your job you need to divide the 18 children who have signed up for the league into three even teams - Dragons, Sharks and Raptors. In years past, the teams have been unevenly matched, so this year you are doing your best to fix that. For each child, you will have the following information: Name, height (in inches), whether or not they have played soccer before, and their guardians’ names. You'll take a list of these children, divide them into teams and output a text file listing the three teams and the players on them. There are three main tasks:

1) The Python program reads the data from the supplied CSV file. Data then gets stored into the appropriate data type so that it can be used in the next task.

2) Logic developed to iterate through all 18 players and assign them to teams such that each team has the same number of players. The number of experienced players on each team is also the same.

3) The program outputs a text file named -- teams.txt -- that contains the league roster listing the team name, and each player on the team including the player's information: name, whether they've played soccer before and their guardians' names.

4) Finally, 18 text files are created ("welcome" letters to the players' guardians). Prorams creates 1 text file for each player. The player’s name is the name of the file, in lowercase and with underscores and ending in .txt. For example, michael_kim.txt.
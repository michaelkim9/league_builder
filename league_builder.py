# League Builder script

# Read a CSV file
# Sort players based on experience
# Create a list of teams
# Write roster to the txt file
# Write letters to the guardians

# Author: Michael Kim


import csv

# Read CSV, sort by experience, and arrange into 3 equal lists (for 3 teams)
# Return list of 3 equal sized lists with equal number of experienced and non-experienced
def open_csv():
    with open('soccer_players.csv',newline='') as csv_file:
        soccer_reader = csv.reader(csv_file,delimiter=',')
        rows = list(soccer_reader)
    rows.pop(0)
    rows.sort(key=lambda x:x[2])
    for row in rows:
        del row[1]
    soccer_list = []
    soccer_list.append([x for x in rows[::3]])
    soccer_list.append([x for x in rows[1::3]])
    soccer_list.append([x for x in rows[2::3]])
    return soccer_list

# Function to create 3 separate team lists with string values so that they can be added to text file
def team_lists(full_list):
    shark_list = []
    dragon_list = []
    raptor_list = []
    for sharks in full_list[0]:
        for shark in sharks:
            shark_list.append(str(shark))
    for dragons in full_list[1]:
        for dragon in dragons:
            dragon_list.append(str(dragon))
    for raptors in full_list[2]:
        for raptor in raptors:
            raptor_list.append(str(raptor))
    return shark_list, dragon_list, raptor_list

# Function to write to the text file
def writer(thing):
    with open('teams.txt','a') as file:
        file.write(thing+'\n')

# Function to write letters to the guardians
def write_letter(team_list,team_string):
    for i in range(0,18,3):
        letter = 'Dear {guardian},\n\n' \
                '{player_name} has been drafted to the {team_name}.\n' \
                'The first practice will be on November 1, 2017.\n\n' \
                'Thank you,\n' \
                'Michael Kim\n'.format(guardian=team_list[i+2],player_name=team_list[i],team_name=team_string)
        letter_file = team_list[i].lower().replace(' ','_') + '.txt'
        parent_letter = open(letter_file,'w')
        parent_letter.write(letter)

if __name__ == '__main__':
	# Read CSV and separte into team lists
    # Write the team roster to the txt file
    sharks = team_lists(open_csv())[0]
    writer('Sharks')
    for i in range(0,18,3):
        writer(', '.join(sharks[i:i+3]))

    dragons = team_lists(open_csv())[1]
    writer('Dragons')
    for i in range(0,18,3):
        writer(', '.join(dragons[i:i+3]))

    raptors = team_lists(open_csv())[2]
    writer('Raptors')
    for i in range(0,18,3):
        writer(', '.join(raptors[i:i+3]))

    # Write letters to the parents/guardians
    # Creates text files for the letters
    write_letter(sharks,'Sharks')
    write_letter(dragons,'Dragons')
    write_letter(raptors,'Raptors')
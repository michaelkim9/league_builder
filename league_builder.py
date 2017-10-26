import csv

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

def writer(thing):
    with open('teams.txt','a') as file:
        file.write(thing+'\n')

def write_letter(team_list):
    for i in range(0,18,3):
        letter = 'Dear {guardian},\n\n' \
                '{player_name} has been drafted to the Sharks.\n' \
                'The first practice will be on November 1, 2017.\n\n' \
                'Thank you,\n' \
                'Michael Kim\n'.format(guardian=team_list[i+2],player_name=team_list[i])
        letter_file = team_list[i].lower().replace(' ','_') + '.txt'
        parent_letter = open(letter_file,'w')
        parent_letter.write(letter)

if __name__ == '__main__':
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

	write_letter(sharks)
	write_letter(dragons)
	write_letter(raptors)
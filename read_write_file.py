import json
def read_json_file():
	input_file_pointer = open("songs.json", "r")
	outer_dictionary = json.load(input_file_pointer)
	list_of_songs = outer_dictionary.get("songlist")
	print("data type for songs", type(list_of_songs))
	print("the actual songs are: \n", list_of_songs)
	input_file_pointer.close()
	return list_of_songs
	
def user_choose(list_of_all_songs):
	playlist = list()		#empty list
	while True:
		print("Here are your song options:\n")
		num = 1
		for song in list_of_all_songs:
			title = song.get("title")
			artist = song.get("artist")
			album = song.get("album")
			print(str(num) + ".", title, "by", artist,"in the album", album)	
			num += 1
		print("\nChoose a song to add to your playist.")
		num_chosen = int(input("Enter the song number: "))
		song_dictionary_chosen = list_of_all_songs[num_chosen - 1]
		song_id = song_dictionary_chosen.get("id")
		title = song_dictionary_chosen.get("title")
		artist = song_dictionary_chosen.get("artist")
		year = song_dictionary_chosen.get("year")
		album = song_dictionary_chosen.get("album")
		inner_list = list()
		inner_list.append(song_id)
		inner_list.append(title)
		inner_list.append(artist)
		inner_list.append(year)
		inner_list.append(album)
		# inner_list = [song_id, title, artist, year, album]
		playlist.append(inner_list)
		choose_again = input("\nDo you want to choose another song? Y or N: ").upper()
		if choose_again == "N":
			break
	return playlist
def write_to_csv_file(two_d_structure):
	output_file_ptr = open("playlist.csv", "w")
	output_file_ptr.write("Number,Song Title,Artist,Year,Album\n")
	for song_inner_list in two_d_structure:
		song_id = str(song_inner_list[0])
		title = song_inner_list[1]
		artist = song_inner_list[2]
		year = str(song_inner_list[3])
		album = song_inner_list[4]
		output_file_ptr.write(song_id + "," + title + "," + artist + "," + year + "," + album + "\n")
		
	output_file_ptr.close()
def main(): 
	list_of_all_songs = read_json_file()
	two_d_structure_of_songs = user_choose(list_of_all_songs)
	write_to_csv_file(two_d_structure_of_songs)

main()

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# DO NOT ADD LIBRARIES/PACKAGES.
# If you want to cover additional error cases other than the given below,
# feel free to create a error message.

spotify = {
    1: {"artists": ["ROSÉ", "Bruno Mars"], "title": "APT.", "length": "2:49"},
    2: {"artists": ["Lady Gaga", "Bruno Mars"], "title": "Die With a Smile",
        "length": "4:11"},
    3: {"artists": ["Ed Sheeran"], "title": "Sapphire", "length": "2:59"},
    4: {"artists": ["Billie Eilish"], "title": "Birds of a Feather",
        "length": "3:30"},
    5: {"artists": ["Benson Boone"], "title": "Beautiful Things",
        "length": "3:00"},
    6: {"artists": ["Sabrina Carpenter"], "title": "Manchild",
        "length": "3:33"},
    7: {"artists": ["Alex Warren"], "title": "Ordinary", "length": "3:06"},
    8: {"artists": ["Billie Eilish"], "title": "Wildflower", "length": "4:21"},
    9: {"artists": ["Sabrina Carpenter"], "title": "Espresso",
        "length": "2:55"},
    10: {"artists": ["Lady Gaga"], "title": "Abracadabra", "length": "3:43"}
}


user_choice_question = "Enter what you would like to browse:\n \
                        \t1: A list of artists in the top 10 most played songs\n \
                        \t2: Song by ranking\n \
                        \t3: Songs by an artist\n \
                        \t4: Songs ordered by length\n \
                        \t0: Exit\n"

ranking_question = "Enter the ranking you're interested in (between 1 and 10): "
ranking_value_error = "Invalid input. Please enter a number."
ranking_range_error = "Ranking out of range."

artist_question = "Enter the name of the artist you're interested in: "
artist_error = "No songs were found by "

length_question = "Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): "
length_value_error = "Invalid vallue. Please enter a number."


# In[ ]:


def menu_options():
    print("""
    Enter what you would like to browse:
        1: A list of unique artists in the top 10 most played songs
        2: Song details by ranking
        3: Songs by an artist
        4: Songs ordered by length
        0: Exit
    """)
    user_input = input()

    return user_input


# In[ ]:


def option_1 (spotify_dict: dict):
    raw_artists = []
    for key, value in spotify_dict.items():
        for item in spotify_dict.get(key).get("artists"):
            if item in raw_artists:
                continue
            else:
                raw_artists.append(item)

    sorted_artists = sorted(raw_artists)

    return ", ".join(sorted_artists)


# In[ ]:


def option_2 (spotify_dict: dict):
    print("Enter the ranking you\'re interested in (between 1 and 10):")
    input_option_2 = input()
    try:
        input_option_2_int = int(input_option_2)
        if input_option_2_int > 10 or input_option_2_int <= 0:
            return 'Ranking out of range.'
        else:
            song_name = spotify_dict.get(input_option_2_int).get('title')
            artists = ", ".join(spotify_dict.get(input_option_2_int).get('artists'))
            return f"{input_option_2_int}: {song_name} by {artists}"
    except ValueError:
        return "Invalid input. Please enter a number."
    return


# In[ ]:


def option_3 (spotify_dict: dict):
    print("Enter the name of the artist you're interested in")
    input_option_3 = input()
    artist_present = False

    for key, value in spotify.items():
        
        for item in spotify_dict.get(key).get('artists'):
            if item.lower() == input_option_3.lower():
                artist_present = True
                rank = key
                title = spotify_dict.get(key).get('title')
                print(f"{rank}: {title}")
    if artist_present == False:
        print(f"{artist_error}{input_option_3}")


# In[ ]:


def option_4(spotify_dict: dict):
    print("Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): ")
    input_option_4 = input()

    try:
        input_option_4_int = int(input_option_4)
        
    except:
        print("Invalid value. Please enter a number.")
    
    songs = []
    for key,value in spotify_dict.items():
        song = []
        raw_time = spotify_dict.get(key).get('length')
        seconds = int(raw_time[:1])*60 + int(raw_time[-2:])

        song.append(spotify_dict.get(key).get('title'))
        song.append(spotify_dict.get(key).get('artists'))
        song.append(seconds)

        songs.append(song)

    songs.sort(key=lambda x: x[2], reverse=(input_option_4_int > 0))
    
    for i in range(abs(input_option_4_int)):
        title = songs[i][0]
        artists = ', '.join(songs[i][1])
        length = songs[i][2] 
        print(f"{title} by {artists} ({length} seconds)")
    
    return


# In[ ]:


while True:

    user_input = menu_options()

    if user_input == '0':
        print("Goodbye!")
        break

    if user_input == "1":
        option_1_output = option_1(spotify)
        print(option_1_output)
    
    elif user_input == "2":
        option_2_output = option_2(spotify)
        print(option_2_output)
    
    elif user_input == "3":
        option_3(spotify)
    
    elif user_input == "4":
        option_4(spotify)


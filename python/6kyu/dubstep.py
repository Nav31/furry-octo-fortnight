def song_decoder(song):
    song = song.split("WUB")
    return_string = ""
    for char in song:
        if char != "":
            return_string += char + " "
    return return_string.rstrip()

print song_decoder("AWUBWUBWUBBWUBWUBWUBC")

# Best
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())
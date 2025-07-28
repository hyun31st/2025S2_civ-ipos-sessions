import time

def bottles_of_beer():

    try:
        from colorama import Fore
    except:
        print("Please install the 'colorama' package first.")
        print('Run the command "pip install colorama" in your Python terminal.')
        return

    NUMBER_OF_BOTTLES = 20

    bottles = NUMBER_OF_BOTTLES

    while bottles >= 0:

        if bottles > 2:
            lyrics = (f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\n"
                      f"Take one down and pass it around, {bottles -1} bottles of beer on the wall.")
        elif bottles == 2:
            lyrics = (f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\n"
                      f"Take one down and pass it around, {bottles -1} bottle of beer on the wall.")
        elif bottles == 1:
            lyrics = (f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.\n"
                      f"Take one down and pass it around, no more bottles of beer on the wall.")
        else :
            lyrics = (f"No more bottles of beer on the wall, no more bottles of beer.\n"
                      f"Go to the store and buy some more, 99 bottles of beer on the wall.")

        lyrics_words = lyrics.split()

        if bottles < 10:
            print_lyrics_in_color(lyrics_words, Fore.RED)
        else :
            print_lyrics_in_color(lyrics_words, "")

        print()
        bottles -= 1

def print_lyrics_in_color(lyrics_words, colour):
    for i in range(len(lyrics_words)):
        print(colour + lyrics_words[i], end=" ")

        time.sleep(0.1)

        if lyrics_words[i][-1] == ".":
            print()

if __name__ == "__main__":
    bottles_of_beer()
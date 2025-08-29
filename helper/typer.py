import time
import sys

# Function to create the typewriter effect
def write_effect(sentence, i):
    # Loop through each character in the sentence
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    if i:
        user = input("")
        return user
    else:
        print("")

    time.sleep(0.2)

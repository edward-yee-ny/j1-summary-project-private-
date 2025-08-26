import time
import sys

# Function to create the typewriter effect
def write_effect(sentence, type_delay):
    # Loop through each character in the sentence
    for char in sentence:

        # Write, display and delay
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)

    # Pause after printing the entire sentence
    time.sleep(1)
def delete_effect(delete_delay):
    for _ in sentence:
        # Write backspace, space, delete and delay
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(delete_delay)

"""
typical settings.
type_delay = 0.05
delete_delay = 0.01
"""
import time
import sys
import select 

# Function to create the typewriter effect
def write_effect(sentence, i):
    # Loop through each character in the sentence
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.027)
    if i:
        u = input("")
        return u
    else:
        print("")

    time.sleep(1)


"""
typical settings.
type_delay = 0.05
delete_delay = 0.01

write_effect("Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!", False)
write_effect("HIIII", False)
"""
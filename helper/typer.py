import time
import sys

saved_lens = []
# Function to create the typewriter effect
def write_effect(sentence, i):
    # Loop through each character in the sentence
    saved_lens.append(len(sentence))
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
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

write_effect("Hello!", False)
write_effect("HIIII", True)

delete_effect()
write_effect("HIIII", False)
"""
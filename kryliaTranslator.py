import sys
import re

# Dictionary of your "con" language
diction = {
    "what": "qhar",
    "like tunge": "poa",
    "gay": "goa",
    "silly": "gogis",
    "good": "aboba",
    "bad": "aboba",
    "horrible": "aboba",
    "sqrt(-1)": "i"
}

# Ask for input
input1 = input("Krylian to English: ")

# Default suffix
suffix = ""

# Check command-line arguments
if len(sys.argv) > 1:
    if sys.argv[1] == "-blankstare":
        repeat_count = 1
        if len(sys.argv) > 2:
            try:
                repeat_count = int(sys.argv[2])
            except ValueError:
                raise ValueError("Second argument must be an integer for repetition count")
        suffix = ".,,.,." * repeat_count

    elif len(sys.argv) > 1:
        if len(sys.argv) > 2:
            raise NameError("Cannot specify repetition without using -blankstare first")
        # No suffix in this case

# Apply all replacements using regex for exact word/phrase matches
for old_word, new_word in diction.items():
    # Escape special regex characters in the phrase
    pattern = r'\b' + re.escape(old_word) + r'\b'
    input1 = re.sub(pattern, new_word, input1)

# Add suffix once at the end
input1 += suffix

print(input1)


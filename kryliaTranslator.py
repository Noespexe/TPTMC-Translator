import sys
import re


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

# Make the program less self centred and be more outward
input1 = input("Krylian to English: ")

# initialise suffix
suffix = ""


if len(sys.argv) > 1:
    if sys.argv[1] == "-blankstare":
        repeat_count = 1
        if len(sys.argv) > 2:
            try:
                repeat_count = int(sys.argv[2])
            except ValueError:
                raise ValueError("Why isn't it a integer?")
        suffix = ".,,.,." * repeat_count

    elif len(sys.argv) > 1:
        if len(sys.argv) > 2:
            raise NameError("use -blankstare first")
        # No suffix in this case

# Be REALLY careful with how the translator works
for old_word, new_word in diction.items():
    pattern = r'\b' + re.escape(old_word) + r'\b'
    input1 = re.sub(pattern, new_word, input1)

# Add suffix once at the end
input1 += suffix
print(input1)


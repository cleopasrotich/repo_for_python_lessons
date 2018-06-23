tabby_cat = "%s" 
persian_cat = "I'm split\non a line." # \n is skipping to the next line
backslash_cat = "I'm \\ a \\ cat."  # 2 backslash puts a backslash in a line.

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat % ("\tI'm tabbed in.") # \t is for tabbing.
print persian_cat
print backslash_cat
print fat_cat 
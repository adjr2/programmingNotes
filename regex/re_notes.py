#%%
import re

backlash_test = "\section"
print(backlash_test)
# double backslash is needed if wants to search for it.
res = re.findall(r"\\", backlash_test)
res[0]
# re.match(r"\sec", backlash_test)

#%%
backlash_test = "\\se\\section"
# double backslash is needed if wants to search for it.
re.findall(r"\\", backlash_test)

# %%
backlash_test = "\\\\section"
# double backslash is needed if wants to search for it.
re.findall(r"\\\\", backlash_test)
# %%
p = re.compile(r"(?P<word>\b\w+\b)")
# p.findall("Fasdf; EOL Fasfa \n Fasee")
m = p.search("(((( Lots of punctuation )))")
# m.group('word')
m.group(1)
# %%

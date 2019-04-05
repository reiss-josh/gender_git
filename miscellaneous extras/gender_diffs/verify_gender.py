#!/usr/bin/env python3
#
# Search conf files for invitees without verified gender and prompt for one.


import csv
import json
import re
import sys
import webbrowser

##############################################################################
# parse_author_name(): break an author string to a name, and potentially also
# an affiliation string (in parenthesis).
def parse_author_name(person):
    if re.match("[a-z]*\(", person) is not None or \
            re.match(".*\(.*[a-zA-Z ]$", person) is not None or \
            re.match(" and ", person):
                print("\t\t!!!!!!!!!! Possibly malformed name:", person)

    m = re.match("([^\(]*) \((.*)\)$", person)
    if m is None:
        return person, None
    else:
        return m.group(1), m.group(2)

##############################################################################
# normalize_author_name(): break an author string to a name and (optional)
# affiliation, and return the name only, last first, title case, no honorifics
def normalized_author_name(name):
    recased = name.title().replace('Jr.', '').replace('Sr.', '').replace('Dr.', '').replace('Prof.', '')
    names = parse_author_name(recased)[0].split()
    return names[-1] + ", " + " ".join(names[:-1])


##############################################################################
######### main

if len(sys.argv) != 2:
    print("Required argument: conference name")
    exit(1)

conf_fn = "data/conf/" + sys.argv[1] + ".json"
gender_fn = "data/verified_gender_mapping.json"
gender_fn2 = "data/verified_gender_mapping_change.json"

# Read in conference data:
try:
    print(conf_fn)
    with open(conf_fn, mode="r", encoding='utf-8') as f:
        confdata = json.load(f)
except:
    print("Couldn't read file", conf_fn)
    raise

# Read in pre-existing gender data:
genders = {}
genders2 = {}
try:
    with open(gender_fn, mode="r", encoding='utf-8') as f:
        genders = json.load(f)
except OSError:
    print("Couldn't read file", gender_fn)
    raise
try:
    with open(gender_fn2, mode="r", encoding='utf-8') as f:
        genders2 = json.load(f)
except OSError:
    print("Couldn't read file", gender_fn2)
    raise

print("Total genders:", len(genders))

for author in confdata['keynote_speakers'] + confdata['session_chairs'] + confdata['panelists'] + confdata['pc_chairs'] + confdata['pc_members']:
    name = normalized_author_name(author)
    if name in genders:
        print("Found", name, "as", genders[name])
    else:
        while (True):
            webbrowser.open_new_tab("http://google.com/search?q=" + author)
            g = input("Please enter gender for " + author + ": ")
            if g == "M" or g == "m":
                genders[name] = "M"
                genders2[name] = genders[name]
                break
            elif g == "F" or g == "f":
                genders[name] = "F"
                genders2[name] = genders[name]
                break
            elif g == "N" or g == "n":
                genders[name] = "N"
                genders2[name] = genders[name]
                break

    with open(gender_fn, mode="w", encoding='utf-8') as f:
        json.dump(genders, f, indent=4, sort_keys=True)
    with open(gender_fn2, mode="w", encoding='utf-8') as f:
        json.dump(genders2, f, indent=4, sort_keys=True)


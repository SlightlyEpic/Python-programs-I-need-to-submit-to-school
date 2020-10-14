# Create a dictionary with the roll number, name and marks of n students in a
# class and display the names of students who have marks above 75.
# 7:46 AM 14-10-2020

# Roll number <str>
#   |--- name <str>
#   |--- marks <int>

d = {
    '1': {
        'name': 'A',
        'marks': 74
    },
    '2': {
        'name': 'B',
        'marks': 80
    },
    '3': {
        'name': 'C',
        'marks': 100
    },
    '4': {
        'name': 'D',
        'marks': 73
    },
    '5': {
        'name': 'E',
        'marks': 75
    }
}

for x in d:
    elm = d[x]
    if(elm['marks'] > 75): print(f"{elm['name']} scored {elm['marks']} marks!")
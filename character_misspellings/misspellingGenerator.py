

def GerneateMisspellings():
    correct_spellings = open('correct_spellings.txt', 'r')

    for correct_spelling in correct_spellings:
        values = correct_spelling.split()
        print(values)
        with open(f'./misspelling_files/{values[0]}.txt', 'w') as f:
            f.write(correct_spelling)
        # correct_spelling.close()


GerneateMisspellings()

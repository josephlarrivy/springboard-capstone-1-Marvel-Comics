

def GerneateMisspellings():
    correct_spellings = open('correct_spellings.txt', 'r')

    for correct_spelling in correct_spellings:
        values = correct_spelling.splitlines()
        string = values[0]

        print(f'values: {values}')
        print(f'string: {string}')
        with open(f'./misspelling_files/{values[0]}.txt', 'w') as f:
            f.write(correct_spelling)
            f.write('\n')

            title = correct_spelling.title()
            f.write(title)
            f.write('\n')

            lower = correct_spelling.lower()
            f.write(lower)
            f.write('\n')

            no_spaces = lower.replace(' ', '')
            f.write(no_spaces)
            f.write('\n')

            title_no_spaces = title.replace(' ', '')
            f.write(title_no_spaces)
            f.write('\n')

            dashed_lower = lower.replace(' ', '-')
            f.write(dashed_lower)
            f.write('\n')

            dashed_upper = title.replace(' ', '-')
            f.write(dashed_upper)
            f.write('\n')

            














        # correct_spelling.close()


GerneateMisspellings()

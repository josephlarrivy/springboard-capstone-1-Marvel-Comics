def gerneate_misspellings():
    correct_spellings = open('correct_spellings.txt', 'r')

    for correct_spelling in correct_spellings:
        values = correct_spelling.splitlines()
        string = values[0]
        final_to_mix = string.replace('-', ' ')

        # print('$$$$$$$$$$$$$$')
        # print(f'correct_spelling: {correct_spelling}')
        # print(f'values: {values}')
        # print(f'string: {string}')
        # print(f'final_to_mix: {final_to_mix}')
        # print('$$$$$$$$$$$$$$')
        # print(' ')

        with open(f'./misspelling_files/{values[0]}.txt', 'w') as f:
            f.write(correct_spelling)
            f.write('\n')

        words = final_to_mix.split()
        # print(f'words: {words}')


########
        if len(words) == 1:
            with open(f'./misspelling_files/{values[0]}.txt', 'a') as f:

                title = correct_spelling.title()
                if title not in f'./misspelling_files/{values[0]}.txt':
                    f.write(title)
                    f.write('\n')

                lower = correct_spelling.lower()
                if lower not in f'./misspelling_files/{values[0]}.txt':
                    f.write(lower)
                    f.write('\n')


        if len(words) > 1:
            with open(f'./misspelling_files/{values[0]}.txt', 'a') as f:
                recombine_first_two_words = f'{words[0]} {words[1]}'
                recombine_without_paranthesis = recombine_first_two_words.replace('(', '').replace(')', '')

                f.write(recombine_without_paranthesis)
                f.write('\n')

                title = recombine_without_paranthesis.title()
                if title not in f'./misspelling_files/{values[0]}.txt':
                    f.write(title)
                    f.write('\n')

                lower = recombine_without_paranthesis.lower()
                if lower not in f'./misspelling_files/{values[0]}.txt':
                    f.write(lower)
                    f.write('\n')

                no_spaces = lower.replace(' ', '')
                if no_spaces not in f'./misspelling_files/{values[0]}.txt':
                    f.write(no_spaces)
                    f.write('\n')

                title_no_spaces = title.replace(' ', '')
                if title_no_spaces not in f'./misspelling_files/{values[0]}.txt':
                    f.write(title_no_spaces)
                    f.write('\n')

                dashed_lower = lower.replace(' ', '-')
                if dashed_lower not in f'./misspelling_files/{values[0]}.txt':
                    f.write(dashed_lower)
                    f.write('\n')

                dashed_upper = title.replace(' ', '-')
                if dashed_upper not in f'./misspelling_files/{values[0]}.txt':
                    f.write(dashed_upper)
                    f.write('\n')

        if len(words) > 2:
            with open(f'./misspelling_files/{values[0]}.txt', 'a') as f:
                recombine_second_two_words = f'{words[1]} {words[2]}'
                recombine_without_paranthesis = recombine_second_two_words.replace('(', '').replace(')', '')

                f.write(recombine_without_paranthesis)
                f.write('\n')

                title = recombine_without_paranthesis.title()
                if title not in f'./misspelling_files/{values[0]}.txt':
                    f.write(title)
                    f.write('\n')

                lower = recombine_without_paranthesis.lower()
                if lower not in f'./misspelling_files/{values[0]}.txt':
                    f.write(lower)
                    f.write('\n')

                no_spaces = lower.replace(' ', '')
                if no_spaces not in f'./misspelling_files/{values[0]}.txt':
                    f.write(no_spaces)
                    f.write('\n')

                title_no_spaces = title.replace(' ', '')
                if title_no_spaces not in f'./misspelling_files/{values[0]}.txt':
                    f.write(title_no_spaces)
                    f.write('\n')

                dashed_lower = lower.replace(' ', '-')
                if dashed_lower not in f'./misspelling_files/{values[0]}.txt':
                    f.write(dashed_lower)
                    f.write('\n')

                dashed_upper = title.replace(' ', '-')
                if dashed_upper not in f'./misspelling_files/{values[0]}.txt':
                    f.write(dashed_upper)
                    f.write('\n')

        if len(words) > 3:
            with open(f'./misspelling_files/{values[0]}.txt', 'a') as f:
                recombine_thid_and_fourth = f'{words[2]} {words[3]}'
                recombine_without_paranthesis = recombine_thid_and_fourth.replace(
                    '(', '').replace(')', '')

                f.write(recombine_without_paranthesis)
                f.write('\n')

                title = recombine_without_paranthesis.title()
                if title not in f'./misspelling_files/{values[0]}.txt':
                    f.write(title)
                    f.write('\n')

                lower = recombine_without_paranthesis.lower()
                if lower not in f'./misspelling_files/{values[0]}.txt':
                    f.write(lower)
                    f.write('\n')

                no_spaces = lower.replace(' ', '')
                if no_spaces not in f'./misspelling_files/{values[0]}.txt':
                    f.write(no_spaces)
                    f.write('\n')

                title_no_spaces = title.replace(' ', '')
                if title_no_spaces not in f'./misspelling_files/{values[0]}.txt':
                    f.write(title_no_spaces)
                    f.write('\n')

                dashed_lower = lower.replace(' ', '-')
                if dashed_lower not in f'./misspelling_files/{values[0]}.txt':
                    f.write(dashed_lower)
                    f.write('\n')

                dashed_upper = title.replace(' ', '-')
                if dashed_upper not in f'./misspelling_files/{values[0]}.txt':
                    f.write(dashed_upper)
                    f.write('\n')



########
        

########
#         if len(words) >= 2:
#             with open(f'./misspelling_files/{values[0]}.txt', 'a') as f:

#                 recombine1 = f'{words[0]} {words[1]}'
#                 recombine4 = recombine1.replace('(', '').replace(')', '')
#                 # print(recombine4)
#                 f.write(recombine4)
#                 f.write('\n')

#                 title = recombine4.title()
#                 f.write(title)
#                 f.write('\n')

#                 lower = recombine4.lower()
#                 f.write(lower)
#                 f.write('\n')

#                 no_spaces = lower.replace(' ', '')
#                 f.write(no_spaces)
#                 f.write('\n')

#                 title_no_spaces = title.replace(' ', '')
#                 f.write(title_no_spaces)
#                 f.write('\n')

#                 dashed_lower = lower.replace(' ', '-')
#                 f.write(dashed_lower)
#                 f.write('\n')

#                 dashed_upper = title.replace(' ', '-')
#                 f.write(dashed_upper)
#                 f.write('\n')

# ########

#         if len(words) > 3:
#             with open(f'./misspelling_files/{values[0]}.txt', 'a') as f:

#                 recombine2 = f'{words[2]} {words[3]}'
#                 recombine3 = recombine2.replace('(', '').replace(')', '')
#                 # print(f'recombine3: {recombine3}')
#                 # print('###############')
#                 f.write(recombine3)
#                 f.write('\n')

#                 title = recombine3.title()
#                 f.write(title)
#                 f.write('\n')

#                 lower = recombine3.lower()
#                 f.write(lower)
#                 f.write('\n')

#                 no_spaces = lower.replace(' ', '')
#                 f.write(no_spaces)
#                 f.write('\n')

#                 title_no_spaces = title.replace(' ', '')
#                 f.write(title_no_spaces)
#                 f.write('\n')

#                 dashed_lower = lower.replace(' ', '-')
#                 f.write(dashed_lower)
#                 f.write('\n')

#                 dashed_upper = title.replace(' ', '-')
#                 f.write(dashed_upper)
#                 f.write('\n')

        else:
            pass

gerneate_misspellings()

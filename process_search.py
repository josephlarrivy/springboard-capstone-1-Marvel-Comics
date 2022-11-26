

# import os
# from forms import SearchForm
# from flask_debugtoolbar import DebugToolbarExtension
# from flask import render_template

# def process_search(search_term, username):
#     searchform = SearchForm

#     title_search_term = search_term.title()
#     search_term = title_search_term.strip()

#     directory = 'character_misspellings/misspelling_files'
#     search_results = []

#     for filename in os.listdir(directory):
#     # print(f'filename: {filename}')
#         f = open(f'{directory}/{filename}', 'r')
#         content = f.read()
#         lines = content.splitlines()
#         for line in lines:
#             # print(f'content: {line}')
#             if search_term in line:
#                 corrected_name = filename.removesuffix('.txt')
#                 # print('##############')
#                 # print(corrected_name)
#                 if corrected_name not in search_results:
#                     search_results.append(corrected_name)
#                 # print(search_results)
#     # if len(search_results) == 0:
#     #     flash("Cannot find a character with that name")
#     #     return redirect('/search/characters')

#     # elif len(search_results) == 1:
#     #     return redirect(f'/view_character/{search_results[0]}')
#     directory = 'series_names/series_names_files'
#     series_search_results = {}

#     for filename in os.listdir(directory):
#         # print('$$$$$$$$$$$$$$')
#         # print(f'filename: {filename}')
#         # print('$$$$$$$$$$$$$$')
#         f = open(f'{directory}/{filename}', 'r')
#         content = f.read()
#         # print(content)
#         # print('########')

#         l = open(f'{directory}/{filename}', 'r')
#         first_line = l.readline()
#         series_name = first_line.removesuffix('\n')

#         # f = open(f'{directory}/{filename}', 'r')
#         series_id = filename.removesuffix('.txt')

#         # print(series_name)
#         # print(series_id)
#         # print('  ')
#         # time.sleep(0.1)

#         split_terms = search_term.split()
#         # print(split_terms)

#         for term in split_terms:
#             if term in content:
#                 # print(term)
#                 # print(content)
#                 series_search_results[series_id] = series_name

#         # print(series_search_results)
#         for item in series_search_results:
#             # print(item)
#             # print(series_search_results[item])
#             pass

#         print(series_search_results)
#         print(search_results)



#         nav_image_src = "/static/images/marvel-logo.webp"
#         return render_template('/content/characters/display_search_results.html', search_results=search_results, series_search_results=series_search_results, nav_image_src=nav_image_src, username=username, searchform=searchform)





        # from spell_correction import correct_misspelling

        # corrected_character_spelling = correct_misspelling(search_term)
        # print(corrected_character_spelling)

        ################

        # from character_misspellings import spell_correct_character_names as spell_correct
        # corrected_character_spelling = spell_correct.search_for_misspelling(search_term)

        # return redirect(f'/view_character/{corrected_character_spelling}')


               # keys = item.keys()
           # print(keys)


           # words = content.split(' ')
           # for word in words:

           #     # print(f'content: {line}')
           #     if search_term == word:
           #         # string_series_id = str(series_id)
           #         # print(' ')
           #         # print(string_series_id)
#         # print('##############')

#         append_one = 0
#         if append_one == 0:
#             series_search_results.append([series_id, series_name])
#             append_one = append_one + 1
#         #     print(append_one)

#         # if (string_series_id in sublist for sublist in series_search_results):
#         #     print(string_series_id)
#         #     print(series_search_results)

#         # # if series_id in series_search_results:
#         # #     pass
#         # else:
#         #     time.sleep(0.1)

#         #     series_search_results.append([series_id, series_name])

#         # # else:
#         #     for element in series_search_results:
#         #         # print(element[0])
#         #         # print(series_search_results)
#         #         # print('??????????')
#         #         # print(element)
#         #         # print(element[0])
#         #         # print('??????????')

#         #         # string_series_id = element[0]
#         #         # print('$$$$$$$$$$$')
#         #         # print(string_series_id)
#         #         # print('$$$$$$$$$$$')

#         #         if series_id in series_search_results:
#         #             pass
#         #         else:
#         #             series_search_results.append([series_id, series_name])

#         def find_int(l, target):
#             for sub_list in range(len(l)):
#                 if target not in l[sub_list]:
#                     # print("It's in a list with index " + str(sub_list))
#                     print("In list with index " + str(sub_list) + ", it has index " + str(l[sub_list].index(target)))
#                     print(' ')
#                     print(str(series_search_results[l[sub_list].index(target)]))
#                     series_search_results.append([series_id, series_name])

#                 else:
#                     pass
#         find_int(series_search_results, series_id)

# if find_int(series_search_results, series_id):
#     pass
# else:
#     series_search_results.append([series_id, series_name])

# if string_series_id not in series_search_results:
#     # series_search_results.append(series_id)
#     # series_search_results.append(str(series_name))
#     series_search_results.append([series_id, series_name])

# print(series_search_results)
# series_search_results_length = len(series_search_results)

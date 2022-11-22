import os
directory = 'misspelling_files'

def search_for_misspelling(search_value):
    for filename in os.listdir(directory):
        # print(f'filename: {filename}')

        f = open(f'{directory}/{filename}', 'r')
        content = f.read()
        lines = content.splitlines()
        for line in lines:
            # print(f'content: {line}')
            if search_value == line:
                corrected_name = filename.removesuffix('.txt')
                print(corrected_name)
        # print("#####################")

        f. close()

search_for_misspelling('doctor strange')
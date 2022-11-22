import os

directory = 'misspelling_files'


def search_for_misspelling(search_value):
    for filename in os.listdir(directory):
        print(f'filename: {filename}')

        f = open(f'{directory}/{filename}', 'r')
        content = f.read()

        # todo: need to add a line that splits the file on each new line so the file can be iterated?

        print(f'      content: {content}')
        if search_value in f.read():
            print("#####################")
        f. close()




        # with open(filename, 'r', encoding='utf-8') as f:
        #     print(filename)
        #     if search_value in f.read():
        #         return filename
        #     else:
        #         pass

################

        # obj = os.scandir(filename)
        # for entry in obj:
        #     print(entry)


search_for_misspelling('captainamerica')

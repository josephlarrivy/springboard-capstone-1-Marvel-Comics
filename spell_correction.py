from models import Character
from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY
marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)
characters = marvel.characters

def correct_misspelling(character_search):
    # check if the spelling that the user gives matches correctly with an entry in the database
    # if Character.query.get(character_search):
    #     # if the spelling will return an entry, keep that spelling and send it back to app.py
    #     return character_search
    # # if the spelling does not return a match in the database, use the data in the list below to try and correct any predictable misspellings
    try:
        response = [sub[0] for sub in spell_corrector if character_search in sub[1]]
        # if a predictabel misspelling is found, return the corrected spelling to app.py
        return (response[0])
    except IndexError:
        # if the search term is not recognized in the common misspellings, let the term go through to the next step
        return IndexError
    # try:
    #     # try and see if the search term will return a match from the API
    #     characters.all(name=f'{character_search}')['data']['results'][0]
    #     # if the term will return a match from the API, return the search term to app.py
    #     return character_search
    # except IndexError:
    #     # if the term will not return a match from the API, return an INDEXERROR
    #     return IndexError
    

# def correct_misspelling(character_search):
#     # check if the spelling that the user gives matches correctly with an entry in the database
#     if Character.query.get(character_search):
#         # if the spelling will return an entry, keep that spelling and send it back to app.py
#         return character_search
#     else:
#         # check if the spelling will return a character from the API
#         try:
#             characters.all(name=f'{character_search}')['data']['results'][0]
#             # if the spelling will return a character from the API, keep the spelling and send it back to app.py
#             return character_search
#         except IndexError:
#             pass
#         # if the search term will not return anything from the database or the API in its current spelling, look in the list below and see if the spelling can be corrected to a spelling that we kow will return a good value either from the database or from the API
#         try:
#             response = [sub[0] for sub in spell_corrector if character_search in sub[1]]
#             return (response[0])
#         except IndexError:
#             pass
    



spell_corrector = [
    ('Captain America',
        ['Captain America', 'Captainamerica', 'Captain-america', 'Captain-America']),
    ('Captain Marvel (Carol Danvers)',
        ['Captain Marvel (Carol Danvers)', 'Captain Marvel', 'Carol Danvers', 'Captainmarvel', 'Captain-marlvel', 'Captain-Marvel']),
    ('Ironheart (Riri Williams)',
        ['Ironheart (Riri Williams)', 'Ironheart', 'Iron Heart', 'Iron-heart', 'iron-heart', 'ironheart']),
    ('Iron Man',
        ['Iron Man', 'Ironman', 'Iron-man', 'Tony Stark']),
    ('Spider-Man (Peter Parker)',
        ['Spider-Man (Peter Parker)', 'Spider-Man', 'spiderman', 'Spider-Man', 'spider-man', 'spidey', 'Spiderman', 'peter parker', 'Peter Parker']),
    ('War Machine (James Rhodes)',
        ['War Machine (James Rhodes)', 'War Machine', 'Warmachine', 'War-machine', 'James Rhodes']),
    ('Quake (Daisy Johnson)',
        ['Quake (Daisy Johnson)', 'Quake', 'Daisy Johnson']),
    ('Ms. Marvel (Kamala Khan)',
        ['Ms. Marvel (Kamala Khan)', 'Ms Marvel', 'Miss Marvel', 'Missmarvel', 'Mrs Marvel', 'Miss-marvel', 'Miss-Marvel']),
    ('Guardians Of The Galaxy',
        ['Guardians Of The Galaxy', 'Guardians Galaxy', 'guardians of the galaxy']),
    ('Avengers',
        ['Avengers', 'The Avengers']),
    ('Star-Lord (Peter Quill)',
        ['Star-Lord (Peter Quill)', 'Star Lord', 'star lord', 'starlord', 'Peter Quill', 'peter quill']),
    ('Tiger Shark',
        ['Tiger Shark', 'Tiger Shark', 'tiger shark', 'tiger-shark', 'Tiger-shark', 'tiger-shark']),
    ('Black Panther',
        ['Black Panther', 'black panther', 'Blackpanther', 'blackpanther', 'Black-panther', 'black-panther']),
    ('Shocker (Herman Schultz)',
        ['Shocker (Herman Schultz)', 'shocker', 'Shocker', 'Herman Schults', 'herman schults']),
    ('Dani Moonstar',
        ['Dani Moonstar', 'Moonstar']),
    ('Quasar (Wendell Vaughn)',
        ['Quasar (Wendell Vaughn)', 'Quasar', 'Quassar', 'Wendell Vaugn', 'wendell vaughn']),
    ('Doctor Strange',
        ['Doctor Strange', 'doctor strange', 'doctor-stange', 'Doctor-strange']),
    ('Quasar (Phyla-Vell)',
        ['Quasar (Phyla-Vell)', 'Quasar', 'quasar', 'quaasar', 'Phyla-Vell', 'Phyla-vell']),
    ('Doctor Doom',
        ['Doctor Doom', 'doctor doom', 'Doctor-doom', 'doctor-doom', 'doctordoom', 'Doctordoom']),
    ('Black Widow',
        ['Black Widow', 'black-widow', 'Black-Widow', 'blackwidow', 'Blackwidow', 'BlackWidow']),
    ('',
        ['', '']),
    ('',
        ['', '']),
    ('',
        ['', '']),
    ('',
        ['', '']),
    ('',
        ['', '']),
    ]

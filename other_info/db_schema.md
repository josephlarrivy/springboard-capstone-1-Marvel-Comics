QuickDstsBaseDiagrams-formatted database schema layout (copy & paste into quickdbd)

<!-- xxxxxxxxxxxxxxxxxxxxxxxx -->

user
-
id
username
password
first_name
last_name

lists
-
list_name
id (pk)
user_id FK >- user.id

list_series
-
list_id FK >- lists.id
series_id FK >- series.series_id

characters
-
character_id
name

series
-
series_id
comic_name

series_character
-
series_id FK >- series.series_id
character_id FK >- characters.character_id

list_character
-
list_id FK >- lists.id
character_id FK >- characters.character_id
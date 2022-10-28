QuickDB formatted database schema layout

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
id (pk)
user_id FK >- user.id
list_name
list_items
list_user_content
comments FK >- user.id

characters
-
character_id
name

title
-
title_id
title_name FK >- lists.list_items
characters

title_character
-
title_id FK >- title.title_id
character_id FK >- characters.character_id

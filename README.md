# watch_next

A program which compares the similarity of a user has just watched to a list of movies and suggests which movie the user
should watch next. 

The program makes use of the en_core_web_md model which uses model vectors to compare the descriptions of two movies and returns a value between 0 and 1 signifying it's similarity. With 1 being extremely similar.

def print_upper_words(words, must_start_with):
   """Print each word on a separate line in all capital letters if the word starts with either "h" or "y"
   """
   # words_upper = [word.upper() for word in words]
   # print(words_upper)

   # start_with = list(must_start_with)
  
   for word in words:
      letter = (word[0])
      if letter in must_start_with:
         print(word.upper())
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with=["h", "y"])


def print_upper_words2(words):
   """Print each word on a separate line in all capital letters.
   """
   for word in words:
      print(word.upper())
print_upper_words2(["Programming", "is", "pretty", "fun"])


def print_upper_words3(words):
   """Print each word on a separate line in all capital letters if the word starts with "e" or "E"
   """
   for word in words:
      if word.startswith("e") or word.startswith("E"):
         print(word.upper())
print_upper_words3(["eagle", "Edward", "Alfred"])
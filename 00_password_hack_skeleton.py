"""
Sample utility to hash a plain text.

Here, we see how it converts it into a stream of hex digits
And it's easy to see how the hex digits changes if the original
changes

Then we see the hashing (SHA-1) and how the new hex digits change
in a strange/unpredictable manner regardless of how the original
text is changed

"""
import hashlib
import os

#  The password hash that I'm trying to crack
# PART 1, one word.  This is just one of the words in the dictionary
my_pwd_hash_1='9f2feb0f1ef425b292f2f94bc8482494df430413'

# PART 2, one word + number.  This is one of the words in the dictionary
# with 0-1 appended to the end.
my_pwd_hash_2='f3628e468ee2a938b35df69c19a29b2416870e2a'

# PART 3, two words.  These are two of the words in the dictionary
#  appended onto each other.
my_pwd_hash_3 = 'a4f66e2aef435ea88df00fbd552dd3979c9635a3'




MY_DIR = os.path.dirname(os.path.realpath(__file__))

dictionary_fname = 'my_password_list.txt'

ifname = f'{MY_DIR}/{dictionary_fname}'

# Module 1 Read all the words

# How to read in all the words from the password dictionary and
# stuff into a list

password_list = []
with open(ifname) as inf:
    for word in inf:
        # strip out the newline char at the end of each word
        word = word.strip()
        print(word)
        password_list.append(word)

# Module 2 hash a word

my_text = 'some_word'
encoded_text = my_text.encode('utf-8')
h = hashlib.sha1(encoded_text)
digest = h.hexdigest()

print(f'word "{my_text}" hashes into {digest}')
print(password_list)

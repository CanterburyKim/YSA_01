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

my_text = 'Hello'

encoded_text = my_text.encode('utf-8')
h = hashlib.sha1(encoded_text)
digest = h.hexdigest()


print(f'my text {my_text} encodes into these hex digits:')
for ch in encoded_text:
    print(f'{ch:02x}' , end = '')

print('\n\nnow doing HASH.  using SHA-1')


print()

print(f'word "{my_text}" hashes into {digest}')

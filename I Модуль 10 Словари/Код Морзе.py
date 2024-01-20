letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']

morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
         '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
         '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----',
         '.----', '..---', '...--', '....-', '.....', '-....', '--...',
         '---..', '----.'
         ]

my_dict = dict(zip(letters, morse))
s = input().upper()
s1 = "".join(c for c in s if c.isalnum())
for letters in s1:
    print(my_dict[letters], end=' ')

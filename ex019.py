import random

h = random.randint(1, 4)
h = random.randrange(1, 5)

if h == 1:
    print("A aluna escolhida a apagar o quadro é a Mariana")
elif h == 2:
    print("A aluna escolhida a apagar o quadro é a Livia")
elif h == 3:
    print("A aluna escolhida a apagar o quadro é a Fernanda")
else:
    print("A aluna escolhida a apagar o quadro é a Duda")

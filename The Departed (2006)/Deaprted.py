cia_jets = []

for i in range(1, 6):
    registration_code = input().strip()
    if "FBI" in registration_code:
        cia_jets.append(i)

if cia_jets:
    print(" ".join(map(str, cia_jets)))
else:
    print("HE GOT AWAY!")

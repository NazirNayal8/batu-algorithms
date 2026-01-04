#BOYD
#CAT

def make_matrix(rows, columns):
    matrix =[[] for _ in range(rows)] # [[], [], []]
    for r in range(rows):
        for c in range(columns):
            matrix[r].append('') # [['', '''', ], ['', '', ''], ['', '', '']]
    return matrix

def encrypt(key, msg):
    pass

def decrypt(key, msg):
    pass

key = input("Enter the key:")
use = int(input("Press 0 to encrypt 1 to decrypt:"))

while use not in [0, 1]:
    use = int(input("Invalid input. Press 0 to encrypt 1 to decrypt:"))

if use == 0:
    msg = input("Enter the message:")
    result = encrypt(key, msg)    
else:
    msg = input("Enter the encrypted message:")
    result = decrypt(key, msg)

print(result)
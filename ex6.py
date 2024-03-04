def check_sequence(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] == '0' and sequence[i + 1] == '1':
            continue
        elif sequence[i] == '1' and sequence[i + 1] == '0':
            continue
        else:
            return False
    return True


sequence1 = "01010101"
sequence2 = "00011100011"

print(check_sequence(sequence1)) 
print(check_sequence(sequence2))  

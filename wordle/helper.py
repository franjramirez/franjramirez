def helperOcc(words, index):
    occurence = [0] * 26
    for word in words:
        if word[index] == 'a':
            occurence[0] += 1
        elif word[index] == 'b':
            occurence[1] += 1
        elif word[index] == 'c':
            occurence[2] += 1
        elif word[index] == 'd':
            occurence[3] += 1
        elif word[index] == 'e':
            occurence[4] += 1
        elif word[index] == 'f':
            occurence[5] += 1
        elif word[index] == 'g':
            occurence[6] += 1
        elif word[index] == 'h':
            occurence[7] += 1
        elif word[index] == 'i':
            occurence[8] += 1
        elif word[index] == 'j':
            occurence[9] += 1
        elif word[index] == 'k':
            occurence[10] += 1
        elif word[index] == 'l':
            occurence[11] += 1
        elif word[index] == 'm':
            occurence[12] += 1
        elif word[index] == 'n':
            occurence[13] += 1
        elif word[index] == 'o':
            occurence[14] += 1
        elif word[index] == 'p':
            occurence[15] += 1
        elif word[index] == 'q':
            occurence[16] += 1
        elif word[index] == 'r':
            occurence[17] += 1
        elif word[index] == 's':
            occurence[18] += 1
        elif word[index] == 't':
            occurence[19] += 1
        elif word[index] == 'u':
            occurence[20] += 1
        elif word[index] == 'v':
            occurence[21] += 1
        elif word[index] == 'w':
            occurence[22] += 1
        elif word[index] == 'x':
            occurence[23] += 1
        elif word[index] == 'y':
            occurence[24] += 1
        elif word[index] == 'z':
            occurence[25] += 1

    return occurence

def helperProb(probabilities, words,index):
    occurence = [0] * len(words)
    count = 0
    for word in words:
        if word[index] == 'a':
            occurence[count] = probabilities[0]
            count += 1
        elif word[index] == 'b':
            occurence[count] = probabilities[1]
            count += 1
        elif word[index] == 'c':
            occurence[count] = probabilities[2]
            count += 1
        elif word[index] == 'd':
            occurence[count] = probabilities[3]
            count += 1
        elif word[index] == 'e':
            occurence[count] = probabilities[4]
            count += 1
        elif word[index] == 'f':
            occurence[count] = probabilities[5]
            count += 1
        elif word[index] == 'g':
            occurence[count] = probabilities[6]
            count += 1
        elif word[index] == 'h':
            occurence[count] = probabilities[7]
            count += 1
        elif word[index] == 'i':
            occurence[count] = probabilities[8]
            count += 1
        elif word[index] == 'j':
            occurence[count] = probabilities[9]
            count += 1
        elif word[index] == 'k':
            occurence[count] = probabilities[10]
            count += 1
        elif word[index] == 'l':
            occurence[count] = probabilities[11]
            count += 1
        elif word[index] == 'm':
            occurence[count] = probabilities[12]
            count += 1
        elif word[index] == 'n':
            occurence[count] = probabilities[13]
            count += 1
        elif word[index] == 'o':
            occurence[count] = probabilities[14]
            count += 1
        elif word[index] == 'p':
            occurence[count] = probabilities[15]
            count += 1
        elif word[index] == 'q':
            occurence[count] = probabilities[16]
            count += 1
        elif word[index] == 'r':
            occurence[count] = probabilities[17]
            count += 1
        elif word[index] == 's':
            occurence[count] = probabilities[18]
            count += 1
        elif word[index] == 't':
            occurence[count] = probabilities[19]
            count += 1
        elif word[index] == 'u':
            occurence[count] = probabilities[20]
            count += 1
        elif word[index] == 'v':
            occurence[count] = probabilities[21]
            count += 1
        elif word[index] == 'w':
            occurence[count] = probabilities[22]
            count += 1
        elif word[index] == 'x':
            occurence[count] = probabilities[23]
            count += 1
        elif word[index] == 'y':
            occurence[count] = probabilities[24]
            count += 1
        elif word[index] == 'z':
            occurence[count] = probabilities[25]
            count += 1
    return occurence
# very simple encrypting logic where when you encrypt something like a string, it takes every character in the string takes the places where it appears in the string and puts all that information
# together in another string


def encrypt(text):
    # initiating and setting some variables
    text = str(text)
    text = list(text)
    chars = []
    chars_check = []

    for character in range(len(text)):
        # checking if we already came across the character
        chars_check.append(text[character])
        if len(chars) >= 1:
            count_bad = 0
            count_good = 0
            for char in text:
                if char == chars_check[len(chars_check)-1]:
                    count_bad += 1
            for char in chars_check:
                if char == text[character]:
                    count_good += 1
            if count_bad > 1 and count_good > 1:
                pass
            else: # if not then add it to the encryption
                chars.append(":"+text[character])


                for character_count in range(len(text)):
                    if text[character] == text[character_count]:
                        chars.append("."+str(character_count))
        else:
            chars.append(":" + text[character])

            for character_count in range(len(text)):
                if text[character] == text[character_count]:
                    chars.append("." + str(character_count))

    result = "".join(chars)
    return result


def decrypt(text):
    loop = True
    count = 0
    biggest = 0
    previous_biggest = 0
    result = ""
    text_list = text.split(':')
    dictionary = {}
    for i in range(1,len(text_list)):
        positions = []
        char_positions = text_list[i].split(".")
        for i2 in range(1,len(char_positions)):
            positions.append(char_positions[i2])
        dictionary[str(char_positions[0])] = '.'.join(positions)
    for character in dictionary:
        places = dictionary[character].split(".")
        for place in places:
            if int(place) > int(previous_biggest):
                biggest = place
            previous_biggest = biggest
    while loop:
        for character in dictionary:
            places = dictionary[character].split(".")
            for place in places:
                if int(place) == count:
                    result += character
        if len(result)-1 == int(biggest):
            loop = False
        count += 1

    return result

encrypted = encrypt('Hi, this is a testing test')
print(encrypted)
print(decrypt(encrypted))

# Kenneth John Costa
# Assignment #2
# Decryption

print("DECRYPTION".center(45, "="))

# Ask the user to enter the message to decrypt
encrypted_message = input("\033[96mPlease enter the message you want to decrypt: ")
decrypted_message = ""

#Substitute the characters by replacing it to corresponding vowels

# If the character is *, change to a
decrypted_message = encrypted_message.replace("*","a")

# If the character is &, change to e
decrypted_message = encrypted_message.replace("&","e")

# If the character is #, change to i
decrypted_message = encrypted_message.replace("#","i")

# If the character is +, change to o
decrypted_message = encrypted_message.replace("+","o")

# If the character is !, change to u
decrypted_message = encrypted_message.replace("!","u")

# Print the decrypted message
print("\033[93mThe decrypted message is:", decrypted_message)

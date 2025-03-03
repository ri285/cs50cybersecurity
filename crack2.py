def custom_decrypt(encrypted_text):
    shift = 3  # Same shift used for encryption
    reversed_text = "".join(chr(ord(c) - shift) for c in encrypted_text)  # Reverse shift
    original_text = reversed_text[::-1]  # Reverse back to original
    print(original_text)

hidden_encrypted_pass = ""  
custom_decrypt(hidden_encrypted_pass)

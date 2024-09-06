import base64

def custom_decode(encoded_data):
    decoded = []
    for i, char in enumerate(encoded_data):
        decoded_char = chr(ord(char) - (i % 5))
        decoded.append(decoded_char)
    return ''.join(decoded)

def solve():
    final_encoded_flag = "SVRFNUdUR316NGFpYTQ5X3VqNDlfNHBmNGQycGpjNXV0M3JnYDVxNHVoakLCgQ=="

    # Step 1: Add padding to the base64 encoded flag 
    padding_needed = len(final_encoded_flag) % 4
    if padding_needed > 0:
        final_encoded_flag += '=' * (4 - padding_needed)

    # Step 2: Base64 decode the flag
    encoded_flag = base64.b64decode(final_encoded_flag).decode('utf-8')

    # Step 3: Reverse the custom encoding
    flag = custom_decode(encoded_flag)

    print("Recovered flag:", flag)


solve()
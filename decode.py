def decode_string(encoded_str, pattern):
    """Decodes the given encoded string using the provided encryption pattern."""
    # first need to reverse pattern because is plain text to encryption as k,v
    reverse_pattern = {v:k for k,v in pattern.items()}
    # iterate through encryption pattern
    out_ls = []
    for char in encoded_str:
        if reverse_pattern.get(char) is None:
            out_ls.append(' ')
        else:
            out_ls.append(reverse_pattern[char])
    return ''.join(out_ls)
    # decoding_map = {v: k for k, v in pattern.items()}  # Reverse the mapping for decoding
    
    # decoded_chars = [decoding_map.get(char, char) for char in encoded_str]  # Replace based on pattern
    
    # return ''.join(decoded_chars)

# Example usage
encryption_pattern = {
    'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q',
    'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v',
    'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a',
    'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f',
    'u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k', 'z': 'l'
}

encoded_message = "tqxxa iadxp"
decoded_message = decode_string(encoded_message, encryption_pattern)
print("Decoded Message:", decoded_message)
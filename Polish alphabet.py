def correct_polish_letters(st): 
    polish_chars = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    corrected_string = ''.join(polish_chars[char] if char in polish_chars else char for char in st)
    return corrected_string
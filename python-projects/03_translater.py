def vowel_translater(text):
    small_vowels = "aeiou"
    capital_vowels = "AEIOU"
    translated_text=""
    for char in text:
        if char in small_vowels:
            translated_text += "g"
        elif char in capital_vowels:
            translated_text += "G"
        else:
            translated_text += char
    return translated_text
            
translated_version = vowel_translater("TalhA")
print("Text after translation :" ,translated_version)
    
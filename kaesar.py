alphabet = "ئابپتجچحخدرڕزژسشعغفڤقکگلڵمنوۆھەیێ"

def encrypt(text, key):
  output = ""
  for char in text:
    if char in alphabet:
      position = alphabet.find(char)
      newposition = (position + key) % 33
      newChar = alphabet[newposition]
      output += newChar
    else:
      output += char
  return output

def decrypt(text, key):
  output = ""
  for char in text:
    if char in alphabet:
      position = alphabet.find(char)
      newposition = (position - key) % 33
      originalChar = alphabet[newposition]
      output += originalChar
    else:
      output += char
  return output

if __name__ == "__main__":
  k = int(input("٠ بنووسە بۆ ئینکریپت یاخود ١ بۆ دیکریپت کردن: "))
  text = input("شتێک بنووسە: ")
  key = int(input("کلیل: "))

  if k == 0: print(encrypt(text, key))
  elif k == 1: print(decrypt(text, key))
  else: print("دووبارە هەوڵ بدەرەوە")
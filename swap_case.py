def swap_case(s):
  swapped = ""
  for i in range(0, len(s)):
    if s[i].isupper():
      swapped += s[i].lower()
    elif s[i].islower():
      swapped += s[i].upper()
    else:
      swapped += s[i]
  return swapped

if __name__ == '__main__':
  s = input()
  result = swap_case(s)
  print(result)

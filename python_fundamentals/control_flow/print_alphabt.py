#!/usr/bin/env python3

result = ""
for alpha_letters in range(ord('a'), ord('z')+1):
    if alpha_letters == ord('e') or alpha_letters == ord('q'):
       continue
    result = result + chr(alpha_letters)
print(result)

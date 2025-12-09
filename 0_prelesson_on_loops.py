# loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# while loops  
# for loops = execute of code a fixed number of times 
    # You can iterate over a r ange, string and sequence etc.

 credit_card = "2318-2132-2132-5434"
for x in credit_card:
   print(x)
for x in reversed(range(1, 11, 2)):
   # print(x)
#for x in range(1, 11, 2):
   # print(x)
# print("Happy New Year")

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)


        
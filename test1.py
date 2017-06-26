
# name = '' 
# print name                           # (1)
# while name != 'your name':          # (2)
#     print('Please type your name.')
#     name = raw_input()
# print name                      # (3)
# print('Thank you!')                 # (4)



# while True:                         # (1)
#     print('Please type your name.')
#     name = raw_input()                  # (2)
#     if name == 'your name':         # (3)
#         break                       # (4)
# print('Thank you!')                 # (5)



while True:
  print('Who are you?')
  name = raw_input()
  if name != 'Joe':       #(1)
    continue              #(2)
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = raw_input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)
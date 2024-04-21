alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
operation=input("enter your choice encode or decode").lower()
message=input(f"your message to {operation} is")
swift= int(input("number of swift"))
if operation=="encode":
    def encryption(m,s):
         cryptotxt=""
         for i in message:
            postion=alphabets.index(i)
            new=postion+swift
            cryptotxt= cryptotxt+alphabets[new]
         print(f" your encoded message is  {cryptotxt}")
    encryption(message,swift)
elif operation=="decode":
    def decryption(m,s):
        pliantext = ""
        for i in message:
            postion=alphabets.index(i)
            new=postion-swift
            pliantext=pliantext+alphabets[new]
        print(f" your decoded message is  {pliantext}")
    decryption(message,swift)


# words = ["apple","orange","banana","lime","Lemon"]
# with open ("./text.txt") as file:
#     paragraph=file.read();

#     paraCount = int(input("paragraph count : "))

#     for count in range(paraCount):
#         with open ("./generator.txt","a") as write_file:
#             write_file.write(paragraph+"\n\n")


from urllib.request import urlretrieve

link =  input("image download link: ")

fileName = input("file Name : ")

urlretrieve(link,"image/"+ fileName + ".jpg")
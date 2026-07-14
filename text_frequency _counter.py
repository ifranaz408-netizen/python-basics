print("welcome to day 7 :Text Frequency Counter")
user = input("enter your name : ")
paragraph = input("Enter your paragraph here: ").lower().replace(",", "").replace(".", "")
word_list = paragraph.split()
text = { word for word in word_list}
frequency_dict = {word: word_list.count(word) for word in text}
print(frequency_dict)

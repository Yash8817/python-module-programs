# -------------check supported languages--------------
# import googletrans
# print(googletrans.LANGUAGES)

# txt = "તમે કેમ છો"
# result3 = translator.translate(txt)
# print(result3.src)

from googletrans import Translator
translator = Translator()
result = translator.translate("cómo estás")
print(result.dest)
print(result.text)

print("")

sentences = ['Bienvenu', 'Comment allez-vous', 'je vais bien']
result2 = translator.translate(sentences )
for trans in result2:
    print(f'{trans.origin} -> {trans.text}')

print("")

mylist = ["Comment allez-vous" , "tu vas bien","nous allons bien","au revoir"]
result4 = translator.translate(mylist, dest="gu")
for trans  in result4:
    print(f'{trans.origin}  ---> {trans.text}')
from rake_nltk import Rake

r = Rake()

text = """ I am a programmer from India India India , and I am here to guide you 
with Data Science, Machine Learning, Python, and C++ for free. 
I hope you will learn a lot in your journey towards Coding, 
Machine Learning and Artificial Intelligence Intelligence Intelligence with me."""

r.extract_keywords_from_text(text)

keyword = r.get_ranked_phrases()
print("All keyword...")
print("\U0001f600")
print(keyword)
print("Repeated words : ")
keyword = r.frequency_dist
print(keyword)


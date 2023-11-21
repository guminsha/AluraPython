from collections import defaultdict, Counter
from account import Account

text_sample = "Bem vindo meu nome eh Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
text_sample = text_sample.lower()
set_text_sample = set(text_sample.split())

# appers = {}
appers = Counter(text_sample.split())

# for word in text_sample.split():
# 	until_now = appers[word]
# 	appers[word] += 1

print(appers)

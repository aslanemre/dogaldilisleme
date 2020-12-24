import nltk
import spacy
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.stem.porter import * 
from nltk.stem.snowball import SnowballStemmer
from snowballstemmer import TurkishStemmer
from nltk import ne_chunk

# CUMLE TOKENİZE ETME İŞLEMİ (SENTENCE TOKENIZATION)

metin = """
Korkma, sönmez bu şafaklarda yüzen al sancak. Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak. O benimdir, o benim milletimindir ancak.
Çatma, kurban olayım çehreni ey nazlı hilâl! Kahraman ırkıma bir gül… ne bu şiddet bu celâl?
Sana olmaz dökülen kanlarımız sonra helâl. Hakkıdır, Hakk’a tapan, milletimin istiklâl."""
       
cumleler = sent_tokenize(metin)

for cumle in cumleler:
    print(cumle)

print()

# KELIME TOKENİZE ETME İŞLEMİ (WORD TOKENIZATION)

cumlelerim = [
    "Korkma, sönmez bu şafaklarda yüzen al sancak.",
    "Sönmeden yurdumun üstünde tüten en son ocak."
    ]

for tokenler in cumlelerim:
    print(word_tokenize(tokenler))

print()

# GÖVDELEME İŞLEMİ (STEMMING) {PORT STEMMER}

kelime = "tokenization"

porter_stemmer = PorterStemmer()

print(porter_stemmer.stem(kelime))

print()

# GÖVDELEME İŞLEMİ (STEMMING) {SNOWBALL STEMMER}

stemmer = SnowballStemmer(language='english')

print(stemmer.stem(kelime))

print()

# TÜRKÇE GÖVDELEME İŞLEMİ (STEMMING) {SNOWBALL STEMMER}

tr_stemmer = TurkishStemmer()


print(tr_stemmer.stemWord('kahkahalar'))

print()

# BAŞ SÖZCÜK ÇIKARMA İŞLEMİ (STEMMING) {LEMMAZATION}

bassozcuk_cikarma = spacy.load('en_core_web_sm')

kelime2 = bassozcuk_cikarma('tokenization')

for token in kelime2:
    print(token.lemma_)

print()

# SÖZCÜK TÜRLERİ {POSTTAGS}

cumle = "Korkma, sönmez bu şafaklarda yüzen al sancak."

tokenss = nltk.word_tokenize(cumle)

print(nltk.pos_tag(tokenss))

print()

# VARLIK İSMİ TANIMA {NER}

tokensss = nltk.word_tokenize(cumle)

isaretlenmis_tokenler = ntlk.pos_tag(tokensss)

girdiler = ntlk.chunk.ne_chunk(isaretlenmis_tokenler)

print(girdiler)


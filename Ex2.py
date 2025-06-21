# A. Import
import pandas as p, matplotlib.pyplot as plt, seaborn as s, string, nltk
from wordcloud import WordCloud as w
from nltk.corpus import stopwords as sw
nltk.download('stopwords', quiet=True)

# B. Load
d = p.read_csv('ex 2/spam.csv', encoding='latin-1')[['v1', 'v2']]
d.columns = ['l', 'm']

# C. Head
print(d.head(), "\n")

# D. Info
print(d.info(), "\n")

# E. Null
print(d.isnull().sum(), "\n")

# F. Count
print(d['l'].value_counts(), "\n")
plt.figure(); s.countplot(x='l', hue='l', data=d, legend=False, palette='pastel')
plt.title('Spam vs Ham'); plt.show()

# G. Length
d['ml'] = d['m'].apply(len)
plt.figure(); d[d['l']=='ham']['ml'].plot.hist(alpha=0.5, label='Ham')
d[d['l']=='spam']['ml'].plot.hist(alpha=0.5, label='Spam')
plt.legend(); plt.title('Length'); plt.show()

# H. Wordcloud Spam
sws = set(sw.words('english'))
d['c'] = d['m'].apply(lambda x: ' '.join([w for w in ''.join(c for c in x if c not in string.punctuation).lower().split() if w not in sws]))
plt.imshow(w(width=600, height=400).generate(' '.join(d[d['l']=='spam']['c'])), interpolation='bilinear')
plt.axis('off'); plt.title('Spam'); plt.show()

# I. Wordcloud Ham
plt.imshow(w(width=600, height=400).generate(' '.join(d[d['l']=='ham']['c'])), interpolation='bilinear')
plt.axis('off'); plt.title('Ham'); plt.show()

# J. Stats
print(d.groupby('l')['ml'].mean(), "\n")
print(d.loc[d[d['l']=='ham']['ml'].idxmax(), 'm'], "\n")
print(d.loc[d[d['l']=='spam']['ml'].idxmax(), 'm'], "\n")

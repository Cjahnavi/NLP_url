# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:22:21 2019

@author: janvi
"""


# Import RegexpTokenizer from nltk.tokenize
from nltk.tokenize import RegexpTokenizer

# Create tokenizer
tokenizer = RegexpTokenizer('\w+')

# Create tokens
tokens = tokenizer.tokenize(text)
tokens
tokens[:8]


# In[26]:


# Initialize new list
words = []


# Loop through list tokens and make lower case
for word in tokens:
    words.append(word.lower())


# Print several items from list as sanity check
words[:8]


# In[30]:


# Import nltk
import nltk
nltk.download('stopwords')

# Get English stopwords and print some of them
sw = nltk.corpus.stopwords.words('english')
sw[:5]


# In[31]:


words_ns = []

# Add to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)

# Print several list items as sanity check
words_ns[:5]


# In[32]:


#Import datavis libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Figures inline and set visualization style
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()

# Create freq dist and plot
freqdist1 = nltk.FreqDist(words_ns)
freqdist1.plot(25)


# In[33]:


##############################


# In[35]:


def plot_word_freq(url):
    #"""Takes a url (from Project Gutenberg) and plots a word frequency
    #distribution"""
    # Make the request and check object type
    r = requests.get(url)
    # Extract HTML from Response object and print
    html = r.text
    # Create a BeautifulSoup object from the HTML
    soup = BeautifulSoup(html, "html5lib")
    # Get the text out of the soup and print it
    text = soup.get_text()
    # Create tokenizer
    tokenizer = RegexpTokenizer('\w+')
    # Create tokens
    tokens = tokenizer.tokenize(text)
    # Initialize new list
    words = []
    # Loop through list tokens and make lower case
    for word in tokens:
        words.append(word.lower())
    # Get English stopwords and print some of them
    sw = nltk.corpus.stopwords.words('english')
    # Initialize new list
    words_ns = []
    # Add to words_ns all words that are in words but not in sw
    for word in words:
        if word not in sw:
            words_ns.append(word)
    # Create freq dist and plot
    freqdist1 = nltk.FreqDist(words_ns)
    freqdist1.plot(25)


# In[36]:


#plot_word_freq('https://www.gutenberg.org/files/42671/42671-h/42671-h.htm')


# In[37]:


#plot_word_freq('https://www.gutenberg.org/files/521/521-h/521-h.htm')


# In[38]:


#plot_word_freq('https://www.google.com')


# In[40]:


#plot_word_freq('https://www.javatpoint.com')


# In[ ]:

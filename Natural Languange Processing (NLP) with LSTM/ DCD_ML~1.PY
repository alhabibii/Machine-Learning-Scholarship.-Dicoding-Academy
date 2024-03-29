# -*- coding: utf-8 -*-
"""Dcd.MLInter.Submission NLP with LSTM.Adil Latif Habibi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dtw3evfTDLuPi-3o21wKKnreXaXRmuPm

##1. *Import semua library yang dibutuhkan diawal aagar terlihat rapi*
"""

import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from scipy.special import softmax
import matplotlib.pyplot as plt

"""## *2. Ubah dataset menjadi dataframe menggunakan pandas, lalu lakukan pengecekan data meliputi pengecekan jumlah kolom, Dtype (apakah ada yang harus dibuang)*"""

df = pd.read_csv('bbc-text.csv')
df.info()

"""## *3.Pengecekan jumlah elemen*"""

df['category'].value_counts()

df['text'].value_counts(2)

"""## *4. Dataframe sebelum dilakukan proses one hot encoding*"""

df

"""## *5. Hasil dari proses one hot encoding dan sample 5 dataframe terakhir*"""

kategori = pd.get_dummies(df.category)
df = pd.concat([df, kategori], axis=1)
df.tail(5)

"""## *6. Buang kolom kategori karena sudah diganti melalui one hot encoding dan tidak diperlukan lagi*"""

ndf = df.drop(columns='category')
ndf.head(2)

"""## *7. Cek jika ada nilai yang kosong, dan hitung banyak kata yang ada dalam kolom teks untuk membantu nanti dalam melakukan modelling*"""

ndf.isna().sum()

Counter(ndf['text'])
print('banyak kata = ', len(ndf['text']))

"""## *8. Gunakan Library NLTK untuk memproses data teks. Hilangkan stopwords dan tanda baca agar data lebih siap untuk dilatih*"""

example_sent = """ A stop word is a commonly used word 
    (such as “the”, “a”, “an”, “in”) that a search engine 
    has been programmed to ignore, both when indexing entries 
    for searching and when retrieving them as the result of a 
    search query. """
  
stop_words = set(stopwords.words('english'))
  
word_tokens = word_tokenize(example_sent)
  
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  
filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
  
print(word_tokens)
print(filtered_sentence)

sentence = "Think and wonder, wonder and think."
 
token = nltk.RegexpTokenizer(r"\w+")
new_words = token.tokenize(sentence)

"""## *9. Ubah nilai-nilai dari dataframe ke dalam tipe data numpy array*"""

text = ndf['text'].values
label = ndf[['business', 'entertainment', 'politics', 'sport', 'tech']].values

"""## *10. Bagi data untuk training dan data untuk testing*"""

text_train, text_test, label_train, label_test = train_test_split(text, label, test_size=0.2, random_state=0)

"""## *11. Lakukan Proses Tokenisasi*"""

tokenizer = Tokenizer(num_words=2225, oov_token='<oov>')

tokenizer.fit_on_texts(text_train)

sekuens_train = tokenizer.texts_to_sequences(text_train)
sekuens_test = tokenizer.texts_to_sequences(text_test)

pad_train = pad_sequences(sekuens_train,
                          maxlen=100,
                          padding='post',
                          truncating='post')
pad_test = pad_sequences(sekuens_test,
                         maxlen=100,
                         padding='post',
                         truncating='post')

"""## *12. Buat arsitektur model menggunakan Sequential, layer Embedding, LSTM, Dense, dan Dropout. Kemudian panggil fungsi compile*"""

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=2225, output_dim=32, input_length=100),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(5, activation='softmax')
])
model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

"""## *13. Gunakan fungsi callback untuk memberi tahu model agar berhenti melakukan pelatihan ketika sudah mencapai target tertentu. Dalam Model ini 92%*"""

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>=0.92 and logs.get('val_accuracy')>=0.92):
      print("\nAkurasi training dan validasi telah mencapai nilai >92%!")
      self.model.stop_training = True
callbacks = myCallback()

"""## *14.Latih model dengan menggunakan fungsi .fit()*"""

history = model.fit(pad_train, label_train, epochs=100,
                    validation_data=(pad_test, label_test), 
                    verbose=2, callbacks=[callbacks])

"""## *15. Plot loss dan akurasi pada saat training dan validation.*"""

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('AKURASI MODEL')
plt.ylabel('AKURASI')
plt.xlabel('JUMLAH EPOCH')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('LOSS MODEL')
plt.ylabel('LOSS')
plt.xlabel('JUMLAH EPOCH')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

#      					**Image Classification**



| Student Name    | [ADIL LATIF HABIBI (alhabibi)](https://www.dicoding.com/users/alhabibi) |
| --------------- | ------------------------------------------------------------ |
| Course          | [Belajar Machine Learning untuk Pemula](https://www.dicoding.com/academies/184) |
| Submission      | [Proyek Akhir : Klasifikasi Gambar](https://www.dicoding.com/academies/184/tutorials/8547) |
| Submission ID   | 118****                                                      |
| Dikirim pada    | 14-Jun-2022 09:46:18                                         |
| Tipe Enrollment | Token: IDCamp 2022: Machine Learning Developer               |
| Rating Nilai    | ★★★★★                                                        |



* Sumber Dataset : **https://github.com/dicodingacademy/assets/releases/download/release/rockpaperscissors.zip***.

* Dataset memiliki **2188** gambar.

* Dataset memiliki **3** kelas, **( Rock, Paper, Scissors )**

* Menggunakan model **Sequential**.

* Ukuran validation set **40%** dari total dataset

* Menggunakan **Conv2D Maxpooling Layer, Flatten, dan Dense**.

* Pembagian train dan validasi menggunakan **splitfolders** 

* Train data menggunakan **ImageDataGenerator**.

* Optimizer menggunakan **Adam**

* Menggunakan **Drop Out Layer**.

* Train accuracy  dan validation accuracy > **95%.** 

* ```
  Epoch 75/75
  25/25 - 9s - loss: 0.0336 - accuracy: 0.9892 - val_loss: 0.0080 - val_accuracy: 0.9933 - 9s/epoch - 363ms/step
  ```

* Prediksi : 

  ```
  uploaded = files.upload()
  
  for fn in uploaded.keys():
  
    path = fn
    img = image.load_img(path, target_size=(200,200))
  
    imgplot = plt.imshow(img)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    print(fn)
    if classes[0,0]!=0:
      print('rock')
    elif classes[0,1]!=0:
      print('paper')
    else:
      print('scissors')
  ```

  

* Dibuat menggunakan **Google Colab**

Project ini adalah Image Classification sederhana menggunakan data latihan yang sudah sangat dikenal dan sering digunakan dalam latihan machine learning, yaitu *rockpaperscissors* dataset. Dataset berisi 2118 gambar yang terdiri dari tiga jenis gambar yang berbeda.  Akurasi training mencapai lebih dari 97%. Hasil prediksi menunjukkan bahwa model dapat memprediksi dengan akurat gambar tangan yang menyimbolkan batu, gunting, dan kertas dengan latar gambar polos dan tidak ada noise.








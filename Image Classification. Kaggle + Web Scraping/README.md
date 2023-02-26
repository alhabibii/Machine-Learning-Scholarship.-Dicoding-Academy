#      		**Image Classification Model Deployment**                                                                							                                                       
#                  **Web Scrapping + Kaggle**



| Student Name    | [ADIL LATIF HABIBI (alhabibi)](https://www.dicoding.com/users/alhabibi) |
| --------------- | ------------------------------------------------------------ |
| Course          | [Belajar Pengembangan Machine Learning](https://www.dicoding.com/academies/185) |
| Submission      | [Proyek Akhir : Image Classification Model Deployment](https://www.dicoding.com/academies/185/tutorials/10629) |
| Submission ID   | 149****                                                      |
| Dikirim pada    | 12-Oct-2022 06:16:38                                         |
| Tipe Enrollment | Token: IDCamp 2022 - Kelas Menengah : Machine Learning Developer |
| Rating Nilai    | ★★★★★                                                        |



* Sumber Dataset : **dataset_binatang.zip***.
* Dataset memiliki **10400 ** gambar.
* Dataset memiliki **4** kelas, **( Cat, Cheetah, Orang Utan, Panda )**.
* Menggunakan **LSTM** dalam arsitektur model.
* Menggunakan model **Sequential**.
* Dataset dibagi menjadi **80% train set** dan **20% test set**.
* Menggunakan **Conv2D Maxpooling Layer, Flatten, dan Dense**.
* Pembagian train dan validasi menggunakan **splitfolders** 
* Train data menggunakan **ImageDataGenerator**.
* Optimizer menggunakan **Adam**
* Menggunakan **Callback**.
* Menggunakan **Drop Out Layer**.
* Train accuracy sebesar **>92%** dan validation accuracy **>92%.** Hal ini menunjukkan model yang dibuat **good fit**.
* "520/520 - 55s - loss: 0.1028 - **accuracy: 0.9605** - val_loss: 0.2448 - **val_accuracy: 0.9312** - 55s/epoch - 106ms/step\n"
* Menulis kode untuk menyimpan model ke dalam format **TF-Lite**.
* Dibuat menggunakan **Google Colab**

Awalnya saya menyiapkan 52000 gambar yang akan saya jadikan dataset gambar. Gambar ini saya *download* dari berbagai macam *resources* termasuk melakukan *Scrapping* pada *search engine bing* menggunakan *bing downloader*. Ini saya lakukan agar saya memiliki resolusi gambar yang tidak seragam. Lalu saya filter lagi gambar - gambar tersebut. 

Pada intinya saya membuat dataset saya sendiri yang awalnya berisi sekitar 50000 buah gambar dengan 6 kelas di dalamnya, dengan ukuran mendekati 1 GB. Ketika saya jalankan di colab, prosesnya sangat lambat walaupun saya sudah menggunakan bantuan GPU atau TPU. Oleh sebab itu saya kemudian mengurangi jumlah gambar dan kelas menjadi sekitar 10400 gambar dengan 4 kelas supaya prosesnya menjadi lebih cepat.

Proses training saja membutuhkan waktu cukup lama, yaitu sekitar hampir 2 jam karena rata-rata 1 epoch memakan waktu sekitar 55 detik dan saya menggunakan 150 epoch. Model saya mencapai akurasi 96% dan val akurasi 93% pada epoch ke 124. Modelnya berkali - kali saya rubah, awalnya saya menambahkan juga transfer layer RestNet tapi itu tidak membantu karena model saya tidak bisa dijalankan. Saya menggunakan RestNet karena saya menyimpulkan bahwa RestNet lebih baik dibandingkan dengan MobileVNet untuk *Image Classification*. Jadi saya tidak jadi menambahkan transfer layer RestNet. 




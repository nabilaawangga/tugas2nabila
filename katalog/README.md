Tugas 2 PBP
Nama: Nabila Zahra Putri Awangga
NPM: 2106703840

link aplikasi heroku: https://katalognabila.herokuapp.com/katalog/

## Bagan

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

Client memberikan request berupa link url di browser dengan mengakses Internet yang mana browser ini akan menyampaikan request client kepada web server. Jika menggunakan django, maka browser akan mengirim request client tersebut ke server django. Manage.py yang menjalankan server django. Server django akan mengextract argumen dari user lalu urls.py akan melakukan routing sesuai sama request yg dikasi dengan liat host, port, dan path yang ada pada url yg ada di request client. Url routing ini akan mem-forward sesuai request ke code yang sesuai. Routing ini menuju ke views.py yang sesuai. Views.py akan berhubungan dengan models.py untuk meminta/menyimpan data yang direquest oleh client. Namun, models.py tidak langsug menyimpan data. models.py bertugas untuk menangani segala hal tentang data yang data tersebut sebenarnya disimpan dalam sebuah database. Ibaratnya, models.py adalah manager dari data yang disimpan. Ketika data yang diminta oleh views.py telah diberikan oleh models.py, maka views.py memerlukan template yang akan digunakan untuk menaruh data pada template tersebut. Lalu, data yang telah diambl di views.py akan dimasukkan ke template html sehingga nantinya akan di-render menjadi sebuah halaman yang utuh sebagai respon untuk request client.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment adalah tool yang dibuat untuk menjaga dependensi yang diperlukan oleh proyek-proyek terpisah agar proyek tersebut terisolasi. Virtual environment digunakan ketika sedang membuat Python based project contohnya seperti Django. Ketika membuat proyek dengan menggunakan Django, kita menggunakan virtual environment untuk menghindari terjadinya error yang diabatkan oleh adanya 2 atau lebih proyek Django dengan versi berbeda yang berada pada directory yang sama. Virtual environment sangat penting untu digunakan ketika membuat proyek menggunakan Django. Misalnya kita membuat 2 proyek Django di mana proyek pertama menggunakan Django 2.2 lalu kita menginstall Django 3.2 untuk proyek kedua. Maka mereka akan akan terakumulasi dalam direktori yang sama dan dengan nama yang sama, memungkinkan terjadinya error akibat adanya 2 versi Django yang berbeda. Oleh karena itu, virtual environment yang berbeda pada dua proyek tersebut akan sangat berguna untuk menjaga dependensi dari environment keduanya.Jika proyek yang sedang dikerjakan bukan package-dependent, masih bisa memungkinkan untuk tidak menggunaka virtual environment dan tidak perlu mengisolasi versi dan package dari proyek tersebut. Tetapi akan lebih baik jika tetap menggunakan virtual enviornment untuk menjaga environment dari proyek tersebut tetap bersih dan aman saat mengembangkan proyek.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
a. Poin 1 - Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.

Pada views.py terdapat fungsi show_katalog yang dibuat untuk mengambil data katalog pada file models.py yang telah tersedia. Data-data yang dibutuhkan pada views.py diambil dari database melalui file models.py. Pada views.py juga ditambahkan variabel-variabel yang dibutuhkan untuk nantinya ditampilkan di halaman web. Lalu data-data yang telah diambil oleh views.py akan dimasukkan ke dalam file HTML dengan mengakses variabel-variabelnya. File html tersebut akan di-render yang nantinya akan menampilkan hasil berupa tampilan halaman web.

b. Poin 2 - Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.

Untuk melakukan routing terhadap fungsi show_katalog yang telah dibuat di views.py, maka pada folder aplikasi katalog, saya menambahkan file bernama urls.py yang berisi:

from django.urls import path
from katalog.views import show_katalog
 
app_name = 'katalog'
 
urlpatterns = [
   path('', show_katalog, name='show_katalog'),
]

dan juga menambahkan aplikasi katalog ke dalam urls.py pada folder project_django dengan menambahkan potongan kode path('wishlist/', include('wishlist.urls')),

c. Poin 3 - Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.

Untuk memetakan data yang telah diambil oleh views.py dari models.py ke dalam HTML, pada file katalog.html diambil data variabel yang ada pada views.py dengan menggunakkan curly brackets {{}} lalu juga menggunakan for loop untuk mengambil data untuk isi dari tabel katalog barang. Selain itu, saya juga menambahkan beberapa potongan kode untuk memperbagus tampilan hasil render html seperti menambah border line untuk tabel katalog barang.

d. Poin 4 - Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Untuk melakuka deployment ke Heroku, saya menghubungkan (connect) aplikasi Heroku yang baru saya buat dengan repositori github yang saya gunakan untuk tugas ini. Lalu saya menyalin API KEY Heroku milik saya dan memasukkan HEROKU_APP_NAME dan HEROKU_API_KEY di github secrets untuk menghubungkan data-data di repositori github tersebut ke Heroku app yang akan saya pakai.
Nama: Nabila Zahra Putri Awangga
NPM: 2106703840
Kelas: PBP F

link heroku:
https://katalognabila.herokuapp.com/todolist/login/?next=/todolist/

https://katalognabila.herokuapp.com/todolist/login/

https://katalognabila.herokuapp.com/todolist/register/

https://katalognabila.herokuapp.com/todolist/create-task/

https://katalognabila.herokuapp.com/todolist/logout/

## TUGAS 4
## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF adalah serangan yang mengirimkan permintaan palsu kepada suatu web padahal permintaan tersebut tidak dikirim oleh si pengguna. csrf_ token digunakan untuk mencegah penyerangan csrf tersebut dengan melakukan validasi dari token yang dimasukkan pengguna dengan yang di simpan di dalam user session. Form akan menolak permintaan jika token yang dimasukkan tidak valid. Website tetap bisa digunakan dan berjalan dengan baik jika tidak ada csrf_token pada form, tetapi akan ada resiko penyerangan CSRF dengan contoh kasus yaitu orang lain selain pengguna akun tersebut dapat menghapus akun dengan mengakses route link yang sesuai tanpa diketahui oleh si pengguna akun tersebut.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Kita masih bisa membuatnya secara manual. Untuk membuat elemen form secara manual, dapat  membuat html form secara manual dengan memasukkan elemen form ke tempat yang sesuai pada file html. 

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Setelah user memencet tombol submit, data yang dimasukkan user akan diambil dan diakses dengan method request.POST.get(nama jenis input). Data-data tersebut akan diproses dan masuk ke dalam database milik models.py. Setelah itu, untuk memunculkan data pada template html, data-data yang ada pada database diakses pada models.py dengan method (nama model).objects.filter(user=request.user) lalu dimasukkan data hasil pengambilan method tersebut ke dalam file html bisa dengan melakukan loop for each. Data akan ditampilkan pada HTML setelah dirender.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1.  Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
Saya menjalankan perintah python manage.py startapp todolist pada direktori yang sesuai

2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
Untuk dapat mengakses path tersebut, saya menambahkan path('todolist/', include('todolist.urls')) di file urls.py pada project django

3.  Membuat sebuah model Task 
Saya membuat class Task pada models.py dan menambahkan field yang diminta pada soal

4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.

Pertama-tama, saya membuat fungsi login, register, logout pada views.py. Lalu saya menambahkan url ketiga fungsi tersebut di urls.py dan membuat file html masing-masing sesuai kebutuhan. Lalu saya menambahkan @login_required(login_url='/todolist/login/') di awal sebelum penulisan fungsi pada views.py

5.  Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.

Saya membuat fungsi show_todolist pada views.py yang akan ditampilkan pada file todolist.html berisi data-data to do list yang dimasukkan user. Lalu saya menambahkan {{username}} pada file html untuk menampilkan username pengguna. Untuk membuat tombol logout dan tambah taskbaru, saya menambahkan 2 kode untuk membuat button pada file todolist.html. Lalu saya juga mengakses isi tabel dengan melakukan loop for each di file todolist.html

6.  Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

Untuk membuat halaman form, saya membuat fungsi membuat_task di views.py terlebih dahulu dan memasukkan url /create-task pada urls.py. Lalu saya membuat HTML bernama task.py untuk membuat halaman web untuk pembuatan task.

7.  Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:

Untuk membuat routing, saya memasukkan kode:

path('', show_todolist, name='show_todolist'),
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
path('create-task/', membuat_task, name='membuat_task'),

Pada file urls.py

8.  Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Melakukan git add, commit serta push ke repositori sehingga akan melakukan update pada aplikasi heroku yang telah terhubung
 
## TUGAS 5
# Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Inline CSS: kode CSS yang ditulis langsung pada atribut elemen HTML.
Contoh: "<div class="card-header text-gray-300" style="background-color: rgb(250, 227, 17);">"
  
Inline CSS ini tidak efisien karena hanya berlaku untuk tiap 1 elemen html yang diberi inline css tersebut. Tetapi cukup membantu ketika hanya ingin menguji dan melihat perubahan pada satu elemen.

2. Internal CSS: kode CSS yang ditulis dalam tag<style> dan kode HTML yang ditulis di bagian header file HTML. 
Internal CSS hanya berlaku di satu halaman saja. Lalu file yang akan diupload lebih sedikit karena file html dan css telah berada di 1 file yang sama karena CSS yang digunakan secara internal pada file HTML

3. External CSS: kode CSS ditulis secara terpisah dari kode HTML yang nantinya diakses pada bagian awal kode HTML.
External CSS lebih efisien karena 1 file external css dapat digunakan oleh banyak halaman web sekaligus. Namun, ketika external css gagal dipanggil oleh file html, tampilan CSS akan berantakan

## Jelaskan tag HTML5 yang kamu ketahui.
<button> untuk membuat button yang clickable
<form> untuk data user input
<div> tempat bagi elemen elemen lain untuk diletakkan, seperti dasarnya
<ul> dan <li> untuk membuat list
<style> untuk menamppung informasi dan perintah untuk mengubah design tampilan halaman web
<p> untuk membuat text paragraf
dan masih banyak lagi :)
  
##  Jelaskan tipe-tipe CSS selector yang kamu ketahui.
'*' -> untuk memilih semua elemen
'#' -> untuk select id
'.' -> untuk memilih kelas pada komponen
dan yang lainnya

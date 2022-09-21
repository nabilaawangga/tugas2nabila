Nama: Nabila Zahra Putri Awangga
NPM: 2106703840
Kelas: PBP F

## Tugas 3
## 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
a. JSON
JSON formatnya ditulis dalam bentuk Javascript. JSON digunakan untuk menyimpan dan mengirimkan data. Kumpulan data dan informasi yang disimpan pada JSON dapat dengan mudah untuk diakses, dibaca, dan dipahami oleh manusia karena menggunakan format map (key/value) untuk menyimpan datanya sehingga data disimpan lebih rapih dan terorganisir. Selain mudah dibaca oleh manusia, data yang disimpan pada JSON juga lebih mudah untuk diakses dan dibaca oleh mesin.

b. XML
XML menggunakan markup language untuk menyimpan dan mengirimkan data. XML bukanlah programming language karena markup language tidak memiliki logic di dalamnya. XML membungkus informasi dan datanya di dalam tag. Walaupun XML tingkat kemudahan untuk dibacanya di bawah JSON, tetapi XML tetap lebih baik untuk digunakan jika mengerjakan proyek yang memerlukan markup dokumen dan informasi metadata.

c. HTML
HTML adalah markup language untuk men-design we browser. HTML bukanlah programming language karena markup language tidak memiliki logic di dalamnya. tree of objects. HTML digunakan untuk menampilkan data dengan tampilan rapih dan menarik pada web page, berbeda dengan JSON dan XML yang hanya menampilkan data tanpa memperhatikan tampilan.

## 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Pada sebuah platform, ada data user yaitu request yang diberikan oleh user dan data server yaitu respons dari request yang diminta oleh user. Data yang direquest dan data untuk respons tersebut pasti akan mengalami pertukaran. Sehingga diperlukan data delivery untuk mempermudah perpindahan data dari user ke server atau dari server ke user. Karena data request user pasti dibutuhkan oleh server untuk dikerjakan dan data respons dari server juga dibutuhkan oleh user sehingga data-data tersebut perlu untuk di-deliver. Data tersebut dikirim dari suatu stack ke stack lainnya dengan bentuk data yang beragam bentuknya.

## 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 3 di atas.

# a. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
Saya membuat aplikasi baru bernama mywatchlist dengan menjalankan perintah "python manage.py startapp mywatchlist" pada direktori yang sama dengan tugas 1. Lalu menambahkan mywatchlist pada variabel installed app pada file settings.py di folder project_django.
b. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
agar dapat mengakses link tersebut, saya menambahkan kode path('mywatchlist/', include('mywatchlist.urls'), pada file urls.py yang ada di dalam folder project_django.

# c. Membuat sebuah model MyWatchList yang memiliki atribut watched, title, rating, release_date, dan review
Saya membuat variabel watched, title, rating, release_date, dan review pada models.py.

# d. Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
membuat berkas bernama initial_mywatchlist_data.json di dalam folder fixtures yang berisikan detail data yang akan ditampilkan pada web page. Data-data tersebut memakai variabel yang telah dibuat pada models.py

# e. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam format json, html, dan xml
Untuk menyajikan data dengan format json, html, dan xml, saya menambahkan import from django.http import HttpResponse dan from django.core import serializers pada file views.py. Lalu membuat 3 function pada views.py yang memberikan return sesuai dengan format json, html, dan xml.

# f. Membuat routing sehingga data di atas dapat diakses melalui URL http://localhost:8000/mywatchlist/html, http://localhost:8000/mywatchlist/json, http://localhost:8000/mywatchlist/xml
Pada views.py, 3 fungsi yang telah dibuat, diimport pada file ini. Lalu menambahkan urlpatterns untuk mengakses fungsi yang tadi telah diimport dengan menuliskan
    
- path('json', show_json, name=’show_json’),
- path('html', show_mywatchlist, name='show_mywatchlist'),
- path('xml', show_xml, name='show_xml'),

di mana name-nya disesuaikan dengan nama fungsi yang dibuat

# g. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Karena pada tugas sebelumnya, saya telah menghubungkan repositori git ini dengan aplikasi heroku yang telah saya buat, yang saya lakukan pada tugas ini agar linknya dapat diakses oleh teman-teman melalui Internet adalah dengan melakukan, add, commit, serta push perubahan file yang saya lakukan ke repositori tersebut.

## POSTMAN
# XML

# JSON

# HTML

## ASSIGNMENT 6
##  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
asynchronous programming adalah programming yang pendekatannya tidak terikat output dan input. Asynchronous programming tidak menjalankan programnya satu per satu, tidak baris per baris sehingga program yang dijalankan lebih cepat dan efisien. Pada AJAX, adynchronous programming ini berpengaruh pada penggunaan refresh yaitu di tugas 6 ini, kita tidak perlu refresh halaman web karena sudah memakai asynchronous programming. Sedangkan synchronous programming berpacu pada input, ouput, dan proses berjalannya fungsi tiap baris kode. Setiap  kode dieksekusi satu per satu. Jadi, pada dasarnya sebuah kode harus menunggu kode sebelumnya untuk dieksekusi.
##  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven programming adalah suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan dari user-client. Tindakan user-client tersebut dapat berupa mengklik tombol atau menggerakkan mouse. Pada tugas ini, penerapan event-driven programming digunakan pada tugas 6 ini adalah pembuatan modal untuk menambahkan task di mana modal ini bersifat pop up dan tidak perlu berpindah ke web page yang lain saat hendak menambahkan task. Event-Driven programming pada AJAX di tugas 6 ini membuat modal dapat hilang dan muncul layaknya pop up. 
##  Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX dan contohnya pada tugas 6 ini adalah kita tidak perlu merefresh/reload web page yang dibuat untuk mendapatkan perubahan yang baru. Karena dengan adanya asynchronous programming dan penerapan event-driven programming, perintah yang dibuat oleh user-client akan dieksekusi secara asynchronous dan tanpa harus menunggu satu persatu kode untuk dieksekusi. AJAX Post dan AJAX get juga membantu memproses dan menampilkan data pada web tanpa perlu reload web page.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat fungsi untuk memberikan response berbentuk json pada views.py dan menambahkan routingnya ke urls.py
2. Membuat modal untuk form add task menggunakan bootstrap
3. Input modal diarahkan ke routing /todolist/add
4. Membuat fungsi buat_todolist untuk menghubungkannya dengan POST GET AJAX
5. Pada todolist.html, membuat fungsi GET dan POST untuk mengambil data dan menampilkannya menggunakan AJAX

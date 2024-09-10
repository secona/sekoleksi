# sekoleksi

E-Commerce Application made with Django

#### 🚀 Deployment

http://muhammad-vito31-sekoleksi.pbp.cs.ui.ac.id/

## ➡️ Langkah Implementasi

#### :one: Membuat sebuah proyek Django baru
Pembuatan proyek Django baru dilakukan dengan menjalankan perintah `django-admin startproject <nama_proyek> .` dengan `<nama_proyek>` diganti dengan nama proyek yang diinginkan, untuk proyek ini `sekoleksi`. `.` di akhir perintah menandakan bahwa proyek akan dibuat di direktori di mana perintah tersebut dijalankan.

#### :two: Membuat aplikasi dengan nama `main` pada proyek tersebut
Pembuatan aplikasi `main` pada proyek dilakukan dengan menjalankan perintah `python manage.py startapp main`. Perintah ini akan membuat subdirektori baru bernama `main`. Di dalam subdirektori tersebut, terdapat beberapa _file_ Python untuk keperluan aplikasi `main`. Perlu diperhatikan bahwa perintah tersebut hanya dapat dijalankan di dalam proyek Django yang sudah dibut.

#### :three: Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`
TODO

#### :four: Membuat model pada aplikasi `main` dengan nama `Product`
Pembuatan model `Product` dilakukan dengan menambahkan definisi _class_ `Product` dalam file `main/models.py`. Class `Product` akan _inherit_ class `models.Model` dengan atribut `name`, `price`, dan `description`. Nilai dari masing-masing atribut disesuaikan dengan tipe data yang dibutuhkan.

- `name` memiliki nilai `models.CharField()` karena _value_ yang disimpan berupa string.
- `price` memiliki nilai `models.IntegerField()` karena _value_ yang disimpan berupa angka.
- `description` memiliki nilai `models.TextField()` karena _value_ yang disimpan berupa string.

#### :five: Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
TODO

#### :six: Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`
TODO

#### :seven: Melakukan _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
TODO

#### :eight: Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-_deploy_, serta jawaban dari beberapa pertanyaan berikut
TODO

## ➡️ Client Request Diagram
TODO

## ➡️ Git dalam Pengembangan Perangkat Lunak
Pada dasarnya git adalah sistem kontrol versi yang digunakan untuk melacak perubahan file menggunakan _commit_. Setiap kali pengembang melakukan _commit_, Git menyimpan versi dari file saat itu, memungkinkan untuk melacak setiap perubahan yang terjadi selama pengembangan. Jika pengembang melakukan kesalahan atau ingin kembali ke versi sebelumnya, Git dengan menggunakan perintah _revert_ yang akan memulihkan versi file tertentu, seolah-olah perubahan setelahnya tidak pernah terjadi, tanpa menghapus riwayat kerja yang sudah ada.

Git memiliki fitur yang bernama _branching_ yang berfungsi untuk membuat cabang yang terpisah dari cabang utama proyek. Dengan _branching_, pengembangan fitur dapat dilakukan di cabang terpisah yang tidak mempengaruhi cabang utama proyek. Setelah fitur selesai dikembangkan dan layak untuk di-_deploy_, pengembang dapat melakukan _merge_ untuk menggabungkan cabang tersebut kembali ke cabang utama. Jika pengembangan fitur tersebut dibatalkan, cabang yang sudah dibuat dapat dihapus dan ini tidak akan mempengaruhi kode lain yang sudah ada di proyek.

Git juga dapat digunakan dengan platform Git, seperti GitHub, GitLab, atau BitBucket, yang memfasilitasi kolaborasi dalam pengembangan proyek. Platform-platform tersebut memudahkan pengembang untuk bekerja dalam tim pada proyek yang sama. Platform-platform tersebut menyediakan fitur seperti Issues untuk pelacakan _bug_ dan tugas, Pull Request untuk _review_ code dan _merge_ ke cabang utama, dan CI/CD untuk otomatisasi pengujian dan _deployment_.

## ➡️ Mengapa Django?
Pertama, Django menggunakan bahasa pemrograman Python, yang populer karena kesederhanaannya. Dengan menggunakan Python, Django menjadi lebih mudah untuk dipahami sebagai permulaan dari pengembangan perangkat lunak.

Kedua, Django sudah memiliki banyak fitur bawaan, seperti otentikasi, URL _routing_, ORM, admin panel, dan form handling. Hal ini memungkinkan pengembang untuk lebih fokus pada pengembangan aplikasi dibandingkan mengatur dan membangun fitur-fitur tersebut dari nol.

Ketiga, Django memiliki komunitas aktif yang cukup besar. Komunitas tersebut memberikan banyak sumber belajar terkait Django, seperti tutorial, forum, blog, dan lain sebagainya.

## ➡️ Model dalam Django dan ORM
Object-Relational Mapping (ORM) adalah teknik yang memetakan tabel-tabel dalam database ke objek-objek dalam suatu program, di mana objek ini adalah instance dari suatu class dalam bahasa pemrograman. Dalam konteks Django, model adalah class Python yang dipetakan ke tabel dalam database yang digunakan. Melalui model-model ini, pengembang dapat berinteraksi dengan database hanya dengan memanggil method-method yang tersedia pada class model. Django akan secara otomatis mentranslasikan metode-metode tersebut menjadi query SQL yang akan dijalankan di database. Sebagai contoh, ketika pengembang ingin menyimpan sebuah objek, Django akan mengonversi objek Python menjadi kolom dalam database. Sebaliknya, ketika pengembang ingin mendapatkan data, Django akan mengonversi kolom dalam database menjadi objek Python. Pendekatan ini menyederhanakan pengelolaan data, mengabstraksikan kompleksitas query SQL, dan mempercepat pengembangan aplikasi.

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
TODO

## ➡️ Mengapa Django?
TODO

## ➡️ Model dalam Django dan ORM
Object-Relational Mapping (ORM) adalah teknik yang memetakan tabel-tabel dalam database ke objek-objek dalam suatu program, di mana objek ini adalah _instance_ dari suatu _class_ dalam bahasa pemrograman. ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan konsep-konsep OOP, tanpa harus menulis query SQL secara manual. Proses ini mengabstraksikan berbagai operasi _database_, seperti _create_, _read_, _update_, dan _delete_.

Dalam Django, model-model yang didefinisikan sebagai _class_ berfungsi sebagai ORM, di mana setiap _class_ merepresentasikan tabel dalam _database_. Melalui model-model ini, pengembang dapat berinteraksi dengan database hanya dengan memanggil method-method yang tersedia pada _class_ model. Django akan secara otomatis mentranslasikan metode-metode tersebut menjadi query SQL yang akan dijalankan di database. Hasil query tersebut kemudian dipetakan ke atribut-atribut dalam class, sehingga mengakses data dari tabel semudah mengakses atribut pada class Python biasa.

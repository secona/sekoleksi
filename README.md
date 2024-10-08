# sekoleksi

E-Commerce Application made with Django.

:rocket: [Deployment](http://muhammad-vito31-sekoleksi.pbp.cs.ui.ac.id)

<details>
<summary>:blue_book: Tugas 2</summary>

## :blue_book: Tugas 2

### ➡️ Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

#### :one: Membuat sebuah proyek Django baru
Pembuatan proyek Django baru dilakukan dengan menjalankan perintah `django-admin startproject <nama_proyek> .` dengan `<nama_proyek>` diganti dengan nama proyek yang diinginkan, untuk proyek ini `sekoleksi`. `.` di akhir perintah menandakan bahwa proyek akan dibuat di direktori di mana perintah tersebut dijalankan.

#### :two: Membuat aplikasi dengan nama `main` pada proyek tersebut
Pembuatan aplikasi `main` pada proyek dilakukan dengan menjalankan perintah `python manage.py startapp main`. Perintah ini akan membuat subdirektori baru bernama `main`. Di dalam subdirektori tersebut, terdapat beberapa _file_ Python untuk keperluan aplikasi `main`. Perlu diperhatikan bahwa perintah tersebut hanya dapat dijalankan di dalam proyek Django yang sudah dibut.

#### :three: Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`
Dalam folder projek, terdapat file `urls.py`. Dalam array `urlpatterns`, tambahkan `path("", include("main.urls"))`, di mana function `include` dan `path` didapatkan dari package `django.urls`. Penambahan ini memuat _urls_ yang didefinisikan di app `main` dan mengonfigurasinya supaya dapat diakses dari proyek.

#### :four: Membuat model pada aplikasi `main` dengan nama `Product`
Pembuatan model `Product` dilakukan dengan menambahkan definisi _class_ `Product` dalam file `main/models.py`. Class `Product` akan _inherit_ class `models.Model` dengan atribut `name`, `price`, dan `description`. Nilai dari masing-masing atribut disesuaikan dengan tipe data yang dibutuhkan.

- `name` memiliki nilai `models.CharField()` karena _value_ yang disimpan berupa string.
- `price` memiliki nilai `models.IntegerField()` karena _value_ yang disimpan berupa angka.
- `description` memiliki nilai `models.TextField()` karena _value_ yang disimpan berupa string.

#### :five: Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
Membuat fungsi bernama `show_main` di file `main/views.py`. Fungsi ini mengembalikan sebuah panggilan ke fungsi `render` dari package `django.shortcuts`. Fungsi tersebut akan me-_render_ template yang berada di `main/templates/main.html` dengan menggunakan nilai-nilai yang didefinisikan di argumen ketiga yang berupa nama, npm, dan kelas.

#### :six: Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`
Dalam folder `main`, terdapat file `urls.py`. Dalam array `urlpatterns`, tambahkan `path("", show_main)` dengan fungsi `show_main` didapatkan dari file `views.py` yang sudah didefinisikan pada step 5. Dengan menambahkan panggilan ke fungsi `path` tersebut, setiap _request_ ke root URL app akan dijalankan fungsi `show_main` yang akan menampilkan nama, npm, serta kelas.

#### :seven: Melakukan _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
Deployment ke PWS dilakukan dengan pertama membuat projek baru di PWS. Lalu, menjalankan perintah yang diberikan, yaitu `git remote add pws <url>` dan `git push main:master`. Dengan ini, PWS akan mendapatkan versi terbaru dari proyek dan dapat di-_run_.

#### :eight: Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-_deploy_, serta jawaban dari beberapa pertanyaan berikut
Membuat file `README.md` dari GitHub web dan menambahkan teks yang dibutuhkan.

### ➡️ Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
![image](https://github.com/user-attachments/assets/c17825ad-e24d-4cf3-a0b4-c34f8df6bdcf)

1. **Request dari Client** &mdash; Client akan melakukan request ke server yang akan di-_handle_ oleh Django, dimulai dari `urls.py` yang berada di proyek atau aplikasi yang sesuai.
2. **URL Routing** &mdash; Jika pola URL yang diminta cocok dengan salah satu pola URL di `urls.py`, Django akan mengarahkan request tersebut ke fungsi view di `views.py` yang sesuai.
3. **Penggunaan Database** &mdash; Dalam fungsi view tersebut, dapat dilakukan beberapa aksi, termasuk penggunaan database melalui `models.py`. Sebagai contoh, jika terdapat request berupa pencarian Item berdasarkan nama, `models.py` akan dipakai untuk mencari Item tersebut di database.
4. **Render Template** &mdash; Setelah data selesai diproses, `views.py` akan menggunakan template dari HTML template yang berada di folder `templates/` untuk menyusun respons. Template ini dapat diisi dengan data yang telah diproses dan variabel-variabel lain yang dibutuhkan.
5. **Response ke Client** &mdash; Setelah template HTML selesai di-_render_, Django akan mengirimkan response akhir kembali ke client berupa halaman HTML yang sudah lengkap dengan data yang diminta.

### ➡️ Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
Pada dasarnya git adalah sistem kontrol versi yang digunakan untuk melacak perubahan file menggunakan _commit_. Setiap kali pengembang melakukan _commit_, Git menyimpan versi dari file saat itu, memungkinkan untuk melacak setiap perubahan yang terjadi selama pengembangan. Jika pengembang melakukan kesalahan atau ingin kembali ke versi sebelumnya, Git dengan menggunakan perintah _revert_ yang akan memulihkan versi file tertentu, seolah-olah perubahan setelahnya tidak pernah terjadi, tanpa menghapus riwayat kerja yang sudah ada.

Git memiliki fitur yang bernama _branching_ yang berfungsi untuk membuat cabang yang terpisah dari cabang utama proyek. Dengan _branching_, pengembangan fitur dapat dilakukan di cabang terpisah yang tidak mempengaruhi cabang utama proyek. Setelah fitur selesai dikembangkan dan layak untuk di-_deploy_, pengembang dapat melakukan _merge_ untuk menggabungkan cabang tersebut kembali ke cabang utama. Jika pengembangan fitur tersebut dibatalkan, cabang yang sudah dibuat dapat dihapus dan ini tidak akan mempengaruhi kode lain yang sudah ada di proyek.

Git juga dapat digunakan dengan platform Git, seperti GitHub, GitLab, atau BitBucket, yang memfasilitasi kolaborasi dalam pengembangan proyek. Platform-platform tersebut memudahkan pengembang untuk bekerja dalam tim pada proyek yang sama. Platform-platform tersebut menyediakan fitur seperti Issues untuk pelacakan _bug_ dan tugas, Pull Request untuk _review_ code dan _merge_ ke cabang utama, dan CI/CD untuk otomatisasi pengujian dan _deployment_.

### ➡️ Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Pertama, Django menggunakan bahasa pemrograman Python, yang populer karena kesederhanaannya. Dengan menggunakan Python, Django menjadi lebih mudah untuk dipahami sebagai permulaan dari pengembangan perangkat lunak.

Kedua, Django sudah memiliki banyak fitur bawaan, seperti otentikasi, URL _routing_, ORM, admin panel, dan form handling. Hal ini memungkinkan pengembang untuk lebih fokus pada pengembangan aplikasi dibandingkan mengatur dan membangun fitur-fitur tersebut dari nol.

Ketiga, Django memiliki komunitas aktif yang cukup besar. Komunitas tersebut memberikan banyak sumber belajar terkait Django, seperti tutorial, forum, blog, dan lain sebagainya.

### ➡️ Mengapa model pada Django disebut sebagai ORM?
Object-Relational Mapping (ORM) adalah teknik yang memetakan tabel-tabel dalam database ke objek-objek dalam suatu program, di mana objek ini adalah instance dari suatu class dalam bahasa pemrograman. Dalam konteks Django, model adalah class Python yang dipetakan ke tabel dalam database yang digunakan. Melalui model-model ini, pengembang dapat berinteraksi dengan database hanya dengan memanggil method-method yang tersedia pada class model. Django akan secara otomatis mentranslasikan metode-metode tersebut menjadi query SQL yang akan dijalankan di database. Sebagai contoh, ketika pengembang ingin menyimpan sebuah objek, Django akan mengonversi objek Python menjadi kolom dalam database. Sebaliknya, ketika pengembang ingin mendapatkan data, Django akan mengonversi kolom dalam database menjadi objek Python. Pendekatan ini menyederhanakan pengelolaan data, mengabstraksikan kompleksitas query SQL, dan mempercepat pengembangan aplikasi.
</details>

<details>
<summary>:blue_book: Tugas 3</summary>
    
## :blue_book: Tugas 3

### :arrow_right: Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?
_Data delivery_ penting untuk diimplementasi pada sebuah platform untuk memungkinkan terjadinya pertukaran informasi antara sistem-sistem yang terlibat. Komunikasi ini terjadi melalui protokol HTTP, di mana data dikirimkan dalam bentuk HTTP _request_ dan diterima sebagai HTTP _response_. Dalam praktiknya, _data delivery_ memungkinkan berbagai macam operasi, seperti pengiriman input dari pengguna ke _server_, pengambilan data, hingga interaksi dengan layanan eksternal.

### :arrow_right: Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
1. **Sintaks yang lebih sederhana** &mdash; Salah satu alasan JSON lebih populer dibandingkan XML adalah sintaksnya. Sintaks dari JSON lebih mudah dibaca dibandingkan XML. JSON menggunakan pasangan _key-value_ dengan petik dua, kurung kurawal, dan kurung siku, sedangkan XML menggunakan tag pembuka dan penutup yang membuat XML lebih sulit untuk di-_manage_.
2. **Integrasi dengan JavaScript** &mdash; JSON adalah akronim dari JavaScript Object Notation. JavaScript sendiri adalah bahasa yang digunakan untuk pengembangan web. Dengan demikian, penggunaan JSON dalam konteks pengembangan web lebih disukai karena lebih mudah untuk dipakai dengan JavaScript dengan menggunakan fungsi `JSON.parse`. Di sisi lain, XML harus menggunakan _parser_ XML tambahan yang akan menambah kompleksitas aplikasi.
3. **JSON lebih ringkas** &mdash; Seperti pada poin 1, XML menggunakan tag pembuka dan penutup, sedangkan JSON menggunakan pasangan _key-value_. Hal ini menyebabkan berkas JSON cenderung lebih kecil daripada berkas XML untuk representasi data yang sama. 

### :arrow_right: Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada Django digunakan untuk melakukan validasi terhadap data yang dikirim dari klien. Validasi ini perlu dilakukan untuk mengecek apakah data tersebut sudah sesuai dengan batasan dan aturan yang telah ditetapkan di form. Sebagai contoh, sebuah aplikasi menerima _field_ `harga` yang bertipe _integer_. Jika klien mengirimkan harga dalam bentuk _string_, tanpa validasi, akan terjadi berbagai error pada aplikasi yang tidak diinginkan saat aplikasi mencoba untuk memproses data tersebut.

Method `is_valid()` bertindak sebagai "penjaga gerbang" yang memastikan data yang diterima valid. Jika validasi berhasil, `is_valid()` akan mengembalikan nilai `True` dan aplikasi melanjutkan proses seperti biasa. Namun, jika validasi gagal, Django akan menyimpan pesan error yang terjadi, dan `is_valid()` akan mengembalikan nilai `False`. Dengan cara ini, error tersebut dapat ditangani dengan menampilkan pesan yang sesuai kepada klien.

### :arrow_right: Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Penggunaan token CSRF adalah salah satu tindakan untuk mencegah terjadinya serangan CSRF. Secara sederhana, serangan CSRF adalah serangan di mana sebuah situs berbahaya memanfaatkan sesi login situs lain untuk melakukan aksi di situs tersebut tanpa sepengetahuan pengguna. Token CSRF berfungsi sebagai lapisan verifikasi tambahan yang memastikan bahwa aksi yang diterima oleh _server_ adalah permintaan yang sah dari pengguna, bukan dari situs berbahaya.

Dalam Django, setiap kali form dibuat, _server_ akan membuat token CSRF yang unik dan menanamkannya dalam form. Saat form tersebut dikirim oleh pengguna, token tersebut akan dikembalikan ke _server_. _Server_ kemudian memeriksa apakah token CSRF yang diterima adalah token sah yang sebelumnya pernah dibuat. Jika token cocok, aksi tersebut dianggap sah dan diproses. Jika token tersebut tidak cocok, permintaan akan ditolak untuk meminimalisasi potensi terjadinya serangan.

### :arrow_right: Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

#### :one: Membuat input form untuk menambahkan objek model pada app sebelumnya.
Forms dalam Django didefinisikan dalam sebuah berkas bernama `forms.py`, yang biasanya diletakkan dalam folder aplikasi. Untuk membuat form, saya menambahkan berkas `forms.py` ke dalam folder `main` dan mendefinisikan kelas `ProductForm`. Kelas ini digunakan sebagai wadah untuk pembuatan objek `Product` baru.

```python3
# main/forms.py

from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
```

Selanjutnya, untuk menampilkan form pembuatan produk baru, saya menambahkan berkas template baru bernama `create_product.html` yang diletakkan di folder `main/templates`. Template ini berisi form yang akan digunakan oleh pengguna untuk membuat produk baru.

```django
{% comment %} create_product.html {% endcomment %}

{% extends 'base.html' %}

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>
{% endblock content %}
```

Di dalam berkas `main/views.py`, saya membuat fungsi baru bernama `create_product`. Fungsi ini bertugas untuk memproses permintaan dari pengguna untuk membuat produk baru dengan menggunakan kelas `ProductForm` di `main/forms.py`. Fungsi ini akan menangani permintaan GET untuk menampilkan form pembuatan produk dan POST untuk memproses data.

```python3
# main/views.py

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    return render(request, 'create_product.html', { 'form': form })
```

Terakhir, dalam berkas `main/urls.py`, saya menghubungkan rute _path_ `/create-product` ke fungsi `create_product`.

```python3
# main/urls.py

urlpatterns = [
    # ...
    path('create-product', create_product, name='create_product'),
    # ...
]
```

Dengan demikian, ketika pengguna mengunjungi halaman `/create-product`, mereka dapat mengisi form untuk menambahkan produk baru, dan setelah data divalidasi, produk tersebut akan disimpan dalam basis data.

#### :two: Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Dalam berkas `main/views.py`, saya definisikan 4 fungsi baru, yaitu `show_xml`, `show_xml_by_id`, `show_json`, dan `show_json_by_id`. Masing-masing fungsi ini berfungsi sesuai dengan namanya, `show_xml` dan `show_json` akan menampilkan seluruh produk dalam XML dan JSON, `show_xml_by_id` dan `show_json_by_id` akan menampilkan produk berdasarkan ID dalam XML dan JSON.

```python3
# main/views.py

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
```

#### :three: Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Dalam berkas `main/urls.py`, saya memperbarui variabel `urlpatterns` dengan menambahkan rute untuk keempat fungsi yang baru didefinisi. Rute-rute ini memastikan bahwa permintaan ke URL akan ditangani oleh fungsi yang sesuai.

```python3
# main/urls.py

urlpatterns = [
    # ...
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<str:id>', show_json_by_id, name='show_json'),
    # ...
]
```

### :camera_flash: Postman Screenshots

#### :one: XML
![image](https://github.com/user-attachments/assets/3cc72ad1-d050-4ac1-b85d-db79bf64c13d)

#### :two: JSON
![image](https://github.com/user-attachments/assets/9f4abf90-69df-4fc9-9257-53b9ea458726)

#### :three: XML by ID
![image](https://github.com/user-attachments/assets/838b5061-2cb7-4998-ba2e-8614ee7cc4f6)

#### :four: JSON by ID
![image](https://github.com/user-attachments/assets/0d463b05-da98-4e74-ba26-97441e034d42)
</details>

<details>
<summary>:blue_book: Tugas 4</summary>

## :blue_book: Tugas 4

### :arrow_right: Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
Redirect dalam HTTP diatur menggunakan _status codes_ dalam rentang `3xx`. Salah satu cara untuk menangani _redirect_ di Django adalah dengan menggunakan `HttpResponseRedirect`, yang merupakan sebuah subclass dari `HttpResponse`. Kelas ini secara otomatis menetapkan _status code_ 302, yaitu _status code_ standar untuk HTTP _redirect_.

Fungsi `redirect` adalah fungsi pembantu yang secara internal akan menghasilkan _response_ HTTP dengan _status code_ 302, sama seperti `HttpResponseRedirect`. Fungsi ini dapat menerima argumen berupa `model`, `view`, atau `url` dan secara otomatis menentukan _path_ yang dituju berdasarkan konteks projek Django.

Secara umum, fungsi `redirect` lebih fleksibel daripada class `HttpResponseRedirect`. `HttpResponseRedirect` hanya digunakan untuk membuat _response_ HTTP dengan _status code_ yang berada di jangkauan `3xx`. Fungsi `redirect` tidak hanya menyediakan _response_ 302, tetapi juga berintegrasi dengan projek Django, sehingga lebih mudah untuk digunakan.

### :arrow_right: Jelaskan cara kerja penghubungan model `Product` dengan `User`!
Penghubungan model `Product` dengan `User` dilakukan dengan relasi menggunakan `models.ForeignKey`. 

```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
```

Pada kode tersebut, `Product` terhubung dengan `User` melalui field `user`. Field tersebut mendeklarasikan bahwa banyak `Product` dapat dimiliki oleh seorang `User`, menciptakan relasi _one-to-many_. Penggunaan `on_delete=models.CASCADE` berarti jika sebuah `User` dihapus, semua `Product` yang terhubung dengan `User` tersebut ikut dihapus.

### :arrow_right: Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Autentikasi adalah proses verifikasi identitas pengguna. Proses autentikasi memastikan bahwa pengguna benar-benar merupakan pengguna yang dia klaim. Otorisasi adalah proses yang menentukan apakah seorang pengguna memiliki hak akses terhadap suatu _resource_. Secara umum, autentikasi menentukan siapa pengguna tersebut dan otorisasi menentukan hak akses yang dimiliki oleh seorang pengguna.

Saat pengguna login, autentikasi akan memverifikasi identitas mereka melalui username dan password. Lalu, username dan password tersebut akan dibandingkan dengan data yang tersimpan dalam basis data. Setelah berhasil diautentikasi, pengguna dapat diotorisasi untuk mengakses fitur-fitur tertentu sesuai dengan hak akses mereka.

Django mengimplementasikan autentikasi melalui modul `django.contrib.auth`. Django menyediakan fungsi-fungsi bawaan untuk memverifikasi identitas pengguna, seperti `login` dan `logout`. Selain itu, Django menyediakan model `User` untuk menyimpan data-data pengguna. Otorisasi dalam Django diterapkan melalui sistem permissions dan groups yang fleksibel, memungkinkan pengembang untuk mengatur hak izin sesuai kebutuhan. Hak akses setiap pengguna dapat diatur secara individu, maupun berdasarkan grup yang mereka ikuti.

### :arrow_right: Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang sudah login dengan menggunakan _session_ dan _cookies_. Saat pengguna berhasil login, Django menyimpan informasi sesi mereka dalam basis data, yang berisi informasi penting seperti identitas pengguna. Kemudian, Django mengirimkan sebuah session ID ke klien dalam bentuk _cookie_. Setiap kali pengguna mengunjungi halaman dalam aplikasi, _cookie_ ini akan dikirimkan kembali ke _server_. Lalu, Django akan membaca _cookie_ tersebut untuk mengambil session ID dan membandingkannya dengan informasi sesi yang tersimpan dalam basis data. Jika terdapat sesi yang cocok dengan session ID, Django dapat membaca informasi pengguna terkait dan melanjutkan interaksi tanpa perlu pengguna untuk login ulang.

Cookies juga memiliki fungsi lain selain untuk _session management_. Cookies biasa digunakan untuk menyimpan data pada browser klien, seperti preferensi pengguna dan data sementara. Cookies juga berfungsi untuk pelacakan aktivitas pengguna, memungkinkan situs untuk menyesuaikan konten atau iklan berdasarkan perilaku pengguna.

Cookies memiliki beberapa konfigurasi untuk mengatur bagaimana cookie tersebut bekerja. Jika sebuah cookie tidak diatur dengan tepat, cookie tersebut dapat menjadi celah untuk dieksploitasi penyerang untuk mencuri data dengan menggunakan sesi pengguna. Beberapa konfigurasi cookie yang perlu diperhatikan adalah sebagai berikut.

1. **HttpOnly** &mdash; Cookie dengan atribut `HttpOnly` tidak dapat diakses oleh JavaScript yang membantu mencegah serangan XSS.
2. **Secure** &mdash; Cookie dengan atribut `Secure` hanya dapat dikirim melalui HTTPS, bukan HTTP. Dengan demikian, data dalam cookie akan terenkripsi dan terjaga saat pengiriman.
3. **SameSite** &mdash; Atribut `SameSite` mengatur apakah sebuah cookie dapat dikirim dengan sebuah permintaan yang akan dilaksanakan. Atribut ini membantu melindungi dari serangan CSRF.
4. **Expiration** &mdash; Atribut `Expiration` mengatur kapan sebuah cookie kadaluwarsa. Adanya waktu kadaluwarsa mengurangi risiko terjadinya serangan dengan memperkecil jendela bagi penyerang untuk mengambil cookie dari pengguna.

### :arrow_right: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### :one: Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
1. Membuat tiga fungsi di `main/views.py`, yaitu `register_user`, `login_user`, dan `logout_user`. Fungsi `register_user` dan `login_user` memanfaatkan class yang disediakan oleh Django, yaitu `UserCreationForm` dan `AuthenticationForm`. 
   ```python
   # ...

   # digunakan ketika seorang pengguna ingin membuat akun baru
   def register_user(request):
       if request.method == "POST":
           form = UserCreationForm(request.POST)
    
           if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
    
       form = UserCreationForm()
       return render(request, 'register.html', { 'form': form })

   # digunakan ketika seorang pengguna ingin login menggunakan akun mereka
   def login_user(request: HttpRequest):
       if request.method == "POST":
           form = AuthenticationForm(data=request.POST)
    
           if form.is_valid():
               user = form.get_user()
               login(request, user)
    
               response = HttpResponseRedirect(reverse('main:show_main'))
               response.set_cookie('last_login', str(datetime.now()))
               return response
    
       form = AuthenticationForm(request)
       return render(request, 'login.html', { 'form': form })

   # digunakan ketika seorang pengguna ingin logout dari akun mereka
   def logout_user(request: HttpRequest):
       logout(request)
       return redirect('main:login')

   # ...
   ```
2. Masing-masing fungsi tersebut dipetakan ke `register/`, `login/`, dan `logout/` dalam `main/urls.py`, supaya dapat diakses.
   ```python
   urlpatterns = [
       # ...
       path('register/', register_user, name='register'),
       path('login/', login_user, name='login'),
       path('logout/', logout_user, name='logout'),
       # ...
   ]
   ```
3. Perlu juga menambahkan _decorator_ `@login_required(login_url='/login')` untuk _views_ yang pengguna perlu login, seperti `/`, dan `/create-product`. Jika pengguna yang belum terautentikasi mencoba untuk mengunjungi halaman tersebut, mereka akan diarahkan ke halaman login terlebih dahulu.
4. Ketika seorang pengguna pertama kali mengunjungi aplikasi, pengguna tersebut akan diarahkan ke formulir login. Setelah berhasil login, pengguna dapat menggunakan aplikasi dengan penuh, seperti mengunjungi _dashboard_ dan menambahkan `Product`.

#### :two: Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

##### Akun dengan Username `A`

![image](https://github.com/user-attachments/assets/7c42400b-b6a8-4552-bb21-d81731b95e31)
![image](https://github.com/user-attachments/assets/b5bcf6a1-6cd5-4207-8064-8f08c375e5b7)
![image](https://github.com/user-attachments/assets/c5fa26b7-0f81-4947-9e68-1beed063624e)
![image](https://github.com/user-attachments/assets/9b959179-3d82-4327-b867-9f5404d90cb3)
![image](https://github.com/user-attachments/assets/b0b7036e-cb54-40d0-a6da-f70c9601e714)

##### Akun dengan Username `B`

![image](https://github.com/user-attachments/assets/9744df57-0903-417a-9d49-53a6e5ba40cd)
![image](https://github.com/user-attachments/assets/b5639afb-43b7-4ee5-bf31-08dde8d08de6)
![image](https://github.com/user-attachments/assets/2e18372d-07d3-4fb9-9944-899ed53b2e4f)
![image](https://github.com/user-attachments/assets/0df6981e-38f7-421c-8533-4ce3e09ced25)
![image](https://github.com/user-attachments/assets/5255ef5b-3ae2-49f6-acbb-4e38f4c10088)


#### :three: Menghubungkan model Product dengan User.
Penghubungan dilakukan dengan menambahkan _field_ pada model `Product`, yaitu field `user` dengan value berupa `models.ForeignKey`. Penambahan ini akan menghubungkan `User` dengan `Product` menggunakan relasi _one-to-many_, yang berarti seorang `User` dapat memiliki banyak `Product`. Perubahan pada model `Product` secara lengkap adalah sebagai berikut.

```python
class Product(models.Model):
    # tambahkan field ini
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
```

##### Penjelasan `models.ForeignKey`
- `User` menandakan bahwa foreign key yang dibuat menunjuk ke sebuah baris dalam tabel `User`.
- `on_delete=models.CASCADE` menandakan bahwa ketika seorang `User` dihapus, `Product` yang terhubung dengan `User` tersebut juga dihapus.

#### :four: Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
1. Pada view `login_user`, dibuat supaya ketika seorang pengguna mencoba untuk log in dan berhasil, sebuah cookie dengan nama `last_login` akan dibuat dengan isi waktu saat pengguna login.
   ```python
   def login_user(request: HttpRequest):
       if request.method == "POST":
           form = AuthenticationForm(data=request.POST)
    
           if form.is_valid():
               user = form.get_user()
               login(request, user)
    
               response = HttpResponseRedirect(reverse('main:show_main'))
               response.set_cookie('last_login', str(datetime.now()))
               return response
    
       form = AuthenticationForm(request)
       return render(request, 'login.html', { 'form': form })
   ```
2. Data `username` dapat diambil dari object `request.user` yang berisi data pengguna yang sedang log in. Cookies tersedia pada dictionary `request.COOKIES`. Pengimplementasian cookie _last login_ dimulai dari fungsi _view_ `login_user`. Kedua data tersebut tersedia dalam fungsi view `show_main`.
   ```python
   @login_required(login_url='/login')
   def show_main(request: HttpRequest):
       products = Product.objects.filter(user=request.user)
    
       return render(request, "main.html", {
           "name": request.user.username,
           "npm": "2306152411",
           "class": "F",
           "products": products,
           "last_login": request.COOKIES['last_login'],
       })
   ```
3. Data nama dan last login diserahkan ke template `main.html`. Dalam template tersebut, dapat ditampilkan datanya dengan menggunakan kurung kurawal ganda.
   ```django
   <p>{{ name }}<p>
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ```

</details>

<details>
<summary>:blue_book: Tugas 5</summary>

# :blue_book: Tugas 5

### :arrow_right: Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika sebuah elemen HTML memiliki beberapa CSS selector, prioritasnya ditentukan berdasarkan spesifisitas, _important rules_, dan urutan pendefinisian.

1. `!important` _rules_ 
    ```html
    <p id="text" class="text" style="color: blue;">Hello World</p>
    ```
    ```css
    p {
        color: red !important;
    }
    ```
    Jika terdapat CSS _rule_ dengan tag `!important`, _rule_ tersebut akan memiliki prioritas tertinggi dan menimpa _rule_ lain dengan selector lain. Teks "Hello World" di atas akan berwarna merah karena CSS _rule_ yang mendefinisikan memiliki atribut `!important` sehingga prioritasnya paling tinggi.

3. Inline Styles
    ```html
    <p id="text" class="text" style="color: blue;">Hello World</p>
    ```
    ```css
    #text {
        color: red;
    }
    ```
    CSS _rule_ yang didefinisikan secara inline di HTML tag akan memiliki prioritas yang tinggi. Teks "Hello World" di atas akan berwarna biru karena _inline style_ memiliki prioritas yang lebih tinggi daripada _selector_ ID.

4. ID
    ```html
    <p id="text" class="text">Hello World</p>
    ```
    ```css
    #text {
        color: red;
    }

    .text {
        color: green;
    }
    ```
    Teks "Hello World" di atas akan berwarna merah karena _selector_ ID memiliki prioritas yang lebih tinggi daripada _selector class_.

5. Classes, pseudo-classes, attribute selectors
    ```html
    <p class="text">Hello World</p>
    ```
    ```css
    .text {
        color: red;
    }

    p {
        color: blue;
    }
    ```
    Teks "Hello World" di atas akan berwarna merah karena _selector class_ memiliki prioritas yang lebih tinggi daripada _selector_ elemen.

6. Elements and pseudo-elements
    ```html
    <p>Hello World</p>
    ```
    ```css
    p {
        color: red;
    }
    ```
    Teks "Hello World" di atas akan berwarna merah karena didefinisikan menggunakan _selector_ elemen.

7. Urutan dalam CSS Stylesheet
   ```html
   <p>Hello World</p>
   ```
   ```css
   p {
       color: red;
   }

   p {
       color: blue;
   }
   ```
   Jika terdapat dua CSS _rule_ yang mendefinisikan dengan prioritas yang sama, CSS _rule_ yang didefinisikan terakhir pada _stylesheet_ akan diterapkan. Teks "Hello World" di atas akan berwarna biru karena _rule_ CSS yang mendefinisikan warna biru lebih akhir daripada _rule_ CSS yang mendefinisikan warna merah.

- https://www.w3schools.com/css/css_specificity.asp
- https://www.w3schools.com/css/css_important.asp

### :arrow_right: Mengapa _responsive design_ menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
_Responsive design_ adalah pendekatan desain web di mana sebuah tampilan dapat beradaptasi dengan berbagai ukuran layar yang ada, seperti untuk desktop, tablet, dan perangkat mobile. Salah satu aspek penting dari penerapan _responsive design_ adalah pengalaman pengguna. Sebuah tampilan web yang responsif akan memiliki pengalaman pengguna yang lebih baik dibandingkan tampilan web yang tidak responsif. Tampilan web yang hanya dirancang untuk ukuran layar besar, seperti desktop, akan sulit untuk dipakai jika web tersebut diakses menggunakan gawai dengan ukuran layar kecil, seperti mobile. Hal ini dapat menyebabkan elemen-elemen pada halaman tampak kecil, tidak proporsional, sulit dijangkau, dan mengurangi kenyamanan pengguna. Sebaliknya, jika web tersebut sudah menerapkan _responsive design_, pengguna yang menggunakan melalui mobile tidak akan menemui masalah apa pun karena tampilannya sudah didesain sedemikian hingga supaya beradaptasi ke ukuran layar yang bervariasi.

Secara umum, sebagian besar web modern sudah mengimplementasikan _responsive design_, terutama pada situs-situs populer seperti Twitter, YouTube, dan Google. Hal ini dapat dilihat dengan mengunjungi web-web tersebut menggunakan mobile, di mana setiap elemen tampil secara proporsional dan tidak ada yang rusak. Namun, masih ada beberapa web yang digunakan sekarang yang belum mengimplementasikan _responsive design_. Salah satu contohnya adalah SiakNG. Ketika diakses melalui perangkat mobile, tampilan SiakNG menunjukkan elemen-elemen yang terlalu kecil, sehingga pengguna perlu memperbesar layar untuk berinteraksi dengan nyaman.

- https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design

### :arrow_right: Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

#### Margin
Margin adalah jarak luar antara elemen dengan elemen lain di sekitarnya. Margin tidak memiliki warna dan mengosongkan daerah di luar border.
```css
div {
    margin: 10px;
}
```
CSS di atas mendefinisikan margin sebesar `10px` untuk semua sisi pada elemen `div`.

#### Border
Border adalah garis yang mengelilingi elemen yang berada diantara padding dan margin. Border dapat diberi warna, lebar, dan _style_ (solid, double, dash, dan seterusnya). Setiap sisi border dapat diatur secara independen.
```css
div {
    border: 1px solid black;
}
```
CSS di atas mendefinisikan border untuk elemen `div` dengan style solid, selebar 1 pixel, dan berwarna hitam.

#### Padding
Padding adalah jarak antara isi elemen dengan border. Padding menciptakan area dalam elemen di antara border dengan isi elemen.
```css
div {
    padding: 10px;
}
```
CSS di atas mendefinisikan padding sebesar `10px` untuk semua sisi pada elemen `div`.


- https://www.w3schools.com/css/css_boxmodel.asp

### :arrow_right: Jelaskan konsep flex box dan grid layout beserta kegunaannya!

#### Flexbox
Flexbox dalam CSS adalah sistem layout 1 dimensi dalam CSS yang digunakan untuk menyusun elemen dalam sebuah container, baik secara horizontal maupun vertikal. Arab dari flexbox dapat diatur menggunakan properti `flex-direction` yang dapat berupa `row`, `row-reverse`, `column`, atau `column-reverse`. `row` untuk horizontal dan `column` untuk vertikal. Flexbox memungkinkan elemen-elemen dalam container untuk menyesuaikan diri dengan ruang yang tersisa.

Dengan flexbox, posisi elemen dalam container dapat dengan mudah diatur di sepanjang sumbu utama (_main axis_) dan sumbu sekunder (_cross axis_) dengan properti berikut.
1. `justify-content`: Mengatur distribusi elemen pada sumbu utama.
2. `align-items`: Mengatur distribusi elemen pada sumbu sekunder.

Flexbox juga memungkinkan untuk mendistribusikan ruang yang tersedia secara proporsional antara elemen dalam container dengan menggunakan properti berikut.
1. `flex-grow`: Mengatur perilaku elemen terhadap ruang yang tersisa, apakah elemen tersebut akan berkembang mengisi ruang yang tersisa, atau tetap pada ukurannya.
2. `flex-shrink`: Mengatur perilaku elemen terhadap ruang yang terbatas, apakah elemen tersebut akan menyusut memberikan tempat ke elemen lain, atau tetap pada ukurannya. 
3. `flex-basis`: Mengatur ukuran inisial elemen sebelum elemen tersebut tumbuh atau menyusut.

Flexbox ideal untuk mengatur posisi elemen dalam 1 dimensi, seperti:
1. Navbar dan sidebar dengan mengatur elemen-elemen _button_ dan _link_ dalam posisi horizontal atau vertikal.
2. List produk yang tersusun dalam satu baris atau satu kolom.
3. Menengahkan secara vertikal elemen-elemen yang berada dalam satu baris.

#### Grid
Grid adalah sistem layout 2 dimensi yang menggunakan baris dan kolom untuk menaruh elemennya. 

Grid bekerja dengan menggunakan sistem baris dan kolom. Pengembang dapat mengatur jumlah baris dan kolom dan mendefinisikan besarnya dengan menggunakan properti sebagai berikut.
1. `grid-template-columns`: Mengatur jumlah kolom dan ukuran masing-masing kolom pada grid.
2. `grid-template-rows`: Mengatur jumlah baris dan ukuran masing-masing baris pada grid.

Grid ideal untuk mengatur posisi elemen dalam 2 dimensi, seperti:
1. Menyusun galeri yang rapi dan terstruktur dengan baris dan kolom yang konsisten
2. Layout halaman utama yang lumayan kompleks dengan header, sidebar, konten utama, dan footer.

#### Perbedaan Utama Flexbox dan Grid
1. Flexbox mengatur elemen satu per satu sepanjang sumbu utama, sedangkan grid mengatur elemen sepanjang dua sumbu secara bersamaan.
2. Flexbox lebih cocok untuk mengatur elemen pada satu sumbu saja, horizontal atau vertikal. Grid lebih cocok untuk mengatur elemen pada dua sumbu, horizontal dan vertikal.

- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Relationship_of_grid_layout_with_other_layout_methods
- https://www.geeksforgeeks.org/comparison-between-css-grid-css-flexbox/

### :arrow_right: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### :one: Implementasikan fungsi untuk menghapus dan mengedit product.
Pertama, membuat fungsi baru di `main/views.py`, yaitu `update_product` dan `delete_product`. Lalu, kedua fungsi ini dipetakan ke _path_ `product/<str:id>/edit` dan `product/<str:id>/delete`. Dengan demikian, ketika seorang pengguna yang sudah terautentikasi mengunjungi _path_ tersebut, mereka dapat menghapus atau mengedit produk berdasarkan ID produk. Definisi kedua fungsi tersebut adalah sebagai berikut.

```python
@login_required(login_url='/login')
def update_product(request: HttpRequest, id):
    obj = get_object_or_404(Product, id=id, user_id=request.user.id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return redirect('main:show_main')

        return redirect('main:show_main')

    form = ProductForm(instance=obj)
    return render(request, 'update_product.html', { 'form': form })

@login_required(login_url='/login')
def delete_product(request: HttpRequest, id):
    obj = get_object_or_404(Product, id=id, user_id=request.user.id)

    if request.method == 'POST':
        obj.delete()
        return redirect('main:show_main')

    return render(request, 'delete_product.html', { 'product': obj })
```

#### :two: Kustomisasi halaman _login_, _register_, dan tambah _product_ semenarik mungkin.
Pertama, saya membuat komponen baru `text_input` dalam direktori `main/templates/components`. Komponen ini akan digunakan dalam setiap formulir supaya konsistensi input teks sama. Kedua, saya membuat tampilan untuk _login_ berupa _card_ menggunakan TailwindCSS. Lalu, tampilan _login_ tersebut saya gunakan lagi untuk halaman _register_, tambah _product_, dan edit _product_. Tampilan dari _login_ adalah sebagai berikut.

```html
<main class="min-h-screen flex flex-col items-center justify-center gap-5">
  <form method="POST" class="px-10 py-8 flex flex-col justify-center gap-4 bg-white rounded-lg shadow-sm border border-gray-300">
    <h1 class="text-3xl font-bold w-full mb-3">Title</h1>
    <!-- Isi Form -->
  </form>
</main>
```

![image](https://github.com/user-attachments/assets/34539053-b955-497e-babf-df40ab8faafb)

#### :three: Kustomisasi halaman daftar _product_ menjadi lebih menarik dan _responsive_. Kemudian, perhatikan kondisi berikut: Jika pada aplikasi belum ada _product_ yang tersimpan, halaman daftar _product_ akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan _card_ (tidak boleh sama persis dengan desain pada Tutorial!).

##### Membuat Tampilan _Responsive_ dengan TailwindCSS
Dengan TailwindCSS, tampilan _responsive_ dapat dengan mudah dicapai meggunakan _breakpoints_, seperti `sm:`, `md:`, `lg:`, dan seterusnya. _Breakpoints_ ini memungkinkan kita untuk menentukan aturan-aturan CSS khusus yang hanya diterapkan ketika ukuran layar sudah melewati batas tertentu. Dengan demikian, kita dapat mendefinisikan _style_ tertentu untuk ukuran layar tertentu.

##### Penggunaan _If Statement_ untuk Menampilkan Produk
Dalam Django, menampilkan daftar produk secara kondisional bisa dilakukan dengan menggunakan tag `if`. Contohnya adalah sebagai berikut. 

```django
{% if not products %}
    <!-- HTML dalam block ini akan ditampilkan jika tidak ada produk -->
{% else %}
    <!-- HTML dalam block ini akan ditampilkan jika terdapat setidaknya 1 produk -->
{% endif %}
```

Dalam penerapannya, saya mengganti komponen HTML dalam _block_ tersebut dengan yang sesuai. Saat tidak ada produk, halaman akan menampilkan gambar yang menunjukkan bahwa belum ada produk terdaftar. Untuk itu, saya perlu menambahkan gambar ke dalam projek Django saya.

##### Menambahkan Gambar
Langkah pertama adalah mengubah `settings.py` dalam direktori `sekoleksi`.

```python
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / 'static']
else:
    STATIC_ROOT = BASE_DIR / 'static'
```

Dengan adanya konfigurasi ini, file-file yang berada dalam direktori `/static/` dapat diakses dalam Django menggunakan tag `static`. Lalu, saya tambahkan gambar bernama `empty-list.png` ke dalam folder `static/image`. Penggunaan gambar tersebut adalah sebagai berikut.

```django
{% load static %}
<img src="{% static 'image/empty-list.png' %}" width="300" class="block mx-auto">
```

Kode tersebut akan menampilkan gambar bernama `empty-list.png` yang berada dalam direktori `static/image`.

##### Menampilkan Daftar Produk
Untuk menampilkan daftar produk, dapat digunakan _for loop_ dalam Django untuk mengiterasikan setiap produk yang ada. Implementasinya adalah sebagai berikut.

```django
{% for product in products %}
  {% include "components/product_card.html" with product=product %}
{% endfor %}
```

Komponen `components/product_card.html` akan dijelaskan di nomor selanjutnya.

#### :four: Untuk setiap _card product_, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
Pertama, saya definisikan komponen HTML baru, yaitu `product_card.html` yang berada dalam direktori `main/templates/components`.

```django
<div class="flex flex-col bg-white rounded-lg border border-gray-200 shadow-sm py-6 px-8 text-wrap break-inside-avoid">
  <div class="flex flex-col max-w-md min-w-md">
    <a href="{% url 'main:show_product' product.id %}">
      <h1 class="text-xl font-bold hover:underline">{{ product.name }}</h1>
    </a>
    <h2 class="text-md mt-1">${{ product.price }}</h2>
    <p class="text-gray-700 my-4 w-full">{{ product.description }}</p>
  </div>
  <div class="flex flex-row justify-end items-center gap-3">
    <a class="text-blue-600 hover:underline" href="{% url 'main:update_product' product.id %}">Edit</a>
    <a class="text-blue-600 hover:underline" href="{% url 'main:delete_product' product.id %}">Delete</a>
  </div>
</div>
```

Kedua button untuk mengedit dan menghapus berupa link yang menuju halaman baru berupa form yang di mana _view_-nya telah didefinisikan di _checklist_ nomor 1. Form tersebut didefinisikan dalam `update_product.html` dan `delete_product.html`. Lalu, komponen tersebut digunakan dalam `main.html` dengan menggabungkan dengan _for loop_ produk.

```python
{% for product in products %}
  {% include "components/product_card.html" with product=product %}
{% endfor %}
```

#### :five: Buatlah _navigation bar (navbar)_ untuk fitur-fitur pada aplikasi yang _responsive_ terhadap perbedaan ukuran device, khususnya _mobile_ dan _desktop_.
Pertama, saya membuat berkas baru bernama `navbar.html` dalam direktori `templates`. Implementasi tampilan _responsive_ dilakukan dengan menggunakan breakpoint TailwindCSS. Berikut adalah implementasi dropdown mobile pada `navbar.html`.

```django
<div class="md:hidden">
  <div class="pt-2 pb-5 space-y-1 mx-auto flex flex-col">
    <a href="#" class="hover:underline py-2 text-white">Home</a>
    <a href="#" class="hover:underline py-2 text-white">Products</a>
    <a href="#" class="hover:underline py-2 text-white">Categories</a>
    <a href="#" class="hover:underline py-2 text-white">Cart</a>
    {% if user.is_authenticated %}
      <p class="text-white">Welcome, {{ user.username }}</p>
      <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
        Logout
      </a>
    {% else %}
      <a href="{% url 'main:login' %}" class="block text-center bg-cyan-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 mb-2">
        Login
      </a>
      <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
        Register
      </a>
    {% endif %}
  </div>
</div>
```

Karena class `md:hidden`, `div` tersebut akan di-_apply_ style `hidden` jika ukuran layar sudah melebihi batas `md`. Dalam kata lain, _dropdown_ hanya ada jika ukuran layar kecil, seperti ukuran layar mobile. _Navigation bar_ ini dapat digunakan dalam template-template lain dengan menggunakan tag `include` pada Django. Implementasinya adalah sebagai berikut.

```django
{% include 'navbar.html' %}
```

</details>

<details>
<summary>:blue_book: Tugas 6</summary>

## :blue_book: Tugas 6

### :arrow_right: Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript adalah salah satu teknologi yang digunakan untuk pengembangan _frontend_. Bersama dengan HTML dan CSS, JavaScript mempunyai peran penting dalam menciptakan pengalaman pengguna yang dinamis dan interaktif. HTML bertugas untuk membangun struktur dasar aplikasi web, sementara CSS bertugas untuk mempercantik visual dari struktur tersebut. JavaScript, di sisi lain, memberikan fungsionalitas interaktif, memungkinkan pengguna untuk berinteraksi langsung dengan pengguna, memberikan pengalaman yang lebih hidup.

- https://www.w3schools.com/js/

### :arrow_right: Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?
Penggunaan `await` saat menggunakan `fetch()` berfungsi untuk menunggu hasil permintaan yang asinkron sebelum melanjutkan eksekusi kode yang sinkron. Seperti yang kita tahu, permintaan ke server tidak instan. Tanpa adanya penggunaan `await`, eksekusi kode akan lanjut tanpa menunggu hasil dari permintaan ke server. Alhasil, dapat terjadi kesalah saat mencoba untuk mengakses data yang belum tersedia. 

- https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

### :arrow_right: Mengapa kita perlu menggunakan decorator `csrf_exempt` pada _view_ yang akan digunakan untuk AJAX `POST`?
Decorator `csrf_exempt` digunakan untuk menonaktifkan perlindungan CSRF untuk view tersebut, sehingga permitnaan AJAX `POST` dapat dilakukan tanpa validasi token CSRF. Secara default, Django akan memblokir POST request tanpa ada token CSRF. Perilaku default ini sedikit mempersulit penggunaan AJAX `POST` di Django. Pada umumnya, form dapat menggunakan `{% csrf_token %}`, tetapi untuk AJAX `POST` kita tidak dapat akses ke CSRF token tersebut. Dengan demikian, untuk mendukung penggunaan AJAX `POST`, validasi token CSRF dinonaktifkan untuk _view_ tersebut.

- https://docs.djangoproject.com/en/5.1/ref/csrf/

### :arrow_right: Pada tutorial PBP minggu ini, pembersihan data _input_ pengguna dilakukan di belakang (_backend_) juga. Mengapa hal tersebut tidak dilakukan di _frontend_ saja?
Pembersihan data juga dilakukan di _backend_ untuk meminimalisasi masuknya data yang tidak bersih. Jika sebuah _view_ terdapat `csrf_exempt`, _view_ tersebut dapat dieksekusi melalui klien HTTP, seperti Postman. Dengan menggunakan Postman untuk melakukan permintaan ke server, kita dapat melewati pembersihan data yang dilakukan di _frontend_. Jika tidak ada pembersihan data _input_ di _backend_, penyerang dapat dengan mudah berinteraksi menggunakan Postman untuk memasukkan data-data yang tidak aman ke basis data. Dengan demikian, perlu juga dilakukan pembersihan data di _backend_.

### :arrow_right: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### :one: AJAX `GET`
Pertama, mengubah fungsi `show_main` di `views.py` untuk tidak melakukan pengambilan data dari basis data. Kita ingin data diambil melalui pemanggilan AJAX di klien.

Kedua, mengubah fungsi `show_xml` dan `show_json` untuk mengambil produk-produk untuk user yang sedang _logged in_. Ini dilakukan dengan menggunakan method `filter` pada `Product` dengan argumen `user=request.user`. Fungsi `show_json` akan dipanggil dari klien dalam bentuk permintaan AJAX.

Ketiga, mengubah kode di `main.html` untuk melakukan permintaan AJAX `GET` untuk mengambil data-data produk. Sebelumnya, pengambilan data dilakukan di _server_ dan kode di `main.html` mengiterasikan untuk setiap produk. Perlu mendefinisikan dua fungsi JavaScript baru di klien, `getProducts`, untuk mengambil data melalui AJAX `GET`, dan `refreshProducts`, untuk menampilkan data.

Implementasi fungsi `getProducts` menggunakan fungsi `fetch` pada JavaScript ke URL `show_json`. Lalu, respons dari server akan diubah menjadi JSON dengan _method_ `.json()`.

```javascript
async function getProducts() {
    return fetch("{% url 'main:show_json' %}").then((res) => res.json());
}
```

Implementasi fungsi `refreshProducts` menggunakan fungsi `getProducts`. Setelah data produk diambil menggunakan fungsi `getProducts`, data-data tersebut di iterasikan dan ditampilkan sebagai _child_ dari elemen `#product-cards`.

```javascript
  async function refreshProducts() {
    const products = await getProducts();

    let classNames = "";
    let htmlString = "";

    if (products.length === 0) {
      classNames = "text-center bg-white rounded-lg border border-gray-200 shadow-sm py-6 px-10 break-inside-avoid";
      htmlString = `
        <img src="{% static 'image/empty-list.png' %}" width="300" class="block mx-auto">
        <p class="text-slate-600">Belum ada produk yang terdaftar</p>
      `;
    } else {
      classNames = "columns-1 md:columns-2 lg:columns-3 xl:columns-4 space-y-3 gap-x-3";
      products.forEach((product) => {
        htmlString += `
          <div class="flex flex-col bg-white rounded-lg border border-gray-200 shadow-sm py-6 px-8 text-wrap break-inside-avoid">
            <div class="flex flex-col max-w-md min-w-md">
                <a href="/product/${product.pk}">
                <h1 class="text-xl font-bold hover:underline">${DOMPurify.sanitize(product.fields.name)}</h1>
              </a>
              <h2 class="text-md mt-1">$${DOMPurify.sanitize(product.fields.price)}</h2>
              <p class="text-gray-700 my-4 w-full">${DOMPurify.sanitize(product.fields.description)}</p>
            </div>
            <div class="flex flex-row justify-end items-center gap-3">
              <a class="text-blue-600 hover:underline" href="/product/${product.pk}/edit">Edit</a>
              <a class="text-blue-600 hover:underline" href="/product/${product.pk}/delete">Delete</a>
            </div>
          </div>
        `;
      })
    }

    productCards.innerHTML = htmlString;
    productCards.className = classNames;
  }
```

Terakhir, pada HTML diperlukan sebuah elemen yang berfungsi sebagai kontainer dari produk-produk. Elemen ini berupa div dengan id `product-cards`.

#### :two: AJAX `POST`
Pertama, perlu mendefinisikan fungsi di `views.py` untuk menambahkan produk menggunakan AJAX, yaitu `create_product_ajax`. Decorator untuk fungsi ini adalah `csrf_exempt` dan `require_POST`. Fungsi ini hanya dapat dipanggil melalui `POST` request. Fungsi ini akan mengambil data `name`, `price`, dan `description` dari _body request_, memasukkannya ke `ProductForm` dan menyimpannya jika data-data valid. Perlu juga fungsi `strip_tags` untuk setiap _field_ data untuk membersihkan supaya tidak ada serangan XSS. Lalu, fungsi tersebut dihubungkan ke URL `product-ajax` di `urls.py` dengan nama `create_product_ajax`.

```python
@csrf_exempt
@require_POST
def create_product_ajax(request):
    product_form = ProductForm(
        data={
            "name": strip_tags(request.POST.get('name')),
            "price": strip_tags(request.POST.get('price')),
            "description": strip_tags(request.POST.get('description')),
        },
    )

    if product_form.is_valid():
        product = product_form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponse(b"CREATED", status=201)
    else:
        return HttpResponse(b"ERROR", status=400)
```

Kedua, perlu didefinisikan _method_ untuk melakukan pembersihan data pada `ProductForm`. _Method_ tersebut menggunakan fungsi `strip_tags` dan _raise_ error ketika _field_ tersebut ternyata berupa string kosong.

```python
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"])
        if not name:
            raise ValidationError("Name cannot be empty.")
        return name

    def clean_price(self):
        price = strip_tags(self.cleaned_data["price"])
        if not price:
            raise ValidationError("Price cannot be empty.")
        return price

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"])
        if not description:
            raise ValidationError("Description cannot be empty.")
        return description
```

Ketiga, perlu didefinisikan fungsi JavaScript baru untuk menambahkan produk melalui AJAX `POST`, yaitu `addProduct`. Fungsi ini akan melakukan `POST` request ke URL `create_product_ajax`. Data untuk request akan berasal dari isi dari form `product-form`. Jika requeset tersebut mengembalikan kode status dalam range `2xx`, maka formnya direset, daftar produk di-_refresh_, dan form modal akan di-_hide_. Dengan demikian, halaman tidak perlu direfresh untuk mendapatkan data baru.

```javascript
  const productForm = document.getElementById("product-form");

  const nameFieldError = document.getElementById("name-field-error");
  const priceFieldError = document.getElementById("price-field-error");
  const descriptionFieldError = document.getElementById("description-field-error");

  async function addProduct() {
    const res = await fetch("{% url 'main:create_product_ajax' %}", {
      method: "POST",
      body: new FormData(productForm),
    })

    if (res.ok) {
      productForm.reset();
      refreshProducts();
      hideModal();
      return;
    }

    const body = await res.json();

    if (body.name) {
      nameFieldError.innerHTML = "<ul>" + body.name.map((error) => `<li>${error.message}</li>`).join("") + "</ul>";
      nameFieldError.classList.remove("hidden");
    } else {
      nameFieldError.classList.add("hidden");
    }

    if (body.price) {
      priceFieldError.innerHTML = "<ul>" + body.price.map((error) => `<li>${error.message}</li>`).join("") + "</ul>";
      priceFieldError.classList.remove("hidden");
    } else {
      priceFieldError.classList.add("hidden");
    }

    if (body.description) {
      descriptionFieldError.innerHTML = "<ul>" + body.description.map((error) => `<li>${error.message}</li>`).join("") + "</ul>";
      descriptionFieldError.classList.remove("hidden");
    } else {
      descriptionFieldError.classList.add("hidden");
    }
  }
```

Keempat, perlu menambahkan fungsi modal form pada HTML, yaitu `show_modal`, dan `hide_modal`. Fungsi `show_modal` akan menampilkan modal dengan menghilangkan class `hidden`. Fungsi `hide_modal` akan menghilangkan modal dengan menambahkan class `hidden`. Button baru juga perlu ditambahkan di mana `onclick` akan mengeksekusi fungsi `showModal()` untuk menampilkan modal. Form pada modal akan mengeksekusi fungsi `addProduct` ketika di-_submit_.

```html
<button data-modal-target="crud-modal" data-modal-toggle="crud-modal" class="text-blue-600 hover:underline" onclick="showModal();">
  Add New Product by AJAX
</button>

...

<div id="crud-modal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
  <div id="crud-modal-content" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
    <!-- Modal header -->
    <div class="flex items-center justify-between p-4 rounded-t">
      <h3 class="text-xl font-semibold text-gray-900">
        Add New Product
      </h3>
      <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn" onclick="hideModal()">
        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
        <span class="sr-only">Close modal</span>
      </button>
    </div>
    <!-- Modal body -->
    <div class="px-6 py-4 space-y-6 form-style">
      <form id="product-form" onsubmit="submitAddProduct">

        <div class="w-full" id="name-field">
          <label for="name" class="text-sm">
            Name
          </label>
          <input
            id="name"
            name="name"
            type="text"
            required
            class="p-2 outline-none border-2 border-gray-200 focus:border-black w-full rounded-lg"
            placeholder="Berserk Deluxe Edition Vol. 1"
          />
          <div id="name-field-error" class="mt-2 bg-rose-200 border-2 border-rose-300 rounded-lg px-4 py-2 hidden"></div>
        </div>

        <div class="w-full" id="price-field">
          <label for="price" class="text-sm">
            Price
          </label>
          <input
            id="price"
            name="price"
            type="text"
            required
            class="p-2 outline-none border-2 border-gray-200 focus:border-black w-full rounded-lg"
            placeholder="60"
          />
          <div id="price-field-error" class="mt-2 bg-rose-200 border-2 border-rose-300 rounded-lg px-4 py-2 hidden"></div>
        </div>

        <div class="w-full" id="description-field">
          <label for="description" class="text-sm">
            Description
          </label>
          <textarea
            id="description"
            name="description"
            rows="10"
            cols="40"
            type="text"
            required
            class="p-2 outline-none border-2 border-gray-200 focus:border-black w-full rounded-lg"
            placeholder="Berserk is a dark fantasy manga that follows the brutal and tragic journey of Guts, a lone mercenary with a mysterious past, as he battles monstrous foes and struggles against fate in a violent medieval world."
          ></textarea>
          <div id="description-field-error" class="mt-2 bg-rose-200 border-2 border-rose-300 rounded-lg px-4 py-2 hidden"></div>
        </div>

        <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
          <button type="button" class="bg-red-600 hover:bg-red-500 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton" onclick="hideModal()">Cancel</button>
          <button type="submit" class="bg-cyan-600 hover:bg-cyan-500 text-white font-bold py-2 px-4 rounded-lg">Save</button>
        </div>
      </form>
    </div>
  </div>
</div>
```

```javascript
  const modal = document.getElementById("crud-modal");
  const modalContent = document.getElementById("crud-modal-content");

  function showModal() {
    modal.classList.remove('hidden'); 
    setTimeout(() => {
      modalContent.classList.remove('opacity-0', 'scale-95');
      modalContent.classList.add('opacity-100', 'scale-100');
    }, 50); 
  }

  function hideModal() {
    nameFieldError.classList.add("hidden");
    priceFieldError.classList.add("hidden");
    descriptionFieldError.classList.add("hidden");

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
      modal.classList.add('hidden');
    }, 150); 
  }
```

</details>

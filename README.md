# Tugas Kecil 3 IF2211 Strategi Algoritma


## Algoritma A *
> Algoritma A* merupakan gabungan antara Greedy Best First Search dan Uniform Search, dimana menggabungkan nilai nilai yang akan diuji dari Cost yang dibutuhkan dan Nilai Ekspektasi (dibebaskan pengambilannya), pada tugas ini, nilai ekspektasi akan diambil dari garis lurus menuju target (Euclidian Distance, namun karena bumi itu tidak datar, maka akan digunakan bantuan Haversine distance) 
## Algoritma A* Pada Program Ini
> Algoritma A* merupakan Algoritma yang melihat cost value dan expected cost dengan cara menarik garis lurus kepada target tujuan

> Algoritma A* ini bekerja dalam bentuk iteratif, representasi graph kami merupakan list of nodes, dengan isi namanya yang bernilai Nama, dan koordinat (latitude, longitudinal), Path dan Cost yang dibutuhkan sampai pada Node tersebut

> Algoritma A* akan mengiterasikan seluruh node pada graph, dan mengiterasikan kembali seluruh Node tetangga pada setiap Node, Pada Node yang dikunjungi, Koordinat Node tersebut akan dimasukkan pada list visited, menandakan node ini sudah dikunjungi, dan Node tidak akan dikunjungi lagi

> Pada setiap Node tetangga yang diiterasikan akan dimasukan kepada list tetangga yang berisikan nilai koordinat dan nama Node, besertakan nilai f(n) (Cost + Nilai Ekspektasi), lalu akan dilakukan update pada setiap Node tetangga, update dilakukan untuk 'keep track' akan path sebuah node dan cost setiap node (Jika Node tetangga tidak memiliki path, maka path akan dilanjutkan sesuai dengan path source, jika sudah ada pathnya, maka akan dilakukan perbandingan antara 2 jalur, dan jalur dengan harga termurah akan dimasukkan pada path node tetangga), sama seperti path, cost juga akan diupdate sesuai dengan nilai cost saat ini, jika nilainya masih bernilai 0, maka cost akan ditambah dengan source dan nilai cost selanjutnya.

> Selanjutnya tetangga akan disimpan pada sebuah list hasiltetangga, dan akan dicari nilai fungsi evaluasi terendahnya menjadi nilai source selanjutnya, sebelumnya nilai source akan disimpan pada before, untuk mengecek node sebelumnya yang diakses, pada akhirnya dilakukan pengecekan apakah source dan target sudah memiliki nama yang sama, sehingga jika sudah ditemukan maka algoritma akan mengembalikan hasil path dan nilai cost

## Dependencies
- Python3
- pip
- Flask v1.1.2

_Python module_ yang perlu di-_install_ dengan pip:
- flask_bootstrap
- plotly.graph_objects
- werkzeug
- chart_studio
- chart_studio.plotly

## Cara Menggunakan
1. Masukkan file yang ingin dites ke dalam folder `test`
2. Masuk ke dalam folder src
3. Jalankan `python3 app.py` pada terminal
4. Buka [http://localhost:2211]
5. Klik tombol 'Choose File' dan pilih file yang ingin digunakan kemudian klik tombol 'Submit'
6. Pilih 2 simpul dan klik tombol 'Astar!' untuk melihat hasil algoritma A*

## Side Note
Jika ingin mencari hasil algoritma kembali, disarankan untuk _refresh_ kembali halaman.

Hindari mengklik tombol 'Sumbit' dua kali karena dapat menyebabkan error.

Ada keterbatasan request api yaitu hanya 100 per hari.

Jika ada masalah penggunaan, dapat menghubungi penulis 

### Author
NIM | Nama | Email
--|--|--|
13519090|Alexander| 13519090@std.stei.itb.ac.id
13519116|Jeane Mikha Erwansyah|13519116@std.stei.itb.ac.id
---

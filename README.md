# Tucil_2_Stima_2022

> Implementasi _Convex Hull_ untuk Visualisasi Tes _Linear Separability Dataset_ dengan Algoritma _Divide and Conquer_

## **Deskripsi Singkat**
Modul `myConvexHull` ini dibuat untuk memenuhi tugas mata kuliah IF 2211 Strategi Algoritma. Modul ini berisi kode untuk menghasilkan _convex hull_ dari kumpulan titik yang tersedia menggunakan algoritma _divide and conquer_. Data diambil dari library `sklearn.datasets`. Kemudian diambil dua atribut untuk dijadikan kumpulan titik (x,y). Kumpulan titik dan _Convex hull_ yang dihasilkan selanjutnya diplot menggunakan library `matplotlib.pyplot`.

## **Requirement**
- Python minimal versi 3.9
- Jupyter Notebook
- Library `sklearn, matplotlib, numpy, pandas`

## **Langkah Compile**
Tidak diperlukan karena Python adalah _interpreted language_

## **Cara Menggunakan**
Buka file `myConvexHull.ipynb` dan jalankan semua block
Fungsi utama yang digunakan untuk mencari kumpulan titik pembentuk convex hull pada program ini adalah `ConvexHull(points)` \
input: array berukuran nx2 dengan n = jumlah titik. \
output: array berukuran mx2 dengan m = jumlah titik pembentuk _convex hull_, diurutkan secara melingkar berlawanan arah jarum jam.

## **Author**
Nama: Diky Restu Maulana \
NIM: 13520017 \
Prodi: Teknik Informatika
# File: main.py
# Berisi program utama untuk visualisasi kumpulan titik dan Convex Hull yang terbentuk

import myConvexHull as mc
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

# Fungsi untuk menerima input pilihan dataset
def pilihDataset():
    print("Daftar dataset:")
    print("1. iris")
    print("2. wine")
    print("3. breast cancer")
    opsi = int(input("Masukkan pilihan dataset: "))
    data = None
    if (opsi == 1):
        data = datasets.load_iris()
    elif (opsi == 2):
        data = datasets.load_wine()
    elif (opsi == 3):
        data = datasets.load_breast_cancer()
    else:
        print("Pilihan tidak valid!\n")
        return pilihDataset()
    return data

# Fungsi untuk melakukan plotting kumpulan titik dan Convex Hull yang dihasilkan  
def visualisasi(data):
    colors = ['b','r','g','c','m','y','k']

    # Membuat dataframe
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    nkolom = len(data.feature_names) # jumlah kolom
    ntarget = len(data.target_names) # jumlah target

    # Cetak pilihan kolom dan meminta masukan sepasang kolom
    for i in range(nkolom):
        print(f"{i+1}. {data.feature_names[i]}")
    opsi = input("Masukkan dua pilihan atribut berbeda (co. 1 2): ")
    xidx = int(opsi.split()[0]) - 1
    yidx = int(opsi.split()[1]) - 1
    try:
        x, y = data.feature_names[xidx], data.feature_names[yidx]
    except:
        print("Pilihan tidak valid! Program dihentikan.")
        exit(0)
    
    # Menampilkan hasil dalam bentuk gambar
    plt.figure(figsize = (10, 6))
    plt.title(f"{x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)
    for i in range(ntarget):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[xidx,yidx]].values
        listbucket = bucket.tolist()
        hull = mc.ConvexHull(listbucket)
        hull.append(hull[0]) # Menambahkan titik pertama supaya terbentuk poligon tertutup
        xs, ys = zip(*hull)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i]) # plot titik
        plt.plot(xs, ys, colors[i]) # plot garis
        plt.legend()
    plt.show()

# Fungsi utama
def main():
    print("Hai kamu... Selamat datang di program visualisasi Convex Hull ini.") 
    print("Silakan ikuti perintah yang muncul setelah ini, ya!\n")
    data = pilihDataset()
    visualisasi(data)

if (__name__ == "__main__"):
    main()
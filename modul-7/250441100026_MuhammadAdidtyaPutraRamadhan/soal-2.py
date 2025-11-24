inventaris = {}

def tampilkan_semua():
    if not inventaris:
        print("Belum ada barang dalam inventaris.")
    else:
        for id_barang, info in inventaris.items():
            print(f"ID: {id_barang} | Nama: {info[0]} | Harga: {info[1]} | Stok: {info[2]}")

def cari_barang():
    id_barang = input("Masukkan ID barang: ")
    if id_barang in inventaris:
        nama, harga, stok = inventaris[id_barang]
        print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}")
    else:
        print("Barang tidak ditemukan.")

def tambah_barang():
    while True:
        id_barang = input("ID Barang (angka saja): ")

        if not id_barang.isdigit():
            print("Error: ID hanya boleh angka!")
            continue

        if id_barang in inventaris:
            print("Error: ID sudah digunakan, buat ID lain.")
            continue

        break

    while True:
        nama = input("Nama Barang: ")
        if not nama.replace(" ", "").isalpha():
            print("Error: Nama tidak boleh mengandung angka atau simbol!")
        else:
            break

    while True:
        harga = input("Harga: ")
        if not harga.isdigit():
            print("Error: Harga hanya boleh angka!")
            continue
        harga = int(harga)
        if harga <= 0:
            print("Error: Harga tidak boleh 0!")
        else:
            break

    while True:
        stok = input("Stok: ")
        if not stok.isdigit():
            print("Error: Stok hanya boleh angka!")
            continue
        stok = int(stok)

        if stok <= 0:
            print("Error: Stok tidak boleh kosong atau 0!")
        else:
            break

    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan.")

def update_stok():
    id_barang = input("Masukkan ID barang yang akan diupdate stoknya: ")

    if id_barang in inventaris:
        stok_lama = inventaris[id_barang][2]

        while True:
            perubahan = input("Masukkan stok baru: ")

            if not perubahan.isdigit():
                print("Error: Stok harus angka!")
                continue

            stok_baru = int(perubahan)

            if stok_baru <= 0:
                print("Error: Stok tidak boleh kosong/0!")
                continue

            # Tidak boleh sama dengan stok sebelumnya
            if stok_baru == stok_lama:
                print("Error: Stok baru tidak boleh sama dengan stok lama!")
                continue

            break

        inventaris[id_barang][2] = stok_baru
        print("Stok berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")

def hapus_barang():
    id_barang = input("Masukkan ID barang yang akan dihapus: ")
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang")
    print("4. Update Stok")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
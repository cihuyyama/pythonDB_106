import tkinter as tk
import sqlite3

# Kelas untuk mengelola aplikasi prediksi prodi
class PrediksiProdiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Prediksi Prodi Pilihan")

        # Koneksi ke SQLite
        self.conn = sqlite3.connect('prediksi_prodi.db')
        self.cursor = self.conn.cursor()
        self.create_table()

        # Membuat UI
        self.create_widgets()

    # Membuat tabel prodi di database SQLite jika belum ada
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS prodi (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                matematika INTEGER,
                                bahasa_inggris INTEGER,
                                geografi INTEGER,
                                prediksi TEXT)''')
        self.conn.commit()

    # Fungsi untuk menyimpan data ke database
    def simpan_ke_db(self, matematika, bahasa_inggris, geografi, prediksi):
        self.cursor.execute('''INSERT INTO prodi (matematika, bahasa_inggris, geografi, prediksi)
                              VALUES (?, ?, ?, ?)''', (matematika, bahasa_inggris, geografi, prediksi))
        self.conn.commit()

    # Fungsi untuk menghitung prediksi prodi berdasarkan nilai input
    def hasil_prediksi(self):
        matematika = int(self.entry_matematika.get())
        bahasa_inggris = int(self.entry_bahasa_inggris.get())
        geografi = int(self.entry_geografi.get())

        # Kondisi prediksi prodi berdasarkan nilai
        if matematika > 80 and bahasa_inggris > 70 and geografi > 75:
            prodi = "Teknologi Informasi"
        elif matematika > 70 and bahasa_inggris > 60 and geografi > 80:
            prodi = "Sistem Informasi"
        elif matematika > 60 and bahasa_inggris > 65 and geografi > 70:
            prodi = "Manajemen"
        else:
            prodi = "Ilmu Sosial"

        # Menampilkan prediksi di label
        self.hasil_label.config(text=f"Prodi yang diprediksi: {prodi}")
        
        # Simpan ke database
        self.simpan_ke_db(matematika, bahasa_inggris, geografi, prodi)

    # Membuat elemen GUI
    def create_widgets(self):
        # Label dan Entry untuk input nilai
        tk.Label(self.root, text="Nilai Matematika:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_matematika = tk.Entry(self.root)
        self.entry_matematika.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Nilai Bahasa Inggris:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_bahasa_inggris = tk.Entry(self.root)
        self.entry_bahasa_inggris.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Nilai Geografi:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_geografi = tk.Entry(self.root)
        self.entry_geografi.grid(row=2, column=1, padx=10, pady=5)

        # Tombol untuk memprediksi prodi
        self.prediksi_button = tk.Button(self.root, text="Hasil Prediksi", command=self.hasil_prediksi)
        self.prediksi_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Label untuk menampilkan hasil prediksi
        self.hasil_label = tk.Label(self.root, text="Prodi yang diprediksi: ", font=("Arial", 12))
        self.hasil_label.grid(row=4, column=0, columnspan=2, pady=10, padx=20)

    # Tutup koneksi ke database
    def close_connection(self):
        self.conn.close()

# Inisialisasi tkinter
root = tk.Tk()
app = PrediksiProdiApp(root)

# Jalankan aplikasi
root.mainloop()

# Tutup koneksi database setelah aplikasi selesai
app.close_connection()

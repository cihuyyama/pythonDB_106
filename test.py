import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

label_mata_pelajaran = []
entry_mata_pelajaran = []
mata_pelajaran = ["Matematika", "Fisika", "Kimia", "Biologi", "Bahasa Indonesia", "Bahasa Inggris", "Sejarah", "Geografi", "Ekonomi", "Sosiologi"]
for i in range(len(mata_pelajaran)):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {mata_pelajaran[i]}:")
    label.grid(row=i+1, column=0, padx=10, pady=5, sticky="n")
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    label_mata_pelajaran.append(label)
    entry_mata_pelajaran.append(entry)


hasil_label = tk.Label(root, text="Prodi yang diprediksi: ", font=("Arial", 12))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10, padx=20)

def hasil_prediksi():
    hasil_label.config(text="Prodi yang diprediksi: Teknologi Informasi")

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()

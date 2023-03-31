# # Import the required libraries
# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk

# # Create an instance of tkinter frame
# win= Tk()

# # Set the size of the tkinter window
# win.geometry("700x350")

# # Define a function to show the popup message
# def show_msg():
#    messagebox.showinfo("Message","Hey There! I hope you are doing well.")

# # Add an optional Label widget
# Label(win, text= "Welcome Folks!", font= ('Aerial 17 bold italic')).pack(pady= 30)

# # Create a Button to display the message
# ttk.Button(win, text= "Click Here", command=show_msg).pack(pady= 20)
# win.mainloop()

# liststring = []
# string='1224x6234:2347'
# number = ''
# ops=[]

# for char in string:
#    liststring.append(char)
# liststring.append('')
   
# # print(liststring)

# for num in liststring:
#    per = str(num)
#    if per.isnumeric():
#       number+=num
#       # print (number)
#    else:
#       # print (number)
#       ops.append(number)
#       ops.append(num)
#       number = ''
#    # print (number)

# print(ops)
# print(help(float))
# print(5.0.is_integer())
# print(5.1.is_integer())
# x = 2.6*1000
# y= 2.51*1000
# print(eval('(2.6*1000-2.51*1000)/1000'))
# print(eval('((0.2*100)+(0.1*100))/100'))
# print(eval('(0.2+0.1)'))
# print(eval('(0.21-2)*0.31'))
# print(float(0.1)+float(0.2))

# print((2.0).is_integer())

# Nama : Laila Fiqy Rahayu
# Kelas : XII RPL 4
# Absen : 18

# import library
import tkinter as tk
# import tkinter.messagebox as msg
from tkinter import StringVar, messagebox

# class utama


class Application(tk.Frame):
    # definisi fungsi utama
    def _init_(self, master=None):
        # inisialisasi objek
        super()._init_(master)
        # mengatur ukuran window
        self.master = master
        # mengatur judul window
        self.pack()
        # memanggil fungsi utama
        self.create_widgets()

    # definisi fungsi utama untuk membuat widget
    def create_widgets(self):

        # label untuk menampilkan judul
        self.conversion_label = tk.Label(
            self, text="Nama : Laila Fiqy Rahayu", font=("Courier", 14))
        # menempatkan label ke window
        self.conversion_label.pack(pady=3)

        self.conversion_label = tk.Label(
            self, text="Absen : 18", font=("Courier", 14))
        self.conversion_label.pack(pady=3)

        self.conversion_label = tk.Label(
            self, text="Kelas : XII RPL 4", font=("Courier", 14))
        self.conversion_label.pack(pady=3)

        self.conversion_label = tk.Label(
            self, text="DP1_DP3", font=("Courier", 14))

        # label untuk meminta input dari pengguna
        self.conversion_label.pack(pady=3)
        # label untuk meminta input dari pengguna
        self.conversion_label = tk.Label(
            self, text="Select an Option:", font=("Cambria", 14))
        # menempatkan label ke window
        self.conversion_label.pack(pady=10)

        # dropdown menu untuk memilih jenis konversi
        self.conversion_options = ["String to ASCII", "String to Binary", "String to Decimal", "String to Octal", "String to Hexadecimal", "Decimal to Binary",
                                   "Decimal to Octal", "Decimal to Hexadecimal", "Binary to Decimal", "Binary to Octal", "Binary to Hexadecimal", "Octal to Binary",
                                   "Octal to Decimal", "Octal to Hexadecimal", "Hexadecimal to Binary", "Hexadecimal to Decimal", "Hexadecimal to Octal"]
        # variabel untuk menyimpan pilihan konversi
        self.conversion_var = tk.StringVar(self)
        # mengatur pilihan konversi defult
        self.conversion_var.set(self.conversion_options[0])
        # dropdown menu
        self.conversion_dropdown = tk.OptionMenu(
            self, self.conversion_var, *self.conversion_options)
        # menempatkan dropdown menu ke window
        self.conversion_dropdown.pack()

        # label untuk meminta input dari pengguna
        self.input_label = tk.Label(
            self, text="Input Number or String :", font=("Cambria", 14))
        # menempatkan label ke window
        self.input_label.pack(side="left")

        # entry untuk input dari pengguna
        self.input_entry = tk.Entry(self)
        # menempatkan entry ke window
        self.input_entry.pack(side="left")

        # button untuk memulai konversi
        self.convert_button = tk.Button(
            self, text="Konversi", command=self.convert, font=("Cambria", 14))
        # menempatkan button ke window
        self.convert_button.pack(side="left")

        # label untuk menampilkan hasil konversi
        self.result_label = tk.Label(self, text="", font=("Cambria", 14))
        # menempatkan label ke window
        self.result_label.pack(side="left")

    # definisi fungsi untuk konversi
    def convert(self):
        # mendapatkan nput dari pengguna
        conversion = self.conversion_var.get()
        # mendapatkan input dari pengguna
        input_value = self.input_entry.get()

        # mengecek apakah input kosong
        try:
            # mengecek apakah input berupa angka
            # String to ASCII
            if conversion == "String to ASCII":
                # mengubah string menjadi ascii
                ascii_value = [ord(char) for char in input_value]
                ascii_str = ", ".join(str(char) for char in ascii_value)
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {ascii_str}")

            # String to Binary
            elif conversion == "String to Binary":
                # mengubah string menjadi binary
                binary = ''.join(format(ord(char), '08b')
                                 for char in input_value)
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {binary}")

            # String to Decimal
            elif conversion == "String to Decimal":
                # mengubah string menjadi decimal
                decimal = ''.join(str(ord(c)) for c in input_value)
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {decimal}")

            # String to Octal
            elif conversion == "String to Octal":
                # mengubah string menjadi octal
                octal = ''.join(format(ord(char), 'o') for char in input_value)
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {octal}")

            # String to Hexadecimal
            elif conversion == "String to Hexadecimal":
                # mengubah string menjadi hexadecimal
                hexa = ''.join(format(ord(char), '02X')
                               for char in input_value)
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {hexa}")

            # Decimal to Binary
            elif conversion == "Decimal to Binary":
                # menjadikan input menjadi integer
                decimal = int(input_value)
                # mengubah decimal menjadi binary
                binary = bin(decimal)[2:]
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {binary}")

            # Decimal to Octal
            elif conversion == "Decimal to Octal":
                # menjadikan input menjadi integer
                decimal = int(input_value)
                # mengubah decimal menjadi octal
                octal = oct(decimal)[2:]
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {octal}")

            # Decimal to Hexadecimal
            elif conversion == "Decimal to Hexadecimal":
                # menjadikan input menjadi int
                decimal = int(input_value)
                # mengubah decimal menjadi hexadecimal
                hexa = hex(decimal)[2:].upper()
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {hexa}")

            # Binary to Decimal
            elif conversion == "Binary to Decimal":
                # menjadikan input menjadi int
                decimal = int(input_value, 2)
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {decimal}")

            # Binary to Octal
            elif conversion == "Binary to Octal":
                # menjadikan input menjadi int
                decimal = int(input_value, 2)
                # mengubah decimal menjadi octal
                octal = oct(decimal)[2:]
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {octal}")

            # Binary to Hexadecimal
            elif conversion == "Binary to Hexadecimal":
                # menjadikan input menjadi int
                decimal = int(input_value, 2)
                # mengubah decimal menjadi hexadecimal
                hexa = hex(decimal)[2:].upper()
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {hexa}")

            # Octal to Binary
            elif conversion == "Octal to Binary":
                # menjadikan input menjadi int
                decimal = int(input_value, 8)
                # mengubah decimal menjadi binary
                binary = bin(decimal)[2:]
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {binary}")

            # Octal to Decimal
            # penggunaan elif untuk mengecek apakah input berupa angka
            elif conversion == "Octal to Decimal":
                # menjadikan input berupa int
                decimal = int(input_value, 8)
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {decimal}")

            # Octal to Hexadecimal
            # penggunaa elif untuk mengecek apakah input berupa angka
            elif conversion == "Octal to Hexadecimal":
                # menjadikan input menjadi int
                decimal = int(input_value, 8)
                # mengubah decimalmenjadi hexadecimal
                hexa = hex(decimal)[2:].upper()
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {hexa}")

            # Hexadecimal to Binary
            elif conversion == "Hexadecimal to Binary":
                # menjadikan input menajdi int
                decimal = int(input_value, 16)
                # mengubah decimal menjadi binary
                binary = bin(decimal)[2:]
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {binary}")

            # Hexadecimal to Decimal
            elif conversion == "Hexadecimal to Decimal":
                # menjadikan input menjadi int
                decimal = int(input_value, 16)
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {decimal}")

            # Hexadecimal to Octal
            elif conversion == "Hexadecimal to Octal":
                # menjadikan input menjadi int
                decimal = int(input_value, 16)
                # mengubah decimal menjadi octal
                octal = oct(decimal)[2:]
                # menampilkan hasil konversi
                self.result_label.configure(text=f"Hasil: {octal}")

        # menampilkan pesan error jika input tidak valid
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")


    # main program
root = tk.Tk()

# set window title
root.title("String Converter By Laila Fiqy")

# set window size and position
root.geometry("800x500+200+80")

#  set window icon
app = Application(master=root)

# tk.Label(text="Nama : Laila Fiqy Rahayu", font=("Courier", 14)).pack(pady=3)

# run the mainloop
app.mainloop()
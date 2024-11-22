import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class HotelReservationApp:
    max_booking = 3

    def __init__(self, root):
        self.root = root
        self.root.title("Hotelkeren.com")
        self.users = {} 
        self.bookings = []  
        self.hotels = [
            {"name": "Hotel Yoyo", "image": r"C:\Users\khies\booking hotel\hotelyoyo.jpg", "rooms": [
                {"type": "Standard Room", "price": 450000, "image": r"C:\Users\khies\booking hotel\room_standard_a.jpg", "booked_count": 0},
                {"type": "Deluxe Room", "price": 850000, "image": r"C:\Users\khies\booking hotel\room_deluxe_a.jpg", "booked_count": 0},
            ]},
            {"name": "Hotel PintuMerah", "image": r"C:\Users\khies\booking hotel\hotel_pintumerah.jpg", "rooms": [
                {"type": "Standard Room", "price": 700000, "image": r"C:\Users\khies\booking hotel\room_standard_b.jpg", "booked_count": 0},
                {"type": "Deluxe Room", "price": 875000, "image": r"C:\Users\khies\booking hotel\room_deluxe_b.jpg", "booked_count": 0},
            ]},
            {"name": "Hotel Whitehouse", "image": r"C:\Users\khies\booking hotel\hotel_Yaudah.jpg", "rooms": [
                {"type": "Standard Room", "price": 1000000, "image": r"C:\Users\khies\booking hotel\room_standard_c.jpg", "booked_count": 0},
                {"type": "Deluxe Room", "price": 1500000, "image": r"C:\Users\khies\booking hotel\room_deluxe_c.jpg", "booked_count": 0},
            ]}
        ]
        self.create_login_page()

    def clear_frame(self):
        """Menghapus semua widget di frame utama."""
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- LOGIN & REGISTER ---

    def create_login_page(self):
        """Halaman login sebelum mengakses aplikasi pemesanan."""
        self.clear_frame()
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)

        tk.Label(self.login_frame, text="Login", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.login_frame, text="Username:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.login_frame, text="Password:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=3, column=0, columnspan=2, pady=20)
        tk.Button(self.login_frame, text="Register", command=self.create_register_page).grid(row=4, column=0, columnspan=2, pady=10)

    def create_register_page(self):
        """Halaman registrasi untuk pengguna baru."""
        self.clear_frame()
        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack(padx=20, pady=20)

        tk.Label(self.register_frame, text="Register", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.register_frame, text="Username:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_register_username = tk.Entry(self.register_frame)
        self.entry_register_username.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.register_frame, text="Password:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_register_password = tk.Entry(self.register_frame, show="*")
        self.entry_register_password.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.register_frame, text="Submit", command=self.register).grid(row=3, column=0, columnspan=2, pady=20)
        tk.Button(self.register_frame, text="Kembali ke Login", command=self.create_login_page).grid(row=4, column=0, columnspan=2, pady=10)

    def register(self):
        """Logika registrasi pengguna baru."""
        username = self.entry_register_username.get()
        password = self.entry_register_password.get()

        if not username or not password:
            messagebox.showerror("Error", "Username dan password tidak boleh kosong.")
            return

        if username in self.users:
            messagebox.showerror("Error", "Username sudah terdaftar.")
            return

        self.users[username] = password
        messagebox.showinfo("Berhasil", "Registrasi berhasil! Silakan login.")
        self.create_login_page()

    def login(self):
        """Proses login untuk memverifikasi pengguna."""
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
            self.create_main_page()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

    # --- MAIN PAGE ---

    def create_main_page(self):
        """Membuat halaman utama untuk reservasi hotel."""
        self.clear_frame()
        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=10)

        tk.Label(main_frame, text="Nama Lengkap Pemesan:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.entry_name = tk.Entry(main_frame)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(main_frame, text="Pilih Hotel:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.hotel_var = tk.IntVar(value=-1)
        for idx, hotel in enumerate(self.hotels):
            tk.Radiobutton(main_frame, text=hotel["name"], variable=self.hotel_var, value=idx,
                           command=self.update_rooms).grid(row=1, column=idx + 1, padx=10, pady=5)

        self.label_hotel_image = tk.Label(main_frame)
        self.label_hotel_image.grid(row=2, column=0, columnspan=4, pady=10)  # Gambar hotel diposisikan di sini

        tk.Label(main_frame, text="Pilih Tipe Kamar:", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.room_var = tk.IntVar(value=-1)
        self.frame_rooms = tk.Frame(main_frame)
        self.frame_rooms.grid(row=3, column=1, columnspan=3, padx=10, pady=5)

        self.label_room_image = tk.Label(main_frame)
        self.label_room_image.grid(row=4, column=0, columnspan=4, pady=10)  # Gambar kamar diposisikan di sini

        tk.Label(main_frame, text="Jumlah Malam:", font=("Arial", 12)).grid(row=5, column=0, sticky="e", padx=10, pady=5)
        self.entry_nights = tk.Entry(main_frame)
        self.entry_nights.grid(row=5, column=1, padx=10, pady=5)

        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=4, pady=10)

        tk.Button(button_frame, text="Reservasi", command=self.reserve).pack(side="left", padx=10)
        tk.Button(button_frame, text="Cek Pemesanan", command=self.create_booking_page).pack(side="left", padx=10)

    def update_rooms(self):
        """Update tipe kamar yang tersedia berdasarkan pilihan hotel."""
        selected_hotel = self.hotel_var.get()
        if selected_hotel == -1:
            return

        hotel = self.hotels[selected_hotel]
        self.room_var.set(-1)
        self.frame_rooms.destroy()
        self.frame_rooms = tk.Frame(self.root)
        self.frame_rooms.grid(row=3, column=1, columnspan=3, padx=10, pady=5)

        for idx, room in enumerate(hotel["rooms"]):
            tk.Radiobutton(self.frame_rooms, text=f"{room['type']} - Rp {room['price']}", variable=self.room_var,
                           value=idx, command=self.update_room_image).grid(row=idx, column=0, padx=10, pady=5)

    def update_room_image(self):
        """Update gambar kamar berdasarkan tipe kamar yang dipilih."""
        selected_hotel = self.hotel_var.get()
        selected_room = self.room_var.get()
        if selected_hotel == -1 or selected_room == -1:
            return

        hotel = self.hotels[selected_hotel]
        room = hotel["rooms"][selected_room]

        img = Image.open(room["image"])
        img = img.resize((200, 200))  # Resize image
        self.room_image = ImageTk.PhotoImage(img)
        self.label_room_image.config(image=self.room_image)

    def reserve(self):
        """Proses reservasi berdasarkan input."""
        name = self.entry_name.get()
        nights = self.entry_nights.get()
        selected_hotel = self.hotel_var.get()
        selected_room = self.room_var.get()

        if not name or not nights.isdigit() or selected_hotel == -1 or selected_room == -1:
            messagebox.showerror("Error", "Semua field harus diisi dengan benar.")
            return

        if len(self.bookings) >= self.max_booking:
            messagebox.showerror("Batas Pemesanan", "Batas pemesanan telah tercapai.")
            return

        hotel = self.hotels[selected_hotel]
        room = hotel["rooms"][selected_room]

        if room["booked_count"] >= 3:
            messagebox.showerror("Kamar Penuh", f"{room['type']} sudah penuh.")
            return

        self.bookings.append({
            "name": name,
            "hotel": hotel["name"],
            "room": room["type"],
            "nights": int(nights),
            "price": room["price"] * int(nights)
        })

        room["booked_count"] += 1
        messagebox.showinfo("Pemesanan Berhasil", f"Pemesanannya berhasil! Total pembayaran: Rp {room['price'] * int(nights)}")
        self.create_main_page()

    def create_booking_page(self):
        """Halaman untuk melihat pemesanan yang sudah dilakukan."""
        self.clear_frame()
        booking_frame = tk.Frame(self.root)
        booking_frame.pack(pady=20)

        tk.Label(booking_frame, text="Daftar Pemesanan", font=("Arial", 16)).grid(row=0, column=0, pady=10)

        if not self.bookings:
            tk.Label(booking_frame, text="Tidak ada pemesanan.", font=("Arial", 12)).grid(row=1, column=0, pady=10)
        else:
            for idx, booking in enumerate(self.bookings):
                tk.Label(booking_frame, text=f"{idx + 1}. {booking['name']} - {booking['hotel']} - {booking['room']} - {booking['nights']} malam - Rp {booking['price']}").grid(row=idx + 1, column=0, pady=5)

        tk.Button(booking_frame, text="Kembali", command=self.create_main_page).grid(row=len(self.bookings) + 1, column=0, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = HotelReservationApp(root)
    root.mainloop()

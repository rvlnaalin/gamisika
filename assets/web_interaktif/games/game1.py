import pygame  # Mengimpor modul pygame untuk membuat game
import sys  # Mengimpor modul sys untuk mengakses sistem
import random  # Mengimpor modul random untuk menghasilkan angka acak

# Inisialisasi Pygame
pygame.init()  # Memula66i semua modul Pygame yang dibutuhkan

# Set ukuran layar
layar = pygame.display.set_mode((800, 600))  # Menetapkan ukuran layar 800x600 piksel
pygame.display.set_caption("Menu Game")  # Menambahkan judul "Menu Game" ke jendela

# Warna
PUTIH = (255, 255, 255)  # Warna putih dalam format RGB
HITAM = (0, 0, 0)        # Warna hitam dalam format RGB
BIRU = (0, 0, 255)       # Warna biru dalam format RGB
MERAH = (255, 0, 0)      # Warna merah dalam format RGB
KUNING = (255, 255, 0)   # Warna biru dalam format RGB

# Font
font = pygame.font.Font(None, 74)           # Mengatur font utama dengan ukuran 74
font_input = pygame.font.Font(None, 50)     # Mengatur font untuk input nama dengan ukuran 50
font_judul = pygame.font.Font(None, 75)    # Mengatur font untuk judul dengan ukuran 100
font_pop_up = pygame.font.Font(None, 50)    # Mengatur font untuk pop-up dengan ukuran 50
font_materi = pygame.font.Font(None, 20)    # Mengatur font untuk materi dengan ukuran 20
font_normal = pygame.font.Font(None, 40)
font_title = pygame.font.Font(None, 30)

# Status game (menu utama, input nama, dan mode game)
STATUS_MENU = 'menu'  # Status untuk menu utama
STATUS_INPUT_NAMA_MODE = 'input_nama_mode'  # Status untuk input nama dan mode game
STATUS_GAME_OVER = 'game_over'  # Status untuk game over
STATUS_MATERI = 'materi'  # Status untuk materi
STATUS_LATIHAN = 'latihan'
status_game = STATUS_MENU  # Mengatur status game awal ke menu

# Status baru untuk materi
STATUS_MATERI_HAL1 = 'materi_halaman_1'  # Status untuk halaman materi 1
STATUS_MATERI_HAL2 = 'materi_halaman_2'  # Status untuk halaman materi 2
STATUS_MATERI_HAL3 = 'materi_halaman_3'  # Status untuk halaman materi 3
STATUS_MATERI_HAL4 = 'materi_halaman_4'  # Status untuk halaman materi 4
STATUS_MATERI_HAL5 = 'materi_halaman_5'  # Status untuk halaman materi 1
STATUS_MATERI_HAL6 = 'materi_halaman_6'  # Status untuk halaman materi 2
STATUS_MATERI_HAL7 = 'materi_halaman_7'  # Status untuk halaman materi 3
STATUS_MATERI_HAL8 = 'materi_halaman_8'  # Status untuk halaman materi 4
STATUS_MATERI_HAL9 = 'materi_halaman_9'  # Status untuk halaman materi 1
STATUS_MATERI_HAL10 = 'materi_halaman_10'  # Status untuk halaman materi 2

# Opsi Menu
opsi_menu = ['Mulai Game', 'Keluar', 'Pembahasan', 'Latihan']  # Daftar opsi di menu utama
opsi_terpilih = 0  # Opsi menu yang dipilih, dimulai dari 0

# Input nama
input_nama = ''  # Variabel untuk menyimpan nama input dari pengguna
maks_input = 10   # Maksimal karakter input nama yang diperbolehkan

# Opsi mode game yang diperbarui
opsi_mode = ['Besaran Fisika', 'Alat Ukur', 'Dimensi', '  Pokok  ', 'Turunan', 'Tokoh Fisika']  # Daftar mode game yang bisa dipilih
opsi_mode_terpilih = 0  # Mode yang dipilih, dimulai dari 0

# Variabel untuk halaman materi
halaman_materi = 0  # Halaman pertama dimulai dari 0
jumlah_halaman_materi = 10  # Total ada 4 halaman

# Posisi untuk setiap mode game
posisi_mode = {
    'Besaran Fisika' : (300, 330),
    '  Pokok  '      : (260, 390),
    'Turunan'        : (428, 390),
    'Alat Ukur'      : (247, 450),
    'Dimensi'        : (430, 450),
    'Tokoh Fisika'   : (317, 230)
}

# Posisi untuk setiap opsi menu
posisi_menu = {
    'Mulai Game': (300, 280),      # Koordinat untuk opsi 'Mulai Game'
    'Keluar': (340, 350),          # Koordinat untuk opsi 'Keluar'
    'Pembahasan': (390, 460),   # Koordinat untuk opsi 'Belajar Materi'
    'Latihan': (195, 460)
}

# Posisi untuk judul
posisi_judul = (400, 100)  # Koordinat untuk judul di layar

# Fungsi untuk menggambar menu utama
def gambar_menu(terpilih):
    layar.fill(PUTIH)  # Mengisi layar dengan warna putih

    # Gambar judul di atas menu
    judul = font_judul.render("DROP DOWN FISIKA", True, HITAM)  # Render teks judul
    layar.blit(judul, (posisi_judul[0] - judul.get_width() // 2, posisi_judul[1]))  # Menampilkan judul di tengah
    judul = font_pop_up.render("Ayo Kita Belajar Fisika Sambil Bermain!", True, HITAM)  # Render teks judul
    layar.blit(judul, (400 - judul.get_width() // 2, 170))  # Menampilkan judul di tengah
    judul = font_normal.render("Tantang Dirimu Setelah Bermain!", True, MERAH)  # Render teks judul
    layar.blit(judul, (400 - judul.get_width() // 2, 410))  # Menampilkan judul di tengah

    # Menggambar setiap opsi menu
    for i, opsi in enumerate(opsi_menu):  # Mengulangi setiap opsi menu
        label = font_input.render(opsi, True, HITAM)  # Render teks untuk setiap opsi menu
        lebar, tinggi = label.get_size()  # Mendapatkan ukuran teks
        x, y = posisi_menu[opsi]  # Mendapatkan posisi dari opsi menu

        # Buat kotak untuk setiap opsi
        kotak_rect = pygame.Rect(x - 20, y - 10, lebar + 40, tinggi + 20)  # Membuat kotak dengan margin di sekitar teks
        pygame.draw.rect(layar, HITAM if i == terpilih else HITAM, kotak_rect, 5)  # Menggambar kotak dengan warna biru jika dipilih

        # Tampilkan teks menu
        layar.blit(label, (x, y))  # Menampilkan teks opsi menu di atas kotak

# Fungsi untuk menggambar input nama dan pilihan mode
def gambar_input_nama_mode(input_nama, terpilih):
    layar.fill(PUTIH)  # Mengisi layar dengan warna putih
    
    # Tampilkan input nama di tengah atas layar
    label = font_input.render("Input Nama:", True, HITAM)  # Render teks "Input Nama"
    layar.blit(label, (400 - label.get_width() // 2, 30))  # Menampilkan teks di layar

    # Kotak input untuk nama
    kotak_input = pygame.Rect(400 - 150, 72, 300, 50)  # Membuat kotak input untuk nama
    pygame.draw.rect(layar, HITAM, kotak_input, 2)  # Menggambar kotak input dengan warna hitam

    # Tampilkan nama yang sudah diinput
    nama_teks = font_input.render(input_nama, True, HITAM)  # Render teks nama yang diinput
    layar.blit(nama_teks, (kotak_input.x + 10, kotak_input.y + 10))  # Tampilkan teks nama di dalam kotak input

    # Tampilkan pilihan mode game di tengah
    label_mode = font_pop_up.render("Pilih Mode Game:", True, HITAM)  # Render teks "Pilih Mode Game"
    layar.blit(label_mode, (400 - label_mode.get_width() // 2, 140))  # Menampilkan teks di layar
    label_mode = font_normal.render("Fisika Kelas 10", True, MERAH)  # Render teks "Pilih Mode Game"
    layar.blit(label_mode, (400 - label_mode.get_width() // 2, 285))  # Menampilkan teks di layar
    label_mode = font_normal.render("Ayo Pemanasan!", True, HITAM)  # Render teks "Pilih Mode Game"
    layar.blit(label_mode, (400 - label_mode.get_width() // 2, 185))  # Menampilkan teks di layar

    # Menggambar kotak untuk setiap mode game
    for i, mode in enumerate(opsi_mode):  # Mengulangi setiap opsi mode
        x, y = posisi_mode[mode]  # Mendapatkan posisi dari mode game
        label_mode_option = font_normal.render(mode, True, HITAM)  # Render teks untuk setiap mode
        lebar, tinggi = label_mode_option.get_size()  # Mendapatkan ukuran teks
        
        # Kotak untuk setiap opsi mode game
        kotak_rect = pygame.Rect(x - 20, y - 10, lebar + 40, tinggi + 20)  # Membuat kotak untuk mode game
        pygame.draw.rect(layar, HITAM if i == terpilih else HITAM, kotak_rect, 5)  # Menggambar kotak dengan warna biru jika terpilih
        layar.blit(label_mode_option, (x, y))  # Menampilkan teks mode game di atas kotak

    # Tombol Kembali
    button_rect = pygame.Rect(250, 510, 300, 50)  # Posisi tombol kembali
    pygame.draw.rect(layar, HITAM, button_rect, 2)  # Menggambar tombol kembali dengan warna hitam
    button_label = font_input.render("Kembali ke Menu", True, HITAM)  # Render teks "Kembali ke Menu"
    layar.blit(button_label, (button_rect.x + (button_rect.width - button_label.get_width()) // 2, 
                               button_rect.y + (button_rect.height - button_label.get_height()) // 2))  # Tampilkan teks di tombol

# Fungsi untuk menggambar materi
def gambar_materi():
    global halaman_materi

    layar.fill(PUTIH)

    # Tampilkan judul materi
    label_judul = font_normal.render("Materi Fisika", True, HITAM)
    layar.blit(label_judul, (400 - label_judul.get_width() // 2, 27))

    # Tentukan materi berdasarkan halaman
    if halaman_materi == 0:
        materi_text = [
        "Pengertian Besaran Pokok:", 
        "Besaran pokok adalah besaran fisika yang tidak dapat diturunkan dari besaran lain dan menjadi dasar pengukuran", 
        "Fungsi Besaran Pokok:", 
        "1. Dasar untuk mengukur besaran turunan", 
        "2. Menyediakan standar pengukuran yang konsisten", 
        "3. Memudahkan komunikasi ilmiah", 

        "Macam-Macam Besaran Pokok:", 
        "1. Panjang: meter (m)", 
        "2. Massa: kilogram (kg)", 
        "3. Waktu: detik (s)", 
        "4. Arus listrik: ampere (A)", 
        "5. Suhu: kelvin (K)", 
        "6. Jumlah zat: mol (mol)", 
        "7. Intensitas cahaya: candela (cd)", 
        ]
        
    elif halaman_materi == 1:
        materi_text = [
        "Pengertian Besaran Satuan:", 
        "Besaran satuan adalah besaran fisika yang dihasilkan dari kombinasi satu atau lebih besaran pokok", 

        "Fungsi Besaran Satuan:", 
        "1. Mendeskripsikan fenomena fisika", 
        "2. Memudahkan pengukuran dan perhitungan", 
        "3. Menganalisis hukum-hukum fisika", 

        "Macam-Macam Besaran Satuan:", 
        "1. Kecepatan (v):", 
        "   - Satuan: meter per detik (m/s)", 
        "   - Rumus: v = s / t", 

        "2. Percepatan (a):", 
        "   - Satuan: meter per detik kuadrat (m/s²)", 
        "   - Rumus: a = (vf - vi) / t", 
        ]

    elif halaman_materi == 2:
        materi_text = [
        "3. Gaya (F):", 
        "   - Satuan: newton (N)", 
        "   - Rumus: F = m × a", 

        "4. Energi (E):", 
        "   - Satuan: joule (J)", 
        "   - Rumus: E = F × d", 

        "5. Daya (P):", 
        "   - Satuan: watt (W)", 
        "   - Rumus: P = E / t", 

        "6. Tekanan (P):", 
        "   - Satuan: pascal (Pa)", 
        "   - Rumus: P = F / A", 

        "7. Volume (V):", 
        "   - Satuan: meter kubik (m³)", 
        "   - Rumus: V = I × w × h"
        ]

    elif halaman_materi == 3:
        materi_text = [
        "Pengertian Dimensi Besaran Pokok:", 
        "Dimensi besaran pokok adalah cara menggambarkan besaran fisika seperti panjang, massa, dan waktu","dalam bentuk simbol untuk menunjukkan sifat fisiknya", 

        "Fungsi Dimensi Besaran Pokok:", 
        "1. Memverifikasi persamaan fisika", 
        "2. Menghubungkan besaran fisika", 
        "3. Mempermudah analisis persamaan", 

        "Macam-Macam Dimensi Besaran Pokok:", 
        "1. Panjang: [L]", 
        "2. Massa: [M]", 
        "3. Waktu: [T]", 
        "4. Jarak: [L]", 

        "Pengertian Dimensi Besaran Turunan:", 
        "Dimensi besaran turunan diperoleh dari kombinasi dimensi besaran pokok, seperti kecepatan, gaya, dan energi", 
        ]

    elif halaman_materi == 4:
        materi_text = [
        "Fungsi Dimensi Besaran Turunan:", 
        "1. Memverifikasi persamaan fisika", 
        "2. Menjelaskan hubungan besaran pokok dan turunan", 
        "3. Mempermudah analisis fisika", 

        "Macam-Macam Dimensi Besaran Turunan:", 
        "1. Luas: [L]²", 
        "2. Volume: [L]³", 
        "3. Kecepatan: [L][T]⁻¹", 
        "4. Percepatan: [L][T]⁻²"
        ]

    elif halaman_materi == 5:
        materi_text = [
        "Pengertian GLB:", 
        "Gerak Lurus Beraturan (GLB) adalah gerak benda dalam lintasan lurus dengan kecepatan tetap tanpa percepatan", 

        "Fungsi GLB:", 
        "1. Menggambarkan gerak benda berkecepatan tetap", 
        "2. Memudahkan perhitungan jarak, waktu, dan kecepatan", 
        "3. Sebagai model dasar mempelajari gerak", 

        "Macam-Macam GLB:", 
        "1. Kecepatan Konstan (tanpa titik mula): s = v ⋅ t", 
        "2. Jarak dan Waktu (dengan titik mula): s = s0 + v ⋅ t", 

        "Pengertian GLBB:", 
        "Gerak Lurus Berubah Beraturan (GLBB) adalah gerak benda dalam lintasan lurus dengan percepatan tetap,","di mana kecepatan benda berubah secara teratur", 
        ]

    elif halaman_materi == 6:
        materi_text = [
        "Fungsi GLBB:", 
        "1. Mendeskripsikan gerakan benda yang mengalami percepatan", 
        "2. Memudahkan perhitungan jarak, waktu, dan kecepatan", 
        "3. Sebagai model dalam aplikasi teknik dan ilmu fisika", 

        "Macam-Macam GLBB:", 
        "1. Kecepatan akhir: v𝑡 = a ⋅ t + v", 
        "2. Jarak: s = v0 ⋅ t + 1/2 a ⋅ t²", 
        "3. Gabungan: vt² = 2 ⋅ a ⋅ s + v0²"
        ]
    elif halaman_materi == 7:
        materi_text = ["Ditunggu ya materi selanjutnya, STAY TUNE!"]
    elif halaman_materi == 8:
        materi_text = ["Ditunggu ya materi selanjutnya, STAY TUNE!"]
    elif halaman_materi == 9:
        materi_text = ["Ditunggu ya materi selanjutnya, STAY TUNE!"]

    # Tampilkan materi
    y_offset = 75
    for line in materi_text:
        label = font_materi.render(line, True, HITAM)
        layar.blit(label, (30, y_offset))
        y_offset += 30  # Jarak antar baris

    # Tombol Kembali
    button_back_rect = pygame.Rect(250, 500, 300, 50)
    pygame.draw.rect(layar, HITAM, button_back_rect, 2)
    button_label = font_input.render("Kembali ke Menu", True, HITAM)
    layar.blit(button_label, (button_back_rect.x + (button_back_rect.width - button_label.get_width()) // 2, 
                               button_back_rect.y + (button_back_rect.height - button_label.get_height()) // 2))

    # Ukuran tombol Previous dan Next
    lebar_tombol = 70  # Atur ukuran lebar tombol
    tinggi_tombol = 40  # Atur ukuran tinggi tombol
    
    # Posisi dan ukuran tombol Next dan Previous
    button_next_rect = pygame.Rect(690, 550, lebar_tombol, tinggi_tombol)
    button_prev_rect = pygame.Rect(50, 550, lebar_tombol, tinggi_tombol)
    
    pygame.draw.rect(layar, PUTIH, button_next_rect)
    pygame.draw.rect(layar, HITAM, button_next_rect, 2)
    pygame.draw.rect(layar, PUTIH, button_prev_rect)
    pygame.draw.rect(layar, HITAM, button_prev_rect, 2)
    
    label_next = font_materi.render("Next", True, HITAM)
    label_prev = font_materi.render("Previous", True, HITAM)
    
    layar.blit(label_next, (button_next_rect.x + (lebar_tombol - label_next.get_width()) // 2, 
                            button_next_rect.y + (tinggi_tombol - label_next.get_height()) // 2))
    layar.blit(label_prev, (button_prev_rect.x + (lebar_tombol - label_prev.get_width()) // 2, 
                            button_prev_rect.y + (tinggi_tombol - label_prev.get_height()) // 2))
    
    pygame.display.flip()

    # Handle events for button clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button_back_rect.collidepoint(event.pos):
                    return 'menu'  # Kembali ke menu utama
                elif button_next_rect.collidepoint(event.pos):
                    if halaman_materi < jumlah_halaman_materi - 1:  # Cek jika halaman belum maksimal
                        halaman_materi += 1
                elif button_prev_rect.collidepoint(event.pos):
                    if halaman_materi > 0:  # Cek jika halaman belum minimal
                        halaman_materi -= 1

    return STATUS_MENU  # Tetap di status materi

def gambar_latihan():
    # Ukuran layar game
    SCREEN_WIDTH = 800  # Lebar layar
    SCREEN_HEIGHT = 600  # Tinggi layar

    layar.fill(PUTIH)

    # Menambahkan input nama pengguna sebelum soal dimulai
    kotak_nama_rect = pygame.Rect(100, 300, 600, 40)
    pygame.draw.rect(layar, HITAM, kotak_nama_rect, 2)
    
    # Tombol kembali ke menu
    button_back_rect = pygame.Rect(50, 50, 150, 40)
    pygame.draw.rect(layar, HITAM, button_back_rect, 2)
    button_label = font_normal.render("Kembali", True, HITAM)
    layar.blit(button_label, (button_back_rect.x + (button_back_rect.width - button_label.get_width()) // 2,
                              button_back_rect.y + (button_back_rect.height - button_label.get_height()) // 2))

    nama_pengguna = ''
    x_instruksi, y_instruksi = 100, 150
    nama_valid = False
    while not nama_valid:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_back_rect.collidepoint(mouse_x, mouse_y):  # Jika tombol kembali diklik
                    return 'menu'  # Kembali ke menu utama
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and nama_pengguna != '':  # Cek jika Enter ditekan
                    nama_valid = True
                elif event.key == pygame.K_BACKSPACE:
                    nama_pengguna = nama_pengguna[:-1]
                else:
                    nama_pengguna += event.unicode

        layar.fill(PUTIH)  # Mengisi layar dengan warna putih
        
        instruksi_nama_text = font_normal.render('Masukkan nama anda:', True, HITAM)
        layar.blit(instruksi_nama_text, (250, 250))  # Menampilkan instruksi pada posisi yang bisa dipindah
        instruksi_nama_text = font_normal.render('Kerjakan dengan Jujur!', True, HITAM)
        layar.blit(instruksi_nama_text, (240, 370))  # Menampilkan instruksi pada posisi yang bisa dipindah
        instruksi_nama_text = font_normal.render('Tekan Enter', True, HITAM)
        layar.blit(instruksi_nama_text, (320, 440))  # Menampilkan instruksi pada posisi yang bisa dipindah
        
        pygame.draw.rect(layar, HITAM, kotak_nama_rect, 2)  # Menggambar kotak untuk input nama
        
        nama_text = font_normal.render(nama_pengguna, True, HITAM)
        layar.blit(nama_text, (kotak_nama_rect.x + 10, kotak_nama_rect.y + 10))  # Menampilkan nama yang sedang diketik
        
        pygame.display.update()
        x_instruksi += 1  # Menambah posisi x untuk membuat instruksi bergerak ke kanan
        if x_instruksi > SCREEN_WIDTH:
            x_instruksi = 100
        pygame.time.delay(20)  # Memberikan delay untuk gerakan yang lebih halus

    soal_list = [
        {
            'soal': 'Apa itu Besaran Fisika?',
            'pilihan': ['A. Sesuatu yang dapat diukur', 'B. Hanya bisa dilihat', 'C. Hanya ada di laboratorium', 'D. Tidak ada hubungan dengan fisika'],
            'jawaban': 'A'
        },
        {
            'soal': 'Apa satuan dari Kecepatan?',
            'pilihan': ['A. Meter', 'B. Meter per detik', 'C. Kilogram', 'D. Newton'],
            'jawaban': 'B'
        },
        {
            'soal': 'Hukum Newton yang pertama adalah?',
            'pilihan': ['A. Hukum gravitasi', 'B. Hukum aksi-reaksi', 'C. Hukum kelembaman', 'D. Hukum gerak'],
            'jawaban': 'C'
        }
    ]

    skor = 0
    
    for soal in soal_list:
        layar.fill(PUTIH)  # Mengisi layar dengan warna putih
        kotak_soal_rect = pygame.Rect(100, 100, 600, 100)
        pygame.draw.rect(layar, HITAM, kotak_soal_rect, 2)
        soal_text = font_normal.render(soal['soal'], True, HITAM)
        layar.blit(soal_text, (kotak_soal_rect.x + 10, kotak_soal_rect.y + 10))

        pilihan_rect = pygame.Rect(100, 250, 600, 180)
        pygame.draw.rect(layar, HITAM, pilihan_rect, 2)
        for i, pilihan in enumerate(soal['pilihan']):
            pilihan_text = font_normal.render(pilihan, True, HITAM)
            layar.blit(pilihan_text, (pilihan_rect.x + 10, pilihan_rect.y + 10 + i * 40))

        instruksi_text = font_normal.render('Masukkan jawaban (A/B/C/D) dan tekan Enter:', True, HITAM)
        layar.blit(instruksi_text, (100, 450))

        kotak_input_rect = pygame.Rect(100, 500, 200, 40)
        pygame.draw.rect(layar, HITAM, kotak_input_rect, 2)
        pygame.display.update()

        jawaban_pengguna = ''
        jawaban_valid = False

        while not jawaban_valid:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        jawaban_pengguna = 'A'
                    elif event.key == pygame.K_b:
                        jawaban_pengguna = 'B'
                    elif event.key == pygame.K_c:
                        jawaban_pengguna = 'C'
                    elif event.key == pygame.K_d:
                        jawaban_pengguna = 'D'
                    elif event.key == pygame.K_RETURN and jawaban_pengguna != '':
                        jawaban_valid = True

            layar.fill(PUTIH)
            layar.blit(soal_text, (kotak_soal_rect.x + 10, kotak_soal_rect.y + 10))
            for i, pilihan in enumerate(soal['pilihan']):
                pilihan_text = font_normal.render(pilihan, True, HITAM)
                layar.blit(pilihan_text, (pilihan_rect.x + 10, pilihan_rect.y + 10 + i * 40))
            layar.blit(instruksi_text, (100, 450))
            pygame.draw.rect(layar, HITAM, kotak_input_rect, 2)
            jawaban_text = font_normal.render(jawaban_pengguna, True, HITAM)
            layar.blit(jawaban_text, (kotak_input_rect.x + 10, kotak_input_rect.y + 10))
            pygame.display.update()

        if jawaban_pengguna == soal['jawaban']:
            skor += 1

        skor_text = font.render(f'Skor: {skor}', True, HITAM)
        layar.blit(skor_text, (350, 500))
        pygame.display.update()
        
        pygame.time.wait(1000)

    # Menampilkan hasil akhir dengan teks rapih di tengah layar
    layar.fill(PUTIH)
    
    # Teks Nama Pengguna dan Skor
    hasil_text = font_normal.render(f'{nama_pengguna}, Latihan selesai! Skor akhir: {skor}', True, HITAM)
    hasil_rect = hasil_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))  # Menyelaraskan teks ke tengah
    layar.blit(hasil_text, hasil_rect)

    # Teks Quote Fisika
    quote_text = font_normal.render('"Fisika adalah seni untuk memahami alam semesta."', True, HITAM)
    quote_rect = quote_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Menyelaraskan teks ke tengah
    layar.blit(quote_text, quote_rect)

    # Tombol Kembali
    button_back_rect = pygame.Rect(250, 500, 300, 50)
    pygame.draw.rect(layar, HITAM, button_back_rect, 2)
    button_label = font_input.render("Kembali ke Menu", True, HITAM)
    layar.blit(button_label, (button_back_rect.x + (button_back_rect.width - button_label.get_width()) // 2, 
                               button_back_rect.y + (button_back_rect.height - button_label.get_height()) // 2))

    pygame.display.update()  # Memperbarui tampilan layar

    kembali = False
    while not kembali:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Deteksi klik mouse
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_back_rect.collidepoint(mouse_x, mouse_y):  # Jika klik pada tombol
                    kembali = True

    return 'menu'  # Mengembalikan ke menu utama setelah klik tombol kembali

# Fungsi untuk menampilkan pop-up game over
def show_game_over_popup(nama, score):
    layar.fill(PUTIH)  # Membersihkan layar dengan warna putih
    
    # Kotak pop-up
    pop_up_rect = pygame.Rect(150, 150, 500, 300)  # Posisi dan ukuran kotak pop-up
    pygame.draw.rect(layar, PUTIH, pop_up_rect)  # Menggambar kotak pop-up
    pygame.draw.rect(layar, HITAM, pop_up_rect, 5)  # Menggambar kontur kotak

    # Teks dalam pop-up
    message1 = font_pop_up.render("Anda Kalah!", True, HITAM)  # Render teks "Anda Kalah!"
    message2 = font_pop_up.render(f"Nama: {nama}", True, HITAM)  # Render teks dengan nama pemain
    message3 = font_pop_up.render(f"Score: {score}", True, HITAM)  # Render teks dengan skor

    layar.blit(message1, (400 - message1.get_width() // 2, 180))  # Tampilkan teks "Anda Kalah!"
    layar.blit(message2, (400 - message2.get_width() // 2, 240))  # Tampilkan nama pemain
    layar.blit(message3, (400 - message3.get_width() // 2, 290))  # Tampilkan skor pemain

    # Ukuran baru untuk tombol kembali ke menu
    button_width = 300  # Ubah ukuran lebar tombol
    button_height = 70  # Ubah ukuran tinggi tombol
    button_rect = pygame.Rect(250, 350, button_width, button_height)  # Posisi dan ukuran tombol

    pygame.draw.rect(layar, PUTIH, button_rect)  # Menggambar tombol kembali
    pygame.draw.rect(layar, HITAM, button_rect, 5)  # Kontur tombol
    button_label = font_pop_up.render("Kembali ke Menu", True, HITAM)  # Render teks "Kembali ke Menu"
    layar.blit(button_label, (button_rect.x + (button_width - button_label.get_width()) // 2, 
                               button_rect.y + (button_height - button_label.get_height()) // 2))  # Tampilkan teks di tombol

    pygame.display.flip()  # Perbarui layar dengan konten yang digambar

    waiting = True  # Status untuk menunggu interaksi pengguna
    while waiting:  # Loop untuk menunggu interaksi
        for event in pygame.event.get():  # Mengambil semua event Pygame
            if event.type == pygame.QUIT:  # Jika pengguna menutup jendela
                pygame.quit()  # Tutup Pygame
                sys.exit()  # Keluar dari program
            if event.type == pygame.MOUSEBUTTONDOWN:  # Jika ada klik mouse
                if event.button == 1 and button_rect.collidepoint(event.pos):  # Jika tombol klik kiri diklik di dalam tombol
                    waiting = False  # Keluar dari pop-up dan kembali ke menu

def game_alat_ukur(nama):
    # Inisialisasi warna yang akan digunakan dalam game
    WHITE = (255, 255, 255)  # Warna putih
    BLACK = (0, 0, 0)        # Warna hitam
    YELLOW = (255, 255, 0)   # Warna kuning
    RED = (255, 0, 0)        # Warna merah

    # Ukuran layar game
    SCREEN_WIDTH = 800  # Lebar layar
    SCREEN_HEIGHT = 600  # Tinggi layar

    # Kecepatan objek yang jatuh dan keranjang
    OBJECT_FALL_SPEED = 5  # Kecepatan objek jatuh
    BASKET_SPEED = 10       # Kecepatan gerakan keranjang

    # Ukuran keranjang
    BASKET_WIDTH = 125      # Lebar keranjang
    BASKET_HEIGHT = 20      # Tinggi keranjang
    FONT_SIZE = 32          # Ukuran font

    # Inisialisasi tampilan layar dan font
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Mengatur ukuran layar
    pygame.display.set_caption('Game Menangkap Rumus')  # Memberi judul pada jendela game
    font = pygame.font.SysFont(None, FONT_SIZE)  # Mengatur font yang akan digunakan

    # Daftar rumus benar dan salah
    rumus_benar = [
    'Termometer',
    'Jangka sorong',
    'Ampere meter',
    'Volt meter',
    'Neraca pegas',
    'Stopwatch',
    'Penggaris'
    ]

    rumus_salah = [
    'Baterai',
    'Kabel',
    'Magnet',
    'Volt meter',
    'Neraca pegas',
    'Fluida',
    'Lampu'
    ]

    # Ucapan untuk jawaban benar, salah, dan terlambat
    ucapan_benar = ["Keren!", "Hebat!", "Pintar!", "Kerja Bagus!", "Jenius!"]
    ucapan_salah = ["Kurang Tepat!", "Berlatih Lagi!", "Belajar Ya!"]
    ucapan_terlambat = "Kamu terlambat!"  # Pesan untuk saat terlambat menangkap rumus

    # Fungsi untuk menggambar keranjang
    def draw_basket(x, y):
        pygame.draw.rect(screen, BLACK, (x, y, BASKET_WIDTH, BASKET_HEIGHT), 2)  # Menggambar keranjang

    # Fungsi untuk menggambar rumus
    def draw_rumus(x, y, rumus_text):
        rumus_surface = font.render(rumus_text, True, BLACK)  # Render rumus menjadi surface
        screen.blit(rumus_surface, (x, y))  # Menampilkan rumus di layar

    # Posisi awal keranjang dan objek rumus
    basket_x = SCREEN_WIDTH // 2 - BASKET_WIDTH // 2  # Tengah layar untuk keranjang
    basket_y = SCREEN_HEIGHT - BASKET_HEIGHT - 10  # Sedikit di atas dasar layar
    rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus secara acak
    object_x = random.randint(0, SCREEN_WIDTH - 200)  # Posisi acak untuk objek
    object_y = -50  # Mulai di atas layar

    # Variabel untuk skor dan jumlah kesalahan
    score = 0  # Skor awal
    salah_count = 0  # Hitung jumlah kesalahan
    max_salah = 5  # Maksimal kesalahan sebelum game over

    # Pesan yang ditampilkan
    message = ""  # Pesan yang akan ditampilkan
    message_color = BLACK  # Warna pesan
    message_timer = 0  # Timer untuk pesan
    
    game_over = False  # Status permainan
    clock = pygame.time.Clock()  # Untuk mengatur kecepatan frame

    while not game_over:  # Loop utama game
        for event in pygame.event.get():  # Mengambil semua event
            if event.type == pygame.QUIT:  # Jika pengguna menutup jendela
                pygame.quit()  # Keluar dari Pygame
                sys.exit()  # Keluar dari program
                
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Jika ada klik mouse
                if event.button == 1:  # Klik kiri mouse
                    mouse_x, mouse_y = event.pos  # Ambil posisi klik
                    exit_button_rect = pygame.Rect(700, 20, 100, 50)  # Posisi dan ukuran tombol exit
                    if exit_button_rect.collidepoint(mouse_x, mouse_y):  # Jika klik di tombol exit
                        return  # Kembali ke menu utama

        # Mengambil input dari keyboard untuk menggerakkan keranjang
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:  # Jika tombol kiri ditekan dan keranjang tidak keluar layar
            basket_x -= BASKET_SPEED  # Gerakkan keranjang ke kiri
        if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - BASKET_WIDTH:  # Jika tombol kanan ditekan
            basket_x += BASKET_SPEED  # Gerakkan keranjang ke kanan

        # Update posisi objek yang jatuh
        object_y += OBJECT_FALL_SPEED  # Menggerakkan objek ke bawah

        # Membuat rectangle untuk keranjang dan objek
        basket_rect = pygame.Rect(basket_x, basket_y, BASKET_WIDTH, BASKET_HEIGHT)  # Rectangle keranjang
        object_rect = pygame.Rect(object_x, object_y, 200, 50)  # Rectangle objek rumus

        # Cek apakah keranjang dan objek bertabrakan
        if basket_rect.colliderect(object_rect):  # Jika terjadi tabrakan
            if rumus_text in rumus_benar:  # Jika rumus benar
                score += 10  # Tambah skor
                message = random.choice(ucapan_benar)  # Pilih ucapan positif
            else:  # Jika rumus salah
                salah_count += 1  # Tambah jumlah kesalahan
                message = random.choice(ucapan_salah)  # Pilih ucapan negatif

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        elif object_y > SCREEN_HEIGHT:  # Jika objek sudah keluar dari layar
            if rumus_text in rumus_benar:  # Jika rumus benar dan keluar dari layar
                salah_count += 1  # Tambah jumlah kesalahan
                message = ucapan_terlambat  # Tampilkan pesan terlambat

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        # Cek apakah ada pesan untuk ditampilkan
        if message:  # Jika ada pesan
            message_timer += 1  # Tambah timer pesan
            if message_timer >= 60:  # Tampilkan pesan selama 1 detik
                message = ""  # Reset pesan
                message_timer = 0  # Reset timer pesan

        # Jika jumlah kesalahan melebihi batas, tampilkan game over
        if salah_count >= max_salah:  # Jika mencapai jumlah kesalahan maksimal
            show_game_over_popup(nama, score)  # Tampilkan pop-up game over
            game_over = True  # Ubah status game menjadi game over

        # Menggambar semua elemen di layar
        screen.fill(WHITE)  # Mengisi layar dengan warna putih
        draw_basket(basket_x, basket_y)  # Menggambar keranjang
        draw_rumus(object_x, object_y, rumus_text)  # Menggambar objek rumus

        # Menampilkan pesan di layar
        message_surface = font.render(message, True, message_color)  # Render pesan
        screen.blit(message_surface, (SCREEN_WIDTH // 2 - message_surface.get_width() // 2, 50))  # Tampilkan pesan di tengah atas

        # Menampilkan skor dan jumlah kesalahan
        score_surface = font.render(f'Score: {score}', True, BLACK)  # Render skor
        screen.blit(score_surface, (10, 10))  # Tampilkan skor di pojok kiri atas

        salah_surface = font.render(f'Kesalahan: {salah_count}', True, BLACK)  # Render kesalahan
        screen.blit(salah_surface, (10, 50))  # Tampilkan jumlah kesalahan di bawah skor

        # Gambar tombol exit
        exit_button_rect = pygame.Rect(700, 20, 85, 50)  # Posisi dan ukuran tombol exit
        pygame.draw.rect(screen, WHITE, exit_button_rect)  # Gambar tombol exit
        pygame.draw.rect(screen, BLACK, exit_button_rect, 5)  # Kontur tombol exit
        exit_text = font.render('Exit', True, BLACK)  # Render teks 'Exit'
        screen.blit(exit_text, (exit_button_rect.x + 20, exit_button_rect.y + 10))  # Tampilkan teks di dalam tombol

        pygame.display.flip()  # Perbarui tampilan layar
        clock.tick(60)  # Atur FPS game

def game_pokok(nama):
    # Inisialisasi warna yang akan digunakan dalam game
    WHITE = (255, 255, 255)  # Warna putih
    BLACK = (0, 0, 0)        # Warna hitam
    YELLOW = (255, 255, 0)   # Warna kuning
    RED = (255, 0, 0)        # Warna merah

    # Ukuran layar game
    SCREEN_WIDTH = 800  # Lebar layar
    SCREEN_HEIGHT = 600  # Tinggi layar

    # Kecepatan objek yang jatuh dan keranjang
    OBJECT_FALL_SPEED = 5  # Kecepatan objek jatuh
    BASKET_SPEED = 10       # Kecepatan gerakan keranjang

    # Ukuran keranjang
    BASKET_WIDTH = 125      # Lebar keranjang
    BASKET_HEIGHT = 20      # Tinggi keranjang
    FONT_SIZE = 32          # Ukuran font

    # Inisialisasi tampilan layar dan font
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Mengatur ukuran layar
    pygame.display.set_caption('Game Menangkap Rumus')  # Memberi judul pada jendela game
    font = pygame.font.SysFont(None, FONT_SIZE)  # Mengatur font yang akan digunakan

    # Daftar rumus benar dan salah
    rumus_benar = [
    'Massa (kg)',
    'Panjang (m)',
    'Waktu (s)',
    'Kuat Arus (A)',
    'Suhu (K)',
    'Intensitas Cahaya (cd)',
    'Energi (Joule)',
    'Tekanan (Pa)',
    'Kecepatan (m/s)',
    ]

    rumus_salah = [
    'Luas (L)',
    'Hasil (R)',
    'Volume (ml)',
    'Waktu (min)',
    'Masa (lb)',
    'Kecepatan (km/h)',
    'Energi (kcal)',
    'Gaya (F)',
    ]

    # Ucapan untuk jawaban benar, salah, dan terlambat
    ucapan_benar = ["Keren!", "Hebat!", "Pintar!", "Kerja Bagus!", "Jenius!"]
    ucapan_salah = ["Kurang Tepat!", "Berlatih Lagi!", "Belajar Ya!"]
    ucapan_terlambat = "Kamu terlambat!"  # Pesan untuk saat terlambat menangkap rumus

    # Fungsi untuk menggambar keranjang
    def draw_basket(x, y):
        pygame.draw.rect(screen, BLACK, (x, y, BASKET_WIDTH, BASKET_HEIGHT), 2)  # Menggambar keranjang

    # Fungsi untuk menggambar rumus
    def draw_rumus(x, y, rumus_text):
        rumus_surface = font.render(rumus_text, True, BLACK)  # Render rumus menjadi surface
        screen.blit(rumus_surface, (x, y))  # Menampilkan rumus di layar

    # Posisi awal keranjang dan objek rumus
    basket_x = SCREEN_WIDTH // 2 - BASKET_WIDTH // 2  # Tengah layar untuk keranjang
    basket_y = SCREEN_HEIGHT - BASKET_HEIGHT - 10  # Sedikit di atas dasar layar
    rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus secara acak
    object_x = random.randint(0, SCREEN_WIDTH - 200)  # Posisi acak untuk objek
    object_y = -50  # Mulai di atas layar

    # Variabel untuk skor dan jumlah kesalahan
    score = 0  # Skor awal
    salah_count = 0  # Hitung jumlah kesalahan
    max_salah = 5  # Maksimal kesalahan sebelum game over

    # Pesan yang ditampilkan
    message = ""  # Pesan yang akan ditampilkan
    message_color = BLACK  # Warna pesan
    message_timer = 0  # Timer untuk pesan
    
    game_over = False  # Status permainan
    clock = pygame.time.Clock()  # Untuk mengatur kecepatan frame

    while not game_over:  # Loop utama game
        for event in pygame.event.get():  # Mengambil semua event
            if event.type == pygame.QUIT:  # Jika pengguna menutup jendela
                pygame.quit()  # Keluar dari Pygame
                sys.exit()  # Keluar dari program
                
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Jika ada klik mouse
                if event.button == 1:  # Klik kiri mouse
                    mouse_x, mouse_y = event.pos  # Ambil posisi klik
                    exit_button_rect = pygame.Rect(700, 20, 100, 50)  # Posisi dan ukuran tombol exit
                    if exit_button_rect.collidepoint(mouse_x, mouse_y):  # Jika klik di tombol exit
                        return  # Kembali ke menu utama

        # Mengambil input dari keyboard untuk menggerakkan keranjang
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:  # Jika tombol kiri ditekan dan keranjang tidak keluar layar
            basket_x -= BASKET_SPEED  # Gerakkan keranjang ke kiri
        if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - BASKET_WIDTH:  # Jika tombol kanan ditekan
            basket_x += BASKET_SPEED  # Gerakkan keranjang ke kanan

        # Update posisi objek yang jatuh
        object_y += OBJECT_FALL_SPEED  # Menggerakkan objek ke bawah

        # Membuat rectangle untuk keranjang dan objek
        basket_rect = pygame.Rect(basket_x, basket_y, BASKET_WIDTH, BASKET_HEIGHT)  # Rectangle keranjang
        object_rect = pygame.Rect(object_x, object_y, 200, 50)  # Rectangle objek rumus

        # Cek apakah keranjang dan objek bertabrakan
        if basket_rect.colliderect(object_rect):  # Jika terjadi tabrakan
            if rumus_text in rumus_benar:  # Jika rumus benar
                score += 10  # Tambah skor
                message = random.choice(ucapan_benar)  # Pilih ucapan positif
            else:  # Jika rumus salah
                salah_count += 1  # Tambah jumlah kesalahan
                message = random.choice(ucapan_salah)  # Pilih ucapan negatif

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        elif object_y > SCREEN_HEIGHT:  # Jika objek sudah keluar dari layar
            if rumus_text in rumus_benar:  # Jika rumus benar dan keluar dari layar
                salah_count += 1  # Tambah jumlah kesalahan
                message = ucapan_terlambat  # Tampilkan pesan terlambat

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        # Cek apakah ada pesan untuk ditampilkan
        if message:  # Jika ada pesan
            message_timer += 1  # Tambah timer pesan
            if message_timer >= 60:  # Tampilkan pesan selama 1 detik
                message = ""  # Reset pesan
                message_timer = 0  # Reset timer pesan

        # Jika jumlah kesalahan melebihi batas, tampilkan game over
        if salah_count >= max_salah:  # Jika mencapai jumlah kesalahan maksimal
            show_game_over_popup(nama, score)  # Tampilkan pop-up game over
            game_over = True  # Ubah status game menjadi game over

        # Menggambar semua elemen di layar
        screen.fill(WHITE)  # Mengisi layar dengan warna putih
        draw_basket(basket_x, basket_y)  # Menggambar keranjang
        draw_rumus(object_x, object_y, rumus_text)  # Menggambar objek rumus

        # Menampilkan pesan di layar
        message_surface = font.render(message, True, message_color)  # Render pesan
        screen.blit(message_surface, (SCREEN_WIDTH // 2 - message_surface.get_width() // 2, 50))  # Tampilkan pesan di tengah atas

        # Menampilkan skor dan jumlah kesalahan
        score_surface = font.render(f'Score: {score}', True, BLACK)  # Render skor
        screen.blit(score_surface, (10, 10))  # Tampilkan skor di pojok kiri atas

        salah_surface = font.render(f'Kesalahan: {salah_count}', True, BLACK)  # Render kesalahan
        screen.blit(salah_surface, (10, 50))  # Tampilkan jumlah kesalahan di bawah skor

        # Gambar tombol exit
        exit_button_rect = pygame.Rect(700, 20, 85, 50)  # Posisi dan ukuran tombol exit
        pygame.draw.rect(screen, WHITE, exit_button_rect)  # Gambar tombol exit
        pygame.draw.rect(screen, BLACK, exit_button_rect, 5)  # Kontur tombol exit
        exit_text = font.render('Exit', True, BLACK)  # Render teks 'Exit'
        screen.blit(exit_text, (exit_button_rect.x + 20, exit_button_rect.y + 10))  # Tampilkan teks di dalam tombol

        pygame.display.flip()  # Perbarui tampilan layar
        clock.tick(60)  # Atur FPS game

def game_turunan(nama):
    # Inisialisasi warna yang akan digunakan dalam game
    WHITE = (255, 255, 255)  # Warna putih
    BLACK = (0, 0, 0)        # Warna hitam
    YELLOW = (255, 255, 0)   # Warna kuning
    RED = (255, 0, 0)        # Warna merah

    # Ukuran layar game
    SCREEN_WIDTH = 800  # Lebar layar
    SCREEN_HEIGHT = 600  # Tinggi layar

    # Kecepatan objek yang jatuh dan keranjang
    OBJECT_FALL_SPEED = 5  # Kecepatan objek jatuh
    BASKET_SPEED = 10       # Kecepatan gerakan keranjang

    # Ukuran keranjang
    BASKET_WIDTH = 125      # Lebar keranjang
    BASKET_HEIGHT = 20      # Tinggi keranjang
    FONT_SIZE = 32          # Ukuran font

    # Inisialisasi tampilan layar dan font
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Mengatur ukuran layar
    pygame.display.set_caption('Game Menangkap Rumus')  # Memberi judul pada jendela game
    font = pygame.font.SysFont(None, FONT_SIZE)  # Mengatur font yang akan digunakan

    # Daftar rumus benar dan salah
    rumus_benar = [
    'W (Usaha) ',
    'F (Gaya)',
    'A (Luas)',
    'v (Kecepatan)',
    'a (Percepatan)',
    'P (Momentum)',
    ]

    rumus_salah = [
    'T (Suhu)',
    'I (Arus)',
    'F (Torsi)',
    'M (Massa) ',
    'A (Volume)',
    'V (LookupErroruas)',
    'l (Panjang)',
    ]

    # Ucapan untuk jawaban benar, salah, dan terlambat
    ucapan_benar = ["Keren!", "Hebat!", "Pintar!", "Kerja Bagus!", "Jenius!"]
    ucapan_salah = ["Kurang Tepat!", "Berlatih Lagi!", "Belajar Ya!"]
    ucapan_terlambat = "Kamu terlambat!"  # Pesan untuk saat terlambat menangkap rumus

    # Fungsi untuk menggambar keranjang
    def draw_basket(x, y):
        pygame.draw.rect(screen, BLACK, (x, y, BASKET_WIDTH, BASKET_HEIGHT), 2)  # Menggambar keranjang

    # Fungsi untuk menggambar rumus
    def draw_rumus(x, y, rumus_text):
        rumus_surface = font.render(rumus_text, True, BLACK)  # Render rumus menjadi surface
        screen.blit(rumus_surface, (x, y))  # Menampilkan rumus di layar

    # Posisi awal keranjang dan objek rumus
    basket_x = SCREEN_WIDTH // 2 - BASKET_WIDTH // 2  # Tengah layar untuk keranjang
    basket_y = SCREEN_HEIGHT - BASKET_HEIGHT - 10  # Sedikit di atas dasar layar
    rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus secara acak
    object_x = random.randint(0, SCREEN_WIDTH - 200)  # Posisi acak untuk objek
    object_y = -50  # Mulai di atas layar

    # Variabel untuk skor dan jumlah kesalahan
    score = 0  # Skor awal
    salah_count = 0  # Hitung jumlah kesalahan
    max_salah = 5  # Maksimal kesalahan sebelum game over

    # Pesan yang ditampilkan
    message = ""  # Pesan yang akan ditampilkan
    message_color = BLACK  # Warna pesan
    message_timer = 0  # Timer untuk pesan
    
    game_over = False  # Status permainan
    clock = pygame.time.Clock()  # Untuk mengatur kecepatan frame

    while not game_over:  # Loop utama game
        for event in pygame.event.get():  # Mengambil semua event
            if event.type == pygame.QUIT:  # Jika pengguna menutup jendela
                pygame.quit()  # Keluar dari Pygame
                sys.exit()  # Keluar dari program
                
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Jika ada klik mouse
                if event.button == 1:  # Klik kiri mouse
                    mouse_x, mouse_y = event.pos  # Ambil posisi klik
                    exit_button_rect = pygame.Rect(700, 20, 100, 50)  # Posisi dan ukuran tombol exit
                    if exit_button_rect.collidepoint(mouse_x, mouse_y):  # Jika klik di tombol exit
                        return  # Kembali ke menu utama

        # Mengambil input dari keyboard untuk menggerakkan keranjang
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:  # Jika tombol kiri ditekan dan keranjang tidak keluar layar
            basket_x -= BASKET_SPEED  # Gerakkan keranjang ke kiri
        if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - BASKET_WIDTH:  # Jika tombol kanan ditekan
            basket_x += BASKET_SPEED  # Gerakkan keranjang ke kanan

        # Update posisi objek yang jatuh
        object_y += OBJECT_FALL_SPEED  # Menggerakkan objek ke bawah

        # Membuat rectangle untuk keranjang dan objek
        basket_rect = pygame.Rect(basket_x, basket_y, BASKET_WIDTH, BASKET_HEIGHT)  # Rectangle keranjang
        object_rect = pygame.Rect(object_x, object_y, 200, 50)  # Rectangle objek rumus

        # Cek apakah keranjang dan objek bertabrakan
        if basket_rect.colliderect(object_rect):  # Jika terjadi tabrakan
            if rumus_text in rumus_benar:  # Jika rumus benar
                score += 10  # Tambah skor
                message = random.choice(ucapan_benar)  # Pilih ucapan positif
            else:  # Jika rumus salah
                salah_count += 1  # Tambah jumlah kesalahan
                message = random.choice(ucapan_salah)  # Pilih ucapan negatif

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        elif object_y > SCREEN_HEIGHT:  # Jika objek sudah keluar dari layar
            if rumus_text in rumus_benar:  # Jika rumus benar dan keluar dari layar
                salah_count += 1  # Tambah jumlah kesalahan
                message = ucapan_terlambat  # Tampilkan pesan terlambat

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        # Cek apakah ada pesan untuk ditampilkan
        if message:  # Jika ada pesan
            message_timer += 1  # Tambah timer pesan
            if message_timer >= 60:  # Tampilkan pesan selama 1 detik
                message = ""  # Reset pesan
                message_timer = 0  # Reset timer pesan

        # Jika jumlah kesalahan melebihi batas, tampilkan game over
        if salah_count >= max_salah:  # Jika mencapai jumlah kesalahan maksimal
            show_game_over_popup(nama, score)  # Tampilkan pop-up game over
            game_over = True  # Ubah status game menjadi game over

        # Menggambar semua elemen di layar
        screen.fill(WHITE)  # Mengisi layar dengan warna putih
        draw_basket(basket_x, basket_y)  # Menggambar keranjang
        draw_rumus(object_x, object_y, rumus_text)  # Menggambar objek rumus

        # Menampilkan pesan di layar
        message_surface = font.render(message, True, message_color)  # Render pesan
        screen.blit(message_surface, (SCREEN_WIDTH // 2 - message_surface.get_width() // 2, 50))  # Tampilkan pesan di tengah atas

        # Menampilkan skor dan jumlah kesalahan
        score_surface = font.render(f'Score: {score}', True, BLACK)  # Render skor
        screen.blit(score_surface, (10, 10))  # Tampilkan skor di pojok kiri atas

        salah_surface = font.render(f'Kesalahan: {salah_count}', True, BLACK)  # Render kesalahan
        screen.blit(salah_surface, (10, 50))  # Tampilkan jumlah kesalahan di bawah skor

        # Gambar tombol exit
        exit_button_rect = pygame.Rect(700, 20, 85, 50)  # Posisi dan ukuran tombol exit
        pygame.draw.rect(screen, WHITE, exit_button_rect)  # Gambar tombol exit
        pygame.draw.rect(screen, BLACK, exit_button_rect, 5)  # Kontur tombol exit
        exit_text = font.render('Exit', True, BLACK)  # Render teks 'Exit'
        screen.blit(exit_text, (exit_button_rect.x + 20, exit_button_rect.y + 10))  # Tampilkan teks di dalam tombol

        pygame.display.flip()  # Perbarui tampilan layar
        clock.tick(60)  # Atur FPS game

def game_besaran_fisika(nama):
    # Inisialisasi warna yang akan digunakan dalam game
    WHITE = (255, 255, 255)  # Warna putih
    BLACK = (0, 0, 0)        # Warna hitam
    YELLOW = (255, 255, 0)   # Warna kuning
    RED = (255, 0, 0)        # Warna merah

    # Ukuran layar game
    SCREEN_WIDTH = 800  # Lebar layar
    SCREEN_HEIGHT = 600  # Tinggi layar

    # Kecepatan objek yang jatuh dan keranjang
    OBJECT_FALL_SPEED = 5  # Kecepatan objek jatuh
    BASKET_SPEED = 10       # Kecepatan gerakan keranjang

    # Ukuran keranjang
    BASKET_WIDTH = 125      # Lebar keranjang
    BASKET_HEIGHT = 20      # Tinggi keranjang
    FONT_SIZE = 32          # Ukuran font

    # Inisialisasi tampilan layar dan font
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Mengatur ukuran layar
    pygame.display.set_caption('Game Menangkap Rumus')  # Memberi judul pada jendela game
    font = pygame.font.SysFont(None, FONT_SIZE)  # Mengatur font yang akan digunakan

    # Daftar satuan benar dan salah
    rumus_benar = [
    'Gaya',
    'Percepatan',
    'Kecepatan',
    'Momentum',
    'Energi',
    'Frekuensi',
    'Perioda',
    'Panjang Gelombang',
    'Suhu',
    'Medan Listrik',
    'Medan Magnet',
    ]

    rumus_salah = [
    'Jangka Sorong',
    'Termometer',
    'Stop Watch',
    'Neraca Pegas',
    'Amperemeter',
    'Kalorimeter',
    ]

    # Ucapan untuk jawaban benar, salah, dan terlambat
    ucapan_benar = ["Keren!", "Hebat!", "Pintar!", "Kerja Bagus!", "Jenius!"]
    ucapan_salah = ["Kurang Tepat!", "Berlatih Lagi!", "Belajar Ya!"]
    ucapan_terlambat = "Kamu terlambat!"  # Pesan untuk saat terlambat menangkap rumus

    # Fungsi untuk menggambar keranjang
    def draw_basket(x, y):
        pygame.draw.rect(screen, BLACK, (x, y, BASKET_WIDTH, BASKET_HEIGHT), 2)  # Menggambar keranjang

    # Fungsi untuk menggambar rumus
    def draw_rumus(x, y, rumus_text):
        rumus_surface = font.render(rumus_text, True, BLACK)  # Render rumus menjadi surface
        screen.blit(rumus_surface, (x, y))  # Menampilkan rumus di layar

    # Posisi awal keranjang dan objek rumus
    basket_x = SCREEN_WIDTH // 2 - BASKET_WIDTH // 2  # Tengah layar untuk keranjang
    basket_y = SCREEN_HEIGHT - BASKET_HEIGHT - 10  # Sedikit di atas dasar layar
    rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus secara acak
    object_x = random.randint(0, SCREEN_WIDTH - 200)  # Posisi acak untuk objek
    object_y = -50  # Mulai di atas layar

    # Variabel untuk skor dan jumlah kesalahan
    score = 0  # Skor awal
    salah_count = 0  # Hitung jumlah kesalahan
    max_salah = 5  # Maksimal kesalahan sebelum game over

    # Pesan yang ditampilkan
    message = ""  # Pesan yang akan ditampilkan
    message_color = BLACK  # Warna pesan
    message_timer = 0  # Timer untuk pesan
    
    game_over = False  # Status permainan
    clock = pygame.time.Clock()  # Untuk mengatur kecepatan frame

    while not game_over:  # Loop utama game
        for event in pygame.event.get():  # Mengambil semua event
            if event.type == pygame.QUIT:  # Jika pengguna menutup jendela
                pygame.quit()  # Keluar dari Pygame
                sys.exit()  # Keluar dari program
                
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Jika ada klik mouse
                if event.button == 1:  # Klik kiri mouse
                    mouse_x, mouse_y = event.pos  # Ambil posisi klik
                    exit_button_rect = pygame.Rect(700, 20, 100, 50)  # Posisi dan ukuran tombol exit
                    if exit_button_rect.collidepoint(mouse_x, mouse_y):  # Jika klik di tombol exit
                        return  # Kembali ke menu utama

        # Mengambil input dari keyboard untuk menggerakkan keranjang
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:  # Jika tombol kiri ditekan dan keranjang tidak keluar layar
            basket_x -= BASKET_SPEED  # Gerakkan keranjang ke kiri
        if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - BASKET_WIDTH:  # Jika tombol kanan ditekan
            basket_x += BASKET_SPEED  # Gerakkan keranjang ke kanan

        # Update posisi objek yang jatuh
        object_y += OBJECT_FALL_SPEED  # Menggerakkan objek ke bawah

        # Membuat rectangle untuk keranjang dan objek
        basket_rect = pygame.Rect(basket_x, basket_y, BASKET_WIDTH, BASKET_HEIGHT)  # Rectangle keranjang
        object_rect = pygame.Rect(object_x, object_y, 200, 50)  # Rectangle objek rumus

        # Cek apakah keranjang dan objek bertabrakan
        if basket_rect.colliderect(object_rect):  # Jika terjadi tabrakan
            if rumus_text in rumus_benar:  # Jika rumus benar
                score += 10  # Tambah skor
                message = random.choice(ucapan_benar)  # Pilih ucapan positif
            else:  # Jika rumus salah
                salah_count += 1  # Tambah jumlah kesalahan
                message = random.choice(ucapan_salah)  # Pilih ucapan negatif

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        elif object_y > SCREEN_HEIGHT:  # Jika objek sudah keluar dari layar
            if rumus_text in rumus_benar:  # Jika rumus benar dan keluar dari layar
                salah_count += 1  # Tambah jumlah kesalahan
                message = ucapan_terlambat  # Tampilkan pesan terlambat

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        # Cek apakah ada pesan untuk ditampilkan
        if message:  # Jika ada pesan
            message_timer += 1  # Tambah timer pesan
            if message_timer >= 60:  # Tampilkan pesan selama 1 detik
                message = ""  # Reset pesan
                message_timer = 0  # Reset timer pesan

        # Jika jumlah kesalahan melebihi batas, tampilkan game over
        if salah_count >= max_salah:  # Jika mencapai jumlah kesalahan maksimal
            show_game_over_popup(nama, score)  # Tampilkan pop-up game over
            game_over = True  # Ubah status game menjadi game over

        # Menggambar semua elemen di layar
        screen.fill(WHITE)  # Mengisi layar dengan warna putih
        draw_basket(basket_x, basket_y)  # Menggambar keranjang
        draw_rumus(object_x, object_y, rumus_text)  # Menggambar objek rumus

        # Menampilkan pesan di layar
        message_surface = font.render(message, True, message_color)  # Render pesan
        screen.blit(message_surface, (SCREEN_WIDTH // 2 - message_surface.get_width() // 2, 50))  # Tampilkan pesan di tengah atas

        # Menampilkan skor dan jumlah kesalahan
        score_surface = font.render(f'Score: {score}', True, BLACK)  # Render skor
        screen.blit(score_surface, (10, 10))  # Tampilkan skor di pojok kiri atas

        salah_surface = font.render(f'Kesalahan: {salah_count}', True, BLACK)  # Render kesalahan
        screen.blit(salah_surface, (10, 50))  # Tampilkan jumlah kesalahan di bawah skor

        # Gambar tombol exit
        exit_button_rect = pygame.Rect(700, 20, 85, 50)  # Posisi dan ukuran tombol exit
        pygame.draw.rect(screen, WHITE, exit_button_rect)  # Gambar tombol exit
        pygame.draw.rect(screen, BLACK, exit_button_rect, 5)  # Kontur tombol exit
        exit_text = font.render('Exit', True, BLACK)  # Render teks 'Exit'
        screen.blit(exit_text, (exit_button_rect.x + 20, exit_button_rect.y + 10))  # Tampilkan teks di dalam tombol

        pygame.display.flip()  # Perbarui tampilan layar
        clock.tick(60)  # Atur FPS game

def game_dimensi(nama):
    # Inisialisasi warna, ukuran, dan kecepatan seperti di game Menangkap Rumus
    WHITE = (255, 255, 255)  # Warna latar belakang
    BLACK = (0, 0, 0)        # Warna teks dan kontur
    YELLOW = (255, 255, 0)   # Warna kuning (tidak digunakan)
    RED = (255, 0, 0)        # Warna merah (tidak digunakan)

    SCREEN_WIDTH = 800        # Lebar layar
    SCREEN_HEIGHT = 600       # Tinggi layar

    OBJECT_FALL_SPEED = 5     # Kecepatan objek yang jatuh
    BASKET_SPEED = 10         # Kecepatan keranjang

    BASKET_WIDTH = 125        # Lebar keranjang
    BASKET_HEIGHT = 20        # Tinggi keranjang
    FONT_SIZE = 32            # Ukuran font

    # Mengatur tampilan layar dan font
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Membuat layar dengan ukuran tertentu
    pygame.display.set_caption('Game Menangkap Rumus')  # Memberi judul pada jendela game
    font = pygame.font.SysFont(None, FONT_SIZE)  # Mengatur font yang akan digunakan

    # Daftar rumus yang benar dan salah
    rumus_benar = [
    '[M]',             # Dimensi massa
    '[L]',             # Dimensi panjang
    '[T]',             # Dimensi waktu
    '[I]',             # Dimensi arus listrik
    '[N]',             # Dimensi zat
    '[J]',             # Dimensi intensitas cahaya
    '[LT^-1]',         # Dimensi kecepatan
    '[MLT^-2]',        # Dimensi gaya
    '[ML^2T^-2]',      # Dimensi energi
    ]

    rumus_salah = [
    '[L^0]',                  # Bilangan tanpa dimensi (terlihat seperti dimensi)
    '[C]',                    # Dimensi muatan listrik (sepertinya dimensi, tetapi bukan dalam konteks ini)
    '[2M]',                   # Tampak seperti dimensi, tetapi bukan (penjumlahan dimensi)
    '[R^2]',                  # Tampak sebagai dimensi, tetapi bisa juga diartikan sebagai luas tanpa konteks
    '[ML^-2T^2]',             # Dimensi energi tapi kebalik
    '[kg/s]',                 # Dimensi aliran massa, terlihat benar tetapi bukan dimensi murni
    '[M^2][L^1]',             # Kombinasi yang aneh, tidak merujuk pada dimensi fisika yang valid
    '[N^0]',                  # Bilangan tanpa dimensi (tetapi terlihat benar)
    '[m + s]',                # Penjumlahan unit, bukan dimensi fisika
    ]

    # Ucapan untuk jawaban benar, salah, dan terlambat
    ucapan_benar = ["Keren!", "Hebat!", "Pintar!", "Kerja Bagus!", "Jenius!"]
    ucapan_salah = ["Kurang Tepat!", "Berlatih Lagi!", "Belajar Ya!"]
    ucapan_terlambat = "Kamu terlambat!"  # Pesan untuk saat terlambat menangkap rumus

    # Fungsi untuk menggambar keranjang
    def draw_basket(x, y):
        pygame.draw.rect(screen, BLACK, (x, y, BASKET_WIDTH, BASKET_HEIGHT), 2)  # Menggambar keranjang

    # Fungsi untuk menggambar rumus
    def draw_rumus(x, y, rumus_text):
        rumus_surface = font.render(rumus_text, True, BLACK)  # Render rumus menjadi surface
        screen.blit(rumus_surface, (x, y))  # Menampilkan rumus di layar

    # Posisi awal keranjang dan objek rumus
    basket_x = SCREEN_WIDTH // 2 - BASKET_WIDTH // 2  # Tengah layar untuk keranjang
    basket_y = SCREEN_HEIGHT - BASKET_HEIGHT - 10  # Sedikit di atas dasar layar
    rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus secara acak
    object_x = random.randint(0, SCREEN_WIDTH - 200)  # Posisi acak untuk objek
    object_y = -50  # Mulai di atas layar

    # Variabel untuk skor dan jumlah kesalahan
    score = 0  # Skor awal
    salah_count = 0  # Hitung jumlah kesalahan
    max_salah = 5  # Maksimal kesalahan sebelum game over

    # Pesan yang ditampilkan
    message = ""  # Pesan yang akan ditampilkan
    message_color = BLACK  # Warna pesan
    message_timer = 0  # Timer untuk pesan
    
    game_over = False  # Status permainan
    clock = pygame.time.Clock()  # Untuk mengatur kecepatan frame

    while not game_over:  # Loop utama game
        for event in pygame.event.get():  # Mengambil semua event
            if event.type == pygame.QUIT:  # Jika pengguna menutup jendela
                pygame.quit()  # Keluar dari Pygame
                sys.exit()  # Keluar dari program
                
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Jika ada klik mouse
                if event.button == 1:  # Klik kiri mouse
                    mouse_x, mouse_y = event.pos  # Ambil posisi klik
                    exit_button_rect = pygame.Rect(700, 20, 100, 50)  # Posisi dan ukuran tombol exit
                    if exit_button_rect.collidepoint(mouse_x, mouse_y):  # Jika klik di tombol exit
                        return  # Kembali ke menu utama

        # Mengambil input dari keyboard untuk menggerakkan keranjang
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:  # Jika tombol kiri ditekan dan keranjang tidak keluar layar
            basket_x -= BASKET_SPEED  # Gerakkan keranjang ke kiri
        if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - BASKET_WIDTH:  # Jika tombol kanan ditekan
            basket_x += BASKET_SPEED  # Gerakkan keranjang ke kanan

        # Update posisi objek yang jatuh
        object_y += OBJECT_FALL_SPEED  # Menggerakkan objek ke bawah

        # Membuat rectangle untuk keranjang dan objek
        basket_rect = pygame.Rect(basket_x, basket_y, BASKET_WIDTH, BASKET_HEIGHT)  # Rectangle keranjang
        object_rect = pygame.Rect(object_x, object_y, 200, 50)  # Rectangle objek rumus

        # Cek apakah keranjang dan objek bertabrakan
        if basket_rect.colliderect(object_rect):  # Jika terjadi tabrakan
            if rumus_text in rumus_benar:  # Jika rumus benar
                score += 10  # Tambah skor
                message = random.choice(ucapan_benar)  # Pilih ucapan positif
            else:  # Jika rumus salah
                salah_count += 1  # Tambah jumlah kesalahan
                message = random.choice(ucapan_salah)  # Pilih ucapan negatif

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        elif object_y > SCREEN_HEIGHT:  # Jika objek sudah keluar dari layar
            if rumus_text in rumus_benar:  # Jika rumus benar dan keluar dari layar
                salah_count += 1  # Tambah jumlah kesalahan
                message = ucapan_terlambat  # Tampilkan pesan terlambat

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        # Cek apakah ada pesan untuk ditampilkan
        if message:  # Jika ada pesan
            message_timer += 1  # Tambah timer pesan
            if message_timer >= 60:  # Tampilkan pesan selama 1 detik
                message = ""  # Reset pesan
                message_timer = 0  # Reset timer pesan

        # Jika jumlah kesalahan melebihi batas, tampilkan game over
        if salah_count >= max_salah:  # Jika mencapai jumlah kesalahan maksimal
            show_game_over_popup(nama, score)  # Tampilkan pop-up game over
            game_over = True  # Ubah status game menjadi game over

        # Menggambar semua elemen di layar
        screen.fill(WHITE)  # Mengisi layar dengan warna putih
        draw_basket(basket_x, basket_y)  # Menggambar keranjang
        draw_rumus(object_x, object_y, rumus_text)  # Menggambar objek rumus

        # Menampilkan pesan di layar
        message_surface = font.render(message, True, message_color)  # Render pesan
        screen.blit(message_surface, (SCREEN_WIDTH // 2 - message_surface.get_width() // 2, 50))  # Tampilkan pesan di tengah atas

        # Menampilkan skor dan jumlah kesalahan
        score_surface = font.render(f'Score: {score}', True, BLACK)  # Render skor
        screen.blit(score_surface, (10, 10))  # Tampilkan skor di pojok kiri atas

        salah_surface = font.render(f'Kesalahan: {salah_count}', True, BLACK)  # Render kesalahan
        screen.blit(salah_surface, (10, 50))  # Tampilkan jumlah kesalahan di bawah skor

        # Gambar tombol exit
        exit_button_rect = pygame.Rect(700, 20, 85, 50)  # Posisi dan ukuran tombol exit
        pygame.draw.rect(screen, WHITE, exit_button_rect)  # Gambar tombol exit
        pygame.draw.rect(screen, BLACK, exit_button_rect, 5)  # Kontur tombol exit
        exit_text = font.render('Exit', True, BLACK)  # Render teks 'Exit'
        screen.blit(exit_text, (exit_button_rect.x + 20, exit_button_rect.y + 10))  # Tampilkan teks di dalam tombol

        pygame.display.flip()  # Perbarui tampilan layar
        clock.tick(60)  # Atur FPS game

def game_tokoh_fisika(nama):
    # Inisialisasi warna, ukuran, dan kecepatan seperti di game Menangkap Rumus
    WHITE = (255, 255, 255)  # Warna latar belakang
    BLACK = (0, 0, 0)        # Warna teks dan kontur
    YELLOW = (255, 255, 0)   # Warna kuning (tidak digunakan)
    RED = (255, 0, 0)        # Warna merah (tidak digunakan)

    SCREEN_WIDTH = 800        # Lebar layar
    SCREEN_HEIGHT = 600       # Tinggi layar

    OBJECT_FALL_SPEED = 5     # Kecepatan objek yang jatuh
    BASKET_SPEED = 10         # Kecepatan keranjang

    BASKET_WIDTH = 125        # Lebar keranjang
    BASKET_HEIGHT = 20        # Tinggi keranjang
    FONT_SIZE = 32            # Ukuran font

    # Mengatur tampilan layar dan font
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Membuat layar dengan ukuran tertentu
    pygame.display.set_caption('Game Menangkap Rumus')  # Memberi judul pada jendela game
    font = pygame.font.SysFont(None, FONT_SIZE)  # Mengatur font yang akan digunakan

    # Daftar rumus yang benar dan salah
    rumus_benar = [
    'Newton',
    'Archimedes',
    'Einstein',
    'Ampere',
    'paskal',
    'Marie Curie',
    'Compton',
    'Michael Faraday',
    'Coulomb'
    ]

    rumus_salah = [
    'Taylor Swift',
    'Lady Gaga',
    'Michael Jackson',
    'Celine Dion',
    'Alexander Graham Bell',
    'Nikola Tesla',
    'James Watt',
    'Joko Widodo',
    'Nagita Slavina',
    'Ibu Selly Feranie'
    ]

    # Ucapan untuk jawaban benar, salah, dan terlambat
    ucapan_benar = ["lah kok tau?", "belajar dimana broh?", "wah, nyontek ya?", "dikasih tau siapa?", "terlalu gampang"]
    ucapan_salah = ["masa gitu aja gatau :v", "wkwk salah!", "jangan tidur dikelas!", "kocak!"]
    ucapan_terlambat = "aelah telat bro!!"  # Pesan untuk saat terlambat menangkap rumus

    # Fungsi untuk menggambar keranjang
    def draw_basket(x, y):
        pygame.draw.rect(screen, BLACK, (x, y, BASKET_WIDTH, BASKET_HEIGHT), 2)  # Menggambar keranjang

    # Fungsi untuk menggambar rumus
    def draw_rumus(x, y, rumus_text):
        rumus_surface = font.render(rumus_text, True, BLACK)  # Render rumus menjadi surface
        screen.blit(rumus_surface, (x, y))  # Menampilkan rumus di layar

    # Posisi awal keranjang dan objek rumus
    basket_x = SCREEN_WIDTH // 2 - BASKET_WIDTH // 2  # Tengah layar untuk keranjang
    basket_y = SCREEN_HEIGHT - BASKET_HEIGHT - 10  # Sedikit di atas dasar layar
    rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus secara acak
    object_x = random.randint(0, SCREEN_WIDTH - 200)  # Posisi acak untuk objek
    object_y = -50  # Mulai di atas layar

    # Variabel untuk skor dan jumlah kesalahan
    score = 0  # Skor awal
    salah_count = 0  # Hitung jumlah kesalahan
    max_salah = 5  # Maksimal kesalahan sebelum game over

    # Pesan yang ditampilkan
    message = ""  # Pesan yang akan ditampilkan
    message_color = BLACK  # Warna pesan
    message_timer = 0  # Timer untuk pesan
    
    game_over = False  # Status permainan
    clock = pygame.time.Clock()  # Untuk mengatur kecepatan frame

    while not game_over:  # Loop utama game
        for event in pygame.event.get():  # Mengambil semua event
            if event.type == pygame.QUIT:  # Jika pengguna menutup jendela
                pygame.quit()  # Keluar dari Pygame
                sys.exit()  # Keluar dari program
                
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Jika ada klik mouse
                if event.button == 1:  # Klik kiri mouse
                    mouse_x, mouse_y = event.pos  # Ambil posisi klik
                    exit_button_rect = pygame.Rect(700, 20, 100, 50)  # Posisi dan ukuran tombol exit
                    if exit_button_rect.collidepoint(mouse_x, mouse_y):  # Jika klik di tombol exit
                        return  # Kembali ke menu utama

        # Mengambil input dari keyboard untuk menggerakkan keranjang
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:  # Jika tombol kiri ditekan dan keranjang tidak keluar layar
            basket_x -= BASKET_SPEED  # Gerakkan keranjang ke kiri
        if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - BASKET_WIDTH:  # Jika tombol kanan ditekan
            basket_x += BASKET_SPEED  # Gerakkan keranjang ke kanan

        # Update posisi objek yang jatuh
        object_y += OBJECT_FALL_SPEED  # Menggerakkan objek ke bawah

        # Membuat rectangle untuk keranjang dan objek
        basket_rect = pygame.Rect(basket_x, basket_y, BASKET_WIDTH, BASKET_HEIGHT)  # Rectangle keranjang
        object_rect = pygame.Rect(object_x, object_y, 200, 50)  # Rectangle objek rumus

        # Cek apakah keranjang dan objek bertabrakan
        if basket_rect.colliderect(object_rect):  # Jika terjadi tabrakan
            if rumus_text in rumus_benar:  # Jika rumus benar
                score += 10  # Tambah skor
                message = random.choice(ucapan_benar)  # Pilih ucapan positif
            else:  # Jika rumus salah
                salah_count += 1  # Tambah jumlah kesalahan
                message = random.choice(ucapan_salah)  # Pilih ucapan negatif

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        elif object_y > SCREEN_HEIGHT:  # Jika objek sudah keluar dari layar
            if rumus_text in rumus_benar:  # Jika rumus benar dan keluar dari layar
                salah_count += 1  # Tambah jumlah kesalahan
                message = ucapan_terlambat  # Tampilkan pesan terlambat

            # Ambil rumus baru untuk jatuh
            rumus_text = random.choice(rumus_benar + rumus_salah)  # Pilih rumus baru secara acak
            object_x = random.randint(0, SCREEN_WIDTH - 200)  # Atur posisi baru untuk objek
            object_y = -50  # Reset posisi objek di atas layar

        # Cek apakah ada pesan untuk ditampilkan
        if message:  # Jika ada pesan
            message_timer += 1  # Tambah timer pesan
            if message_timer >= 60:  # Tampilkan pesan selama 1 detik
                message = ""  # Reset pesan
                message_timer = 0  # Reset timer pesan

        # Jika jumlah kesalahan melebihi batas, tampilkan game over
        if salah_count >= max_salah:  # Jika mencapai jumlah kesalahan maksimal
            show_game_over_popup(nama, score)  # Tampilkan pop-up game over
            game_over = True  # Ubah status game menjadi game over

        # Menggambar semua elemen di layar
        screen.fill(WHITE)  # Mengisi layar dengan warna putih
        draw_basket(basket_x, basket_y)  # Menggambar keranjang
        draw_rumus(object_x, object_y, rumus_text)  # Menggambar objek rumus

        # Menampilkan pesan di layar
        message_surface = font.render(message, True, message_color)  # Render pesan
        screen.blit(message_surface, (SCREEN_WIDTH // 2 - message_surface.get_width() // 2, 50))  # Tampilkan pesan di tengah atas

        # Menampilkan skor dan jumlah kesalahan
        score_surface = font.render(f'Score: {score}', True, BLACK)  # Render skor
        screen.blit(score_surface, (10, 10))  # Tampilkan skor di pojok kiri atas

        salah_surface = font.render(f'Kesalahan: {salah_count}', True, BLACK)  # Render kesalahan
        screen.blit(salah_surface, (10, 50))  # Tampilkan jumlah kesalahan di bawah skor

        # Gambar tombol exit
        exit_button_rect = pygame.Rect(700, 20, 85, 50)  # Posisi dan ukuran tombol exit
        pygame.draw.rect(screen, WHITE, exit_button_rect)  # Gambar tombol exit
        pygame.draw.rect(screen, BLACK, exit_button_rect, 5)  # Kontur tombol exit
        exit_text = font.render('Exit', True, BLACK)  # Render teks 'Exit'
        screen.blit(exit_text, (exit_button_rect.x + 20, exit_button_rect.y + 10))  # Tampilkan teks di dalam tombol

        pygame.display.flip()  # Perbarui tampilan layar
        clock.tick(60)  # Atur FPS game

# Loop utama untuk menjalankan game
berjalan = True
while berjalan:  # Selama 'berjalan' bernilai True, loop akan terus berjalan
    for event in pygame.event.get():  # Mengambil semua event yang terjadi di Pygame
        if event.type == pygame.QUIT:  # Jika event yang diterima adalah QUIT (menutup jendela)
            pygame.quit()  # Menghentikan Pygame
            sys.exit()  # Menghentikan program secara keseluruhan

        if status_game == STATUS_MENU:  # Jika status game berada di menu utama
            if event.type == pygame.KEYDOWN:  # Jika ada event penekanan tombol
                if event.key == pygame.K_UP:  # Jika tombol UP ditekan
                    opsi_terpilih = (opsi_terpilih - 1) % len(opsi_menu)  # Pindah ke opsi menu sebelumnya
                elif event.key == pygame.K_DOWN:  # Jika tombol DOWN ditekan
                    opsi_terpilih = (opsi_terpilih + 1) % len(opsi_menu)  # Pindah ke opsi menu selanjutnya
                elif event.key == pygame.K_RETURN:  # Jika tombol ENTER ditekan
                    if opsi_terpilih == 0:  # Jika opsi yang dipilih adalah opsi pertama
                        status_game = STATUS_INPUT_NAMA_MODE  # Pindah ke status input nama
                    elif opsi_terpilih == 1:  # Jika opsi yang dipilih adalah opsi kedua
                        pygame.quit()  # Menghentikan Pygame
                        sys.exit()  # Menghentikan program secara keseluruhan
                    elif opsi_terpilih == 2:  # Jika opsi yang dipilih adalah opsi ketiga (Belajar Materi)
                        status_game = STATUS_MATERI  # Pindah ke status materi
                    elif opsi_terpilih == 3:
                        status_game = STATUS_LATIHAN

            # Tambahkan event untuk mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Jika ada klik mouse
                if event.button == 1:  # Jika tombol kiri mouse diklik
                    mouse_x, mouse_y = event.pos  # Ambil posisi klik mouse
                    for i, opsi in enumerate(opsi_menu):  # Iterasi melalui opsi menu
                        x, y = posisi_menu[opsi]  # Ambil posisi dari opsi menu
                        kotak_rect = pygame.Rect(x - 20, y - 10, font.render(opsi, True, HITAM).get_width() + 40,
                                                  font.render(opsi, True, HITAM).get_height() + 20)  # Membuat rectangle untuk opsi menu
                        if kotak_rect.collidepoint(mouse_x, mouse_y):  # Jika klik di dalam rectangle opsi menu
                            if i == 0:  # Jika opsi pertama (Mulai)
                                status_game = STATUS_INPUT_NAMA_MODE  # Pindah ke status input nama
                            elif i == 1:  # Jika opsi kedua (Keluar)
                                pygame.quit()  # Menghentikan Pygame
                                sys.exit()  # Menghentikan program secara keseluruhan
                            elif i == 2:  # Jika klik pada "Belajar Materi"
                                status_game = STATUS_MATERI  # Pindah ke status materi
                            elif i == 3:
                                status_game = STATUS_LATIHAN

        elif status_game == STATUS_INPUT_NAMA_MODE:  # Jika status game berada di mode input nama
            if event.type == pygame.KEYDOWN:  # Jika ada event penekanan tombol
                if event.key == pygame.K_RETURN and input_nama != '':  # Jika tombol ENTER ditekan dan input nama tidak kosong
                    # Lanjutkan ke pemilihan mode game
                    print(f"Nama: {input_nama}")  # Tampilkan nama di console
                elif event.key == pygame.K_BACKSPACE:  # Jika tombol BACKSPACE ditekan
                    input_nama = input_nama[:-1]  # Hapus karakter terakhir dari input nama
                elif len(input_nama) < maks_input:  # Jika panjang input nama kurang dari maksimum
                    input_nama += event.unicode  # Tambahkan karakter baru ke input nama

                # Pilihan mode game
                if event.key == pygame.K_UP:  # Jika tombol UP ditekan
                    opsi_mode_terpilih = (opsi_mode_terpilih - 1) % len(opsi_mode)  # Pindah ke mode sebelumnya
                elif event.key == pygame.K_DOWN:  # Jika tombol DOWN ditekan
                    opsi_mode_terpilih = (opsi_mode_terpilih + 1) % len(opsi_mode)  # Pindah ke mode selanjutnya
                elif event.key == pygame.K_RETURN:  # Jika tombol ENTER ditekan
                    mode_terpilih = opsi_mode[opsi_mode_terpilih]  # Ambil mode yang dipilih
                    print(f"Nama: {input_nama} - Mode: {mode_terpilih}")  # Tampilkan nama dan mode di console

                    # Tambahkan logika untuk mode yang dipilih
                    if mode_terpilih == 'Alat Ukur':  # Jika mode yang dipilih adalah 'Rumus'
                        game_alat_ukur(input_nama)  # Jalankan game Menangkap Rumus
                    elif mode_terpilih == '  Pokok  ':  # Jika mode yang dipilih adalah 'Pokok'
                        game_pokok(input_nama)  # Jalankan game Menangkap Massa
                    elif mode_terpilih == 'Turunan':  # Jika mode yang dipilih adalah 'Turunan'
                        game_turunan(input_nama)  # Jalankan game Menangkap Massa
                    elif mode_terpilih == 'Besaran Fisika':  # Jika mode yang dipilih adalah 'Besaran'
                        game_besaran_fisika(input_nama)  # Jalankan game Menangkap Besaran
                    elif mode_terpilih == 'Dimensi':  # Jika mode yang dipilih adalah 'Massa'
                        game_dimensi(input_nama)  # Jalankan game Menangkap Massa
                    elif mode_terpilih == 'Tokoh Fisika':  # Jika mode yang dipilih adalah 'Tokoh Fisika'
                        game_tokoh_fisika(input_nama)  # Jalankan game Menangkap Tokoh Fisika

            # Tambahkan event untuk mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Jika ada klik mouse
                if event.button == 1:  # Jika tombol kiri mouse diklik
                    mouse_x, mouse_y = event.pos  # Ambil posisi klik mouse
                    for i, mode in enumerate(opsi_mode):  # Iterasi melalui opsi mode
                        x, y = posisi_mode[mode]  # Ambil posisi dari opsi mode
                        kotak_rect = pygame.Rect(x - 20, y - 10, font_input.render(mode, True, HITAM).get_width() + 40,
                                                  font_input.render(mode, True, HITAM).get_height() + 20)  # Membuat rectangle untuk opsi mode
                        if kotak_rect.collidepoint(mouse_x, mouse_y):  # Jika klik di dalam rectangle opsi mode
                            mode_terpilih = opsi_mode[i]  # Ambil mode yang dipilih
                            print(f"Nama: {input_nama} - Mode: {mode_terpilih}")  # Tampilkan nama dan mode di console

                            if mode_terpilih == 'Alat Ukur':  # Jika mode yang dipilih adalah 'Rumus'
                                game_alat_ukur(input_nama)  # Jalankan game Menangkap Rumus
                            elif mode_terpilih == '  Pokok  ':  # Jika mode yang dipilih adalah 'Pokok'
                                game_pokok(input_nama)  # Jalankan game Menangkap Massa
                            elif mode_terpilih == 'Turunan':  # Jika mode yang dipilih adalah 'Turunan'
                                game_turunan(input_nama)  # Jalankan game Menangkap Massa
                            elif mode_terpilih == 'Besaran Fisika':  # Jika mode yang dipilih adalah 'Besaran'
                                game_besaran_fisika(input_nama)  # Jalankan game Menangkap Besaran
                            elif mode_terpilih == 'Dimensi':  # Jika mode yang dipilih adalah 'Massa'
                                game_dimensi(input_nama)  # Jalankan game Menangkap Massa
                            elif mode_terpilih == 'Tokoh Fisika':  # Jika mode yang dipilih adalah 'Tokoh Fisika'
                                game_tokoh_fisika(input_nama)  # Jalankan game Menangkap Tokoh Fisika

            # Cek jika tombol "Kembali" diklik
            button_rect = pygame.Rect(300, 400, 200, 50)  # Posisi tombol kembali yang sama dengan gambar
            if button_rect.collidepoint(mouse_x, mouse_y):
                status_game = STATUS_MENU  # Kembali ke menu utama
                input_nama = ''  # Reset input nama jika perlu

            # Tombol Kembali
            if status_game == STATUS_INPUT_NAMA_MODE and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_rect = pygame.Rect(250, 500, 300, 50)  # Posisi tombol kembali
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        status_game = STATUS_MENU  # Kembali ke menu

        # Cek untuk tombol kembali di STATUS_MATERI
        elif status_game == STATUS_MATERI:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    button_rect = pygame.Rect(250, 500, 300, 50)  # Posisi tombol Kembali
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        status_game = STATUS_MENU  # Kembali ke menu utama

        # Cek untuk tombol kembali di STATUS_MATERI
        elif status_game == STATUS_LATIHAN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    button_rect = pygame.Rect(250, 500, 300, 50)  # Posisi tombol Kembali
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        status_game = STATUS_MENU  # Kembali ke menu utama

            # Tombol Kembali
            if status_game == STATUS_INPUT_NAMA_MODE and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_rect = pygame.Rect(250, 500, 300, 50)
                if button_rect.collidepoint(mouse_x, mouse_y):
                    status_game = STATUS_MENU  # Kembali ke menu
            
            # Kembali ke menu dari materi
            if status_game == STATUS_MATERI and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_rect = pygame.Rect(250, 500, 300, 50)  # Posisi tombol Kembali
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        status_game = STATUS_MENU  # Kembali ke menu

            # Kembali ke menu dari materi
            if status_game == STATUS_LATIHAN and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_rect = pygame.Rect(250, 500, 300, 50)  # Posisi tombol Kembali
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        status_game = STATUS_MENU  # Kembali ke menu

    # Gambar menu sesuai status game
    if status_game == STATUS_MENU:
        gambar_menu(opsi_terpilih)
    elif status_game == STATUS_INPUT_NAMA_MODE:
        gambar_input_nama_mode(input_nama, opsi_mode_terpilih)
    elif status_game == STATUS_MATERI:
        gambar_materi()
    elif status_game == STATUS_LATIHAN:
        gambar_latihan()

    pygame.display.flip()


from telebot import *
import re
import random
import joblib
import os
import mysql.connector

api = 'YOUR API'
bot = TeleBot(api)

db_connection = mysql.connector.connect(
    host="YOUR HOST",
    user="YOUR USER",
    password="YOUR DB PASSWORD",
    database="YOUR DATABASE NAME"
)
db_cursor = db_connection.cursor()

model = joblib.load(open('decision_tree_model.h5', 'rb'))

# start
@bot.message_handler(commands=['start'])
def mulai(message):
    chatid = message.chat.id
    bot.send_message(chatid, 'Halo! Selamat datang di Pantau Stunting Bot')
    kirim_menu(chatid)

def kirim_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton('/cek_status_gizi_balita')
    item2 = types.KeyboardButton('/tanya_jawab_gizi_balita')
    item3 = types.KeyboardButton('/informasi_gizi_balita')
    item4 = types.KeyboardButton('/kembali')
    markup.add(item1, item2)
    markup.add(item3,item4)
    bot.send_message(chat_id, 'Apakah ada yang dapat saya bantu dengan layanan fitur Pantau Stunting: \n /cek_status_gizi_balita \n /tanya_jawab_gizi_balita \n /informasi_gizi_balita \nJika tidak ada, Terima Kasih telah menggunakan Pantau Stunting. Semoga bot ini selalu membantu Ibu/Bapak dalam memantau gizi Balita 🙏🏻 ', reply_markup=markup)

@bot.message_handler(commands=['kembali'])
def kembali_ke_menu_utama(message):
    chat_id = message.chat.id
    kirim_menu(chat_id)

data = {}
#Fitur Deteksi Status Gizi Balita
@bot.message_handler(commands=['cek_status_gizi_balita'])
def awalan(message):
    chat_id = message.chat.id
    data[chat_id] = {}
    msg = bot.send_message(message.chat.id, f"Silahkan isi data balita sesuai format.\nMasukkan Nama Balita:")
    bot.register_next_step_handler(msg, proses_nama)

def proses_nama(message):
    chat_id = message.chat.id
    text_lower = message.text.lower()  # Mengubah teks pesan menjadi huruf kecil
    if text_lower == 'kembali'or text_lower == '/kembali':
        kirim_menu(chat_id)
    elif text_lower == '/tanya_jawab_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/cek_status_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/informasi_gizi_balita':
        kirim_menu(chat_id)
    else:
        data[chat_id]['nama'] = message.text
        msg = bot.send_message(chat_id, f"Masukkan Kota tinggal Balita:")
        bot.register_next_step_handler(msg, proses_kota)

def proses_kota(message):
    chat_id = message.chat.id
    text_lower = message.text.lower()  # Mengubah teks pesan menjadi huruf kecil

    #Logika
    if text_lower == 'kembali'or text_lower == '/kembali':
        kirim_menu(chat_id)
    elif text_lower == '/tanya_jawab_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/cek_status_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/informasi_gizi_balita':
        kirim_menu(chat_id)
    else:
        data[chat_id]['kota'] = message.text
        msg = bot.send_message(chat_id, f"Masukkan Usia Balita (Ketik dalam Bulan):")
        bot.register_next_step_handler(msg, proses_usia)

def proses_usia(message):
    chat_id = message.chat.id
    usia_input = message.text.replace(',', '.')
    text_lower = message.text.lower()  # Mengubah teks pesan menjadi huruf kecil

    #Logika
    if text_lower == 'kembali'or text_lower == '/kembali':
        kirim_menu(chat_id)
    elif text_lower == '/tanya_jawab_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/cek_status_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/informasi_gizi_balita':
        kirim_menu(chat_id)
    else:
        # Menggunakan regular expression untuk mencari angka dalam input
        angka_usia = re.search(r'(\d+\.\d+|\d+)', usia_input)

        if angka_usia:
            angka_usia = angka_usia.group()  # Mengambil empat angka pertama yang ditemukan
            data[chat_id]['usia'] = float(angka_usia)
            msg = bot.send_message(chat_id, f"Masukkan Jenis Kelamin Balita:")
            bot.register_next_step_handler(msg, proses_JK)
        else:
            msg = bot.send_message(chat_id, "Mohon masukkan usia balita dalam format angka. Contoh: 23 Bulan")
            bot.register_next_step_handler(msg, proses_usia)
            return

def proses_JK(message):
    chat_id = message.chat.id
    text_lower = message.text.lower()  # Mengubah teks pesan menjadi huruf kecil
    jk_input = message.text.lower()

        #Logika
    if text_lower == 'kembali'or text_lower == '/kembali':
        kirim_menu(chat_id)
    elif text_lower == '/tanya_jawab_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/cek_status_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/informasi_gizi_balita':
        kirim_menu(chat_id)
    else:
        if 'laki-laki' in jk_input:
            jenis_kelamin = 'L'
        elif 'laki - laki' in jk_input:
            jenis_kelamin = 'L'
        elif 'laki' in jk_input:
            jenis_kelamin = 'L'
        elif 'l' in jk_input:
            jenis_kelamin = 'L'
        elif 'cowo' in jk_input:
            jenis_kelamin = 'L'
        elif 'cowok' in jk_input:
            jenis_kelamin = 'L'
        elif 'perempuan' in jk_input:
            jenis_kelamin = 'P'
        elif 'p' in jk_input:
            jenis_kelamin = 'P'
        elif 'cewe' in jk_input:
            jenis_kelamin = 'P'
        elif 'cewek' in jk_input:
            jenis_kelamin = 'P'
        else:
            msg = bot.send_message(chat_id, "Mohon masukkan Jenis Kelamin balita  (L/P/Cowok/Cewek).")
            bot.register_next_step_handler(msg, proses_JK)
            return
    data[chat_id]['jenis_kelamin'] = jenis_kelamin
    msg = bot.send_message(chat_id, f"Masukkan Berat Badan Balita (Ketik dalam (Kg)):")
    bot.register_next_step_handler(msg, proses_BB)

def proses_BB(message):
    chat_id = message.chat.id
    bb_input = message.text.replace(',', '.')

    text_lower = message.text.lower()  # Mengubah teks pesan menjadi huruf kecil

    #Logika
    if text_lower == 'kembali'or text_lower == '/kembali':
        kirim_menu(chat_id)
    elif text_lower == '/tanya_jawab_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/cek_status_gizi_balita':
        kirim_menu(chat_id)
    elif text_lower == '/informasi_gizi_balita':
        kirim_menu(chat_id)
    else:
        # Menggunakan regular expression untuk mencari angka dalam input
        angka_bb = re.search(r'(\d+\.\d+|\d+)', bb_input)

        if angka_bb:
            angka_bb = angka_bb.group()
            data[chat_id]['berat_badan'] = float(angka_bb)
            msg = bot.send_message(chat_id, f"Masukkan Tinggi Badan Balita (Ketik dalam (cm)):")
            bot.register_next_step_handler(msg, proses_TB)
        else:
            msg = bot.send_message(chat_id, "Mohon masukkan berat badan balita dalam format angka. Contoh: 10 Kg")
            bot.register_next_step_handler(msg, proses_BB)
            return

def proses_TB(message):
    chat_id = message.chat.id
    tb_input = message.text.replace(',', '.')
    # Menggunakan regular expression untuk mencari angka dalam input
    angka_tb = re.search(r'(\d+\.\d+|\d+)', tb_input)

    if angka_tb:
        angka_tb = angka_tb.group()
        data[chat_id]['tinggi_badan'] = float(angka_tb)

        if data[chat_id]['jenis_kelamin'] == "L":
            jk = 0
        else:
            jk = 1

        X_new = [[data[chat_id]['usia'], jk, data[chat_id]['berat_badan'], data[chat_id]['tinggi_badan']]]
        BBU, TBU, BBTB = model.predict(X_new)[0]
        status_gizi = classify_status_gizi(BBU, TBU, BBTB)  # Fungsi untuk mengklasifikasikan status gizi
        saran_rekomendasi = rekomendasi_ahli(BBU, TBU, data[chat_id]['usia'])
        kesimpulan_status = kesimpulan(BBU, TBU)

        #save_to_database(data[chat_id]['nama'], data[chat_id]['kota'], data[chat_id]['usia'], data[chat_id]['jenis_kelamin'], data[chat_id]['berat_badan'], data[chat_id]['tinggi_badan'], status_gizi, kesimpulan_status, saran_rekomendasi)

        bot.send_message(chat_id, f"Halo, Balita dengan\nNama: <b>{data[chat_id]['nama']}</b>\nKota Tinggal: <b>{data[chat_id]['kota']}</b>\nUsia: <b>{data[chat_id]['usia']} Bulan</b>\nJenis Kelamin: <b>{data[chat_id]['jenis_kelamin']}</b>\nBerat Badan: <b>{data[chat_id]['berat_badan']} Kg</b>\nTinggi Badan: <b>{data[chat_id]['tinggi_badan']} Cm</b>\n\nBerstatus Gizi : <b>{kesimpulan_status}</b>", parse_mode="HTML") #hasil klasifikasi
        bot.send_message(chat_id, f"<b>Rekomendasi Ahli Gizi:</b>{saran_rekomendasi}", parse_mode = "HTML")
        data.pop(chat_id, None)
        kirim_menu(chat_id)
    else:
        msg = bot.send_message(chat_id, "Mohon masukkan tinggi badan balita dalam format angka. Contoh: 80")
        bot.register_next_step_handler(msg, proses_TB)


def save_to_database(nama, kota, usia, jenis_kelamin, berat_badan, tinggi_badan, status_gizi, kesimpulan_status, saran_rekomendasi):
    sql_insert = "INSERT INTO statusgizi (nama_balita, kota, usia, jenis_kelamin, berat_badan, tinggi_badan, bbu_status, tbu_status, bbtb_status, kesimpulan_status, saran_ahli) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val_insert = (
        nama, kota, usia, jenis_kelamin, berat_badan, tinggi_badan,
        status_gizi['BBU'], status_gizi['TBU'], status_gizi['BBTB'], kesimpulan_status,
        saran_rekomendasi)
    db_cursor.execute(sql_insert, val_insert)
    db_connection.commit()

def kesimpulan(BBU, TBU):
    if BBU == "Risiko Berat Badan Lebih" and TBU == "Sangat Pendek":
        status = 'Risiko Berat Badan Lebih dan Tinggi Badan jauh di bawah batas normal atau Sangat Pendek (Severely Stunted)'
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Tinggi":
        status = 'Risiko Berat Badan Lebih dan Tinggi Badan di atas batas normal (Tinggi)'
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Normal":
        status = 'Risiko Berat Badan Lebih dan Tinggi Badan Normal'
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Pendek":
        status = 'Risiko Berat Badan Lebih dan Tinggi Badan di bawah batas normal atau Pendek (Stunted)'

    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Sangat Pendek":
        status = 'Berat Badan Sangat Kurang dan Tinggi Badan jauh di bawah batas normal atau Sangat Pendek (Severely Stunted)'
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Tinggi":
        status = 'Berat Badan Sangat Kurang dan Tinggi Badan di atas batas normal (Tinggi)'
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Normal":
        status = 'Berat Badan Sangat Kurang dan Tinggi Badan Normal'
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Pendek":
        status = 'Berat Badan Sangat Kurang dan Tinggi Badan di bawah batas normal atau Pendek (Stunted)'

    elif BBU == "Berat Badan Normal" and TBU == "Sangat Pendek":
        status = 'Berat Badan Normal dan Tinggi Badan jauh di bawah batas normal atau Sangat Pendek (Severely Stunted)'
    elif BBU == "Berat Badan Normal" and TBU == "Tinggi":
        status = 'Berat Badan Normal dan Tinggi Badan di atas batas normal (Tinggi)'
    elif BBU == "Berat Badan Normal" and TBU == "Normal":
        status = 'Berat Badan Normal dan Tinggi Badan Normal'
    elif BBU == "Berat Badan Normal" and TBU == "Pendek":
        status = 'Berat Badan Normal dan Tinggi Badan di bawah batas normal atau Pendek (Stunted)'

    elif BBU == "Berat Badan Kurang" and TBU == "Sangat Pendek":
        status = 'Berat Badan Kurang dan Tinggi Badan jauh di bawah batas normal atau Sangat Pendek (Severely Stunted)'
    elif BBU == "Berat Badan Kurang" and TBU == "Tinggi":
        status = 'Berat Badan Kurang dan Tinggi Badan di atas batas normal (Tinggi)'
    elif BBU == "Berat Badan Kurang" and TBU == "Normal":
        status = 'Berat Badan Kurang dan Tinggi Badan Normal'
    elif BBU == "Berat Badan Kurang" and TBU == "Pendek":
        status = 'Berat Badan Kurang dan Tinggi Badan di bawah batas normal atau Pendek (Stunted)'
    return status


def classify_status_gizi(BBU, TBU, BBTB):
    if BBU == "Risiko Berat Badan Lebih":
        status_bbu = 'Risiko Berat Badan Lebih'
    elif  BBU == "Berat Badan Sangat Kurang" :
        status_bbu = 'Berat Badan Sangat Kurang'
    elif BBU == "Berat Badan Normal" :
        status_bbu = 'Berat Badan Normal'
    else:
        status_bbu = 'Berat Badan Kurang'

    if TBU == "Sangat Pendek":
        status_tbu = 'Sangat Pendek'
    elif TBU == "Tinggi":
        status_tbu = 'Tinggi'
    elif TBU == "Normal":
        status_tbu = 'Normal'
    else:
        status_tbu = 'Pendek'

    if BBTB == "Obesitas":
        status_bbtb = 'Obesitas'
    elif BBTB == "Gizi Buruk":
        status_bbtb = 'Gizi Buruk'
    elif BBTB == "Berisiko Gizi Lebih":
        status_bbtb = 'Berisiko Gizi Lebih'
    elif BBTB == "Gizi baik":
        status_bbtb = 'Gizi Baik'
    elif BBTB == "Gizi Lebih":
        status_bbtb = 'Gizi Lebih'
    else:
        status_bbtb = 'Gizi Kurang'
    return{
        'BBU': status_bbu,
        'TBU': status_tbu,
        'BBTB': status_bbtb
    }


def rekomendasi_ahli(BBU, TBU, usia):

    rekomendasi = ""

    #Logika untuk "Risiko BB Lebih dan Sangat Pendek"
    if BBU == "Risiko Berat Badan Lebih" and TBU == "Sangat Pendek" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Sangat Pendek" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam). Berikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 2-3 kali sehari, tergantung napsu makan, berikan 1-2 kali selingan"
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Sangat Pendek" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 2-3 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Sangat Pendek" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Sangat Pendek" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Sangat Pendek" and usia >= 25 and usia <= 60:
        rekomendasi += "\nOptimalkan asupan gizi seimbang sesuai dengan anjuran 'isi piringku' disertai pemberian protein hewani dan nabati tambahan seperti (rolade ikan, nugget ikan/ayam dengan sayur, perkedel tahu/tempe, pudding susu). Berikan suplemen tambahan sebagai upaya tumbuh kembang yang optimal pada anak seperti Vitamin A, Zinc, Zat Besi, Kalsium, dan Yodium sesuai anjuran dokter gizi. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan: Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa. Batasi konsumsi makanan berlemak tinggi, makanan terlalu manis dan terlalu asin. Pemberian porsi makan sebanyak 5 kali sehari (3 kali makan berat dan 2 kali makan selingan/camilan)."

    #Logika untuk "Risiko BB Lebih dan Pendek"
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Pendek" and usia <= 5:
        rekomendasi += "\nPemberian ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Pendek" and usia == 6:
        rekomendasi += "\nPemberian ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan :\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam). Berikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 2-3 kali sehari, tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Pendek" and usia >= 7 and usia <= 8:
        rekomendasi += "\nPemberian ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan :\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam)."
        rekomendasi += "\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 2-3 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Pendek" and usia >= 9 and usia <= 11:
        rekomendasi += "\nPemberian ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan :\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam)."
        rekomendasi += "\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Pendek" and usia >= 12 and usia <= 24:
        rekomendasi += "\nPemberian ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan :\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam)."
        rekomendasi += "\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Pendek" and usia >= 25 and usia <= 60:
        rekomendasi += "\nOptimalkan asupan gizi seimbang sesuai dengan anjuran 'isi piringku' disertai pemberian protein hewani dan nabati tambahan seperti (rolade ikan, nugget ikan/ayam dengan sayur, perkedel tahu/tempe, pudding susu). Berikan suplemen tambahan sebagai upaya tumbuh kembang yang optimal pada anak seperti Vitamin A, Zinc, Zat Besi, Kalsium, dan Yodium sesuai anjuran dokter gizi. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. "
        rekomendasi += "\n\n*Catatan: Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa. Batasi konsumsi makanan berlemak tinggi, makanan terlalu manis dan terlalu asin. Pemberian porsi makan sebanyak 5 kali sehari (3 kali makan berat dan 2 kali makan selingan/camilan)."

    #Logika untuk "Risiko BB Lebih dan Normal"
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Normal" and usia <= 5:
        rekomendasi += "\nBeriksn ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Normal" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 2-3 kali sehari, tergantung napsu makan, berikan 1-2 kali selingan"
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Normal" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan (balita stunting):\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 2-3 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Normal" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan (balita stunting):\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Normal" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan (balita stunting):\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Normal" and usia >= 25 and usia <= 60:
        rekomendasi += "\nBerikan asupan gizi seimbang sesuai dengan anjuran 'isi piringku'. Ajak anak untuk melakukan aktivitas fisik ringan untuk olah stimulasi misalnya bermain sembari berolahraga. Berikan porsi makan yang sesuai dengan kebutuhan per hari. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan: Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa. Batasi konsumsi makanan berlemak tinggi, makanan terlalu manis dan terlalu asin. Pemberian porsi makan sebanyak 4-5 kali sehari (3 kali makan berat dan 1-2 kali makan selingan/camilan)."


    #Logika untuk "Risiko BB Lebih dan Tinggi"
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Tinggi" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Tinggi" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 2-3 kali sehari, tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Tinggi" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan (balita stunting):\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 2-3 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Tinggi" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan (balita stunting):\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Tinggi" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan (balita stunting):\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Risiko Berat Badan Lebih" and TBU == "Tinggi" and usia >= 25 and usia <= 60:
        rekomendasi += "\nBerikan asupan gizi seimbang sesuai dengan anjuran 'isi piringku'. Batasi konsumsi makanan terlalu berlemak, terlalu asin, terlalu manis. Ajak anak untuk melakukan aktivitas fisik misalnya bermain dan berolahraga ringan. Berikan porsi makan yang sesuai dengan kebutuhan per hari (porsi makan sebanyak 4-5 kali sehari (3 kali makan berat dan 1-2 kali makan selingan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan: Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa. Batasi konsumsi makanan berlemak tinggi, makanan terlalu manis dan terlalu asin. Pemberian porsi makan sebanyak 4-5 kali sehari (3 kali makan berat dan 1-2 kali makan selingan/camilan)."


    #Logika untuk "BB Normal dan Sangat Pendek"
    elif BBU == "Berat Badan Normal" and TBU == "Sangat Pendek" and usia <= 5:
        rekomendasi += "\nOptimalkan pemberian ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Berat Badan Normal" and TBU == "Sangat Pendek" and usia == 6:
        rekomendasi += "\nOptimalkan pemberian ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan :\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam). Berikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 2-3 kali sehari, tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Sangat Pendek" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 2-3 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Berat Badan Normal" and TBU == "Sangat Pendek" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Sangat Pendek" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Sangat Pendek" and usia >= 25 and usia <= 60:
        rekomendasi += "\nOptimalkan asupan gizi seimbang sesuai dengan anjuran 'isi piringku' disertai pemberian protein hewani dan nabati tambahan seperti (rolade ikan, nugget ikan/ayam dengan sayur, perkedel tahu/tempe, pudding susu). Berikan suplemen tambahan sebagai upaya tumbuh kembang yang optimal pada anak seperti Vitamin A, Zinc, Zat Besi, Kalsium, dan Yodium sesuai anjuran dokter gizi. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan: Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa. Perbanyak konsumsi sayur dan buah."

    #Logika untuk "BB Normal dan Pendek"
    elif BBU == "Berat Badan Normal" and TBU == "Pendek" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Berat Badan Normal" and TBU == "Pendek" and usia == 6 :
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam). Berikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 2-3 kali sehari, tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Pendek" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 2-3 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Berat Badan Normal" and TBU == "Pendek" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Pendek" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Pendek" and usia >= 25 and usia <= 60:
        rekomendasi += "\nOptimalkan asupan gizi seimbang sesuai dengan anjuran 'isi piringku' disertai pemberian protein hewani dan nabati tambahan seperti (rolade ikan, nugget ikan/ayam dengan sayur, perkedel tahu/tempe, pudding susu). Berikan suplemen tambahan sebagai upaya tumbuh kembang yang optimal pada anak seperti Vitamin A, Zinc, Zat Besi, Kalsium, dan Yodium sesuai anjuran dokter gizi. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan: Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa. Perbanyak konsumsi sayur dan buah."

    #Logika untuk "BB Normal dan Normal"
    elif BBU == "Berat Badan Normal" and TBU == "Normal" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Berat Badan Normal" and TBU == "Normal" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 2-3 kali sehari, tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Normal" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan:\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 2-3 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Berat Badan Normal" and TBU == "Normal" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan:\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Normal" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan:\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Normal" and usia >= 25 and usia <= 60:
        rekomendasi += "\nBerikan asupan gizi seimbang sesuai dengan anjuran 'isi piringku'. Ajak anak untuk melakukan aktivitas fisik ringan untuk olah stimulasi misalnya bermain sembari berolahraga. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\nCatatan: Berikan porsi makan yang sesuai dengan kebutuhan per hari (porsi makan sebanyak 5 kali sehari, terdiri dari 3 kali makan berat dan 2 kali makan selingan).Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa."

    #Logika untuk "BB Normal dan Tinggi"
    elif BBU == "Berat Badan Normal" and TBU == "Tinggi" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Berat Badan Normal" and TBU == "Tinggi" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 2-3 kali sehari, tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Tinggi" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan:\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 2-3 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Berat Badan Normal" and TBU == "Tinggi" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan:\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Tinggi" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan:\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Normal" and TBU == "Tinggi" and usia >= 25 and usia <= 60:
        rekomendasi += "\nBerikan asupan gizi seimbang sesuai dengan anjuran 'isi piringku'. Ajak anak untuk melakukan aktivitas fisik ringan untuk olah stimulasi misalnya bermain sembari berolahraga. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan: Berikan porsi makan yang sesuai dengan kebutuhan per hari (porsi makan sebanyak 5 kali sehari, terdiri dari 3 kali makan berat dan 2 kali makan selingan).Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa."

    #Logika untuk "BB Kurang dan Sangat Pendek"
    elif BBU == "Berat Badan Kurang" and TBU == "Sangat Pendek" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Berat Badan Kurang" and TBU == "Sangat Pendek" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam). Berikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Sangat Pendek" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Berat Badan Kurang" and TBU == "Sangat Pendek" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Sangat Pendek" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 4-5 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Sangat Pendek" and usia >= 25 and usia <= 60:
        rekomendasi += "\nOptimalkan asupan gizi seimbang sesuai dengan anjuran 'isi piringku' disertai pemberian protein hewani dan nabati tambahan seperti (rolade ikan, nugget ikan/ayam dengan sayur, perkedel tahu/tempe, pudding susu). Berikan suplemen tambahan sebagai upaya tumbuh kembang yang optimal pada anak seperti Vitamin A, Zinc, Zat Besi, Kalsium, dan Yodium sesuai anjuran dokter gizi. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan:\nMemperbanyak variasi menu makanan bagi anak agar napsu makan anak meningkat. Pemberian porsi makan sebanyak 6 kali sehari (3 kali makan berat dan 3 kali makan selingan/camilan)."

    #Logika untuk "BB Kurang dan Pendek"
    elif BBU == "Berat Badan Kurang" and TBU == "Pendek" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Berat Badan Kurang" and TBU == "Pendek" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam). Berikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Pendek" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah) Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Berat Badan Kurang" and TBU == "Pendek" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Pendek" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 4-5 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Pendek" and usia >= 25 and usia <= 60:
        rekomendasi += "\nOptimalkan asupan gizi seimbang sesuai dengan anjuran 'isi piringku' disertai pemberian protein hewani dan nabati tambahan seperti (rolade ikan, nugget ikan/ayam dengan sayur, perkedel tahu/tempe, pudding susu). Berikan suplemen tambahan sebagai upaya tumbuh kembang yang optimal pada anak seperti Vitamin A, Zinc, Zat Besi, Kalsium, dan Yodium sesuai anjuran dokter gizi. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan:\nMemperbanyak variasi menu makanan bagi anak agar napsu makan anak meningkat. Pemberian porsi makan sebanyak 6 kali sehari (3 kali makan berat dan 3 kali makan selingan/camilan)."

    #Logika untuk "BB Kurang dan Normal"
    elif BBU == "Berat Badan Kurang" and TBU == "Normal" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Berat Badan Kurang" and TBU == "Normal" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Normal" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan:\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Berat Badan Kurang" and TBU == "Normal" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan:\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Normal" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan:\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 4-5 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Normal" and usia >= 25 and usia <= 60:
        rekomendasi += "\nBerikan asupan gizi seimbang sesuai dengan anjuran 'isi piringku'. Memperbanyak variasi menu makanan bagi anak agar napsu makan anak meningkat. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan:\nBerikan porsi makan yang sesuai dengan kebutuhan per hari (porsi makan sebanyak 6 kali sehari, terdiri dari 3 kali makan berat dan 3 kali makan selingan).Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa."

    #Logika untuk "BB Kurang dan Tinggi"
    elif BBU == "Berat Badan Kurang" and TBU == "Tinggi" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif BBU == "Berat Badan Kurang" and TBU == "Tinggi" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, Berikan 2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Tinggi" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan:\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif BBU == "Berat Badan Kurang" and TBU == "Tinggi" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan:\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Tinggi" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan:\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 4-5 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif BBU == "Berat Badan Kurang" and TBU == "Tinggi" and usia >= 25 and usia <= 60:
        rekomendasi += "\nBerikan asupan gizi seimbang sesuai dengan anjuran 'isi piringku'. Memperbanyak variasi menu makanan bagi anak agar napsu makan anak meningkat. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan:\nBerikan porsi makan yang sesuai dengan kebutuhan per hari (porsi makan sebanyak 6 kali sehari, terdiri dari 3 kali makan berat dan 3 kali makan selingan).Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa."


    #Logika untuk "BB Sangat Kurang dan Sangat Pendek"
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Sangat Pendek" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Sangat Pendek" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam). Berikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Sangat Pendek" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Sangat Pendek" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Sangat Pendek" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 4-5 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Sangat Pendek" and usia >= 25 and usia <= 60:
        rekomendasi += "\nOptimalkan asupan gizi seimbang sesuai dengan anjuran 'isi piringku' disertai pemberian protein hewani dan nabati tambahan seperti (rolade ikan, nugget ikan/ayam dengan sayur, perkedel tahu/tempe, pudding susu). Berikan suplemen tambahan sebagai upaya tumbuh kembang yang optimal pada anak seperti Vitamin A, Zinc, Zat Besi, Kalsium, dan Yodium sesuai anjuran dokter gizi. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan:\nMemperbanyak variasi menu makanan bagi anak agar napsu makan anak meningkat. Pemberian porsi makan sebanyak 6 kali sehari (3 kali makan berat dan 3 kali makan selingan/camilan)."

    #Logika untuk "BB Sangat Kurang dan Pendek"
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Pendek" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Pendek" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan asupan makanan dengan protein tinggi (telur, tahu, tempe, ikan, udang, ayam). Berikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Pendek" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Pendek" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Pendek" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Berikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan (balita stunting):\nBerikan asupan makanan dengan protein tinggi (kuning telur, tahu, tempe, ikan, udang)."
        rekomendasi += "\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 4-5 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Pendek" and usia >= 25 and usia <= 60:
        rekomendasi += "\nOptimalkan asupan gizi seimbang sesuai dengan anjuran 'isi piringku' disertai pemberian protein hewani dan nabati tambahan seperti (rolade ikan, nugget ikan/ayam dengan sayur, perkedel tahu/tempe, pudding susu). Berikan suplemen tambahan sebagai upaya tumbuh kembang yang optimal pada anak seperti Vitamin A, Zinc, Zat Besi, Kalsium, dan Yodium sesuai anjuran dokter gizi. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan:\nMemperbanyak variasi menu makanan bagi anak agar napsu makan anak meningkat. Pemberian porsi makan sebanyak 6 kali sehari (3 kali makan berat dan 3 kali makan selingan/camilan)."

    #Logika untuk "BB Sangat Kurang dan Normal"
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Normal" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Normal" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 2-3 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Normal" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan:\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Normal" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 9-11 bulan:\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Normal" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 12-24 bulan:\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 4-5 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Normal" and usia >= 25 and usia <= 60:
        rekomendasi += "\nBerikan asupan gizi seimbang sesuai dengan anjuran 'isi piringku'. Ajak anak untuk melakukan aktivitas fisik ringan untuk olah stimulasi misalnya bermain sembari berolahraga. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan:\nBerikan porsi makan yang sesuai dengan kebutuhan per hari (porsi makan sebanyak 5 kali sehari, terdiri dari 3 kali makan berat dan 2 kali makan selingan).Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa."

    #Logika untuk "BB Sangat Kurang dan Tinggi"
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Tinggi" and usia <= 5:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Tinggi" and usia == 6:
        rekomendasi += "\nBerikan ASI eksklusif (minimal 8 kali sehari) dan rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat. Pada usia 6 bulan mulai dapat diberikan makanan pendamping ASI (MPASI) sebagai pengenalan tekstur makanan tahap awal."
        rekomendasi += "\n*Pedoman Pemberian Makanan Anak usia 6 bulan:\nBerikan 1 jenis bahan dasar yang dilumatkan, sebagai pengenalan rasa. Porsi makan diberikan bertahap. Frekuensi makan 3-4 kali tergantung napsu makan, berikan 2-3 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Tinggi" and usia >= 7 and usia <= 8:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan:\nBerikan 2 jenis bahan dasar makanan (dapat dicampur atau dipisah). Frekuensi makan 3-4 kali tergantung napsu makan, berikan 1-2 kali selingan. Porsi makan bertahap."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Tinggi" and usia >= 9 and usia <= 11:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan:\nBerikan 3-4 jenis bahan dasar (dapat dicampur atau dipisah). Tekstur makanan ditingkatkan bertahap. Frekuensi makan 4 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Tinggi" and usia >= 12 and usia <= 24:
        rekomendasi += "\nBerikan ASI setidaknya 2 kali sehari disertai pemberian Makanan Pendamping ASI (MPASI). Berikan satu jenis makanan pengenal untuk anak seperti buah/sayur yang dilumatkan (dihaluskan). Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Pedoman Pemberian Makanan Anak usia 7-8 bulan:\nDapat diberikan makanan keluarga, makanan bertekstur padat, porsi makan dapat disesuaikan. Frekuensi makan 4-5 kali tergantung napsu makan, berikan 1-2 kali selingan."
    elif  BBU == "Berat Badan Sangat Kurang" and TBU == "Tinggi" and usia >= 25 and usia <= 60:
        rekomendasi += "\nBerikan asupan gizi seimbang sesuai dengan anjuran 'isi piringku'. Memperbanyak variasi menu makanan agar napsu makan meningkat. Rutin melakukan pemeriksaan fisik pada anak di posyandu/puskesmas/klinik terdekat."
        rekomendasi += "\n\n*Catatan:\nBerikan porsi makan yang sesuai dengan kebutuhan per hari (porsi makan sebanyak 5 kali sehari, terdiri dari 3 kali makan berat dan 2 kali makan selingan).Batasi penggunaan garam dan gula pada menu makanan, agar tidak terjadi penyakit serius ketika dewasa."

    else: None

    return rekomendasi

#Fitur Tanya Jawab
@bot.message_handler(commands=['tanya_jawab_gizi_balita'])
def tanya_jawab_gizi_balita(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Selamat datang di fitur Tanya Jawab Gizi Balita! Pada fitur ini dikhususkan untuk pertanyaan seputar stunting")
    bot.send_message(chat_id, "Silakan ajukan pertanyaan. \nKirim pesan 'kembali' atau klik tombol '/kembali' jika ingin ke menu utama.")
    bot.register_next_step_handler(message, proses_pertanyaan)

def jawab_pertanyaan(pertanyaan, chat_id):
    if 'status gizi' in pertanyaan:
        jawaban = "Status Gizi balita menurut kemenkes merupakan keadaan tubuh akibat dari pengaturan proses tubuh melalui konsumsi makanan, pertumbuhan, dan pemeliharaan jaringan tubuh pada anak usia 0-59 Bulan. Gizi Balita yang baik melibatkan asupan nutrisi yang cukup untuk mendukung pertumbuhan dan perkembangannya. Pastikan juga balita mendapatkan asupan cairan yang cukup."
    elif 'ciri stunting' in pertanyaan or 'ciri-ciri stunting' in pertanyaan:
        jawaban = "Ciri-ciri balita stunting antara lain yaitu berat badan lebih rendah dibanding anak se-usianya dan proporsi tubuh cenderung normal tetapi tampak lebih kecil dari se-usianya."
    elif 'dampak stunting' in pertanyaan:
        jawaban = "Dampak stunting yaitu terhambatnya perkembangan kecerdasan yang mempengaruhi kemampuan atau produktivitas dan kreativitas anak se-usianya."
    elif 'penyebab balita stunting' in pertanyaan or 'penyebab stunting' in pertanyaan or 'faktor balita stunting' in pertanyaan or 'faktor stunting' in pertanyaan or 'faktor yang mempengaruhi stunting' in pertanyaan or 'faktor yang memengaruhi stunting' in pertanyaan or 'faktor yang mempengaruhi balita stunting' in pertanyaan or 'faktor yang memengaruhi balita stunting' in pertanyaan:
        jawaban = "Beberapa faktor penyebab stunting antara lain yaitu perekonomian keluarga, pengaruh genetik (keturunan), kondisi lingkungan, penyakit atau infeksi yang terjadi berkali-kali."
    elif 'pencegahan stunting' in pertanyaan or 'cara mencegah stunting' in pertanyaan or 'tips mencegah stunting' in pertanyaan:
        jawaban = "Pencegahan terhadap stunting antara lain yaitu menjalankan pola hidup sehat (konsumsi makanan gizi seimbang), pemenuhan nutrisi pada 1000 hari pertama kehidupan anak, perbaiki pola asuh dalam praktek pemberian makan bagi bayi dan balita, menjaga kebersihan diri dan keluarga, dan rutin melakukan imunisasi serta vaksinasi pada anak."
    elif 'tips mengatasi stunting' in pertanyaan or 'cara mengatasi stunting' in pertanyaan or 'menangani stunting' in pertanyaan or 'tips menaikan tinggi badan' in pertanyaan or 'tips menaikkan tinggi badan' in pertanyaan or 'cara menaikan tinggi badan' in pertanyaan or 'cara menaikkan tinggi badan' in pertanyaan or 'cara menambah tinggi badan' in pertanyaan or 'tips menambah tinggi badan' in pertanyaan:
        jawaban = "tips mengatasi stunting atau tips menaikkan tinggi badan anak antara lain yaitu menjalankan pola hidup sehat (konsumsi makanan gizi seimbang), pemenuhan nutrisi pada 1000 hari pertama kehidupan anak, perbaiki pola asuh dalam praktek pemberian makan bagi bayi dan balita, menjaga kebersihan diri dan keluarga, dan rutin melakukan imunisasi serta vaksinasi pada anak."
    elif 'stunting' in pertanyaan:
        jawaban = "Stunting merupakan suatu keadaan gagal tumbuh pada balita yang ditandai dengan tinggi badan dibawah batas normal akibat kekurangan gizi."
    elif 'masalah gizi' in pertanyaan:
        jawaban = "Masalah Gizi merupakan suatu keadaan ketidakseimbangan antara asupan gizi dengan kebutuhan tubuh yang terjadi pada seseorang. Pada balita terdapat beberapa masalah gizi yaitu stunting (pendek), wasting(kurus), underweight (Berat badan dibawah batas normal), dan overweight (kelebihan gizi diatas batas normal)."
    elif 'isi piringku' in pertanyaan or 'isi piring' in pertanyaan:
        jawaban = "Isi Piringku adalah pedoman yang disusun oleh Kementerian Kesehatan (kemenkes) untuk mengkampanyekan konsumsi makanan sesuai dengan pedoman gizi seimbang. Dalam satu piring setiap kali makan, setengah piring diisi dengan sayur dan buah, sedangkan setengah lainnya diisi dengan makanan pokok dan lauk pauk."
    elif 'faktor yang mempengaruhi berat badan ideal balita' in pertanyaan or 'faktor berat badan ideal' in pertanyaan or 'faktor yang memengaruhi berat badan' in pertanyaan:
        jawaban = "Terdapat beberapa faktor yang dapat memengaruhi berat badan ideal balita, di antaranya faktor genetik, asupan gizi, aktivitas yang dilakukan, hingga kondisi medis tertentu, seperti:"
        jawaban += "\nPenyakit kanker.\nKelainan kelenjar tiroid.\nTuberkulosis.\nDiabetes.\nGangguan pencernaan, seperti diare."
    elif 'cara menaikkan berat badan' in pertanyaan or 'cara menaikan berat badan' in pertanyaan or 'tips menaikkan berat badan' in pertanyaan or 'tips menaikan berat badan' in pertanyaan or 'tips menambah berat badan' in pertanyaan or 'cara menambah berat badan' in pertanyaan:
        jawaban = "Berikut beberapa cara menaikkan berat badan anak:"
        jawaban += "\n-Memastikan anak makan tiga kali sehari."
        jawaban += "\n-Bagi anak yang memiliki porsi makan sedikit, ubah jadwal makannya menjadi 4–5 kali sehari dengan porsi yang kecil."
        jawaban += "\n-Mengenalkan anak pada konsep kenyang dan lapar dengan membuat jadwal makan, seperti memberikan jeda makan selama dua jam. Misalnya, anak makan jam 12.00, maka berikan camilan lagi setelah jam 14.00."
        jawaban += "\n-Memberikan camilan sehat untuk anak sebanyak 1–2 kali sehari."
        jawaban += "\n-Memberikan anak makanan dan minuman yang kaya nutrisi, seperti susu."
        jawaban += "\n-Menghindari minuman yang mengandung gula tinggi, seperti sirup dan minuman bersoda."
        jawaban += "\n-Membatasi jenis makanan cepat saji, permen, atau keripik karena tidak mengandung nutrisi yang dibutuhkan tubuh."
        jawaban += "\n-Hindari memberikan minum terlalu banyak karena dapat menyebabkan anak mudah kenyang."
        jawaban += "\n\nBila perlu, orang tua bisa berkonsultasi dengan dokter mengenai cara yang tepat dalam menurunkan maupun menaikkan berat badan anak agar mencapai angka ideal. Apabila anak mengalami keluhan yang mengkhawatirkan, jangan ragu mengunjungi puskesmas/klinik terdekat untuk berkonsultasi dan mendapatkan penanganan yang tepat dari dokter."
    elif 'cara menurunkan berat badan' in pertanyaan or 'tips menurunkan berat badan' in pertanyaan or 'cara mengurangi berat badan' in pertanyaan or 'tips mengurangi berat badan' in pertanyaan:
        jawaban = "Tidak hanya kekurangan berat badan, kelebihan berat badan pada anak juga perlu mendapatkan perhatian lebih dari orang tua. Pasalnya, anak dengan status kelebihan gizi justru dapat meningkatkan risiko anak mengalami berbagai penyakit, seperti diabetes, kolesterol, hingga hipertensi."
        jawaban += "\nBeberapa hal yang dapat dilakukan untuk menurunkan berat badan dan mencapai berat badan ideal balita adalah sebagai berikut:"
        jawaban += "\n-Menerapkan pola makan sehat, seperti rutin mengonsumsi buah, sayur, dan susu tanpa lemak serta memperbanyak asupan air putih."
        jawaban += "\n-Mengurangi konsumsi minuman dan makanan tinggi lemak dan manis.\n-Membimbing anak untuk melakukan aktivitas fisik, seperti berjalan-jalan atau berolahraga ringan."
        jawaban += "\n-Mengurangi waktu pasif anak dengan mengajaknya melakukan aktivitas yang aktif, seperti membaca buku dan bermain bersama."
        jawaban += "\n\nBila perlu, orang tua bisa berkonsultasi dengan dokter mengenai cara yang tepat dalam menurunkan maupun menaikkan berat badan anak agar mencapai angka ideal. Apabila anak mengalami keluhan yang mengkhawatirkan, jangan ragu mengunjungi puskesmas/klinik terdekat untuk berkonsultasi dan mendapatkan penanganan yang tepat dari dokter."
    elif 'cara balita sehat' in pertanyaan or 'cara agar balita sehat' in pertanyaan or'tips' in pertanyaan or 'tips agar balita sehat' in pertanyaan or 'tips balita sehat' in pertanyaan:
        jawaban = "Berikut tips agar balita sehat: penuhi asupan nutrisi harian sesuai dengan “isi piringku”, berikan 3 kali porsi makanan berat dan 2 kali makanan selingan dalam sehari, berikan vitamin untuk melindungi balita dari resiko penyakit dan agar tumbuh kembang balita optimal. *Note: vitamin diberikan setelah berusia 6 bulan dan sudah dapat mengonsumsi makanan padat. Saran diatas harus sesuai dengan anjuran dokter gizi anak."
    elif 'menu' in pertanyaan or 'saran makanan' in pertanyaan:
        jawaban = "Makanan yang tepat untuk bayi dan balita:\n\nUsia 0-6 Bulan, berikan ASI eksklusif paling sedikit 8 kali sehari.\n\nUsia 6-9 Bulan, selain ASI berikan makanan pendamping ASI 2 kali sehari seperti bubur tim lumat yang ditambahkan ayam/ikan/daging sapi/tahu/tempe/kuning telur/wortel/bayam/santan.\n\nUsia 9-12 Bulan, selain ASI berikan bubur nasi ditambahkan ayam/ikan/daging sapi/tahu/tempe/kuning telur/wortel/bayam/santan. Makanan diberikan 3 kali sehari.\n\nUsia 12-60 Bulan, Dapat diberikan makanan dengan konsistensi dengan kemampuan anak. Berikan variasi menu makanan dengan gizi seimbang seperti makanan pokok (nasi putih/kentang), lauk hewani(telur/ayam/ikan/daging sapi), lauk nabati (tahu/tempe), sayuran (bayam/sawi/brokoli/wortel), dan buah (pisang/apel/jeruk/melon).\n\n*Note: pengolahan makanan disesuaikan dengan ketersediaan bahan dirumah masing-masing, bumbu yang digunakan tidak berbau tajam, dan penggunaan penyedap/MSG dibatasi. Untuk balita dengan kategori stunting (pendek) terdapat pemberian makanan tambahan tinggi protein."
    elif 'ideal' in pertanyaan or 'tinggi badan ideal' in pertanyaan or 'berat badan ideal' in pertanyaan or 'tinggi badan yang ideal' in pertanyaan or 'berat badan yang ideal' in pertanyaan:
        image_path = '/home/nutrigood/project1/assets/Tabel BB TB Ideal.png'
        jawaban = "Gambar di atas merupakan Berat Badan (BB) dan Tinggi Badan (TB) ideal bagi balita berdasarkan usianya."
        bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
    else:
        jawaban = None  # Jika tidak ada keyword yang cocok, jawaban None
    return jawaban

def proses_pertanyaan(message):
    chat_id = message.chat.id
    pertanyaan = message.text.lower()

    if pertanyaan == 'kembali' or pertanyaan == '/kembali':
        kirim_menu(chat_id)
    elif pertanyaan == '/tanya_jawab_gizi_balita':
        kirim_menu(chat_id)
    elif pertanyaan == '/cek_status_gizi_balita':
        kirim_menu(chat_id)
    elif pertanyaan == '/informasi_gizi_balita':
        kirim_menu(chat_id)
    else:
        jawaban = jawab_pertanyaan(pertanyaan, chat_id)

        if jawaban:
            bot.send_message(chat_id, jawaban)
        else:
            bot.send_message(chat_id, "Mohon maaf🙏🏻, Sebagai model chatbot gizi balita umum, saya tidak dapat menjawab pertanyaan yang anda berikan. \nSilakan coba lagi dengan pertanyaan lain.")
        bot.send_message(chat_id, "Silahkan ajukan pertanyaan lain.\nKirim pesan 'kembali' atau klik tombol '/kembali' jika ingin ke menu utama.")
        bot.register_next_step_handler(message, proses_pertanyaan)

#Logika untuk fitur Informasi Gizi
def informasi_gizi_recursive(chat_id, image_paths, captions, index=0):
    if index < len(image_paths):
        image_path = image_paths[index]
        caption = captions[index]

        if os.path.exists(image_path):
            with open(image_path, 'rb') as image_file:
                bot.send_photo(chat_id, image_file, caption=caption)
        else:
            bot.send_message(chat_id, f"Gambar '{image_path}' tidak ditemukan.")

        index += 1
        informasi_gizi_recursive(chat_id, image_paths, captions, index)
    else:
        bot.send_message(chat_id, f"Berikut saran channel Youtube yang dapat memberikan edukasi seputar Gizi Balita untuk Ibu/Bapak ikuti: \n 1. https://www.youtube.com/@BKKBNOFFICIAL/videos \n 2. https://www.youtube.com/@KementerianKesehatanRI \n 3. https://www.youtube.com/channel/UCRegOgcQOhki7wlRTVCnt8g")
        kirim_menu(chat_id)

#Fitur Informasi Gizi Balita Secara Umum
@bot.message_handler(commands=['informasi_gizi_balita'])
def informasi_gizi(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Berikut Informasi gizi balita secara umum yang dapat Pantau Stunting sampaikan:')

    image_paths = ['assets/Masalah Gizi di Indonesia.png', 'assets/Sehatkan Balita.png', 'assets/PHBS.png']
    captions = [
        'Permasalahan Gizi yang ada di Indonesia.',
        'Gizi seimbang pada Balita.',
        'Perilaku Hidup Bersih dan Sehat.'
    ]
    informasi_gizi_recursive(chat_id, image_paths, captions)

# sapa chatbot
sapa = {'halo': 'halo juga', 'hai': 'hai juga', 'hi': 'hi juga', 'apa kabar': 'saya baik, terima kasih!', 'selamat pagi': 'selamat pagi juga!', 'selamat siang | siang': 'selamat siang juga!', 'selamat sore': 'selamat sore juga!', 'selamat malam': 'selamat malam juga!'}
@bot.message_handler(content_types=['text'])
def chatbot(message):
    teks = message.text.lower()  # Mengubah pesan menjadi huruf kecil untuk mempermudah pencocokan

    if teks in sapa:
        chatid = message.chat.id
        balasan = sapa[teks]
        bot.send_message(chatid, balasan)
    else:
        chatid = message.chat.id
        bot.send_message(chatid, 'Saya tidak mengenali kata tersebut')

bot.infinity_polling()
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.events import EventType
from rasa_sdk.events import UserUtteranceReverted, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
import random
import logging

# class ActionGreet(Action):
#     def name(self) -> str:
#         return "action_greet"

#     def run(self, dispatcher, tracker, domain) -> List[EventType]:
#         dispatcher.utter_message(text="Halo! Selamat datang di athena! Ada yang bisa saya bantu?")
#         return []
    
class ActionSetComputerPref(Action):
    def name(self) -> Text:
        return "action_set_computer_preference"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, any]) -> List[Dict[Text, any]]:
        last_intent = tracker.latest_message['intent'].get('name')
        if last_intent == "affirm":
            return [SlotSet("likes_computer", True)]
        elif last_intent == "deny":
            return [SlotSet("likes_computer", False)]
        return []

class ActionGreetTime(Action):
    def name(self):
        return "action_set_greeting_time"
    
    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text").lower()
        
        if "pagi" in user_message:
            time = "pagi"
        elif "siang" in user_message:
            time = "siang"
        elif "sore" in user_message:
            time = "sore"
        elif "malam" in user_message:
            time = "malam"
        else:
            time = "hari"
        
        # dispatcher.utter_message(text=f"Selamat {time}, saya Athena siap membantu anda")
        return [SlotSet("time", time)]

class ActionSetJurusan(Action):
    def name(self):
        return "action_set_jurusan"
    
    def run(self, dispatcher, tracker, domain):
        jurusan = tracker.latest_message.get('text')
        jurusan_dict = {
            "Teknik Las": "Teknik Las di SMK Tunas Harapan Pati merupakan salah satu Program keahlian yang Membekali peserta didik dengan keterampilan, pengetahuan dan sikap agar kompeten mengembangkan kemampuan dan kemandirian dalam berwirausaha dibidang pengelasan, menyiapkan peserta didik agar memiliki pribadi yang jujur, sopan dan berwibawa, Menyiapkan peserta didik yang terampil dibidang pengelasan sesuai dengan kebutuhan industri",
            "Teknik Jaringan Komputer dan Telekomunikasi" : "Teknik Jaringan Komputer dan Telekomunikasi (TJKT) merupakan salah satu program keahlian SMK yang bergerak di bidang Informasi dan Teknologi. Belajar mengenai teknologi informasi siswa dan siswi jurusan TJKT dididik untuk mampu melakukan installasi jaringan komputer, tidak hanya belajar tentang jaringan namun juga belajar tentang pemprograman. Membuat berbagai program mulai dari yang paling sederhana, membuat game interaktif sampai dengan membuat aplikasi untuk perkantoran dan pertokoan.",
            "Kimia Analisis" : "Kimia Analisis adalah cabang kimia yang berhubungan dengan pengembangan dan penggunaan teknik untuk pengukuran kimia. Kimiawan menggunakan teknik-teknik untuk menentukan komposisi kimia suatu zat. Kimia analisis bisa bersifat kualitatif atau kuantitatif. Analisis kualitatif mengidentifikasi unsur-unsur atau senyawa yang membentuk zat.",
            "Broadcasting TV & Film" : "Broadcasting merujuk pada penyiaran atau penyebaran informasi, suara, atau gambar kepada khalayak luas melalui saluran penyiaran, Perfilman merupakan industri atau seni pembuatan film. Film merupakan medium visual yang menggunakan rangkaian gambar bergerak untuk menyampaikan cerita atau pesan kepada penonton.",
            "Teknik Mesin" : "Teknik Mesin adalah suatu disiplin ilmu teknik yang menggabungkan fisika teknik dan prinsip-prinsip matematika dengan ilmu material (bahan) untuk mendesain, menganalisa, dan membuat serta mempertahankan sistem mekanis.",
            "Teknik Otomotif" : "Teknik otomotif adalah salah satu cabang ilmu teknik mesin yang mempelajari tentang bagaimana merancang, membuat dan mengembangkan alat-alat transportasi darat yang menggunakan mesin, terutama sepeda motor, mobil, bis dan truk. Teknik otomotif menggabungkan elemen-elemen pengetahuan mekanika, listrik, elektronik, keselamatan dan lingkungan serta matematika, fisika, kimia, biologi dan manajemen.",
            "Desain Komunikasi Visual" : "Desain Komunikasi Visual adalah suatu disiplin ilmu tentang metode penyampaian pesan (komunikasi) dan ungkapan kreatif dengan menggunakan elemen-elemen visual/ rupa/ gambar. Proses kreatif ini menggabungkan seni visual dan teknologi digital.",
            "Teknik Instalasi Tenaga Listrik" : "Teknik Instalasi Tenaga Listrik adalalah jurusan yang mempelajari listrik dalam rangka menyediakan listrik yang aman dan stabil sesuai standart industri serta penerangan ( LIGHTING ) baik yang diperlukan di pabrik maupun perumahan ( komersial ).",
            "Teknik Otomasi Industri" : "Teknik Otomasi Industri adalalah jurusan yang mempelajari elektronika dan listrik serta mekanik dalam rangka membuat rangkaian atau sistem kerja yang dapat bekerja sendiri ( OTOMATIS ). Jurusan ini lebih fokus pada pembuatan mesin industri ( alat bantu produksi ) dipabrik seperti mesin MIXER ( pencampur ), LIFT ( pengangkat barang ), mesin pengemasan ( Pakaging ), mesin Pemanas ( HEATER )dan sebagainya, yang dapat bekerja sendiri serta dipadukan dengan ROBOT baik maupun ARM ROBOT ( lengan )."
        }
        
        for key in jurusan_dict.keys():
            if key.lower() in jurusan.lower():
                return [SlotSet("jurusan", key), SlotSet("informasi_jurusan", jurusan_dict[key])]
            
        dispatcher.utter_message(text="Maaf, di tunas harpan pati tidak memiliki jurusan yang anda maksud.")
        return []
    
    
daftar_jurusan = {
    "Teknik Las": "Teknik Las di SMK Tunas Harapan Pati merupakan salah satu Program keahlian yang Membekali peserta didik dengan keterampilan, pengetahuan dan sikap agar kompeten mengembangkan kemampuan dan kemandirian dalam berwirausaha dibidang pengelasan, menyiapkan peserta didik agar memiliki pribadi yang jujur, sopan dan berwibawa, Menyiapkan peserta didik yang terampil dibidang pengelasan sesuai dengan kebutuhan industri",
    "Teknik Jaringan Komputer dan Telekomunikasi" : "Teknik Jaringan Komputer dan Telekomunikasi (TJKT) merupakan salah satu program keahlian SMK yang bergerak di bidang Informasi dan Teknologi. Belajar mengenai teknologi informasi siswa dan siswi jurusan TJKT dididik untuk mampu melakukan installasi jaringan komputer, tidak hanya belajar tentang jaringan namun juga belajar tentang pemprograman. Membuat berbagai program mulai dari yang paling sederhana, membuat game interaktif sampai dengan membuat aplikasi untuk perkantoran dan pertokoan.",
    "Kimia Analisis" : "Kimia Analisis adalah cabang kimia yang berhubungan dengan pengembangan dan penggunaan teknik untuk pengukuran kimia. Kimiawan menggunakan teknik-teknik untuk menentukan komposisi kimia suatu zat. Kimia analisis bisa bersifat kualitatif atau kuantitatif. Analisis kualitatif mengidentifikasi unsur-unsur atau senyawa yang membentuk zat.",
    "Broadcasting TV & Film" : "Broadcasting merujuk pada penyiaran atau penyebaran informasi, suara, atau gambar kepada khalayak luas melalui saluran penyiaran, Perfilman merupakan industri atau seni pembuatan film. Film merupakan medium visual yang menggunakan rangkaian gambar bergerak untuk menyampaikan cerita atau pesan kepada penonton.",
    "Teknik Mesin" : "Teknik Mesin adalah suatu disiplin ilmu teknik yang menggabungkan fisika teknik dan prinsip-prinsip matematika dengan ilmu material (bahan) untuk mendesain, menganalisa, dan membuat serta mempertahankan sistem mekanis.",
    "Teknik Otomotif" : "Teknik otomotif adalah salah satu cabang ilmu teknik mesin yang mempelajari tentang bagaimana merancang, membuat dan mengembangkan alat-alat transportasi darat yang menggunakan mesin, terutama sepeda motor, mobil, bis dan truk. Teknik otomotif menggabungkan elemen-elemen pengetahuan mekanika, listrik, elektronik, keselamatan dan lingkungan serta matematika, fisika, kimia, biologi dan manajemen.",
    "Desain Komunikasi Visual" : "Desain Komunikasi Visual adalah suatu disiplin ilmu tentang metode penyampaian pesan (komunikasi) dan ungkapan kreatif dengan menggunakan elemen-elemen visual/ rupa/ gambar. Proses kreatif ini menggabungkan seni visual dan teknologi digital.",
    "Teknik Instalasi Tenaga Listrik" : "Teknik Instalasi Tenaga Listrik adalalah jurusan yang mempelajari listrik dalam rangka menyediakan listrik yang aman dan stabil sesuai standart industri serta penerangan ( LIGHTING ) baik yang diperlukan di pabrik maupun perumahan ( komersial ).",
    "Teknik Otomasi Industri" : "Teknik Otomasi Industri adalalah jurusan yang mempelajari elektronika dan listrik serta mekanik dalam rangka membuat rangkaian atau sistem kerja yang dapat bekerja sendiri ( OTOMATIS ). Jurusan ini lebih fokus pada pembuatan mesin industri ( alat bantu produksi ) dipabrik seperti mesin MIXER ( pencampur ), LIFT ( pengangkat barang ), mesin pengemasan ( Pakaging ), mesin Pemanas ( HEATER )dan sebagainya, yang dapat bekerja sendiri serta dipadukan dengan ROBOT baik maupun ARM ROBOT ( lengan )."
}    
    
class ActionJelaskanJurusan(Action):
    def name(self):
        return "action_jelaskan_jurusan"

    def run(self, dispatcher, tracker, domain):
        jurusan = tracker.get_slot("jurusan")
        informasi_jurusan = tracker.get_slot("informasi_jurusan")

        if jurusan and informasi_jurusan:
            dispatcher.utter_message(f"Berikut informasi mengenai {jurusan}: {informasi_jurusan}")
        else:
            # dispatcher.utter_message("Jurusan mana yang ingin kamu tanyakan?")
            dispatcher.utter_message(response="utter_tanya_jurusan")
        return []

    
class ActionSetNamaUser(Action):
    def name(self):
        return "action_set_nama_user"

    def run(self, dispatcher, tracker, domain):
        # Ambil nama_user dari entitas
        nama_user = next(tracker.get_latest_entity_values("nama_user"), None)
                
        if nama_user:
            nama_user1 = nama_user.title()
            return [SlotSet("nama_user", nama_user1)]
            # dispatcher.utter_message(text=f"Senang bertemu denganmu, {nama_user}!")
        else:
            dispatcher.utter_message(text="Maaf, saya tidak mendapatkan nama Anda.")
            return []

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ActionLogFallback(Action):
    def name(self):
        return "action_log_fallback"
    
    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text", "")
        fallback_count = tracker.get_slot("fallback_count") or 0
        
        logger.info(f"Fallback count saat ini: {fallback_count}")
        
        with open("fallback_logs.txt", "a") as file:
            file.write(f"{user_message}\n")
            
        fallback_count += 1
        
        if fallback_count >= 3:
            dispatcher.utter_message(text="Mohon maaf saya belum dapat memahami, silahkan hubungi admin untuk hal lebih lanjut [kontak]")
            return [SlotSet("fallback_count", 0), FollowupAction("action_listen")]
            
        fallback_responses = [
            "Maaf, saya tidak memahami pesan Anda.",
            "Saya belum mengerti maksud Anda. Mohon berikan pertanyaan mengenai SMK Tunas Harapan Pati.",
            "Sepertinya saya tidak bisa memproses pesan Anda. Coba tanyakan sesuatu yang lain mengenai SMK Tunas Harapan Pati.",
            "Maaf, saya belum bisa membantu dengan pertanyaan itu. Apakah ada hal lain yang bisa saya bantu?"
        ]
        
        selected_response = random.choice(fallback_responses)
        dispatcher.utter_message(text=selected_response)
        
        return [SlotSet("fallback_count", fallback_count), FollowupAction("action_listen")]
    
# class ActionLogConversationID(Action):
#     def name(self):
#         return "action_log_conversation_id"
    
#     def run(self, dispatcher, tracker, domain):
#         conversationId = tracker.sender_id
        
#         dispatcher.utter_message(
#             text=f"ID percakapan anda: {conversationId}"
#         )
        
#         return []
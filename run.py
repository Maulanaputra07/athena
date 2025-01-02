import subprocess

def start_rasa_server():
    print("Menjalankan server rasa..")
    subprocess.run(['rasa', 'run', '--enable-api'])
    
def start_rasa_shell():
    print('mulai percakapan dengan bot..')
    subprocess.run(['rasa', 'shell'])
    
if __name__ == "__main__":
    # Menjalankan server dan memulai percakapan
    start_rasa_server()
    start_rasa_shell()
import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from config.settings import BASE_URL, make_headers


def upload_user_avatar(auth_token):
    headers = make_headers(auth_token)

    root = Tk()
    root.withdraw()
    file_path = askopenfilename(
        title="Выберите изображение",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")]
    )

    if not file_path:
        print("Файл не выбран.")
        return

    if not file_path.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
        print("Неверный формат файла.")
        return

    with open(file_path, 'rb') as file:
        files = {'image': (file_path.split("/")[-1], file)}

        return requests.post(f'{BASE_URL}/api/files/upload', headers=headers, files=files)

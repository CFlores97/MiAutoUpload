from selenium import webdriver
import os
import pyautogui
import time
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

# Métodos
def isValid(filepath):
    invalid_extensions = [".zip", ".rar", ".7z"]
    extension = os.path.splitext(filepath)[1]

    if extension not in invalid_extensions and not os.path.isdir(filepath):
        return True
    else:
        return False

def verificarISBN(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)

            if len(dir_name) == 10:
                for file in os.listdir(dir_path):
                    file_name, file_ext = os.path.splitext(file)
                    new_file_name = f"{dir_name}{file_ext}"
                    old_file_path = os.path.join(dir_path, file)
                    new_file_path = os.path.join(dir_path, new_file_name)

                    if file_name != dir_name:
                        os.rename(old_file_path, new_file_path)

def subir(directorio):
    for fil in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, fil)
        if isValid(ruta_archivo):
            try:
                upload_input = wait.until(EC.presence_of_element_located((By.NAME, 'file')))
                upload_input.send_keys(ruta_archivo)

                try:
                    WebDriverWait(driver, 25).until(
                        EC.text_to_be_present_in_element(
                            (By.CLASS_NAME, 'file-input-submit'),
                            'already exists in '
                        )
                    )
                    print(f"El archivo: '{ruta_archivo}' ya existe!")
                    shutil.move(str(ruta_archivo), uploaded_folder)
                    driver.find_element(By.LINK_TEXT, 'upload a file').click()
                    continue

                except Exception as e:
                    print("Archivo pasa exitosamente!")

                wait.until(EC.presence_of_element_located((By.ID, 'progress_text')))

                wait.until(
                    EC.text_to_be_present_in_element(
                        (By.ID, 'progress_text'),
                        'Uploading has been started...'
                    )
                )

                print(f"Subiendo \"{fil}\"")

                file_name, file_ext = os.path.splitext(fil)
                print(file_name)

                isbn_input = WebDriverWait(driver, 2000).until(
                    EC.presence_of_element_located(
                        (By.NAME, "metadata_query")
                    )
                )
                isbn_input.send_keys(file_name)

                select = Select(driver.find_element(By.NAME, "metadata_source"))
                select.select_by_visible_text("Amazon.com")

                fetch_button = driver.find_element(By.NAME, "fetch_metadata")
                fetch_button.click()

                time.sleep(3)

                # Le da a submit
                submit_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit')))
                submit_input.click()

                print("Uploaded!")

                shutil.move(str(ruta_archivo), uploaded_folder)

                driver.find_element(By.LINK_TEXT, 'Go to the upload page').click()

            except Exception as e:
                print(e)

    for root, dirs, files in os.walk(directorio):
        for dire in dirs:
            dir_path = os.path.join(root, dire)

            for file in os.listdir(dir_path):
                ind_file = os.path.join(dir_path, file)
                if isValid(ind_file):
                    try:
                        upload_input = wait.until(EC.presence_of_element_located((By.NAME, 'file')))
                        upload_input.send_keys(ind_file)

                        try:
                            WebDriverWait(driver, 25).until(
                                EC.text_to_be_present_in_element(
                                    (By.CLASS_NAME, 'file-input-submit'),
                                    'already exists in '
                                )
                            )
                            print(f"El archivo: '{ind_file}' ya existe!")
                            shutil.move(str(ind_file), uploaded_folder)
                            driver.find_element(By.LINK_TEXT, 'upload a file').click()
                            continue

                        except Exception as e:
                            print("Archivo pasa exitosamente!")

                        wait.until(EC.presence_of_element_located((By.ID, 'progress_text')))

                        wait.until(
                            EC.text_to_be_present_in_element(
                                (By.ID, 'progress_text'),
                                'Uploading has been started...'
                            )
                        )

                        print(f"Subiendo \"{file}\"")

                        file_name, file_ext = os.path.splitext(file)
                        print(file_name)

                        isbn_input = WebDriverWait(driver, 2000).until(
                            EC.presence_of_element_located(
                                (By.NAME, "metadata_query")
                            )
                        )
                        isbn_input.send_keys(file_name)

                        select = Select(driver.find_element(By.NAME, "metadata_source"))
                        select.select_by_visible_text("Amazon.com")

                        fetch_button = driver.find_element(By.NAME, "fetch_metadata")
                        fetch_button.click()

                        time.sleep(3)

                        # Le da a submit
                        submit_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit')))
                        submit_input.click()

                        print("Uploaded!")

                        shutil.move(str(ind_file), uploaded_folder)

                        driver.find_element(By.LINK_TEXT, 'Go to the upload page').click()

                    except Exception as e:
                        print(e)

if __name__ == '__main__':
    base_path = os.path.dirname(__file__)

    folder_path = os.path.join(base_path, 'to_upload')
    uploaded_folder = os.path.join(base_path, 'uploaded')

    verificarISBN(folder_path)

    username = 'genesis'
    password = 'upload'

    options = Options()

    # Ruta del driver
    driver_path = r'gecko_driver_path' #replace with driver path 
    service = Service(executable_path=driver_path)

    driver = webdriver.Firefox( options=options)

    wait = WebDriverWait(driver, 2000)

    url = f'http://library.bz/main/upload/'

    driver.get(url)

    time.sleep(1)

    # Enviar el nombre de usuario y la contraseña
    pyautogui.write('genesis')
    pyautogui.press('tab')
    pyautogui.write('upload')
    pyautogui.press('enter')

    subir(folder_path)

    # Bucle que recorre los archivos

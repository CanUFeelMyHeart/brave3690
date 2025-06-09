
import pyautogui as pag

# Указываем путь к изображению кнопки
button_image_path = "/Users/egorceban/PycharmProjects/FB/tri.png"


def find_and_click_button(button_path):
    """
    Функция находит изображение на экране и кликает по нему.
    :param button_path: Путь к файлу изображения кнопки.
    :return: True, если кнопка найдена и нажата, иначе False.
    """
    try:
        # Ищем изображение на экране
        button_location = pag.locateOnScreen(button_path)
        if button_location is not None:
            # Кликаем по центру изображения
            print(f"Кнопка найдена и нажата!")
            return True
        else:
            print("Кнопка не найдена на экране.")
            return False
    except Exception as e:  # Поймем любое исключение
        print(f"Произошла ошибка: {e}")
        return False


def main():
    while True:
            for X in range(30):
                # Ищем кнопку
                if find_and_click_button(button_image_path):
                    print("Кнопка успешно нажата!")

                    pag.press("enter", 1, 1),
                    pag.sleep(1),
                    pag.press('down', 2),
                    pag.press("enter", 1, 1)
                    pag.sleep(4)
                    pag.press('tab', 1, 0.05)  # Выбираем группу
                    for X in range(20):
                        pag.press('tab', 1, 0.06)  # Выбираем группу
                        pag.press("enter", 1, 0.06)
                    pag.keyDown('shift')
                    pag.press("tab", 21, 0.06)
                    pag.keyUp('shift')
                    pag.sleep(1)
                    pag.press("enter", 1, 1)
                    pag.sleep(1)
                else:
                    print("Кнопка не найдена. Нажимаю ESC...")
                    pag.sleep(1)  # Пауза перед следующей попыткой
            for X in range(3):
                # Ищем кнопку
                if find_and_click_button(button_image_path):
                    print("Кнопка успешно нажата!")
                    pag.press('tab', 5, 0.05)  # Выбираем группу
                    pag.sleep(1)
                else:
                    print("Кнопка не найдена. Нажимаю ESC...")
                    pag.sleep(1)  # Пауза перед следующей попыткой

if __name__ == "__main__":
    main()








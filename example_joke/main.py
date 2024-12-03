# fh = open('test.txt')
# # операції над файлом
# fh.close()

# fh = open('test1.py', 'w')
# symbols_written = fh.write('hello!')
# print(symbols_written) # 6
# fh.close()

# fh= open("Ihorsdocument.py",'w')
# symbols_written=fh.write("hello world!")
# print(symbols_written)
# fh.close()

# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(0)

# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'

# # fh.close()

# rek = open('test.txt', 'w')
# rek.write('hello!')
# rek.close()

# rek = open('test.txt', 'r')
# while True:
#     symbol = rek.read(1)
#     if len(symbol) == 0:
#         break
#     print(symbol)

# rek.close()
# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b'Hello world!')
# for num in [127, 255, 156]:
#   print(hex(num))
# text = """У німецькій мові, літера "ß" (так званий "sharp S" або "eszett") використовується для позначення специфічного звука, 
# що наближений до подвоєного "ss". Ця літера не має прямого еквіваленту у верхньому регістрі. 
# Традиційно, коли слово, що містить "ß", потрібно написати великими літерами, "ß" перетворюється на "SS"."""
# print(text.casefold())
# print(text.lower())
# if text.lower()==text.casefold():
#     print("вони однакові")
# else:
#     print("вони різні")

# import shutil

# # Specify the directory to archive
# root_dir = r'C:\Users\Apprienticeship\Desktop\DScience\myfirstrepository'

# # Create the ZIP archive
# shutil.make_archive(r'C:\Users\Apprienticeship\Desktop\Dscience\myfirstrepository', 'zip', root_dir)

# print("Archive created successfully!")
# from pathlib import Path

# # Початковий шлях
# base_path = Path(r"C:\Users\Apprienticeship\Desktop\DScience")

# # Додавання додаткових частин до шляху
# full_path = base_path / "subdir" / "script.py"

# full_path.parent.mkdir(parents=True, exist_ok=True)

# full_path.touch(exist_ok=True)

# print(f"Folder and file created at: {full_path}")
# from pathlib import Path
# relative_path = Path("main.py")
# absolute_path = relative_path.absolute()
# print(absolute_path)

# from pathlib import Path
# original_path=Path("myfirstrepository/test.txt")
# new_path=original_path.with_name("igor.py")
# print(new_path)

# from pathlib import Path
# directory = Path('/DScience/myfirstrepository/new_folder')
# directory.mkdir(parents=True, exist_ok=True)

# import shutil
# from pathlib import Path

# source = Path(r'/DScience/myfirstrepository')
# destination= Path(r'/DScience/subdir')
# shutil.copy(source, destination)

# import shutil
# from pathlib import Path

# # Define the directory paths
# source = Path(r'C:\DScience\myfirstrepository')  # Source directory
# destination = Path(r'C:\DScience\subdir')        # Target directory

# # # Ensure the source directory exists
# # if source.exists() and source.is_dir():
# #     shutil.copytree(source, destination)
# #     print(f"Directory copied to: {destination}")
# # else:
# #     print(f"Source directory not found or invalid: {source}")

# from pathlib import Path
# import time

# # Specify the file path
# file_path = Path(r"C:\Users\Apprienticeship\Desktop\GoIt\resume_example.png")

# # Check if the file exists
# if file_path.exists() and file_path.is_file():
#     # Get the file size
#     size = file_path.stat().st_size
#     print(f"Розмір файла: {size} байтів")
# else:
#     print(f"Файл не знайдено або це не файл: {file_path}")

# creation_time = file_path.stat().st_ctime
# modification_time = file_path.stat().st_mtime

# print(f"Час створення: {time.ctime(creation_time)}")
# print(f"Час модифікації: {time.ctime(modification_time)}")

# from math import pi, sin

# sin_pi = sin(pi)

# print(sin_pi)

# main.py

# main.py
# import mymodule

# print(mymodule.say_hello("World"))

# from mymodule import say_hello

# print(say_hello("World"))

# main.py
# from mymodule import say_hello as greeting

# print(dir())
# print(greeting("World"))

# def say_hello(name):
#     print(f'Hello, {name}')

# if __name__ == '__main__':
#     print("You imported hello.py")
#     say_hello('user')

# def say_hello(name):
#     print(f'Hello {name}')

# def main():
#     print("You imported hello.py")
#     say_hello('user')

# if __name__ == '__main__':
#     main()

# from joke import get_random_joke

# def main():
#     name = input("Введіть ваше імя:")
#     print(f"Привіт, {name}!")

#     while True: 
#        user_response= input(f"Не бажаєте {name} почути анекдот (так/ні):").lower()
#        if user_response =="так":
#            print(get_random_joke())
#        elif user_response =="ні":
#            print(f"До побачення, {name}")
#            break
# if __name__=="__main__":
#     main()

#  pip install requests
# python -m venv .venv

# def is_palindrome(s: str) -> bool:
#     new_s = ""
#     for char in s:
#         if char.isalnum():
#             new_s += char.lower()

#     s = new_s
#     return s == s[::-1]
# # Використання функції
# print(is_palindrome("Козак з казок"))  # Виведе: True
# def is_palindrome(s:str) -> str:
#      new_s = ""
#      for char in s:
#         if char.isalnum():
#             new_s += char.lower()
#      s==("Козак з казок")
#      print(s)

# Розрахунок площі 
length1, width1 = 5, 10
area1 = length1 * width1

# Багато різного коду

length2, width2 = 7, 12
area2 = length2 * width2

def calculate_area(length: float, width: float) -> float:
    return length * width

area1 = calculate_area(5, 10)
area2 = calculate_area(7, 12)






       

    

count = 0  

while True:
    user_input = input("Введите'СТОП' для завершения: ")
    
    if user_input == "СТОП":
        print("Программа завершена.")
        break
    
    if count >= 2:
        print("СТОП!!!")
    
    count += 1

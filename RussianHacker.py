#GLOBAL: импорты

#переменные
modulesubprocess = None
moduleos = None
moduleart = None
modulegoogletrans = None
stop = False

#импорты

try:
    import os
    moduleos = True
except:
    moduleos = False
try:
    import subprocess
    modulesubprocess = True
except:
    modulesubprocess = False
if not moduleos:
    if not modulesubprocess:
        stop = True
try:
    import art
    moduleart = True
except:
    try:
        if modulesubprocess:
            if subprocess:
                subprocess.call(["pip", "install", "art"])
            else:
                if moduleos:
                    os.system("pip install art")
        import art
    except:
        moduleart = False
try:
    from googletrans import Translator, constants
    modulegoogletrans = True
except:
    try:
        if modulesubprocess:
            if subprocess:
                subprocess.call(["pip", "install", "googletrans==3.1.0a0"])
            else:
                if moduleos:
                    os.system("pip install googletrans==3.1.0a0")
        from googletrans import Translator, constants
    except:
        modulegoogletrans = False
if modulegoogletrans:
    translator = Translator()


if stop:
    print("Похоже, произошла какая-та ошибка, давайте выясним.")
    input("Запускать диагностику?")
    try:
        if not moduleart:
            print("Не загружен: art.")
        if not moduleos:
            print("Не загружен: os.")
        if not modulesubprocess:
            print("Не загружен: subprocess.")
    finally:
        print("Диагностика завершена.")
else:
    #GLOBAL: терминал.
    
    #функции
    def title():
        if moduleos:
            os.system("clear")
        else:
            if modulesubprocess:
                subprocess.run("clear", shell=True)
        if moduleart:
            title = art.text2art("R|Hacker")
        else:
            title = "R|Hacker\n"
        print(title)
    
    #терминал
    title()
    print("""Дополнительные программы: 
1. команда: stop - Останавливает программу, некоторые функции программе не доступны.
2. префикс: os - выполнение без перевода.
          """)
    while True:
        command = input("$ ")
        if command.split(" ")[0] == "os":
            try:
                os.system(command.split(maxsplit=1)[1])
            except ValueError:
                pass
        elif command == "stop":
            break
        else:
            commands = []
            for i in range(command.count(" ") + 1):
                commands.append(command.split(" ")[i])
            try:
                output = subprocess.check_output(commands, shell=True)
            except:
                if moduleos:
                    print("Произошла ошибка! Автоматическое выполнение без перевода.")
                    os.system(command)
                else:
                    print("Произошла ошибка! Автоматическое выполнение без вывода - невозможно.")
            try:
                output = output.decode("utf-8")
            except:
                pass
            try:
                if output != "":
                    try:
                        translation = translator.translate(text=output, dest="ru")
                        translation = translation.text.replace('\\"', '"')
                        print(f"Перевод:\n{translation}\n\nBy RussianHacker.")
                    except:
                        output = output.replace('\\"', '"')
                        print(f"Не удалось перевести:\n{output}\n\nBy RussianHacker.")
                else:
                    print("Вывода нету.")
            except:
                pass

print("RussianHacker - остановлен.")

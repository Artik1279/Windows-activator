# Активация Windows 
Я знаю что у многих пользователей системы Windows к большому сожалению она не активирована некоторые, до сих пор думают что исправить это можно лишь тратой деняг на официальный ключ, на самом деле это не так, и этот проект этому доказательство. 


### Внимание:
**Я бы хотел предупредить что все ниже описанные действия делайте на свой страх и риск, я не ручаюсь за то, как это будет работать именно на вашем компьютере!**


Сегодня я бы хотел осветить достаточно простой способ активации Windows. Всё что вам понадобится, это умение писать и читать.

Для начала откройте командную строку (`cmd.exe`) от имени администратора. Вы можете сделать это написав в поиске cmd, нажав правый клик по нужному приложению и выбрать из меню `"Запуск от имени администратора"`

![Администратор](imgs/admin.png)


После у вас должна открыться командная строка, не бойтесь её, ничего програмировать мы не будем, а лишь напишем пару нужных команд:
## 1. Установка корпоротивного ключа:
Для успешной активации нам необходимо воспользоваться общедоступным корпоративным ключом, для разных версий Windows они разные, ниже я провёл самые популярные:
| Издание           | Ключ                          |
|-------------------|-------------------------------|
| Windows 10/11 Pro | W269N-WFGWX-YVC9B-4J6C9-T83GX |
| Windows 8.1 Pro   | GCRJD-8NW9H-F2CDX-CCM8D-9D6T9 |
| Windows 7 Pro     | FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4 |

**Если вы не нашли ваше издание то больше ключей находятся здесь:**
*https://learn.microsoft.com/ru-ru/windows-server/get-started/kms-client-activation-keys*

После того как вы заполучили нужный вам ключ, в командную строку необходимо ввести следующую команду:
```
slmgr /ipk ВАШ_КЛЮЧ
```
![Первый шаг](imgs/1.png)
После этого вам должны сообщить:




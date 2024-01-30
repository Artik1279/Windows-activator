# Activate Windows

I know that many Windows users, unfortunately, do not have it activated. Some people still think that the only way to fix this is by spending money on an official key. In fact, this is not the case, and this project is proof of this.

### ❗ Attention:

I would like to warn you that all the actions described below are illegal, you can buy an official key for Windows on the official website:
*https://microsoft.com*

### For Windows 10/11:
### If you don't want to suffer, you can download my ready-made [file](https://github.com/Artik1279/Windows-activator/blob/main/ActivatorWindows10-11.bat) with all the commands. All you need to do is run it as administrator!

Today I would like to highlight a fairly simple way to activate Windows. All you need is the ability to write and read.

To begin, open cmd.exe as an administrator. You can do this by typing cmd in the search, right-clicking on the desired application and selecting "Run as administrator" from the menu.

![Administrator](imgs/admin.png)

Afterwards you should have a command prompt open. Don’t be afraid of it, we won’t program anything, we’ll just write a couple of necessary commands:

## 1. Installing a corporate key:

For successful activation, we need to use a public corporate key, they are different for different versions of Windows, below I have listed the most popular ones:
| Edition | Key |
|-------------------|---------------------------- --|
| Windows 10/11 Pro | W269N-WFGWX-YVC9B-4J6C9-T83GX |
| Windows 8.1 Pro   | GCRJD-8NW9H-F2CDX-CCM8D-9D6T9 |
| Windows 7 Pro     | FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4 |

If you did not find your edition, then more keys can be found here: *https://learn.microsoft.com/ru-ru/windows-server/get-started/kms-client-activation-keys*

After you have obtained the key you need, enter the following command on the command line:
slmgr /ipk YOUR_KEY

After this you should be informed:

![First step](imgs/1.png)

If so, then let's continue!

## 2. Set the activation service:

For successful activation, we need to set the required name for the activation service; this name is the address of the official server.

Enter the following command into the console:
slmgr /skms kms.digiboy.ir

Result:

![Second step](imgs/2.png)

## 3. Activation and completion:

After all the previously described actions, all we have to do is enter the activation command:
slmgr /ato

After entering this command, wait a few seconds and you will be told:

![Third step](imgs/3.png)

Don't forget to restart your computer for all actions to take effect!

## ✅ Congratulations! Your copy of Windows has been successfully activated!

![Fourth step](imgs/4.png)

If you have any problems, please create [Issues](https://github.com/Artik1279/Windows-activator/issues) and I will try to help you!

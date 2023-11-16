# from pyfiglet import figlet_format
# text =figlet_format("FFS")
# print(text)


from termcolor import colored
text = colored('Hello World!', 'white', attrs=['bold', 'underline'])
print(text)
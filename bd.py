import requests
import os
os.system('clear')

main='''\033[1;32;40m
╭╮╱╭┳━━━╮╱╱╱╱╭━━━╮╭╮╱╭━━━╮╱╱╱╭╮╱╱╭┳━━━╮
┃┃╱┃┃╭━╮┃╱╱╱╱┃╭━╮┣╯╰╮┃╭━╮┃╱╱╭╯┃╱╱┃┃╭━╮┃
┃╰━╯┃┃┃┃┣━┳━╮╰╯╭╯┣╮╭╯┃╰━━┳━━╋╮┃╭━╯┣╯╭╯┣━┳━━╮
┃╭━╮┃┃┃┃┃╭┫╭╮┳╮╰╮┃┃┃╱╰━━╮┃╭╮┃┃┃┃╭╮┣╮╰╮┃╭┫━━┫
┃┃╱┃┃╰━╯┃┃┃┃┃┃╰━╯┃┃╰╮┃╰━╯┃╰╯┣╯╰┫╰╯┃╰━╯┃┃┣━━┃
╰╯╱╰┻━━━┻╯╰╯╰┻━━━╯╰━╯╰━━━┫╭━┻━━┻━━┻━━━┻╯╰━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
'''
logo='''\033[1;32;40m
  ░█████╗░██╗░░░██╗████████╗░█████╗░
  ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
  ███████║██║░░░██║░░░██║░░░██║░░██║
  ██╔══██║██║░░░██║░░░██║░░░██║░░██║
  ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
  ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░

  ██╗░░░██╗██╗███████╗░██╗░░░░░░░██╗
  ██║░░░██║██║██╔════╝░██║░░██╗░░██║
  ╚██╗░██╔╝██║█████╗░░░╚██╗████╗██╔╝
  ░╚████╔╝░██║██╔══╝░░░░████╔═████║░
  ░░╚██╔╝░░██║███████╗░░╚██╔╝░╚██╔╝░
  ░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░
'''
print("\033[1;34;40m=============================================")
print("\033[1;33;40m|        DEVELOPED BY MD SUMON ISLAM        |")
print("\033[1;34;40m=============================================")
print(main)
print("\033[1;34;40m=============================================")
print("\033[1;33;40m|        DEVELOPED BY MD SUMON ISLAM        |")
print("\033[1;34;40m=============================================")
print("\033[1;33;40mCODE NAME: H0rn3t Sp1d3rs ")
print("GITHUB : HTTPS://GITHUB.COM/H0rn3t-Sp1d3rs")
print("Website : https://m4ds0ul.blogspot.com")
print("\033[1;34;40m=============================================")
print("\033[1;33;40m|        DEVELOPED BY MD SUMON ISLAM        |")
print("\033[1;34;40m=============================================")
print()
print("\033[1;31;40m[\033[1;32;40m01\033[1;31;40m]\033[1;32;40m START YOUR TOOLS ")
print("\033[1;31;40m[\033[1;32;40m02\033[1;31;40m]\033[1;32;40m CONTACT MY PAGE ")
opton=input("\033[1;33;40mSELECT YOUR OPTION :\033[1;32;40m")
os.system('clear')
if opton=='01' or opton=='1':
	print("\033[1;34;40m=============================================")
	print("\033[1;33;40m|        DEVELOPED BY MD SUMON ISLAM        |")
	print("\033[1;34;40m=============================================")
	print(logo)
	print("\033[1;34;40m=============================================")
	print("\033[1;33;40m|        DEVELOPED BY MD SUMON ISLAM        |")
	print("\033[1;34;40m=============================================")
	print()
	url=str(input("\033[1;33;40m Enter Your Web:\033[1;35;40m "))
	amount=int(input("\033[1;33;40m Enter Your Amount:\033[1;35;40m "))


	agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"
	

	for i in range (amount):
		resp = requests.get(url,agent)
		if resp.status_code == resp.status_code:
			print("\033[1;32;40m ")
			print(str(i+1)+" [√]View Sent Success")
	
		else:
			print("\033[1;31;40m[×]View Sent Faild")

elif opton=='2' or opton=='02':
	os.system(" xdg-open https://www.facebook.com/H0rn3t.Sp1d3rs")
	os.system('python bd.py')

else:
	print('\033[1;31;40mWRONG')

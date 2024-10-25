# Color snippets
black = "\033[0;30m"
red = "\033[0;31m"
bred = "\033[1;31m"
green = "\033[0;32m"
bgreen = "\033[1;32m"
yellow = "\033[0;33m"
byellow = "\033[1;33m"
blue = "\033[0;34m"
bblue = "\033[1;34m"
purple = "\033[0;35m"
bpurple = "\033[1;35m"
cyan = "\033[0;36m"
bcyan = "\033[1;36m"
white = "\033[0;37m"
nc = "\033[00m"

# Regular Snippets
ask = f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error = f"{blue}[{white}!{blue}] {red}"
info = f"{yellow}[{white}+{yellow}] {cyan}"
info2 = f"{green}[{white}•{green}] {purple}"


banner = f"""
{red}⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⢀⣀⣀⣀⠀⢀⣀⣀⡀
{red}  ⠈⢻⣿⣷⣀⣾⣿⠟ ⣿⣿⠀⢸⣿⣿⣿⣷⣶⡄⠀⣠⣶⣿⣿⣿⣶⣄⢸⣿⣿⣿⣿⣿⣿⡇⣿⣿⡇⠀⣴⣾⣿⣿⣷⣦⠀⠀⠀⠀⠀⠈⠳⡄⠈⣦⠞⢁⣽⠃
{blue}⠀ ⠀⠹⣿⣿⣿⠏⠀⠀⣿⣿⠀⢸⣿⣿⠀⢹⣿⣿⢠⣿⣿⠏⠀⢹⣿⣿⡀⠀⢰⣿⣿⠀⠀⠀ ⣿⣿⡇⢸⣿⣿⠁⠈⠿⠿⠇⠀⢀⣀⣀⣀⠀⢙⣄⠈⠀⡾⠁⠀
{red}⠀  ⢀⣾⣿⢿⣿⣧⡀⠀⣿⣿⠀⢸⣿⣿⣀⣸⣿⣿⠈⣿⣿⣆⣀⣸⣿⣿⠁⠀⢸⣿⣿⠀⠀⠀⣿⣿⡇⠸⣿⣿⣄⣀⣶⣶⡆⠀⠸⠧⠤⠼⢠⡞⢀⣤⡀⠙⣆⠀
{red}  ⠠⠿⠿⠏⠈⠿⠿⠷⠄⠿⠿⠀⠸⠿⠿⠿⠿⠟⠁⠀⠘⠻⠿⠿⠿⠟⠁⠀⠀⠸⠿⠿⠀⠀⠀⠿⠿⠇⠀⠙⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠠⠯⠤⠞⠁⠳⠤⠬⠧
{cyan}                                         [{blue}By {green}Aayush-xid-su{cyan}]
"""

#Program to fetch the http status code give the url/api
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import emoji

#Taking input url from user
requestURL = input("Enter the URL to be invoked: ")

#Gets the response from URL and prints the status code, corresponding emoji and message accordingly
try:
    response = urlopen(requestURL)
    #In case of success, prints success status code and thumbs_up emoji
    print('Status code : ' + str(response.code) + ' ' + emoji.emojize(':thumbs_up:'))
    print('Message : ' + 'Request succeeded. Request returned message - ' + response.reason)
except HTTPError as e:
    #In case of request failure, prints HTTP error status code and thumbs_down emoji
    print('Status : ' + str(e.code) + ' ' + emoji.emojize(':thumbs_down:'))
    print('Message : Request failed. Request returned reason - ' + e.reason)
except URLError as e:
    #In case of bad URL or connection failure, prints Win Error and thumbs_down emoji
    print('Status :',  str(e.reason).split(']')[0].replace('[','') +  ' ' + emoji.emojize(':thumbs_down:'))
    print('Message : '+ str(e.reason).split(']')[1])
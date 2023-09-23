import requests
import socket

from urllib.parse import urlparse

# To gather information about the website
def get_website(url):
    try:
        response=requests.get(url)
        print("OTHER INFORMATION")
        print("URL :",response.url)
        print("Status Code:",response.status_code)
        print("Content-Type",response.headers.get("Content-Type"))
        print("server:",response.headers.get("Server"))
    except requests.exceptions.RequestException as e:
        print("Error",e)



# To get IP Address of the URL provided 
def get_ip_address(url):
        try:
            ip_address = socket.gethostbyname(url)
            return ip_address

        except socket.gaierror as e:
            return    
        
if __name__=="__main__":
    website_url = input("Enter the website URL: ")
    ip_address = get_ip_address(website_url)
    print("IP address :", {ip_address})
    if not urlparse(website_url).scheme:
        website_url = "https://" + website_url
   
    get_website(website_url)
    
    print("--"*20)



   

    




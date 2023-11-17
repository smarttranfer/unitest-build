import requests
import argparse


parser = argparse.ArgumentParser(description="Just an example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-u", "--url", help="url_git")
parser.add_argument("-f", "--file", help="path_file ")
parser.add_argument("-p", "--url_api", help="url_api")
args = parser.parse_args()

url = f"{args.url_api}"
payload = {'id': f'{args.url}'}
files=[('file',(f'{args.file}',open(f"{args.file}",'rb'),'application/octet-stream'))]
headers = {}
response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(response.text)





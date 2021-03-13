import requests,time, json

print("Loading Theo's webhook console")

time.sleep(0.5)

print("Loaded.")

def main():
    while True:
        option = input('''
        [0] Sets the webhook URL
        [1] Webhook message spammer
        [2] Delete webhook
        [3] Show webhook info
        [4] Change webhook name
        [5] Say one message
        [6] Checks the version
        ==> ''')

        if option == "0":
            hook = input("Webhook URL: ")
            print("Setting the webhook url to: ",hook)
            time.sleep(0.5)
            print("Success! Set the url to: ",hook," To change it again just run 0")
        
        if option == "1":
            message = input("Message to spam: ")
            amount = int(input("Amount to spam: "))
            wait = float(input("Message delay: "))

            headers = {"content-type": "application/json"}
            data = {"content": message}
            time.sleep(wait)
            print("Starting...")

            for _ in range(amount):
                r = requests.post(hook, json=data,headers=headers)
                
                if r.status_code == 200:
                    print("Done")

        if option == "2":
           
            requests.delete(hook)
            print("Deleting...")
            time.sleep(0.5)
            print("The requested webhook has been deleted.\n") 

        if option == "3":
            r = requests.get(hook)
            print("Getting webhook info...")
            time.sleep(0.5)
            print(r.content)
                
        if option == "4":
            wbname = input("Set name: ")
            print("Processing...")
            time.sleep(0.5)
            requests.patch(hook, json={"name": wbname})
            print("succsesfully changed webhook name to: ",wbname)

        if option == "5":
            message = input("Message to say: ")
            headers = {"content-type": "application/json"}
            data = {"content": message}
            print("Sending...")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Sent!")
        
        if option == "6":
            print("Loading version...")
            time.sleep(0.5)
            print("Version: V1.2 (You may need to download the latest version at https://github.com/TheoTheEpic/Theos-Webhook-Console)")

if __name__ == "__main__":
  main()

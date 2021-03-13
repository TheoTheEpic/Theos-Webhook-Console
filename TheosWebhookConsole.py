import requests,time, json

print("Loading Theo's webhook console")

time.sleep(0.5)

print("Loaded.")

def main():
    while True:
        print("Command list (Just type a number and press enter):")
        option = input('''
        [0] Sets the webhook URL
        [1] Webhook message spammer
        [2] Delete webhook
        [3] Show webhook info
        [4] Change webhook name
        [5] Say one message
        [6] Checks the version
        [7] Posts an ad for this webhook console
        [8] Pings everyone... :troll:
        ==> ''')

        version = "V1.5"

        if option == "0":
            hook = input("Webhook URL: ")
            data = {"content": "Success, connected to this webhook. Thanks for using Theo's Webhook Console by TheoTheEpic#0069"}
            headers = {"content-type": "application/json"}
            print("Setting the webhook url to: ",hook)
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Success! Connected to the webhook: ",hook)

        
        if option == "1":
            message = input("Message to spam: ")
            amount = int(input("Amount to spam: "))
            wait = float(input("Message delay: "))

            headers = {"content-type": "application/json"}
            data = {"content": message}
            time.sleep(wait)
            print("Starting...")
            print("Started!")

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
            print("Succsesfully changed webhook name to: ",wbname)

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
            print("Version: ",version," (You may need to download the latest version at https://github.com/TheoTheEpic/Theos-Webhook-Console)")

        if option == "7":
            data = {"content": "Get Theo's webhook console today! At: https://github.com/TheoTheEpic/Theos-Webhook-Console"}
            headers = {"content-type": "application/json"}
            print("Posting ad...")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Posted")

        if option == "8":
            data = {"content": "@everyone :sunglasses:"}
            headers = {"content-type": "application/json"}
            print("Sending @everyone ping...")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Sent @everyone ping!")

        if option == "9":
           print("WIP")


if __name__ == "__main__":
  main()

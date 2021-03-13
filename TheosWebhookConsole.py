import requests,time, json

print("Loading Theo's webhook console")

time.sleep(0.5)

print("Loaded.")

def main():
    while True:
        print("Command list:")
        option = input('''
        [set] Sets the webhook URL
        [spam] Webhook message spammer
        [delete] Delete webhook
        [info] Show webhook info
        [change-name] Change webhook name
        [say] Say one message
        [version] Checks the version
        [ad] Posts an ad for this webhook console
        [everyone] Pings everyone... :troll:
        [sus] Sends sus!1!!!
        [rick] Sends a rickroll with a bit.ly link
        ==> ''')

        version = "V1.6"

        if option == "set":
            hook = input("Webhook URL: ")
            data = {"content": "Console message (Ignore): Logged into *this* webhook. (Webhook Console by TheoTheEpic#0069)"}
            headers = {"content-type": "application/json"}
            print("Setting the webhook url to: ",hook)
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Success! Connected to the webhook, you can now use commands!")

        
        if option == "spam":
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

        if option == "delete":
           
            requests.delete(hook)
            print("Deleting...")
            time.sleep(0.5)
            print("The requested webhook has been deleted.\n") 

        if option == "info":
            r = requests.get(hook)
            print("Getting webhook info...")
            time.sleep(0.5)
            print(r.content)
                
        if option == "change-name":
            wbname = input("Set name: ")
            print("Processing...")
            time.sleep(0.5)
            requests.patch(hook, json={"name": wbname})
            print("Succsesfully changed webhook name to: ",wbname)

        if option == "say":
            message = input("Message to say: ")
            headers = {"content-type": "application/json"}
            data = {"content": message}
            print("Sending...")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Sent!")
        
        if option == "version":
            print("Loading version...")
            time.sleep(0.5)
            print("Version: ",version," (You may need to download the latest version at https://github.com/TheoTheEpic/Theos-Webhook-Console)")

        if option == "ad":
            data = {"content": "Get Theo's webhook console today! At: https://github.com/TheoTheEpic/Theos-Webhook-Console"}
            headers = {"content-type": "application/json"}
            print("Posting ad...")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Posted")

        if option == "everyone":
            data = {"content": "@everyone :sunglasses:"}
            headers = {"content-type": "application/json"}
            print("Sending @everyone ping...")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Sent @everyone ping!")

        if option == "sus":
         data = {"content": "When the imposter is sus :flushed:"}
         data2 = {"content": "https://media.discordapp.net/attachments/804662853059608627/820368810942398464/sus2.png"}
         headers = {"content-type": "application/json"}
         print("Sending sus :flushed:")
         time.sleep(0.5)
         r = requests.post(hook, json=data,headers=headers)
         r = requests.post(hook, json=data2,headers=headers)
         print("Sent sus :flushed:")

        if option == "rick":
            data = {"content": "Come watch this epic video! :money_mouth: <http://bit.ly/pog-video>"}
            headers = {"content-type": "application/json"}
            print("Sending rickroll...")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Sent rickroll!")


if __name__ == "__main__":
  main()

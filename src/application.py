import json
import sys


class Application:
    # @brief Reads the configuration file in binary
    def readConfigFile(self, path='config/configme.json'):
        try:
            configFile = open(path, 'r')
        except IOError:
            print('Does configuration file exist?', file=sys.stderr)
        else:
            return configFile

    # @brief Parses a JSON string file
    def parseJsonConfig(self, file):
        try:
            jsonParsed = json.load(file)
        except json.JSONDecodeError:
            print('Is JSON syntax correct?', file=sys.stderr)
        else:
            return jsonParsed

    # @brief initialize the application
    def initialize(self):
        configFile = self.readConfigFile()
        self.configAttr = self.parseJsonConfig(configFile)

        print("""GrandChat : A simple messenger for geeks and stuff
        Motto: Whoever wants speak, has the right
        ==================================================================""")

        quit = False
        while not quit:
            option = self.menu()

            # -*- direct conversation -*-
            if option == 1:
                print('I am right here')
                self.startDirectChat()
            # -*- group conversation -*-
            elif option == 2:
                self.startGroupConversation()
            # -*- right now this can only be the way out -*-
            else:
                quit = True

        sys.exit(0)

    def menu(self):
        print("""\nSon, welcome to machine. You have two options so far:
1) Start a direct conversation
2) Start or enter a group
3) Go fuck yourself outta here

Option> """, end='')

        option = int(input())
        while option not in range(1, 4):
            print("Stop wasting your time, piece of shit")
            print("Option> ")
            option = int(input())

        return option

    def startDirectChat(self):
        print("Starting direct conversation")

    def startGroupConversation(self):
        print("Starting group conversation")

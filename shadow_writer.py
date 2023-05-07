import json

class ShadowWriterPlugin:
    def __init__(self):
        self.characters = []

    def extract_character_data(self, chat_logs):
        for chat in chat_logs:
            # extract the relevant information from the chat log
            name = chat["name"]
            age = chat["age"]
            occupation = chat["occupation"]
            personality = chat["personality"]
            background = chat["background"]
            current_status = chat["current_status"]
            emotion = chat["emotion"]
            gender = chat["gender"]
            sexuality = chat["sexuality"]
            strength = chat["strength"]
            agility = chat["agility"]
            intelligence = chat["intelligence"]
            charisma = chat["charisma"]
            willpower = chat["willpower"]

            # create a character dictionary
            character = {
                "name": name,
                "age": age,
                "occupation": occupation,
                "personality": personality,
                "background": background,
                "current_status": current_status,
                "emotion": emotion,
                "gender": gender,
                "sexuality": sexuality,
                "strength": strength,
                "agility": agility,
                "intelligence": intelligence,
                "charisma": charisma,
                "willpower": willpower
            }
            # add the character to the list of characters
            self.characters.append(character)

    def save_characters(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.characters, file, indent=4)

    def load_characters(self, filename):
        with open(filename) as file:
            self.characters = json.load(file)

import os
import unittest
from shadow_writer import ShadowWriterPlugin

class TestShadowWriterPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = ShadowWriterPlugin()

    def test_create_character(self):
        self.plugin.create_character(name="Alice", age=25, occupation="Writer", personality=["Creative", "Introverted"], background="Alice grew up in a small town and always loved writing stories...", current_status="Alice is working on a new novel and feeling inspired...", emotion="Excited", gender="Female", sexuality="Straight", strength=6, agility=7, intelligence=9, charisma=5, willpower=8)
        self.assertEqual(len(self.plugin.characters), 1)

    def test_save_and_load_characters(self):
        self.plugin.create_character(name="Bob", age=30, occupation="Software Developer", personality=["Logical", "Detail-oriented"], background="Bob studied computer science at MIT and has been working as a software developer for 5 years...", current_status="Bob is working on a new project and feeling stressed...", emotion="Stressed", gender="Male", sexuality="Straight", strength=5, agility=8, intelligence=10, charisma=3, willpower=7)

        # save the character data to a temporary file
        filename = "test_characters.json"
        self.plugin.save_characters(filename)

        # load the character data from the file and check that it matches the original data
        self.plugin.load_characters(filename)
        self.assertEqual(len(self.plugin.characters), 1)
        self.assertEqual(self.plugin.characters[0]["name"], "Bob")
        self.assertEqual(self.plugin.characters[0]["age"], 30)
        self.assertEqual(self.plugin.characters[0]["occupation"], "Software Developer")
        self.assertEqual(self.plugin.characters[0]["personality"], ["Logical", "Detail-oriented"])
        self.assertEqual(self.plugin.characters[0]["background"], "Bob studied computer science at MIT and has been working as a software developer for 5 years...")
        self.assertEqual(self.plugin.characters[0]["current_status"], "Bob is working on a new project and feeling stressed...")
        self.assertEqual(self.plugin.characters[0]["emotion"], "Stressed")
        self.assertEqual(self.plugin.characters[0]["gender"], "Male")
        self.assertEqual(self.plugin.characters[0]["sexuality"], "Straight")
        self.assertEqual(self.plugin.characters[0]["strength"], 5)
        self.assertEqual(self.plugin.characters[0]["agility"], 8)
        self.assertEqual(self.plugin.characters[0]["intelligence"], 10)
        self.assertEqual(self.plugin.characters[0]["charisma"], 3)
        self.assertEqual(self.plugin.characters[0]["willpower"], 7)

        # delete the temporary file
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()


class Story:
 def __init__(self,title,length,moral_lessons,age_group):
   self.title  = title
   self.length = length
   self.moral_lessons = moral_lessons
   self.age_group = age_group

class StoryTeller(Story):
 def __init__(self,name):
     self.name = name
   
 def tell_story(self):
   return f"The story tellers name is {self.name}"
  
class Translator(Story):
 def __init__(self,language,name):
   self.language = language
   self.name = name
  
  
 def get_translation(self):
   return f"{self.name} is able to translate stories to {self.language}"
  
  
story1 = StoryTeller("Lemaiyan")
print(story1.tell_story())

story = Story("Born a crime",100,"Embrace equity","Adults")
print(story)

translator = Translator("Agikuyu","Jane")
print(translator.get_translation())
   

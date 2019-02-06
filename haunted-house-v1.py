from textwrap import dedent
import time

# my timer that i want to use when it is a time sensitive option but i dont know how to have the input of you desicion to cancel the timer while running
def timer():
    seconds = 5
    for i in range(seconds):
        print(str(seconds - i) + " seconds remain")
        time.sleep(1)

 #  i did not want to use the same engine but i was unable to think o
class Engine(object):
# intialing the engine with a scene map
    def __init__(self, scene_map):
        self.scene_map = scene_map
# play function is where the switching between rooms/scens is going to happen
# creating a variable current scene and setting it to whatever is passed in as the opening scene
    def play(self):
        current_scene = self.scene_map.opening_scene()
        # creating an arbitrary id for the last scene
        last_scene = self.scene_map.next_scene('end_scene')
        # loop to establish that the scene you are currently on is not the last
        while current_scene != last_scene:
            # the next scene is set to the current scene so that we can refernce back to the next scene map
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            # calling the function enter inside the new scene
            current_scene.enter()


# where you will awake up in this dark scary hosue
class Outside(object):
    def enter(self):
        print(dedent('''
         You are Dirk the Daring, a knight attempting to rescue Princess Daphne , the beautiful daughter of King Aethelred who is in need of your rescue from the evil dragon Singe who has locked the princess in his foul wizard Mordroc's castle. You must choose choose the right option in order to move on to another section of the caste

         You aproach the castle equipped with a sword, shield and armor. The sword has been masterly crafted just for you to defeat the evil wizard. The castle is surrounded with dark clouds with lightning string all around. It is so dark that only when the lightning strikes you get a glimpse of the giant fire breathing dragon flying around guarding the castle. Are you brave enought to keep going?
         '''))

        choice = input('> ')

        if choice == 'yes':
            print('You start you journey to save the princess. You aproach the bridge to get into the castle')
            return 'draw-bridge'

        elif choice == 'no':
            print('Wow how unadventures you are.')
            return 'death'

        else:
            print('WAT')
            return 'death'

# this is where are player will encounter his first moat monster
class DrawBridge(object):

    def enter(self):
        print(dedent('''
        You are walking along the bridge keeping your guard up when out of no where the floor falls beneath you. You are just barely able to hold on when you notice a giant purple monster with giant tentacle eyes coming right for you!'''))

        # my timer will start
        timer()
        choice = input('> ')

        if choice == 'attack':
            print('Need an object')
            return 'draw-bridge'

        elif choice == 'attack with sword':
            print('''With your one hand holding on for dear life you are still able to draw your sword and slice off two of the monsters tentacles. With one giant swing, purple ooz spews everywhere as the tentacles fall into the mirky moat below.''')
            return 'draw_bridge_two'

        elif choice == 'block':
            print(dedent('''
            You attempt to block the creature but he has already grabbed ahold of your legs and drug into the depths of the moat.'''))
            return 'outside'

        else:
            print(dedent('''
            You grabbed by the tentacles of the giant moat monster and were never seen again
            '''))
            return 'depths'

# After the encounter with the moat monster
class DrawBridgeTwo(object):
    def enter(self):
        print(dedent('''
        One hand still grabbing on to the ledge you feel yourself slipping.'''))

        choice = input('> ')

        if choice == 'climb up':
            print('You attempt to climb up but the ooz from the monster has coated the entire bridge and you fall to your death')
            return 'outside'

        elif choice == 'parkour':
            print(dedent('''
            You swing yourself up while doing a tripple backflip while drawing your sworb back into your sling.'''))
            return 'inside-gate'

# phase 4
class InsideGate(object):
    def enter(self):
        print(dedent('''
        You make your way into the castle and you approach three doors, one to the left, one to the right and one straight ahead. The cieling starts to crumble above you, act fast.'''))

        choice = input('> ')

        if choice == 'left':
            print('You fall into the abyss freefalling for etirnity')
            return 'outside'
        elif choice == 'straight':
            print('As you go to enter a stamped of elephants comes running in to trample you.')
            return 'outside'
        elif choice == 'right':
            print('You walk into the door on the right when you here a crash behind you barricading, you notice the wall has collapsed trapping you inside. ')
            return 'brick-room'

        else:
            print('WAT')
            return 'inside-gate'

class BrickRoom(object):
    def enter(self):
        print(dedent('''
        As you are looking for a passage to get out from, you cant shake this uneasy feeling that someone... or something is watching you. You notice a small passage just on the other side of the room. As you walk toward it you notice furniture and rubble satrt floating and being tossed all around the room, the rubble is stacking up creating a supernatural barriar keeping you from leaving. A couch flying right at you!'''))

        choice = input('> ')

        if choice == 'charge':
            print(dedent('''
            As you charge the wall a brick comes flying out of nowhere and you get knocked out'''))

            return 'end_scene'




# phase 5
class EndScene(object):
            def enter(self):
                print("You won! You have saved the princess!")
                return 'end_scene'

class Map(object):
# where my dictionary is  order  to reference the opening scene
# this is where i   m adding my scenes as im making them
    map_area = {
    'outside': Outside(),
    'draw-bridge': DrawBridge(),
    'draw_bridge_two': DrawBridgeTwo(),
    'inside-gate': InsideGate(),
    'end_scene': EndScene()
    }
# i am initializing the map class and creating my start_scene instance
    def __init__(self, start_scene):
        self.start_scene = start_scene
#  ret_value has been assigned the Map directory to reference the scene names with the class names
    def next_scene(self, scene_name):
        ret_value = Map.map_area.get(scene_name)
        return ret_value

    def opening_scene(self):
        return self.next_scene(self.start_scene)


start_map = Map('outside')
the_game = Engine(start_map)

the_game.play()

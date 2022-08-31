class Node:
    def __init__(self, value, utility: list, text: list, choice:list, nextValue: list) -> None:
        self.data = value
        self.dataGame = []
        self.dataGame.append(utility)
        self.dataGame.append(text)
        self.dataGame.append(choice)
        self.nextVal = nextValue
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value, utility, text, choice, nextValue):
        # DFS helper function
        def DFS(current, value, utility, text, choice, nextValue):
            # Base Condition jika valuenya masih none return data yang dimasukkan ke dalam pemanggilnya
            if current == None:
                return Node(value, utility, text, choice, nextValue)
            # Traversal (mencari lokasi yang benar)
            if value < current.data:
                current.left = DFS(current.left, value, utility, text, choice, nextValue)

            elif value > current.data:
                current.right = DFS(current.right, value, utility, text, choice, nextValue)

            return current

        if self.root == None:
            self.root = Node(value, utility, text, choice, nextValue)
        else:
            self.root = DFS(self.root, value, utility, text, choice, nextValue)

    def search(self, value):
        def DFS(cur, value):
            # Base Condition
            if cur.data == value:
                return cur

            if value < cur.data:
                return DFS(cur.left, value)

            if value > cur.data:
                return DFS(cur.right, value)

        return DFS(self.root, value)

    def delete(self, value):
        def DFS(current, value):
            # Base Condition jika valuenya masih none return data yang dimasukkan ke dalam pemanggilnya
            if current.data == value:
                if current.right != None and current.left != None:
                    pilihan = input('Data yang ingin diambil (kiri atau kanan) : ')
                    if pilihan.lower() == 'kiri':
                        current = current.left
                    elif pilihan.lower() == 'kanan':
                        current = current.right
                else:
                    if current.right != None and current.left == None:
                        current = current.right

                    elif current.right == None and current.left != None:
                        current = current.left

                    elif current.right == None and current.left == None:
                        current = None
                        current.nextVal = [None]

                return current
            # Traversal (mencari lokasi yang benar)
            if value < current.data:
                current.left = DFS(current.left, value)
                current.nextVal[0] = current.left.data

            elif value > current.data:
                current.right = DFS(current.right, value)
                current.nextVal[1] = current.right.data

            return current

        if self.root.data == value:
            if self.root.right != None and self.root.left != None:
                pilihan = input('Data yang ingin diambil (kiri atau kanan) : ')
                if pilihan.lower() == 'kiri':
                    self.root = self.root.left
                elif pilihan.lower() == 'kanan':
                    self.root = self.root.right
            else:
                if self.root.right != None and self.root.left == None:
                    self.root = self.root.right
                elif self.root.right == None and self.root.left != None:
                    self.root = self.root.left
                elif self.root.right == None and self.root.left == None:
                    self.root = None
                    print('Data habis')
            return
        else:
            DFS(self.root, value)
            # self.root = DFS(self.root, value)

    def edit(self, value, newUtility: list, newText: list, newChoice: list): #edit sebagian
        def DFS(cur, value):
            # Base Condition
            if cur.data == value:
                cur.dataGame = []
                cur.dataGame.append(newUtility)
                cur.dataGame.append(newText)
                cur.dataGame.append(newChoice)
                return

            if value < cur.data:
                return DFS(cur.left, value)

            if value > cur.data:
                return DFS(cur.right, value)

        DFS(self.root, value)

    def edit2(self, value): #Edit seluruhnya
        def DFS(cur, value):
            # Base Condition
            if cur.data == value:
                cur.dataGame = []
                utility = []
                text = []
                choice = []
                j = 0
                data = input('Isikan BGM / SFX anda dalam format wav : ')
                data2 = input('Isikan Format Background anda dalam format jpg/png : ')
                utility.append(data2)
                utility.append(data)
                cur.dataGame.append(utility)
                while True:
                    print('Keluar Isikan text = 0')
                    data = input('Isikan text ' + str(int(j + 1)) + ' anda : ')
                    if data != '0':
                        text.append(data)
                    else:
                        break
                    j += 1
                cur.dataGame.append(text)
                data = input('Isikan Left Choice : ')
                data2 = input('Isikan Right Choice : ')
                choice.append(data)
                choice.append(data2)
                cur.dataGame.append(choice)
                return

            if value < cur.data:
                return DFS(cur.left, value)

            if value > cur.data:
                return DFS(cur.right, value)

        DFS(self.root, value)

    def print_tree(self, val="data", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * \
                '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + \
                (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root, val, left, right)
        for line in lines:
            print(line)

    def printInorder(self):
        def DFS(cur):
            if not cur:
                return

            DFS(cur.left)
            print(cur.data, end=" ")  # = inorder
            DFS(cur.right)

        DFS(self.root)
        print("")

bst = BST()
#1. Game Root / Awal cerita / #65
util = ['Car_crash_BnW.png', 'CarCrashSkid.wav']
text = ['One day, you want to go hiking', 'But on the way, your car got stuck in deep woods', 'What would you do?']
choice = ['Wait in car', 'Find some help']
nextValue = [33, 97]
bst.insert(65, util, text, choice, nextValue)

#FULL KANAN!
#Path 97 (kanan)
util = ['97_forest_path_BnW.png', '97_Animal_sound.wav']
text = ['You choice to find some help', 'You go deep into the woods', 'Suddenly, you hear some scary sound', 'What would you do?']
choice = ['Lari ke kiri', 'Lari ke kanan']
nextValue = [81, 113]
bst.insert(97, util, text, choice, nextValue)

#Path DIE 81 (kiri)
util = ['81_Tiger.jpg', 'dead.wav']
text = ['You died, some hungry tiger suddenly appeared before you', 'He jump straight into your body, as he seen a weak and meaty body of yours.']
choice = [None]
nextValue = [None]
bst.insert(81, util, text, choice, nextValue)

#Path 113 (kanan)
util = ['113.png', 'Silent.wav']
text = ['You saw some strange symbol hinting to go right', 'It maybe a good sign, or a bad sign..']
choice = ['Go opposite way', 'Follow the symbol']
nextValue = [105, 121]
bst.insert(113, util, text, choice, nextValue)

#Path 105 (kiri)
util = ['105.png', 'Silent.wav']
text = ['You ran to the opposite way from the symbol', 'You see some light from afar', 'It seems some local villagers may want to meet you..']
choice = ['Ran Away!!', 'Meet the villagers']
nextValue = [101, 109]
bst.insert(105, util, text, choice, nextValue)

#Path 121 (kanan)
util = ['121.png', 'Search.wav']
text = ['It seems that symbol made by the last survivor.', 'He/ She left you a flashlight and a map', 'The notes tells you where to get the map and some clues to get it']
choice = ['Follow the notes', 'Ignore the notes']
nextValue = [117, 125]
bst.insert(121, util, text, choice, nextValue)

#Path 117 (kiri)
util = ['117.png', '17.FootStep.wav']
text = ['The notes tells you the map located in the Canibal\'s house', 'You are in front the door of the canibal\'s house']
choice = ['Kill the canibal', 'Come inside sneakily']
nextValue = [115, 119]
bst.insert(117, util, text, choice, nextValue)

#Path 125 (kanan)
util = ['125.png', '17.FootStep.wav']
text = ['You keep walking and start entering the fog', 'After some time, you see some silhouette.. It looks like some people standing']
choice = ['Approach them', 'Go back']
nextValue = [123, 127]
bst.insert(125, util, text, choice, nextValue)

#Path 123 (kiri)
util = ['127_123.png', '123.127_Zombie_Eat.wav']
text = ['WHOA! It\'s a DAMN.. ZOMBIE.. APOCALYPSE..', 'They surrounded you and have a banquet on you', 'Only your bones remained..']
choice = [None]
nextValue = [None]
bst.insert(123, util, text, choice, nextValue)

#Path 127 (kanan)
util = ['127_123.png', '123.127_Zombie_Eat.wav']
text = ['You tried to run', 'But a rock tripped your feet and they quickly eat every part of you', 'You Died..']
choice = [None]
nextValue = [None]
bst.insert(127, util, text, choice, nextValue)

#Path 115 (kiri)
util = ['115.png', 'Search.wav']
text = ['You collected your thoughts and planned to kill the canibal!', 'The notes tells you the canibal set his own traps around his own house..', 'You make use of that and killed the canibal!', 'The only thing left is to search for the map..']
choice = ['Search Bedroom', 'Search the canibal\'s corpse']
nextValue = [114, 116]
bst.insert(115, util, text, choice, nextValue)

#Path 119 (kanan)
util = ['119.png', 'Running_2.wav']
text = ['After doing some long consideration, you choose to sneak inside his house..', 'But you immediately trigerred the canibal\'s traps!', 'The canibal knows you are inside his house and chases you!', 'After running through a corridor, you see two doors']
choice = ['Go in the kitchen', 'Hide in the Bedroom']
nextValue = [118, 120]
bst.insert(119, util, text, choice, nextValue)

#Path 114 (kiri)
util = ['dieScreen.png', '114.Shotgun.wav']
text = ['You tried to search the canibal\'s bedroom.', 'Unfortunately.. while searching the map', 'Your foot slipped and triggerred his last trap..', 'Causing you to be shot by a rifle in your face..', 'You Died..']
choice = [None]
nextValue = [None]
bst.insert(114, util, text, choice, nextValue)

#Path 116 (kanan)
util = ['23.png', 'Silent.wav']
text = ['You decided to search for the corpse first', 'And the map was hidden in his inner most pocket', 'You found the map and with the notes.., you managed to survive in the forest', 'You searched around the house and found a galon of gas', 'You flee from the forest in the morning']
choice = [None]
nextValue = [None]
bst.insert(116, util, text, choice, nextValue)

#Path 118 (kiri)
util = ['118.png', 'Sad_End.wav']
text = ['You go in the kitchen to find a weapon', 'You found a kitchen knife', 'You used it to stab the canibal, But..', 'It turns out to be a replica knife', 'The canibal caught you.. ', 'You Died..']
choice = [None]
nextValue = [None]
bst.insert(118, util, text, choice, nextValue)

#Path 120 (kanan)
util = ['dieScreen.png', '120_explosion.wav']
text = ['You choose to hide inside his bedroom', 'Unfortunately, your foot steps on the wrong plank and triggered a trap', 'You Died..']
choice = [None]
nextValue = [None]
bst.insert(120, util, text, choice, nextValue)

#Path 101 (kiri)
util = ['101.png', '101.Animal_trap.wav']
text = ['You are getting scared and decided to run away', 'But your feet get caught in an animal trap', 'The villagers think you are a wild animal and hunted you..', 'You Died..']
choice = [None]
nextValue = [None]
bst.insert(101, util, text, choice, nextValue)

#Path 109 (kanan)
util = ['109.png', '17.FootStep.wav']
text = ['You muster up your courage and meet the villagers', 'Gambling if they are good people or not..', 'The villagers seems nice and get you a place to stay the night.','But for some reason.. they seem kind of suspicious..']
choice = ['Leave at night', 'Stay the night']
nextValue = [107, 111]
bst.insert(109, util, text, choice, nextValue)

#Path 107 (kiri)
util = ['107_dikejar.png', 'Running_2.wav']
text = ['The more you think about it, the more suspicious it becomes..', 'You decided to leave the village at night.', 'Before you go, you bring a rifle full of ammo hidden in the house you\'re at', 'It seems the villager noticed you\'re gone and started looking for you', 'The nice facade they put up had long gone and they showed their hostility to you.. ']
choice = ['Kill them', 'Hide in an abandoned house']
nextValue = [106, 108]
bst.insert(107, util, text, choice, nextValue)

#Path 111 (kanan)
util = ['41_111_cult.png', 'Sad_End.wav']
text = ['You gather your thoughts and decided that it just your negative thinking while eating a dinner they provided', 'Unknowingly to you, the villagers had made you ate a brainwashing pill in your dinner soup', 'When you wake up in the morning, you forget who you are.', 'Turns out, the villagers of that village was a believer of a heretical cult', 'And one of them, is you..']
choice = [None]
nextValue = [None]
bst.insert(111, util, text, choice, nextValue)

#Path 106 (kiri)
util = ['106_crazyman.png', 'Sad_End.wav']
text = ['You started to get tired of all of this', 'You decided to go back and kill everybody', 'After you shot them al with your rifle and burned down their village, you started to regret what you\'re doing', 'You don\'t know a way out and started to lose your mind while wandering in the woods alone', 'You Died of hunger..']
choice = [None]
nextValue = [None]
bst.insert(106, util, text, choice, nextValue)

#Path 108 (kanan)
util = ['108.png', '108.Man_Scream.wav']
text = ['The villagers surrounding the house you\'re at right now.', 'They started chanting some kind of spell and burned the house down.', 'Looks like they wanted to make you a sacrifice', 'You tried to escape but they caught you and slain you on the spot', 'You Died..']
choice = [None]
nextValue = [None]
bst.insert(108, util, text, choice, nextValue)


#FULL KIRI!
#Path 33 (kiri)
util = ['33.png', '33.wav']
text = ['When waiting in car, you saw a faint light from afar', 'A man came closer to you and seeing your condition, he suggest you to come with him to his house..']
choice = ['Go with him', 'Run away to woods']
nextValue = [17, 49]
bst.insert(33, util, text, choice, nextValue)

#Path 17 (kiri)
util = ['17_Stalker_BnW.png', '17.FootStep.wav']
text = ['His house decorated with many hunting equipment', 'He also offered you dinner and a place to stay', 'He looks like a good guy, but strangely, he sees you with a hungry eye']
choice = ['Spend the night', 'Leave at night']
nextValue = [9, 25]
bst.insert(17, util, text, choice, nextValue)

#Path 9 (kiri)
util = ['9.png', '9.eaten.wav']
text = ['You are so tired after eating full course dinner in his house', 'You are getting ready to sleep after such a long and tiring day', 'After some time, you started to feel a little pain from your hand', 'You wake up being chained to the butcher table', 'Turns out that man was a canibal and he is ready to butcher you', 'You Died..']
choice = [None]
nextValue = [None]
bst.insert(9, util, text, choice, nextValue)

#Path 25 (kanan)
util = ['25_run.png', 'U_Never_Run_2.wav']
text = ['Your guts tells you this man is dangerous and leave the house at night', 'And its proved to be true.. That man chased after you with a shotgun in his hand']
choice = ['Hide in a bush', 'Jump to the river']
nextValue = [21, 29]
bst.insert(25, util, text, choice, nextValue)

#Path 21 (kiri)
util = ['21.Jungle_Bush.jpg', '121.Bush.wav']
text = ['You hide in nearby bush', 'In your panic, you see a sharp branch']
choice = ['Attack him', 'Stay silent']
nextValue = [19, 23]
bst.insert(21, util, text, choice, nextValue)

#Path 19 (kiri)
util = ['19_shottedSerial.png', '114.Shotgun.wav']
text = ['You gamble your way out and attack him with the brach you found', 'But you missed and he managed to shot you', 'You Died..']
choice = [None]
nextValue = [None]
bst.insert(19, util, text, choice, nextValue)

#Path 23 (kanan)
util = ['23.png', '121.Bush.wav']
text = ['You decided this was not the right time to act brave and stay hidden in the bush', 'After a long time, the Canibal finally gave up on you.. you sleep in the bush until morning and continue to search for help']
choice = [None]
nextValue = [None]
bst.insert(23, util, text, choice, nextValue)

#Path 29 (kanan)
util = ['29_sungai.png', '29._Jump_To_water.wav']
text = ['You run away from him until you found a river', 'Cornered by the Canibal, you jumped to the river and luckily stranded by the side of a city']
choice = ['Tell the cops', 'Forget Everything']
nextValue = [27, 31]
bst.insert(29, util, text, choice, nextValue)

#Path 27 (kiri)
util = ['27_wall.png', '27_Scream_group.wav']
text = ['You search for the police and told them all that happened', 'But the police only laugh and shrugged your story.', 'You desperately told them that your story was true, but the police started to doubt your sanity', 'You\'re assigned to local mental hospital']
choice = [None]
nextValue = [None]
bst.insert(27, util, text, choice, nextValue)

#Path 31 (kanan)
util = ['31_traumatise.png', 'Silent.wav']
text = ['After recuperating in the hospital for sometime, you are having a severe trauma about dark woods and forest', 'But you decided that life must go on and decided to forget about everything.']
choice = [None]
nextValue = [None]
bst.insert(31, util, text, choice, nextValue)

#Path 49 (kanan)
util = ['49.png', 'Running_2.wav']
text = ['You are scared and run away deeper to the woods', 'Suddenly you stumbled upon a ruin.' ]
choice = ['Explore', 'Enter the ruin']
nextValue = [41, 57]
bst.insert(49, util, text, choice, nextValue)

#Path 41 (kiri)
util = ['41_111_cult.png', 'Sad_End.wav']
text = ['While exploring the ruin, you realized that it looks more like temple than a ruin. All of a sudden, the cult followers surrounded you', 'They brought you inside the temple and brainwashed you there until you become a loyal followers just like them.']
choice = [None]
nextValue = [None]
bst.insert(41, util, text, choice, nextValue)

#Path 57 (kanan)
util = ['57.png', '57.Monster_Growl.wav']
text = ['You decide to hide in the ruins for some time', 'Unfortunately, you triggered the curse that casted on the ruins', 'The curse turns you into a monster!', 'You hear many footsteps behind you', 'Those people was the followers of a hidden cult, and this ruin is their temple.']
choice = ['Talk to them', 'Hide and run']
nextValue = [53, 61]
bst.insert(57, util, text, choice, nextValue)

#Path 53 (kiri)
util = ['53.png', '114.Shotgun.wav']
text = ['You are hoping those people would know how to break the curse and decided to talk to them.', 'But those people get scared of you and hunted you on the spot!', 'You Died..']
choice = [None]
nextValue = [None]
bst.insert(53, util, text, choice, nextValue)

#Path 61 (kanan)
util = ['61_bigFoot.png', '61._Monster_sound.wav']
text = ['You run away and accepted your fate as a monster']
choice = [None]
nextValue = [None]
bst.insert(61, util, text, choice, nextValue)

bst.print_tree()
bst.printInorder()
# bst.delete(17)
# bst.edit2(97)







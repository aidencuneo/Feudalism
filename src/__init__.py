import contextlib, os, random, sys, time

if sys.version_info[0] < 3:
	import urllib2
else:
	import urllib.request
if os.name == 'nt':
	import msvcrt
else:
	import termios

##
## Game created by Aiden Blishen Cuneo.
## Last update: 16/8/2018.
##

king = {
	'money': 50,
	'money_mult': 1,
	'food': 100,
	'food_mult': 1,
	'metal': 10,
	'nobles': 1,
	'knights': 2,
	'peasants': 8,

	'MAXNOBLES': 4,
	'MAXKNIGHTS': 8,
	'MAXPEASANTS': 24,

	'MAXMONEY': 500,
	'MAXFOOD': 1000,
	'MAXMETAL': 100,

	'defense': 6,
}

# Noble variables:

# Knight variables:

# Peasant variables:

__version__ = '0.2.8a'
dayCount = 1
user = 'peasant'

# THIS WEBSITE CONTAINS A LIST OF ALL PRONOUNS: 'https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61767&view=co'

lines = ['', '', '', '', '', '', '', '']


@contextlib.contextmanager
def raw_mode(file):
	global OS
	if OS.startswith("Darwin"):
		old_attrs = termios.tcgetattr(file.fileno())
		new_attrs = old_attrs[:]
		new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
		try:
			termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
			yield
		finally:
			termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


def kbfunc():
	global OS
	if OS.startswith("Windows"):
	    if msvcrt.kbhit():
	        ret = msvcrt.getch()
	    else:
	        ret = False
	    return ret


class Peasant: # INCOMPLETE SECTION
	def __init__(self):
		money = 10
		food = 10
		rye: 0
		wheat: 0
		corn: 0
		grain: 0
		cornflour: 0
		milk: 0
		beef: 0
		flour': 0
		yeast': 0

		family': 1
		cows': 2

		MAXFAMILY': 3
		MAXCOWS': 14
		MAXMONEY': 100
		MAXFOOD': 100
		MAXCROPS': 10

		crops': 0
		current_crop_type': None

		corn_price': 3
		wheat_price': 2
		rye_price': 1
		corn_time': 4
		wheat_time': 3
		rye_time': 2

		plant_crops_var': 1
		cook_food_var': 0

		mill_var': 0
		mill_var2': 0
		mill_var3': 0



class Key:

	def get_key(self):
		global OS
		if OS.startswith("Darwin"):
			with raw_mode(sys.stdin):
				try:
					while True:
						ch = sys.stdin.read(1)
						if ch != None:
							return ch
							break
				except(KeyboardInterrupt, EOFError):
					sys.exit()
		if OS.startswith("Windows"):
			while True:
				ch = kbfunc()
				if ch != None:
					return ch
					break
	
	def pause(self):
		ch = input.getKey()
		if OS.startswith("Windows"):
			ch = ch.decode()
		while True:
			if ch != False and ch != None:
				if  ch == "\r":
					break
	
	def compare(self, ch, ktype):
		if OS.startswith("Windows"):
			ch = ch.decode()
		print(ch)


class KeyListener:

	def __init__(self, actions):
		self.actions = actions

	def listen(self, key):
		if key in self.actions:
			if self.actions[key] != '':
				self.actions[key]()


mainKeyListen = KeyListener({
	'm': tradeFoodOrMoney,
	'n': buyMetal,
	'1': assignNoble,
	'2': hireKnight,
	'3': newPeasant,
	'z': raidEnemyStart,
})


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def displayHelp():
	if user == "king":
		print("1 - Assign noble. 2 - Hire knight. 3 - Bring in peasant. H - Display help. M - Buy stockpile of food. N - Buy container of metal. Z - Raid nearby towns.")
	if user == "noble":
		print("No help is available for your class.")
	if user == "knight":
		print("No help is available for your class.")
	if user == "peasant":
		print("1 - Marry someone/Have child. 2 - Plant crops. 3 - Harvest crops. M - Go to mill. C - Cook food. B - Sell crops. G - Market. H - Display help. P - Cow menu. Q - Upgrade to knight.")
	if sys.version_info[0] < 3:
		cont = raw_input()
	if sys.version_info[0] >= 3:
		cont = input()
	printPeasantMenu()

def asciiMenuMain():
	global line1
	global line2
	global line3
	global line4
	global line5
	global line6
	global line7
	global line8
	if knights >= 1:
		line1 = "  ()-"
	if knights >= 2:
		line1 = "  ()-  ()-"
	if knights >= 3:
		line2 = "  ()-"
	if knights >= 4:
		line2 = "  ()-  ()-"
	if knights >= 5:
		line3 = "  ()-"
	if knights >= 6:
		line3 = "  ()-  ()-"
	if knights >= 7:
		line4 = "  ()-"
	if knights >= 8:
		line4 = "  ()-  ()-"
	if peasants >= 1:
		line5 = "  ."
	if peasants >= 2:
		line5 = "  . ."
	if peasants >= 3:
		line5 = "  . . ."
	if peasants >= 4:
		line5 = "  . . . ."
	if peasants >= 5:
		line5 = "  . . . . ."
	if peasants >= 6:
		line5 = "  . . . . . ."
	if peasants >= 7:
		line6 = "  ."
	if peasants >= 8:
		line6 = "  . ."
	if peasants >= 9:
		line6 = "  . . ."
	if peasants >= 10:
		line6 = "  . . . ."
	if peasants >= 11:
		line6 = "  . . . . ."
	if peasants >= 12:
		line6 = "  . . . . . ."
	if peasants >= 13:
		line7 = "  ."
	if peasants >= 14:
		line7 = "  . ."
	if peasants >= 15:
		line7 = "  . . ."
	if peasants >= 16:
		line7 = "  . . . ."
	if peasants >= 17:
		line7 = "  . . . . ."
	if peasants >= 18:
		line7 = "  . . . . . ."
	if peasants >= 19:
		line8 = "  ."
	if peasants >= 20:
		line8 = "  . ."
	if peasants >= 21:
		line8 = "  . . ."
	if peasants >= 22:
		line8 = "  . . . ."
	if peasants >= 23:
		line8 = "  . . . . ."
	if peasants >= 24:
		line8 = "  . . . . . ."
def asciiMenuN1():
	print("|                   |" + line1)
	print("|                   |" + line2)
	print("|                   |" + line3)
	print("|       Noble       |" + line4)
	print("|                   |" + line5)
	print("|                   |" + line6)
	print("|                   |" + line7)
	print("|                   |" + line8)
def asciiMenuN2():
	print("|         |         |" + line1)
	print("|         |         |" + line2)
	print("|         |         |" + line3)
	print("|  Noble  |  Noble  |" + line4)
	print("|         |         |" + line5)
	print("|         |         |" + line6)
	print("|         |         |" + line7)
	print("|         |         |" + line8)
def asciiMenuN3():
	print("| \               / |" + line1)
	print("|    \  Noble  /    |" + line2)
	print("|      \     /      |" + line3)
	print("|        \|/        |" + line4)
	print("|         |         |" + line5)
	print("|  Noble  |  Noble  |" + line6)
	print("|         |         |" + line7)
	print("|         |         |" + line8)
def asciiMenuN4():
	print("|         |         |" + line1)
	print("|  Noble  |  Noble  |" + line2)
	print("|         |         |" + line3)
	print("|_________|_________|" + line4)
	print("|         |         |" + line5)
	print("|  Noble  |  Noble  |" + line6)
	print("|         |         |" + line7)
	print("|         |         |" + line8)

def pAsciiMenuMain():
	global line1
	global line2
	global line3
	global line4
	global line5
	global line6
	global line7
	global pcows
	line1 = " " * 12
	line2 = " " * 12
	line3 = " " * 12
	line4 = " " * 12
	line5 = " " * 12
	line6 = " " * 12
	line7 = " " * 12
	if pcows >= 1:
		line1 = "  COW       "
	if pcows >= 2:
		line1 = "  COW  COW  "
	if pcows >= 3:
		line2 = "  COW       "
	if pcows >= 4:
		line2 = "  COW  COW  "
	if pcows >= 5:
		line3 = "  COW       "
	if pcows >= 6:
		line3 = "  COW  COW  "
	if pcows >= 7:
		line4 = "  COW       "
	if pcows >= 8:
		line4 = "  COW  COW  "
	if pcows >= 9:
		line5 = "  COW       "
	if pcows >= 10:
		line5 = "  COW  COW  "
	if pcows >= 11:
		line6 = "  COW       "
	if pcows >= 12:
		line6 = "  COW  COW  "
	if pcows >= 13:
		line7 = "  COW       "
	if pcows >= 14:
		line7 = "  COW  COW  "
def pAsciiMenu1():
	print("      /  \          |" + line1 + "|")
	print("    /      \        |" + line2 + "|")
	print("   /        \       |" + line3 + "|")
	print(" /            \     |" + line4 + "|")
	print("|              |    |" + line5 + "|")
	print("|     You      |    |" + line6 + "|")
	print("|              |    |" + line7 + "|")
	print("|              |    --------------")
	print("|              |    Beef = " + str(pbeef) + ", Milk = " + str(pmilk))
def pAsciiMenu2():
	print("      /||\          |" + line1 + "|")
	print("    /  ||  \        |" + line2 + "|")
	print("   /   ||   \       |" + line3 + "|")
	print(" /     ||     \     |" + line4 + "|")
	print("|      ||      |    |" + line5 + "|")
	print("| You  || Wife |    |" + line6 + "|")
	print("|      ||      |    |" + line7 + "|")
	print("|      ||      |    --------------")
	print("|      ||      |    Beef = " + str(pbeef) + ", Milk = " + str(pmilk))
def pAsciiMenu3():
	print("      /||\          |" + line1 + "|")
	print("    /  ||  \        |" + line2 + "|")
	print("   /   ||   \       |" + line3 + "|")
	print(" /     ||     \     |" + line4 + "|")
	print("| You  || Wife |    |" + line5 + "|")
	print("|      ||      |    |" + line6 + "|")
	print("|--------------|    |" + line7 + "|")
	print("|    Child     |    --------------")
	print("|              |    Beef = " + str(pbeef) + ", Milk = " + str(pmilk))

def assignNoble():
	global money
	global nobles
	global moneyMult
	if nobles < MAXNOBLES:
		print("")
		print("The Monarchy has assigned a new noble.")
		print("Nobles +1")
		print("Money -10")
		nobles += 1
		money -= 10
		moneyMult += 0.2
	else:
		print("The Monarchy tried to assign a new noble, but there wasn't enough space.")

def hireKnight():
	global metal
	global knights
	global defense
	global foodMult
	if knights < MAXKNIGHTS:
		if metal >= 10:
			print("")
			print("One of the Monarchy's nobles has hired a knight.")
			print("Knights +1")
			print("Metal -10")
			knights += 1
			metal -= 10
			defense += 3
			foodMult -= 0.1
		else:
			print("One of the Monarchy's nobles tried to hire a knight, but they didn't have enough metal.")
	else:
		print("One of the Monarchy's nobles tried to hire a knight, but there wasn't enough space.")

def newPeasant():
	global food
	global peasants
	global foodMult
	if peasants < MAXPEASANTS:
		print("")
		print("One of the Monarchy's knights brought in a new peasant.")
		print("Peasants +1")
		print("Food -5")
		peasants += 1
		food -= 5
		foodMult += 0.1
	else:
		print("One of the Monarchy's knights tried to bring in a new peasant, but there wasn't enough space.")

def raidEnemyStart():
	global defense
	global money
	global food
	global metal
	global enemyTownName1
	global enemyTownName2
	global enemyTownName3
	if knights > 0:
		print("")
		print("Would you like to raid for money(1), food(2), or metal(3)? Esc to exit and end day.")
		enemyTownNameOpened = urllib2.urlopen(enemyTownNameSite)
		pronounList = enemyTownNameOpened.read()
		enemyTownNameList = pronounList.splitlines()
		random1 = random.randint(1, 3)
		if random1 >= 1:
			enemyTownName1 = random.choice(enemyTownNameList)
		if random1 >= 2:
			enemyTownName2 = random.choice(enemyTownNameList)
		if random1 >= 3:
			enemyTownName3 = random.choice(enemyTownNameList)
		raidEnemyKeyListen()
		cls()
		if raidEnemyVar == 1:
			print("Raiding for money.")
			sleep(0.25)
			print("Searching for towns nearby...")
			sleep(1.5)
			print("")
			print("Town to attack:")	
			print(str(enemyTownName1) + " " + str(enemyTownName2) + " " + str(enemyTownName3))
			raidEnemyMain()
		if raidEnemyVar == 2:
			print("Raiding for food.")
			sleep(0.25)
			print("Searching for towns nearby...")
			sleep(1.5)
			print("")
			print("Town to attack:")	
			print(str(enemyTownName1) + " " + str(enemyTownName2) + " " + str(enemyTownName3))
			raidEnemyMain
		if raidEnemyVar == 3:
			print("Raiding for metal.")
			sleep(0.25)
			print("Searching for towns nearby...")
			sleep(1.5)
			print("")
			print("Town to attack:")	
			print(str(enemyTownName1) + " " + str(enemyTownName2) + " " + str(enemyTownName3))
			raidEnemyMain()

def raidEnemyMain():
	global defense
	global money
	global food
	global metal
	global raidEnemyVar
	enemyDefense = random.randint(1, 20)
	print("")
	print("Your strength = " + str(defense))
	print("Enemy strength = " + str(enemyDefense))
	print("")
	sleep(0.25)
	if raidEnemyVar == 1:
		if defense > enemyDefense:
			print("You won the battle and earned: " + str(enemyDefense) + " Money.")
			money = money + enemyDefense
		if defense < enemyDefense:
			print("You lost the battle and also lost " + str(defense) + " Money.")
			money = money - defense
		if defense == enemyDefense:
			lastMinuteVar = random.randint(1, 2)
			if lastMinuteVar == 1:
				print("You won the battle and earned: " + str(enemyDefense) + " Money.")
				money = money + enemyDefense
			if lastMinuteVar == 2:
				print("You lost the battle and also lost " + str(defense) + " Money.")
				money = money - defense
		print("Continuing in 5 seconds.")
		sleep(5)
		cls()
		main()
	if raidEnemyVar == 2:
		if defense > enemyDefense:
			print("You won the battle and earned: " + str(enemyDefense) + " Food.")
			food = food + enemyDefense
		if defense < enemyDefense:
			print("You lost the battle and also lost " + str(defense) + " Food.")
			food = food - defense
		if defense == enemyDefense:
			lastMinuteVar = random.randint(1, 2)
			if lastMinuteVar == 1:
				print("You won the battle and earned: " + str(enemyDefense) + " Food.")
				food = food + enemyDefense
			if lastMinuteVar == 2:
				print("You lost the battle and also lost " + str(defense) + " Food.")
				food = food - defense
		print("Continuing in 5 seconds.")
		sleep(5)
		cls()
		main()
	if raidEnemyVar == 3:
		if defense > enemyDefense:
			print("You won the battle and earned: " + str(enemyDefense) + " Metal.")
			metal = metal + enemyDefense
		if defense < enemyDefense:
			print("You lost the battle and also lost " + str(defense) + " Metal.")
			metal = metal - defense
		if defense == enemyDefense:
			lastMinuteVar = random.randint(1, 2)
			if lastMinuteVar == 1:
				print("You won the battle and earned: " + str(enemyDefense) + " Metal.")
				metal = metal + enemyDefense
			if lastMinuteVar == 2:
				print("You lost the battle and also lost " + str(defense) + " Metal.")
				metal = metal - defense
		print("Continuing in 5 seconds.")
		sleep(5)
		cls()
		main()

def tradeFoodOrMoney():
	global money
	global food
	global pmoney
	global pfood
	global prye
	global pwheat
	global pcorn
	if user == "king":
		if money > 20:
			print("")
			print("The Monarchy has traded money for a stockpile of food.")
			print("Food +20")
			print("Money -20")
			money -= 20
			food += 20
		else:
			print("The Monarchy tried to trade money for food, but he didn't have enough money.")
	if user == "noble":
		print("Not implemented yet.")
	if user == "knight":
		print("Not implemented yet.")
	if user == "peasant":
		var = prye + pwheat + pcorn
		var2 = prye * ryePrice + pwheat * wheatPrice + pcorn * cornPrice
		if var >= 1:
			print("")
			print("You sold your crops.")
			print("Money +" + str(var2))
			print("Crops -" + str(var))
			prye = 0
			pwheat = 0
			pcorn = 0
			pmoney += var2
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
		else:
			print("You don't have any crops to sell.")

def market():
	print("This feature will be implemented in version 0.2.7a or 0.2.8a.")
	if sys.version_info[0] < 3:
		cont = raw_input()
	if sys.version_info[0] >= 3:
		cont = input()
	printPeasantMenu()

def buyMetal():
	global money
	global metal
	if money > 20:
		print("")
		print("The Monarchy has traded money for a container of metal.")
		print("Metal +5")
		print("Money -20")
		money -= 20
		metal += 5
	else:
		print("The Monarchy tried to trade money for metal, but he didn't have enough money.")

def upgrade():
	global user
	global pmoney
	if user == "peasant":
		if pmoney >= 100:
			user = "knight"
			pmoney == 0

def addFamilyMember():
	global pfamily
	global PMAXFAMILY
	global MAXCROPS
	if pfamily < PMAXFAMILY:
		if pfamily == 1:
			var = 1
		if pfamily == 2:
			var = 2
		if var == 1:
			print("You have married someone and now have a wife.")
			pfamily += 1
			MAXCROPS += 10
		if var == 2:
			print("You have had a child with your wife.")
			pfamily += 1
			MAXCROPS += 10
		if pfamily > PMAXFAMILY:
			pfamily = PMAXFAMILY
	else:
		print("There is no room for another child.")

def plantCrops():
	global pfamily
	global plantCropsVar
	global MAXCROPS
	global cropsInField
	global cropTypeInField
	if cropTypeInField == None:
		if cropsInField <= 0:
			print("What would you like to plant? Rye(1), wheat(2), or corn(3).")
			plantCropsKeyListen()
			if plantCropsVar == 0:
				print("Continue in 2 seconds.")
				sleep(2)
			if plantCropsVar == 1:
				print("Planted " + str(MAXCROPS) + " rye into the field.")
				cropsInField = MAXCROPS
				cropTypeInField = "rye"
				plantCropsVar = 0
				print("Continue in 2 seconds.")
				sleep(2)
			if plantCropsVar == 2:
				print("Planted " + str(MAXCROPS) + " wheat into the field.")
				cropsInField = MAXCROPS
				cropTypeInField = "wheat"
				plantCropsVar = 0
				print("Continue in 2 seconds.")
				sleep(2)
			if plantCropsVar == 3:
				print("Planted " + str(MAXCROPS) + " corn into the field.")
				cropsInField = MAXCROPS
				cropTypeInField = "corn"
				plantCropsVar = 0
				print("Continue in 2 seconds.")
				sleep(2)
	else:
		print("You already have crops in your field.")

def cowMenu():
	global OS
	global ch
	global pcows
	global pmilk
	global pbeef
	global cowMenuVar
	print("")
	print("Cow menu:")
	print("Kill a cow(1).    Collect milk(2)")
	print("")
	if OS.startswith("Darwin"):
	    with raw_mode(sys.stdin):
	        try:
	            while True:
	                ch = sys.stdin.read(1)
	                if ch == "1":
	                	cowMenuVar = 1
	                	break
	                if ch == "2":
	                	cowMenuVar = 2
	                	break
	                if ord(ch) == 27:
	                	sys.exit()
	        except (KeyboardInterrupt, EOFError):
	            pass
	if OS.startswith("Windows"):
		while True:
			ch = kbfunc()
			if ch != False:
				if ch.decode() == "1":
					cowMenuVar = 1
					break
				if ch.decode() == "2":
					cowMenuVar = 2
					break
				if ch == chr(27).encode():
					sys.exit()
	if cowMenuVar == 1:
		if pcows > 0:
			print("You have killed one of your cows.")
			print("Beef +1")
			pcows -= 1
			pbeef += 1
		else:
			print("You don't have any cows to kill.")
	if cowMenuVar == 2:
		if pcows > 0:
			print("You have milked your cows.")
			print("Milk +" + str(pcows))
			pmilk += pcows
		else:
			print("You don't have any cows to milk.")

def cropCheck():
	global cropTypeInField
	global ryeTime
	global wheatTime
	global cornTime
	if cropTypeInField == "rye":
		ryeTime -= 1
	if cropTypeInField == "wheat":
		wheatTime -= 1
	if cropTypeInField == "corn":
		cornTime -= 1

def cowBreeding():
	global pcows
	global PMAXCOWS
	if pcows >= 2:
		one = pcows * 2
		two = PMAXCOWS - pcows
		if one >= two:
			one = two - 1
		cowChance = random.randint(one, two)
		if cowChance == one:
			pcows += 1
		if pcows > PMAXCOWS:
			pcows = PMAXCOWS

def harvestCrops():
	global cropTypeInField
	global ryeTime
	global cropsInField
	global ryePrice
	global wheatTime
	global wheatPrice
	global pfood
	global cornTime
	global cornPrice
	global prye
	global pwheat
	global pcorn
	if cropTypeInField != None:
		if cropTypeInField == "rye":
			if ryeTime <= 0:
				ryeTime = 2
				print("Harvested " + str(cropsInField) + " rye.")
				prye = cropsInField
				cropTypeInField = None
				cropsInField = 0
			else:
				print("Your crops aren't ready.")
		if cropTypeInField == "wheat":
			if wheatTime <= 0:
				wheatTime = 3
				print("Harvested " + str(cropsInField) + " wheat.")
				pwheat = cropsInField
				cropTypeInField = None
				cropsInField = 0
			else:
				print("Your crops aren't ready.")
		if cropTypeInField == "corn":
			if cornTime <= 0:
				cornTime = 4
				print("Harvested " + str(cropsInField) + " corn.")
				pcorn = cropsInField
				cropTypeInField = None
				cropsInField = 0
			else:
				print("Your crops aren't ready.")

def cookFood():
	global cookFoodVar
	global pgrain
	global pfood
	global pcorn
	global pbeef
	global pyeast
	print("")
	print("Recipes:")
	print("Grain stew(1).    Pottage(2).")
	print("Cost: 2 grain.    Cost: 3 corn, 1 grain.")
	print("")
	print("Roast Beef(3).    Bread loaf(4).")
	print("Cost: 2 beef.     Cost: 2 flour, 1 yeast.")
	print("")
	pCookFoodKeyListen()
	if cookFoodVar == 1:
		if pgrain >= 2:
			print("Cooked grain stew.")
			print("Grain -2")
			print("Food +4")
			pgrain -= 2
			pfood += 4
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
		else:
			print("You don't have the required items to cook this.")
			cont = raw_input()
			printPeasantMenu()
	if cookFoodVar == 2:
		if pgrain >= 1:
			if pcorn >= 3:
				print("Cooked pottage.")
				print("Corn -3")
				print("Grain -1")
				print("Food +10")
				pgrain -= 1
				pcorn -= 3
				pfood += 12
				if sys.version_info[0] < 3:
					cont = raw_input()
				if sys.version_info[0] >= 3:
					cont = input()
				printPeasantMenu()
			else:
				print("You don't have the required items to cook this.")
				if sys.version_info[0] < 3:
					cont = raw_input()
				if sys.version_info[0] >= 3:
					cont = input()
				printPeasantMenu()
		else:
			print("You don't have the required items to cook this.")
			cont = raw_input()
			printPeasantMenu()
	if cookFoodVar == 3:
		if pbeef >= 2:
			print("Cooked roast beef.")
			print("Beef -2")
			print("Food +12")
			pbeef -= 2
			pfood += 12
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
		else:
			print("You don't have the required items to cook this.")
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
	if cookFoodVar == 4:
		if pyeast >= 1:
			if pflour >= 2:
				print("Cooked a bread loaf.")
				print("Flour -2")
				print("Yeast -1")
				print("Food +8")
				pflour -= 2
				pyeast -= 1
				pfood += 8
				if sys.version_info[0] < 3:
					cont = raw_input()
				if sys.version_info[0] >= 3:
					cont = input()
				printPeasantMenu()
			else:
				print("You don't have the required items to cook this.")
				if sys.version_info[0] < 3:
					cont = raw_input()
				if sys.version_info[0] >= 3:
					cont = input()
				printPeasantMenu()
		else:
			print("You don't have the required items to cook this.")
			cont = raw_input()
			printPeasantMenu()

def mill():
	global prye
	global pwheat
	global pcorn
	global pgrain
	global pcornflour
	global pflour
	global millVar
	global millVar2
	global millVar3
	global ch
	global OS
	print("")
	print("Craft:")
	print("Grain(1).       2 Grain(2).")
	print("Cost: 1 rye.    Cost: 1 wheat.")
	print("")
	print("Cornflour(3).   1 Flour(4).")
	print("Cost: 1 corn.   Cost: 1 grain.")
	print("")
	pMillKeyListen()
	ch = None
	if millVar == 1:
		if prye >= 1:
			print("Crafted 1 grain.")
			print("Rye -1")
			print("Grain +1")
			prye -= 1
			pgrain += 1
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
		else:
			print("You don't have the required materials.")
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
	if millVar == 2:
		if pwheat >= 1:
			print("Crafted 2 grain.")
			print("Wheat -1")
			print("Grain +2")
			pwheat -= 1
			pgrain += 2
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
		else:
			print("You don't have the required materials.")
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
	if millVar == 3:
		if pcorn >= 1:
			print("Crafted 1 cornflour.")
			print("Corn -1")
			print("Cornflour +1")
			pcorn -= 1
			pcornflour += 1
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
		else:
			print("You don't have the required materials.")
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
	if millVar == 4:
		if pgrain >= 1:
			print("Crafted 1 flour.")
			print("Grain -1")
			print("Flour +1")
			pgrain -= 1
			pflour += 1
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()
		else:
			print("You don't have the required materials.")
			if sys.version_info[0] < 3:
				cont = raw_input()
			if sys.version_info[0] >= 3:
				cont = input()
			printPeasantMenu()

cls()
print('Version: ' + __version__)
print('Game created by Aiden Blishen Cuneo.')
print('Continue in 5 seconds.')
time.sleep(5)
cls()
print('')


def printPeasantMenu():
	cls()
	print("Day: " + str(dayCount))
	print("Money = " + str(pmoney) + ", Food = " + str(pfood) + ", Rye = " + str(prye) + ", Wheat = " + str(pwheat) + ", Corn = " + str(pcorn))
	print("Grain = " + str(pgrain) + ", Cornflour = " + str(pcornflour))
	print("Flour = " + str(pflour) + ", Yeast = " + str(pyeast))
	print("       /\           --------------")
	if pfamily == 1:
		pAsciiMenuMain()
		pAsciiMenu1()
	if pfamily == 2:
		pAsciiMenuMain()
		pAsciiMenu2()
	if pfamily == 3:
		pAsciiMenuMain()
		pAsciiMenu3()
	print("----------------")

input = Key()


def main():
	global OS
	global money
	global pmoney
	global dayCount
	global food
	global pfood
	global pfamily
	global metal
	global nobles
	global knights
	global peasants
	global foodMult
	global moneyMult

	if user == "king":

		if money <= 0:
			print("The Monarchy has become broke and lost control of his people.")
			print("You have lost the game.")
			print("You survived " + str(dayCount - 1) + " days.")
			exit()
		if food <= 0:
			print("The Monarchy can no longer provide food for anyone. His people rebelled and the Monarchy lost control of his kingdom.")
			print("You have lost the game.")
			print("You survived " + str(dayCount - 1) + " days.")
			exit()

		print("Day: " + str(dayCount))
		print("Money = " + str(money) + ", Food = " + str(food) + ", Metal = " + str(metal))
		currentMoney = money
		currentFood = food
		currentMetal = metal

		print("---------------------")
		if nobles == 1:
			asciiMenuMain()
			asciiMenuN1()
		if nobles == 2:
			asciiMenuMain()
			asciiMenuN2()
		if nobles == 3:
			asciiMenuMain()
			asciiMenuN3()
		if nobles == 4:
			asciiMenuMain()
			asciiMenuN4()
		print("---------------------")

		mainKeyListen(input.getKey())

		population = nobles + knights + peasants

		var = population
		food = food - var

		food = food + peasants * foodMult
		var3 = population / 2
		money = money + var3 * moneyMult
		metal = metal + peasants / 8

		if money > MAXMONEY:
			money = MAXMONEY
		if food > MAXFOOD:
			food = MAXFOOD
		if metal > MAXMETAL:
			metal = MAXMETAL

		newMoney = money - currentMoney
		newFood = food - currentFood
		newMetal = metal - currentMetal

		print("")
		print("Daily gains and losses: Money " + str(newMoney) + ", Food " + str(newFood) + ", Metal " + str(newMetal))

		dayCount += 1
		input.pause()
		cls()
		print("")

	if user == "noble":
		print("You can not be a noble yet.")
		sys.exit()
	
	if user == "knight":
		print("You can not be a knight yet.")
		sys.exit()

	if user == "peasant":
		if dayCount % 7 == 0:
			pmoney -= pfamily * 4

		if pmoney <= 0:
			print("You have no money and when the knight came to collect taxes, he took everything you had and killed you.")
			print("You have lost the game.")
			print("You survived " + str(dayCount - 1) + " days.")
			exit()
		if pfood <= 0:
			print("You have no food left and you starve to death.")
			print("You have lost the game.")
			print("You survived " + str(dayCount - 1) + " days.")
			exit()

		cowBreeding()

		printPeasantMenu()
		currentMoney = pmoney
		currentFood = pfood

		cropCheck()

		if dayCount % 7 == 0:
			print("Taxes paid.")

		ch = input.getKey()
		input.compare(input.getKey, "pKeyListen")

		pfood = pfood - pfamily

		if pmoney > PMAXMONEY:
			pmoney = PMAXMONEY
		if pfood > PMAXFOOD:
			pfood = PMAXFOOD

		newMoney = pmoney - currentMoney
		newFood = pfood - currentFood

		print('')
		print('Daily gains and losses: Money ' + str(newMoney) + ', Food ' + str(newFood))

		input.pause()

		dayCount += 1
		cls()
		print('')

while True:
	main()

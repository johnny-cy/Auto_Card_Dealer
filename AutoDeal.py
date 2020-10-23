COVERT_TABLE = {
    "SPADE-1": "31", "SPADE-2": "32", "SPADE-3": "33", "SPADE-4":"34", "SPADE-5":"35","SPADE-6":"36","SPADE-7":"37","SPADE-8":"38", "SPADE-9":"39", "SPADE-10":"3A", "SPADE-11":"3B","SPADE-12":"3C","SPADE-13":"3D",\
    "HEART-1": "21", "HEART-2": "22", "HEART-3": "23", "HEART-4":"24", "HEART-5":"25","HEART-6":"26","HEART-7":"27","HEART-8":"28", "HEART-9":"29", "HEART-10":"2A", "HEART-11":"2B","HEART-12":"2C","HEART-13":"2D",\
    "DIAMOND-1": "11", "DIAMOND-2": "12", "DIAMOND-3": "13", "DIAMOND-4":"14", "DIAMOND-5":"15","DIAMOND-6":"16","DIAMOND-7":"17","DIAMOND-8":"18", "DIAMOND-9":"19", "DIAMOND-10":"1A", "DIAMOND-11":"1B","DIAMOND-12":"1C","DIAMOND-13":"1D",\
    "CLUB-1": "01", "CLUB-2": "02", "CLUB-3": "03", "CLUB-4":"04", "CLUB-5":"05","CLUB-6":"06","CLUB-7":"07","CLUB-8":"08", "CLUB-9":"09", "CLUB-10":"0A", "CLUB-11":"0B","CLUB-12":"0C","CLUB-13":"0D",\
    }



"""
命名方式:
	黑桃1~13 spade1~13
	紅心1~13 heart1~13
	方塊1~13 diamond1~13
	梅花1~13 club1~13

"""
import sys
import random
import time

# 解除回歸的次數限制
# RecursionError: maximum recursion depth exceeded while calling a Python object
sys.setrecursionlimit(3000)

class AutoDeal(object):
    cc = 0
    count = 0
    
    
    all_cards = []

    current_cards = []
    # card_nums = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
    card_nums = []
    # card_types = ["SPADE", "HEART", "DIAMOND", "CLUB"]
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.all_cards = ["SPADE-1","SPADE-2","SPADE-3","SPADE-4","SPADE-5","SPADE-6","SPADE-7","SPADE-8","SPADE-9","SPADE-10","SPADE-11","SPADE-12","SPADE-13",\
                "HEART-1","HEART-2","HEART-3","HEART-4","HEART-5","HEART-6","HEART-7","HEART-8","HEART-9","HEART-10","HEART-11","HEART-12","HEART-13",\
                "DIAMOND-1","DIAMOND-2","DIAMOND-3","DIAMOND-4","DIAMOND-5","DIAMOND-6","DIAMOND-7","DIAMOND-8","DIAMOND-9","DIAMOND-10","DIAMOND-11","DIAMOND-12","DIAMOND-13",\
                "CLUB-1","CLUB-2","CLUB-3","CLUB-4","CLUB-5","CLUB-6","CLUB-7","CLUB-8","CLUB-9","CLUB-10","CLUB-11","CLUB-12","CLUB-13"]
    
    def get_three_of_a_kind(self):
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        self.count +=1
        if len(self.all_cards) < 3:
            print(f"all_cards only left {len(self.all_cards)}.")
            return 
        rand_card = self.get_a_random_card()
        """if there are three same number left ?"""
        t=rand_card.split("-")[0]
        n=int(rand_card.split("-")[1])
        if self.card_nums.count(n) >= 3:
            # 若有找到，card_nums先移除三個當作記號, 並且將rand_card從all_card中移除
            # self.all_cards.remove(rand_card) # 別用remove，統一用交差集
            
            # self.all_cards = list(set(self.all_cards) - set(rand_card))
            self.all_cards.remove(rand_card)
            for i in range(3):
                self.card_nums.remove(n)
            # get cards that contains 3 in it
            # 先將all_cards重新拆成只剩下後面的數字，並存在變數_
            # 再找出這變數中所有3的索引，利用索引重新將all_cards[索引]獲得有三的所有牌，將這些牌放到cards
            _ = [ i.split("-")[1] for i in self.all_cards ] 
            cards = []
            for i,v in enumerate(_):
                if int(v) == n:
                    cards.append(self.all_cards[i])
            # 因為是get_three所以只能在三張中選2張
            cards = cards[:2]
            cards.append(rand_card)
            # 然後將這兩張確定能用的牌從all_cards中移除 , 統一利用減交集
            self.all_cards = list(set(self.all_cards) - set(cards))
            # 打印出3張的結果
            dorecurive = False
            self.count = 0
        else:
            dorecurive = True
            # 若超過規定次數內就會跳出
            if self.count >= 50:
                print("too much...")
                return
        if dorecurive:
            # print(f"重抽第{self.count}")
            # 重抽
            return self.get_three_of_a_kind()
        else:
            return cards
    
    def get_one_pair(self):
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        self.count += 1
        if len(self.all_cards) < 2:
            print(f"all_cards only left {len(self.all_cards)}.")
            return
        rand_card = self.get_a_random_card()
        t=rand_card.split("-")[0]
        n=int(rand_card.split("-")[1])
        if self.card_nums.count(n) >= 2:
            self.all_cards.remove(rand_card)
            for i in range(2):
                self.card_nums.remove(n)
            _ = [ i.split("-")[1] for i in self.all_cards ] 
            cards = []
            for i,v in enumerate(_):
                if int(v) == n:
                    cards.append(self.all_cards[i])
            cards = cards[:1]
            cards.append(rand_card)
            self.all_cards.remove(cards[0])
            # print(rand_card,cards[0])
            self.count = 0
            dorecurive = False
        else:
            dorecurive = True
            if self.count > 50:
                print("too much...")
                return

        if dorecurive:
            return self.get_one_pair()
        else:
            return cards

    def high_card(self,n=5,strict=True): # strict True means they must be different numbers of five, otherwise it allows some cards in the same
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        self.count += 1
        if len(self.all_cards) < n:
            print(f"all_cards only left {len(self.all_cards)}.")
            return
        if n > 13:
            # print("n range must be in 1 < 13")
            return "n range must be in 1 < 13"
        cards= []
        for i in range(n):
            cards.append(self.get_a_random_card(remove=True))
        
        # check cards if there are same num in it.
        checkcards = [ i.split("-")[1] for i in cards ]
        if len(set(checkcards)) != len(cards):
            # push cards back and redraw
            self.count += 1
            self.all_cards = self.all_cards + cards
            dorecurive = True
        else:
            self.count = 0
            dorecurive = False
        if dorecurive:
            return self.high_card(n)
        else:
            return cards

    def get_flush_only(self):
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        cards = []
        tmp = self.all_cards.copy()
        tmp_SPADE = [ card for card in tmp if card.split("-")[0] == "SPADE"]
        tmp_HEART = [ card for card in tmp if card.split("-")[0] == "HEART"]
        tmp_DIAMOND = [ card for card in tmp if card.split("-")[0] == "DIAMOND"]
        tmp_CLUB = [ card for card in tmp if card.split("-")[0] == "CLUB"]
        li = []
        if len(tmp_SPADE) >= 5:
            li.append(1)
        if len(tmp_HEART) >= 5:
            li.append(2)
        if len(tmp_DIAMOND) >= 5:
            li.append(3)
        if len(tmp_CLUB) >= 5:
            li.append(4)
        target = random.sample(li, 1)[0]
        if target == 1:
            for i in range(10): # try 10 times
                cards = []
                for j in range(5):
                    r = random.randint(0, len(tmp_SPADE)-1)
                    cards.append(tmp_SPADE[r])
                num_is_continue = [int(i.split("-")[1]) for i in cards ]
                num_is_continue.sort()
                if num_is_continue[0]+1 == num_is_continue[1] and \
                    num_is_continue[0]+2 == num_is_continue[2] and \
                    num_is_continue[0]+3 == num_is_continue[3] and \
                    num_is_continue[0]+4 == num_is_continue[4]:
                    cards = []
                    continue
        if cards:
            self.all_cards = list(set(self.all_cards) - set(cards))
            return cards
        
        if target == 2:
            for i in range(10): # try 10 times
                cards = []
                for j in range(5):
                    r = random.randint(0, len(tmp_HEART)-1)
                    cards.append(tmp_HEART[r])
                num_is_continue = [int(i.split("-")[1]) for i in cards ]
                num_is_continue.sort()
                if num_is_continue[0]+1 == num_is_continue[1] and \
                    num_is_continue[0]+2 == num_is_continue[2] and \
                    num_is_continue[0]+3 == num_is_continue[3] and \
                    num_is_continue[0]+4 == num_is_continue[4]:
                    cards = []
                    continue
        if cards:
            self.all_cards = list(set(self.all_cards) - set(cards))
            return cards
        
        if target == 3:
            for i in range(10): # try 10 times
                cards = []
                for j in range(5):
                    r = random.randint(0, len(tmp_DIAMOND)-1)
                    cards.append(tmp_DIAMOND[r])
                num_is_continue = [int(i.split("-")[1]) for i in cards ]
                num_is_continue.sort()
                if num_is_continue[0]+1 == num_is_continue[1] and \
                    num_is_continue[0]+2 == num_is_continue[2] and \
                    num_is_continue[0]+3 == num_is_continue[3] and \
                    num_is_continue[0]+4 == num_is_continue[4]:
                    cards = []
                    continue
        if cards:
            self.all_cards = list(set(self.all_cards) - set(cards))
            return cards
        
        if target == 4:
            for i in range(10): # try 10 times
                cards = []
                for j in range(5):
                    r = random.randint(0, len(tmp_CLUB)-1)
                    cards.append(tmp_CLUB[r])
                num_is_continue = [int(i.split("-")[1]) for i in cards ]
                num_is_continue.sort()
                if num_is_continue[0]+1 == num_is_continue[1] and \
                    num_is_continue[0]+2 == num_is_continue[2] and \
                    num_is_continue[0]+3 == num_is_continue[3] and \
                    num_is_continue[0]+4 == num_is_continue[4]:
                    cards = []
                    continue
        if cards:
            self.all_cards = list(set(self.all_cards) - set(cards))
            return cards
        
        return "there might not have flush_only...."

    def get_straight(self, flush=False, count=0):
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        self.cc +=1
        self.count = count
        if len(self.all_cards) < 5:
            print(f"all_cards only left {len(self.all_cards)}.")
            return
        cards = []
        rand_card = self.get_a_random_card()
        t = rand_card.split("-")[0]
        n = int(rand_card.split("-")[1])
        if n > 10:
            # 重抽
            return self.get_straight(flush=flush,count=self.count)
            
        a,b,c,d,e = str(n), str(n+1), str(n+2), str(n+3), str(n+4)
        if n == 10:
            e = str(1) # 10+4 = 1
        _ = [ i.split("-")[1] for i in self.all_cards] 
        if not flush:
            if a in _ and b in _ and c in _ and d in _ and e in _:
                # print("start drawing")
                while True:
                    x = self.get_a_random_card()
                    y = x.split("-")[1]
                    if a == y:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                while True:
                    x = self.get_a_random_card()
                    y = x.split("-")[1]
                    if b == y:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                while True:
                    x = self.get_a_random_card()
                    y = x.split("-")[1]
                    if c == y:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                while True:
                    x = self.get_a_random_card()
                    y = x.split("-")[1]
                    if d == y:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                while True:
                    x = self.get_a_random_card()
                    y = x.split("-")[1]
                    if e == y:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                return cards
            else:
                self.count += 1
                if self.count > 50:
                    # 重抽 , 若超過50次則跳出回傳no straight left
                    return "there is no straight left..."
                else:
                    return self.get_straight(flush=flush,count=self.count) 
        elif flush:
            if t+"-"+str(a) in self.all_cards and t+"-"+str(b) in self.all_cards and t+"-"+str(c) in self.all_cards and t+"-"+str(d) in self.all_cards and t+"-"+str(e) in self.all_cards:
                while True:
                    self.cc += 1
                    x = self.get_a_random_card()
                    m = x.split("-")[0]
                    y = x.split("-")[1]
                    if a == y and m == t:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                while True:
                    self.cc += 1
                    x = self.get_a_random_card()
                    m = x.split("-")[0]
                    y = x.split("-")[1]
                    if b == y and m == t:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                    
                while True:
                    self.cc += 1
                    x = self.get_a_random_card()
                    m = x.split("-")[0]
                    y = x.split("-")[1]
                    if c == y and m == t:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                while True:
                    self.cc += 1
                    x = self.get_a_random_card()
                    m = x.split("-")[0]
                    y = x.split("-")[1]
                    if d == y and m == t:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                while True:
                    self.cc += 1
                    x = self.get_a_random_card()
                    m = x.split("-")[0]
                    y = x.split("-")[1]
                    if e == y and m == t:
                        cards.append(x)
                        self.all_cards.remove(x)
                        self.card_nums.remove(int(y))
                        break
                return cards
            else:
                # 重抽 , 若超過50次則跳出回傳too much
                self.count += 1
                if self.count > 50:
                    print("too much")
                    return
                return self.get_straight(flush=flush,count=self.count)
            
        else:
            print(f"there is no straight flush left...")

    def get_a_random_card(self, remove=False):
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        r = random.randint(0, len(self.all_cards)-1)
        if remove:
            one = self.all_cards.pop(r)
            return one
        return self.all_cards[r]

    def get_four_of_a_kind(self): 
        
        """
        四隻
        """
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        # get existing four_of_a_kind numbers 
        cards = []
        four_existing_list = []
        for i in range(1,14): #   check from 1 to 13 see if there is any four same numbers in card_nums, append if found.
            count_result = self.card_nums.count(i)
            if count_result == 4:
                four_existing_list.append(i)
        if four_existing_list: 
            random.shuffle(four_existing_list)
            n = four_existing_list.pop() # pop any number from four_existing_list
            for i in range(4): # remove every n in card_nums , every means four
                self.card_nums.remove(n)
            _iter = map(lambda x: x+"-"+str(n), ["SPADE","HEART","DIAMOND","CLUB"]) # use color of four directly and combin them with the number
            cards = [ card for card in _iter]
            self.all_cards = list(set(self.all_cards) - set(cards))
            # print(len(self.all_cards))
            random.shuffle(cards)
            return cards
        else:
            print("there is no four_of_a_kind left...")

    def get_small_five(self):
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        i = 0
        while i < 100:
            i += 1
            cards = []
            tmp = self.all_cards.copy()
            tmp = [ i for i in tmp if int(i.split("-")[1]) <5 ]
            tmp.sort(key=lambda x: x.split("-")[1])
            for n in range(5):
                r = random.randint(0, round(len(self.all_cards)/5))
                cards.append(tmp[r])
            numbers = [ int(card.split("-")[1]) for card in cards ]
            if sum(numbers) >= 10:
                # 重抽
                # time.sleep(1)
                cards = []
                continue
            else:
                break
        if cards:
            self.all_cards = list(set(self.all_cards) - set(cards))
            return cards
        else:
            return f"got {cards} , either sum >= 10 or any one of cards <5 "
        
    def get_above_10(self, n=5, ten=False):
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        if ten:
            tmp = [ i  for i in self.all_cards if int(i.split("-")[1]) >= 10]
        else:
            tmp = [ i  for i in self.all_cards if int(i.split("-")[1]) > 10]
        if len(tmp) > n:
            cards = []
            for i in range(n):
                r = random.randint(0, len(tmp)-1)
                cards.append(tmp[r])
            check = [ i.split("-")[0] for i in cards]
            if len(set(check)) >= 4:
                return self.get_above_10()
            self.all_cards = list(set(self.all_cards) - set(cards))
            return cards
        else:
            return "there is no five above_10 left.. "
    
    def get_two(self, sum10=False):
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        cards = []
        i = 0
        while i < 500:
            i += 1
            cards = []
            for n in range(2):
                cards.append(self.get_a_random_card())
            check = [ int(card.split("-")[1]) for card in cards ]
            
            if sum(check) == 10 and sum10:
                break
            elif sum(check) != 10 and not sum10:
                break
            else:
                cards = []
        if cards:
            self.all_cards = list(set(self.all_cards) - set(cards))
            return cards
        else:
            return "there is no two sum 10 left...."

    def get_13(self):
        self.card_nums = [ int(i.split("-")[1]) for i in self.all_cards ]
        cards = []
        tmp = []
        while True:
            rand_card = self.get_a_random_card()
            n = rand_card.split("-")[1]
            if n not in tmp:
                tmp.append(n)
                cards.append(rand_card)
                self.all_cards.remove(rand_card)
            if len(cards) == 13:
                break
        return cards
        
        

                    


print("""
1. 同花順牛, 五小牛, 雜, 雜, 雜
2. 五小牛, 炸彈牛, 雜, 雜, 雜
3. 炸彈牛, 葫蘆牛, 雜, 雜, 雜
4. 葫蘆牛, 同花牛, 雜, 雜, 雜
5. 同花牛, 五花牛, 雜, 雜, 雜
6. 五花牛, 順子牛, 雜, 雜, 雜
7. 順子牛, 牛牛, 雜, 雜, 雜
8. 牛牛, 有牛, 雜, 雜, 雜
9. 有牛, 無牛, 雜, 雜, 雜 
10. 四家都是一條龍（隨機花色）
0. 退出
    """)

while True:
    v = input("輸入要第幾副牌型： ")
    ad = AutoDeal() # start a new class for every game ( it initial reset for all_cards)
    if v == "1":
        """
        同花順牛, 五小牛, 雜, 雜, 雜
        """
        print("您選的是-->同花順牛, 牛小五, 雜, 雜, 雜 ")
        
        player1 = ad.get_straight(flush=True)
        player2 = ad.get_small_five()
        player3 = ad.high_card()
        player4 = ad.high_card()
        player5 = ad.high_card()
    elif v == "2":
        print("您選的是-->五小牛, 炸彈牛, 雜, 雜, 雜 ")
        """
        五小牛, 炸彈牛, 雜, 雜, 雜
        """
        player1 = ad.get_small_five()
        player2 = ad.get_four_of_a_kind()
        player2.append(ad.get_a_random_card())
        player3 = ad.high_card()
        player4 = ad.high_card()
        player5 = ad.high_card()
    elif v == "3":
        print("您選的是-->炸彈牛, 葫蘆牛, 雜, 雜, 雜")
        """
        炸彈牛, 葫蘆牛, 雜, 雜, 雜
        """
        player1 = ad.get_four_of_a_kind()
        player1.append(ad.get_a_random_card())
        player2 = ad.get_three_of_a_kind()
        player2 = player2 + ad.get_one_pair()
        player3 = ad.high_card()
        player4 = ad.high_card()
        player5 = ad.high_card()
    elif v == "4":
        print("您選的是-->葫蘆牛, 同花牛, 雜, 雜, 雜")
        """
        葫蘆牛, 同花牛, 雜, 雜, 雜
        """
        player1 = ad.get_three_of_a_kind()
        player1 = player1 + ad.get_one_pair()
        player2 = ad.get_flush_only()
        player3 = ad.high_card()
        player4 = ad.high_card()
        player5 = ad.high_card()
    elif v == "5":
        print("您選的是-->同花牛, 五花牛, 雜, 雜, 雜")
        """
        同花牛, 五花牛, 雜, 雜, 雜
        """
        player1 = ad.get_flush_only()
        player2 = ad.get_above_10()
        player3 = ad.high_card()
        player4 = ad.high_card()
        player5 = ad.high_card()
    elif v == "6":
        print("您選的是-->五花牛, 順子牛, 雜, 雜, 雜")
        """
        五花牛, 順子牛, 雜, 雜, 雜
        """
        player1 = ad.get_above_10()
        player2 = ad.get_straight()
        player3 = ad.high_card()
        player4 = ad.high_card()
        player5 = ad.high_card()
    elif v == "7":
        print("您選的是-->順子牛, 牛牛, 雜, 雜, 雜")
        """
        順子牛, 牛牛, 雜, 雜, 雜
        """
        player1 = ad.get_straight()
        player2 = ad.get_above_10(3, ten=True)
        player2 = player2 + ad.get_two(sum10=True)
        player3 = ad.high_card()
        player4 = ad.high_card()
        player5 = ad.high_card()
    elif v == "8":
        print("您選的是-->牛牛, 有牛, 雜, 雜, 雜")
        """
        牛牛, 有牛, 雜, 雜, 雜
        """
        player1 = ad.get_above_10(3, ten=True)
        player1 = player1 + ad.get_two(sum10=True)
        player2 = ad.get_above_10(3, ten=True)
        player2 = player2 + ad.get_two(sum10=False)
        player3 = ad.high_card()
        player4 = ad.high_card()
        player5 = ad.high_card()
    elif v == "9":
        print("您選的是-->有牛, 無牛, 雜, 雜, 雜 ")
        """
        有牛, 無牛, 雜, 雜, 雜 
        """
        player1 = ad.get_above_10(3, ten=True)
        player1 = player1 + ad.get_two(sum10=False)
        player2 = ad.high_card()
        player3 = ad.high_card()
        player4 = ad.high_card()
        player5 = ad.high_card()
    elif v == "10":
        print("您選的是-->四家都是一條龍（隨機花色）")
        """
        四家都是一條龍（隨機花色）
        """
        player1 = ad.get_13()
        player2 = ad.get_13()
        player3 = ad.get_13()
        player4 = ad.get_13()


    elif v == "0":
        print("bye~")
        break

    
    # print(player1)
    # print(player2)
    # print(player3)
    # print(player4)
    # print(player5)


    # print(player1 + player2 + player3 + player4 + player5)
    if v in ["1","2","3","4","5","6","7","8","9"]:
        final_list = player1 + player2 + player3 + player4 + player5
        final_list = [ COVERT_TABLE[i] for i in final_list]
        print(final_list)
    elif v in ["10"]:
        final_list = player1 + player2 + player3 + player4
        final_list = [ COVERT_TABLE[i] for i in final_list]
        print(final_list)
        # print(player1)
        # print(player2)
        # print(player3)
        # print(player4)


"""
發牌機器:
選定要發的牌，最後轉成一串撲克牌代碼即可。
概念：
每一局就是一副牌就是一個class，初始化後會有所有52張牌(all_cards)，與當前0張已出的牌(current_cards)
每抽走一張牌時，all_cards就remove它，同時current_cards就append它。
"""
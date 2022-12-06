class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

#Omat

class All:
    def __init__(self):
        self._value = True

    def test(self, player):
        return self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Not:
    def __init__(self, ehto):
        self._ehto = ehto

    def test(self, player):
        tulos = self._ehto.test(player)
        if tulos == True:
            return False
        else:
            return True

class Or:
    #def __init__(self, ehto1, ehto2 = None, ehto3 = None):
    #olisi ollut aika rumaa ehtolauseella
    def __init__(self, *args):
        self._ehdot = []
        i = 0
        while i < len(args): 
            self._ehdot.append(args[i])
            i = i + 1
        #self._ehdot.append(ehto1)
        #if ehto2 != None:
            #self._ehdot.append(ehto2)
            #if ehto3 != None:
                #self._ehdot.append(ehto3)

    def test(self, player):
        for ehto in self._ehdot:
            if ehto.test(player) == True:
                return True
        return False

class QueryBuilder:
    def __init__(self, matcher = All()):
        self.matcher_olio = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self.matcher_olio,PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher_olio,HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher_olio,HasFewerThan(value, attr)))

    def oneOf(self, *args):
        or_olio = Or(args[0])
        for arg in args:
            or_olio = Or(or_olio, arg)
        return QueryBuilder(or_olio)

    def build(self):
        return self.matcher_olio
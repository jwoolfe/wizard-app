#!/usr/bin/env python3

## HOMEWORK
# Unit tests:
# test everything your game does
#
#  Questions:
#   This test's string output, but how do you test arithmetic, etc. 
#       ex:  purse , relax_not_in_forest
#


import unittest
import wiz11

class WizTest(unittest.TestCase):
    def test_travel_tower(self):
        wiz = wiz11.Wizard(location="village")
        self.assertEqual(
            wiz11.request(wiz, "tower"),
            "You travel to your tower where there is peace and quiet."
        )

    def test_travel_tower_already_there(self):
        wiz = wiz11.Wizard(location="tower")
        self.assertEqual(
            wiz11.request(wiz, "tower"),
            "You are already in the tower."
        )

    def test_travel_village(self):
        wiz = wiz11.Wizard(location="tower")
        self.assertEqual(
            wiz11.request(wiz, "village"),
            "You travel to your village where you can work, sell goods and shop."
        )

    def test_travel_village_already_there(self):
        wiz = wiz11.Wizard(location="village")
        self.assertEqual(
            wiz11.request(wiz, "village"),
            "You are already in the village."
        )

    def test_travel_brc(self):
        wiz = wiz11.Wizard(location="tower")
        self.assertEqual(
            wiz11.request(wiz, "black rock city"),
            "You travel to the playa )'(."
        )

    def test_travel_brc_already_there(self):
        wiz = wiz11.Wizard(location="black rock city")
        self.assertEqual(
            wiz11.request(wiz, "black rock city"),
            "You are already in the black rock city."
        )

    def test_study_in_tower(self):
        wiz = wiz11.Wizard(location="tower")
        self.assertEqual(
            wiz11.request(wiz, "study"),
            "Your skill level is now 1."
        )

    def test_study_not_tower(self):
       for loc in ("village", "black rock city", "forest"):
            wiz = wiz11.Wizard(location=loc)
            self.assertEqual(
                wiz11.request(wiz, "study"),
                "You cannot study in the " + wiz.location + "."
        )

    def test_study_with_books(self):
        wiz = wiz11.Wizard(location="tower", books=1)
        self.assertEqual(
            wiz11.request(wiz, "study"),
            "Your skill level is now 1."
        )

    def test_study_with_no_books(self):
        wiz = wiz11.Wizard(location="tower", books=0)
        self.assertEqual(
            wiz11.request(wiz, "study"),
            "You have no more new books to read."
        )

    def test_brew_not_tower(self):
       for loc in ("village", "black rock city", "forest"):
            wiz = wiz11.Wizard(location=loc)
            self.assertEqual(
                wiz11.request(wiz, "brew"),
                "You cannot brew potions in the " + wiz.location + "."
        )
    
    def test_brew_no_mushrooms(self):
        wiz = wiz11.Wizard(location="tower", mushrooms=0)
        self.assertEqual(
            wiz11.request(wiz, "brew"),
            "You can't brew potions without mushrooms."
        )

    def test_brew_tower_mushrooms(self):
        wiz = wiz11.Wizard(location="tower", mushrooms=3, potions=1)
        self.assertEqual(
            wiz11.request(wiz, "brew"),
            "You now have 2 potions."
        )
        self.assertEqual(wiz.mushrooms, 2)
        self.assertEqual(wiz.potions, 2)
        self.assertEqual(wiz.stress, -1)

    def test_forage_in_forest(self):
        wiz = wiz11.Wizard(location="forest")
        self.assertEqual(
            wiz11.request(wiz, "forage"),
            "You now have 1 mushrooms."
        )

    def test_forage_not_forest(self):
       for loc in ("village", "black rock city", "tower"):
            wiz = wiz11.Wizard(location=loc)
            self.assertEqual(
                wiz11.request(wiz, "forage"),
                "There are no mushrooms in the " + wiz.location + "."
        )

    def test_gift_in_brc(self):
        wiz = wiz11.Wizard(location="black rock city", potions=6, stress=0)
        self.assertEqual(
            wiz11.request(wiz, "gift"),
            "You now have 5 potions."
        )

    def test_gift_in_brc_with_stress(self):
        wiz = wiz11.Wizard(location="black rock city", potions=6, stress=2)
        self.assertEqual(
            wiz11.request(wiz, "gift"),
            "You now have 5 potions and you have lowered your stress level."
        )

    def test_gift_not_in_brc(self):
        for loc in ("village", "forest", "tower"):
            wiz = wiz11.Wizard(location=loc)
            self.assertEqual(
                wiz11.request(wiz, "gift"),
                "You cannot give gifts in the " + wiz.location + "."
        )

    def test_gift_no_potions(self):
        wiz = wiz11.Wizard(location="black rock city")
        self.assertEqual(
            wiz11.request(wiz, "gift"),
            "You have no potions to gift."
        )

    def test_purse(self):
        wiz = wiz11.Wizard(books=2, gold=2, mushrooms=0, potions=4)
        self.assertEqual(
            wiz11.request(wiz, "purse"),
            '''   You have 2 books\n'''
            '''   You have 2 gold\n'''
            '''   You have 0 mushrooms\n'''
            '''   You have 4 potions'''
        )

    def test_health(self):
        wiz = wiz11.Wizard(stress=5, skill=5)
        self.assertEqual(
            wiz11.request(wiz, "health"),
            '''   You have a stress level of 5.\n'''
            '''   You have a skill level of 5.'''
        )

    def test_relax_in_forest(self):
        wiz = wiz11.Wizard(location="forest", stress=1)
        self.assertEqual(
            wiz11.request(wiz, "relax"),
            "You now have 0 stress level."
        )

    def test_relax_not_in_forest(self):
       for loc in ("village", "black rock city", "tower"):
            wiz = wiz11.Wizard(location=loc)
            self.assertEqual(
                wiz11.request(wiz, "relax"),
                "You can't relax in " + wiz.location + "."
        )

    def test_sell_in_village_no_potions(self):
        wiz = wiz11.Wizard(location="village", gold=3)
        self.assertEqual(
            wiz11.request(wiz, "sell"),
            "You have no brewed potions to sell."
        )

    def test_sell_in_village(self):
        wiz = wiz11.Wizard(location="village", gold=3, potions=3)
        self.assertEqual(
            wiz11.request(wiz, "sell"),
            "You now have 4 gold."
        )

    def test_sell_not_village(self):
       for loc in ("tower", "black rock city", "forest"):
            wiz = wiz11.Wizard(location=loc)
            self.assertEqual(
                wiz11.request(wiz, "sell"),
                "You can't sell goods in the " + wiz.location + "."
        )

    def test_shop_in_village(self):
        wiz = wiz11.Wizard(location="village", gold=1)
        self.assertEqual(
            wiz11.request(wiz, "shop"),
            "You now have 2 books and 0 gold."
        )

    def test_shop_not_village(self):
       for loc in ("tower", "black rock city", "forest"):
            wiz = wiz11.Wizard(location=loc)
            self.assertEqual(
                wiz11.request(wiz, "shop"),
                "You can't shop in the " + wiz.location + "."
        )

    def test_shop_too_stressed(self):
        wiz = wiz11.Wizard(location="village", gold=1, stress=11)
        self.assertEqual(
            wiz11.request(wiz, "shop"),
            "You are too stressed out. Go do relaxing things."
        )

    def test_shop_no_gold(self):
        wiz = wiz11.Wizard(location="village", gold=0)
        self.assertEqual(
            wiz11.request(wiz, "shop"),
            "You have 0 gold. You must work to earn gold."
        )

    def test_work_in_village(self):
        wiz = wiz11.Wizard(location="village", gold=2, skill=3)
        self.assertEqual(
            wiz11.request(wiz, "work"),
            "All in a day's work. You now have 3 gold."
        )

    def test_work_not_village(self):
       for loc in ("tower", "black rock city", "forest"):
            wiz = wiz11.Wizard(location=loc)
            self.assertEqual(
                wiz11.request(wiz, "work"),
                "There is no work in the " + wiz.location + "."
        )

    def test_work_no_skills(self):
        wiz = wiz11.Wizard(location="village", skill=0)
        self.assertEqual(
            wiz11.request(wiz, "work"),
            "You can't work without any skills."
        )

    def test_shop_too_stressed(self):
        wiz = wiz11.Wizard(location="village", stress=11, skill=2)
        self.assertEqual(
            wiz11.request(wiz, "work"),
            "You are too stressed out. Go do relaxing things."
        )



if __name__ =='__main__':
    unittest.main()
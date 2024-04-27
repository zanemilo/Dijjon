# Dijjon weather
# Author: Zane M Deso
# Purpose: This class handles weather effects for the purpose of simple calling of routine weather patterns at varying serverities.

class Weather:
    """This class handles weather effects for the purpose of simple calling of routine weather patterns at varying severities."""
    
    def __init__(self):
        pass

    def rain(self):
        print("It starts to rain, softening the ground and filling the air with the scent of wet earth.")
        # Effects: Minor visibility reduction, slow movement on dirt roads

    def rain_storm(self):
        print("The rain intensifies into a storm, reducing visibility and making travel treacherous.")
        # Effects: Significant visibility reduction, very slow movement, potential flooding

    def lightning(self):
        print("Lightning flashes across the sky, followed by thunder, electrifying the air.")
        # Effects: Chance of fires starting, sudden noise could alert creatures

    def fog(self):
        print("A thick fog rolls in, obscuring sight beyond a few feet.")
        # Effects: Severe visibility reduction, navigation challenges, stealth opportunities

    def blizzard(self):
        print("Snow whirls around in a fierce blizzard, reducing visibility to near zero and making it difficult to move.")
        # Effects: Extreme visibility reduction, movement halved, risk of hypothermia

    def sandstorm(self):
        print("A whipping sandstorm kicks up, stinging skin and obscuring the landscape.")
        # Effects: Moderate visibility reduction, minor damage over time, electronic interference

    def hurricane(self):
        print("A powerful hurricane sweeps through, with howling winds and torrential rains.")
        # Effects: Massive area effect, destruction of weak structures, flooding

    def heatwave(self):
        print("A brutal heatwave settles over the area, sapping strength and slowing the pace.")
        # Effects: Increased water needs, reduced stamina, slower recovery

    def cold_snap(self):
        print("The temperature plummets in a sudden cold snap, freezing water sources and numbing extremities.")
        # Effects: Water sources frozen, increased food needs, risk of frostbite

    def dust_devil(self):
        print("A small but fierce dust devil swirls up, tossing debris and disorienting travelers.")
        # Effects: Temporary visibility obstruction, minor physical damage, disorientation

    def hailstorm(self):
        print("Ice falls from the sky as a hailstorm pummels the area.")
        # Effects: Physical damage, crop damage, hazardous walking conditions

    def sleet(self):
        print("Sleet begins to fall, coating everything in a slippery layer of ice and snow.")
        # Effects: Slipping hazards, minor visibility reduction, cold exposure

    def tornado(self):
        print("A tornado tears through the landscape, uprooting trees and demolishing structures in its path.")
        # Effects: Extreme localized damage, displacement of objects and creatures, loud

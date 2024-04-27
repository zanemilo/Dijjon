# Dijjon weather
# Author: Zane M Deso
# Purpose: This class handles weather effects for the purpose of simple calling of routine weather patterns at varying serverities.

class Weather:
    """This class manages weather effects, providing a simplified mechanism for invoking routine weather patterns at various intensities."""
    
    def __init__(self):
        pass

    def rain(self):
        print("Gentle rain begins to fall, the droplets pattering softly against the ground, releasing the earthy aroma of damp soil.")
        # Effects: Minor visibility reduction, slow movement on dirt roads

    def rain_storm(self):
        print("The skies darken as the rain escalates into a fierce storm, each drop slashing at the landscape, turning paths into muddy torrents.")
        # Effects: Significant visibility reduction, very slow movement, potential flooding

    def lightning(self):
        print("Streaks of lightning tear through the heavy clouds, each flash illuminating the sky followed by the deep rumble of thunder.")
        # Effects: Chance of fires starting, sudden noise could alert creatures

    def fog(self):
        print("A dense fog creeps over the landscape, swallowing the surroundings in a thick, opaque shroud that muffles sound and sight.")
        # Effects: Severe visibility reduction, navigation challenges, stealth opportunities

    def blizzard(self):
        print("The air fills with a swirling chaos of snow, the wind howling as visibility drops to nothing and the cold bites into flesh and bone.")
        # Effects: Extreme visibility reduction, movement halved, risk of hypothermia

    def sandstorm(self):
        print("Gritty winds whip up a sandstorm, the air thick with sand grains that scratch at exposed skin and cloak the sun.")
        # Effects: Moderate visibility reduction, minor damage over time, electronic interference

    def hurricane(self):
        print("With ferocious power, the hurricane roars ashore, its winds screaming as they bend trees and toss debris like toys in the deluge.")
        # Effects: Massive area effect, destruction of weak structures, flooding

    def heatwave(self):
        print("The air turns oppressively hot as a heatwave descends, the sun's glare relentless, draining vigor and wilting plants alike.")
        # Effects: Increased water needs, reduced stamina, slower recovery

    def cold_snap(self):
        print("Temperatures plummet unexpectedly, a cold snap turning moisture to ice, stiffening the landscape in a silent, frosty grip.")
        # Effects: Water sources frozen, increased food needs, risk of frostbite

    def dust_devil(self):
        print("Suddenly, a dust devil spins into existence, a whirling column of dirt and debris that dances chaotically across the terrain.")
        # Effects: Temporary visibility obstruction, minor physical damage, disorientation

    def hailstorm(self):
        print("The sky unleashes a torrent of ice, as hailstones clatter against the ground, rooftops, and anything unfortunate enough to be caught beneath.")
        # Effects: Physical damage, crop damage, hazardous walking conditions

    def sleet(self):
        print("Sleet slashes through the air, mixing rain with ice, each pellet tinkling as it freezes upon contact, layering the world in a treacherous sheen.")
        # Effects: Slipping hazards, minor visibility reduction, cold exposure

    def tornado(self):
        print("A menacing tornado spirals destructively through the area, its roaring funnel claiming everything in its path as it reshapes the landscape.")
        # Effects: Extreme localized damage, displacement of objects and creatures, loud


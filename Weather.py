# Dijjon weather
# Author: Zane M Deso
# Purpose: This class manages weather effects, offering a system to simulate routine weather patterns at varied intensities for dynamic environmental storytelling.

class Weather:
    """This class manages weather effects, offering a system to simulate routine weather patterns at varied intensities for dynamic environmental storytelling."""
    
    def __init__(self):
        pass

    def rain(self, intensity=1):
        descriptions = {
            1: "A soft drizzle begins, casting a gentle veil over the landscape and awakening the sweet scent of petrichor.",
            2: "Steady rain envelops the area, rhythmically drumming on rooftops and saturating the thirsty earth.",
            3: "Torrential rain lashes down in sheets, transforming streets into rivers and sweeping away all but the sturdiest of shelters."
        }
        print(descriptions.get(intensity, "An unprecedented deluge overwhelms the region, blurring lines between sky and land."))
        # Effects based on intensity

    def rain_storm(self, intensity=1):
        descriptions = {
            1: "The rain intensifies, accompanied by bursts of gusty winds that rattle windows and challenge umbrellas.",
            2: "Violent storms dominate the horizon, their winds howling fiercely as they uproot trees and scatter debris.",
            3: "Cataclysmic storms unleash their fury, with relentless rain and devastating winds that herald floods and destruction."
        }
        print(descriptions.get(intensity, "Apocalyptic storms reshape the landscape, sparing nothing from their wrath."))
        # Effects based on intensity

    def lightning(self, frequency=1):
        descriptions = {
            1: "A distant flash of lightning momentarily brightens the horizon, followed by a subdued rumble of thunder.",
            2: "Lightning strikes more frequently, a spectacular display of nature's power, with thunder rolling across the skies.",
            3: "Continuous, violent lightning forks across the sky, a dazzling yet terrifying orchestra of light and sound."
        }
        print(descriptions.get(frequency, "An unrelenting storm of lightning terrorizes the area, sparking fires and chaos."))
        # Effects based on frequency

    def fog(self, density=1):
        descriptions = {
            1: "A whispy fog settles, slightly blurring distant forms and softening the landscape’s edges.",
            2: "Dense fog swathes the environment, turning familiar paths into eerie, muffled labyrinths.",
            3: "An almost tangible fog envelops everything, isolating individuals in a silent, impenetrable white void."
        }
        print(descriptions.get(density, "A supernatural fog cloaks all in obscurity, leaving the world ghostly quiet and hidden."))
        # Effects based on density

    def blizzard(self, intensity=1):
        descriptions = {
            1: "Light snowfall dances in the chilly air, dusting the landscape in a fine white powder.",
            2: "A fierce blizzard sweeps through, its icy winds howling as snow blankets everything in relentless cold.",
            3: "An all-out arctic fury descends, obliterating visibility and freezing everything in its unstoppable path."
        }
        print(descriptions.get(intensity, "A monstrous blizzard claims dominion over the land, a whiteout of epic proportions."))
        # Effects based on intensity

    def sandstorm(self, intensity=1):
        descriptions = {
            1: "The air fills with fine grains of sand, a dusty haze that clouds the horizon.",
            2: "Gritty winds escalate, carrying a torrent of sand that scrapes and scours exposed surfaces.",
            3: "A roaring sandstorm engulfs the landscape, a blinding, suffocating wall of sand that transforms day into night."
        }
        print(descriptions.get(intensity, "The desert's wrath unleashes a catastrophic sandstorm, reshaping the terrain."))
        # Effects based on intensity

    def hurricane(self, intensity=1):
        descriptions = {
            1: "Tropical winds begin to howl, the ocean’s spray hinting at the growing fury of the coming storm.",
            2: "The hurricane's might builds, its roaring winds and pounding rains battering against all in its path.",
            3: "A relentless hurricane devastates miles of coastline, its monstrous winds and floods leaving nothing but ruin."
        }
        print(descriptions.get(intensity, "An epic hurricane of historical scale descends, its power unmatched and utterly destructive."))
        # Effects based on intensity

    def heatwave(self, intensity=1):
        descriptions = {
            1: "The air warms to an uncomfortable degree, the sun's rays more insistent as shadows shrink away.",
            2: "Heat clamps down like an oven, the air shimmering and stifling as it saps strength and scorches the earth.",
            3: "An oppressive inferno envelops the region, with temperatures soaring to deadly peaks that threaten all life."
        }
        print(descriptions.get(intensity, "The land succumbs to a brutal scorcher, its effects catastrophic and far-reaching."))
        # Effects based on intensity

    def cold_snap(self, severity=1):
        descriptions = {
            1: "A brisk chill sweeps through, a sudden reminder of winter's reach as it nips at exposed skin.",
            2: "A biting cold snap freezes the area, ice crystallizing swiftly as breath turns to mist in the frigid air.",
            3: "A brutal cold front descends, the temperature plummeting to lethal lows, freezing everything in an icy grip."
        }
        print(descriptions.get(severity, "An arctic blast renders the world a frozen wasteland, perilous and unyielding."))
        # Effects based on severity

    def dust_devil(self, intensity=1):
        descriptions = {
            1: "A playful whirl of dust spins across the dry ground, a brief dance of debris in the afternoon sun.",
            2: "A robust dust devil tears through, swirling dust and small debris into a menacing column.",
            3: "A towering dust devil rampages, a formidable force of nature moving earth and sand in a powerful display."
        }
        print(descriptions.get(intensity, "A colossal dust devil wreaks havoc, formidable and uncontrollable."))
        # Effects based on intensity

    def hailstorm(self, intensity=1):
        descriptions = {
            1: "Small hailstones clatter down, bouncing on hard surfaces with a persistent tap-tap.",
            2: "A barrage of hail pounds the area, larger stones drumming loudly on roofs and threatening damage.",
            3: "A vicious hailstorm assaults the landscape, large and deadly hailstones causing havoc and destruction."
        }
        print(descriptions.get(intensity, "A catastrophic hailstorm unleashes nature’s icy fury, relentless and destructive."))
        # Effects based on intensity

    def sleet(self, intensity=1):
        descriptions = {
            1: "A gentle sleet begins to fall, dusting the world in a thin, icy veneer that glistens underfoot.",
            2: "Thick sleet blankets the area, coating everything with a slick, icy layer that makes travel treacherous.",
            3: "Heavy sleet storms down, the ice accumulating rapidly, paralyzing transport and encasing the landscape in a frozen shell."
        }
        print(descriptions.get(intensity, "An extreme sleet storm encases the region in ice, severe and immobilizing."))
        # Effects based on intensity

    def tornado(self, intensity=1):
        descriptions = {
            1: "A brief tornado touches down, its path narrow but marked by upturned earth and scattered debris.",
            2: "A powerful tornado carves through the area, its funnel cloud a terrifying swirl of destructive force.",
            3: "An immense tornado devastates everything in its swath, a relentless beast of wind that obliterates landscapes and shatters lives."
        }
        print(descriptions.get(intensity, "A legendary tornado of apocalyptic strength redefines the very fabric of the affected regions."))
        # Effects based on intensity



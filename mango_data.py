import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mangocare.settings")
django.setup()

from pest_disease.enums.pest_enums import Category, Severity, Type, TypeDetail, AffectedPart

# Define all pest and disease data
pest_disease_data = [
    {
        "item_id": 1,
        "name": "Mango Seed Weevil",
        "category": Category.PEST,
        "severity": Severity.HIGH,
        "type": Type.INSECT,
        "type_detail": f"{TypeDetail.BEETLE.value}, {TypeDetail.COLEOPTERA.value}",
        "affected_part": f"{AffectedPart.SEED.value}, {AffectedPart.FRUIT_PULP.value}",
        "season": "Dry season",
        "sci_name": "Sternochetus mangiferae",
        "egg": "Creamy white, 2mm long",
        "larvae": "Legless, brown head, white body",
        "adult": "Gray-brown with a long snout, 10mm long",
        "long_desc": "The female weevil lays eggs on young fruits (30mm), covering them with wax from her oviposition cuts. Larvae tunnel into seeds, consuming the kernel over 53 days, leaving the fruit externally intact but internally destroyed. This quarantine pest causes significant economic losses by rendering infested fruits unfit for export",
        "life_cycle": "T1 generation/year. Eggs laid on young fruits (30mm). Larvae burrow into seeds, develop in 53 days",
        "symptoms": "Sap exudate on young fruit, seed tunneling",
        "damage": "Sap exudate on young fruit, seed tunneling",
        "monitoring": "Inspect fallen fruits; cut fruits to examine seeds",
        "intervention": "5% infested young fruits",
        "control_measures": "Pre- and post-fruit set insecticides, orchard sanitation",
        "ref": "Mango field guide part 1 page 24-25",
    },
    {
        "item_id": 2,
        "name": "Fruitspotting Bug",
        "category": Category.PEST,
        "severity": Severity.MODERATE_HIGH,
        "type": Type.INSECT,
        "type_detail": f"{TypeDetail.TRUE_BUG.value}, {TypeDetail.HEMIPTERA.value}",
        "affected_part": f"{AffectedPart.YOUNG_SHOOT.value}, {AffectedPart.IMMATURE_FRUIT.value}",
        "season": "Late wet season to early dry season",
        "sci_name": "Amblypelta lutescens lutescens, A. nitida",
        "egg": "Pale green, 2mm long",
        "larvae": "No description",
        "adult": "Light green with brown wings, 15mm long",
        "long_desc": "Adults suck sap from shoots and fruits, causing necrotic black lesions that lead to fruit cracking and premature drop. They hide under leaves during the day and are active at night, making detection difficult. Scarring on mature fruits reduces market value.",
        "life_cycle": "4-5 generations/year; egg-to-adult development in 35-42 days",
        "symptoms": "Black lesions on shoots, cracks on young fruits",
        "damage": "Fruit drop, yield loss",
        "monitoring": "Weekly checks on new shoots",
        "intervention": "10% damaged shoots",
        "control_measures": "Insecticide sprays during fruit set",
        "ref": "Mango field guide part 1 page 32-33",
    },
    {
        "item_id": 3,
        "name": "Fruit Flies",
        "category": Category.PEST,
        "severity": Severity.VERY_HIGH,
        "type": Type.INSECT,
        "type_detail": f"{TypeDetail.FLY.value}, {TypeDetail.DIPTERA.value}",
        "affected_part": f"{AffectedPart.RIPE_FRUIT.value}",
        "season": "Wet season",
        "sci_name": "Bactrocera tryoni, B. jarvisi",
        "egg": "Creamy white, 1mm long",
        "larvae": "White maggots, 8mm long",
        "adult": "Yellow-brown with patterned wings, 9-10mm long",
        "long_desc": "Females lay eggs under the skin of ripe fruits, where larvae tunnel through the flesh, causing internal rot. Infested fruits develop small exit holes with oozing sap and are often discarded post-harvest. Adults are attracted to ripening fruits and rapidly spread across orchards",
        "life_cycle": "Larvae develop in 6-8 days; pupation in soil (10-12 days)",
        "symptoms": "Puncture marks on ripe fruit, internal rot",
        "damage": "Fruit decay, export rejection",
        "monitoring": "Pheromone traps, ripe fruit inspection",
        "intervention": "1 fly/week in traps",
        "control_measures": "Bait sprays, orchard hygiene",
        "ref": "Mango field guide part 1 page 56-57",
    },
    {
        "item_id": 4,
        "name": "Mango Leafhopper",
        "category": Category.PEST,
        "severity": Severity.MODERATE,
        "type": Type.INSECT,
        "type_detail": f"{TypeDetail.LEAFHOPPER.value}, {TypeDetail.HEMIPTERA.value}",
        "affected_part": f"{AffectedPart.YOUNG_LEAF.value}, {AffectedPart.FLOWER.value}",
        "season": "Flowering to fruit",
        "sci_name": "Idioscopus nitidulus, I. clypealis",
        "egg": "Cigar-shaped, creamy yellow",
        "larvae": "No description",
        "adult": "Golden-brown, 4-5mm long",
        "long_desc": "Nymphs and adults feed on young shoots and flowers, excreting honeydew that promotes sooty mold growth. The black mold coats leaves, reducing photosynthesis and causing flower abortion. Their rapid reproduction during dry seasons is signaled by distinctive 'clicking' sounds",
        "life_cycle": "Egg-to-adult in 12-20 days",
        "symptoms": "Curled leaves, honeydew, sooty mold",
        "damage": "Reduced fruit set, tree decline",
        "monitoring": "Listen for 'clicking' sounds from large populations",
        "intervention": "20 hoppers/inflorescence",
        "control_measures": "Imidacloprid sprays, encourage natural enemies",
        "ref": "Mango field guide part 1 page 38-39",
    },
    {
        "item_id": 5,
        "name": "Mango Fruit Borer",
        "category": Category.PEST,
        "severity": Severity.HIGH,
        "type": Type.INSECT,
        "type_detail": f"{TypeDetail.MOTH.value}, {TypeDetail.LEPIDOPTERA.value}",
        "affected_part": f"{AffectedPart.IMMATURE.value}, {AffectedPart.RIPE_FRUIT.value}",
        "season": "Wet season",
        "sci_name": "Citripestis eutraphera",
        "egg": "White, turning red after 1 day",
        "larvae": "Pink-brown with black head",
        "adult": "Brown wings, 24mm wingspan",
        "long_desc": "Larvae bore into fruit near the stem, creating tunnels filled with moist frass, leading to internal rot and fruit drop. Infested fruits are unmarketable due to decay. Nocturnal moths target susceptible mango varieties, laying eggs on developing fruits",
        "life_cycle": "Egg-to-adult in 30 days",
        "symptoms": "Boreholes in fruit, frass around stems",
        "damage": "Fruit rot, commercial loss",
        "monitoring": "Check young and fallen fruits",
        "intervention": "5% infested fruits",
        "control_measures": "Insecticide sprays during early fruit development",
        "ref": "Mango field guide part 1 page 44-45",
    },
    {
        "item_id": 6,
        "name": "Redbanded Thrips",
        "category": Category.PEST,
        "severity": Severity.MODERATE,
        "type": Type.INSECT,
        "type_detail": f"{TypeDetail.THRIPS.value}, {TypeDetail.THYSANOPTERA.value}",
        "affected_part": f"{AffectedPart.UNDERSIDES_OF_LEAF.value}, {AffectedPart.FRUIT_SURFACE.value}",
        "season": "Dry season",
        "sci_name": "Selenothrips rubrocinctus",
        "egg": "Kidney-shaped, black when dry",
        "larvae": "No description",
        "adult": "Dark brown with red abdominal bands",
        "long_desc": "Thrips scrape leaf surfaces to feed on sap, turning leaves silvery and curling their edges. On fruits, feeding causes brown scars that degrade quality. They thrive in hot, dry conditions and hide on the undersides of leaves",
        "life_cycle": "Egg-to-adult in 14-21 days",
        "symptoms": "Silvery leaves, brown scars on fruit",
        "damage": "Reduced photosynthesis, cosmetic fruit damage",
        "monitoring": "Hand lens inspection of leaf undersides",
        "intervention": "10 thrips/leaf",
        "control_measures": "Target larval stages with insecticides",
        "ref": "Mango field guide part 1 page 82-83",
    },
    {
        "item_id": 7,
        "name": "Tea Mosquito Bug",
        "category": Category.PEST,
        "severity": Severity.HIGH,
        "type": Type.INSECT,
        "type_detail": f"{TypeDetail.MIRID_BUG.value}, {TypeDetail.HEMIPTERA.value}",
        "affected_part": f"{AffectedPart.YOUNG_SHOOT.value}, {AffectedPart.FLOWER.value}, {AffectedPart.FRUIT.value}",
        "season": "Late wet season to harvest",
        "sci_name": "Helopeltis pernicialis",
        "egg": "White, embedded in plant tissue",
        "larvae": "No description",
        "adult": "Black with orange thorax, 6-7mm long",
        "long_desc": "Bugs inject toxins into shoots, flowers, and fruits, causing black necrotic spots and deformed growth. Infested young fruits often abort or drop, while shoots wilt and die. They prefer dense foliage and are challenging to detect due to their small size",
        "life_cycle": "Egg-to-adult in 15-30 days",
        "symptoms": "Black necrotic spots on shoots and fruits",
        "damage": "Flower drop, deformed fruits",
        "monitoring": "Inspect new shoots and fruits",
        "intervention": "2 bugs/branch",
        "control_measures": "Prune dense foliage, insecticide sprays",
        "ref": "Mango field guide part 1 page 36-37",
    },
    {
        "item_id": 8,
        "name": "Mango Malformation Disease",
        "category": Category.DISEASE,
        "severity": Severity.VERY_HIGH,
        "type": Type.FUNGAL,
        "season": "Dry season",
        "sci_name": "Fusarium mangiferae",
        "affected_part": f"{AffectedPart.SHOOT_TIP.value}, {AffectedPart.FLOWER.value}",
        "short_desc": "Enters through wounds; spreads via mites",
        "long_desc": "Fusarium mangiferae disrupts cell division, causing twisted shoots and dense, sterile flower clusters. The fungus spreads via pruning tools, wind, or mites. Severe infections can completely halt fruit production in affected trees",
        "life_cycle": "Soil-borne spores; thrives at 20-25°C",
        "symptoms": "Twisted shoots, malformed flowers",
        "damage": "Severe yield loss",
        "monitoring": "Inspect new shoots in early dry season",
        "intervention": "1 infected branch/tree",
        "control_measures": "Prune infected shoots, apply Carbendazim",
        "ref": "Mango field guide part 1 page 142",
    },
    {
        "item_id": 9,
        "name": "Algal Leaf Spot",
        "category": Category.DISEASE,
        "severity": Severity.MODERATE,
        "type": Type.ALGAL,
        "season": "Wet season",
        "sci_name": "Cephaleuros virescens",
        "affected_part": f"{AffectedPart.MATURE_LEAF.value}, {AffectedPart.BARK.value}",
        "short_desc": "Algae form orange-gray spots on leaves",
        "long_desc": "Cephaleuros virescens forms raised orange-gray spots on mature leaves, reducing photosynthetic efficiency. Spores spread via rain and wind, thriving in prolonged wet conditions. While non-lethal, the disease weakens trees and lowers yields",
        "life_cycle": "Spreads via rain/wind; thrives in high humidity",
        "symptoms": "Gray-orange spots on leaves/bark",
        "damage": "Weakens trees",
        "monitoring": "Check mature leaves during wet seasons",
        "intervention": "20% infected leaves",
        "control_measures": "Copper sprays, pruning",
        "ref": "Mango field guide part 1 page 132",
    },
    {
        "item_id": 10,
        "name": "Stem End Rot",
        "category": Category.DISEASE,
        "severity": Severity.HIGH,
        "type": Type.FUNGAL,
        "season": "Post-harvest",
        "sci_name": "Lasiodiplodia theobromae",
        "affected_part": f"{AffectedPart.FRUIT_STEM.value}, {AffectedPart.PULP.value}",
        "short_desc": "Enters through stem wounds or natural openings",
        "long_desc": "Lasiodiplodia theobromae enters fruits through stem wounds or harvest injuries, causing black rot that spreads inward from the stem. Infected fruits emit a fermented odor and become unmarketable. The fungus persists in soil and plant debris, reinfecting during rains",
        "life_cycle": "Soil-borne; active at 28-32°C",
        "symptoms": "Black rot from stem end inward",
        "damage": "Post-harvest losses",
        "monitoring": "Inspect ripe fruits pre-harvest",
        "intervention": "5% infected ripe fruits",
        "control_measures": "Hot water treatment (55°C), cold storage",
        "ref": "Mango field guide part 1 page 154",
        "image_url": "/static/images/ser.jpeg"
    },
    {
        "item_id": 11,
        "name": "Bacterial Black Spot",
        "category": Category.DISEASE,
        "severity": Severity.HIGH,
        "type": Type.BACTERIAL,
        "season": "Wet season",
        "sci_name": "Xanthomonas campestris",
        "affected_part": f"{AffectedPart.LEAF.value}, {AffectedPart.FRUIT.value}",
        "short_desc": "Spreads via rain, wind, and pruning tools",
        "long_desc": "Xanthomonas campestris invades through stomata or wind/rain-induced wounds, creating black leaf spots with yellow halos and fruit cracks. Rainy seasons accelerate spread, particularly in dense orchards. Scarred fruits lose commercial value due to cosmetic damage",
        "life_cycle": "Enters through stomata/wounds; thrives at 25-30°C",
        "symptoms": "Black spots with yellow halos on leaves; fruit cracks",
        "damage": "Leaf drop, unmarketable fruit",
        "monitoring": "Check young leaves after heavy rain",
        "intervention": "10% infected leaves",
        "control_measures": "Copper-based bactericides, avoid overhead irrigation",
        "ref": "Mango field guide part 1 page 160",
    },
    {
        "item_id": 12,
        "name": "Pink Disease",
        "category": Category.DISEASE,
        "severity": Severity.MODERATE,
        "type": Type.FUNGAL,
        "season": "Wet season",
        "sci_name": "Erythricium salmonicolor",
        "affected_part": f"{AffectedPart.BRANCH.value}, {AffectedPart.TREE_TRUNK.value}",
        "short_desc": "Pink fungal growth on bark",
        "long_desc": "Erythricium salmonicolor forms pink fungal growth on bark, eventually cracking stems and causing sap oozing. Infected branches die back, reducing canopy density and productivity. The disease thrives in humid, shaded orchards and spreads via water or insects",
        "life_cycle": "Spreads via water/insects; thrives at >80% humidity",
        "symptoms": "Pink powdery coating on branches; oozing sap",
        "damage": "Branch dieback",
        "monitoring": "Check branches for pink growth",
        "intervention": "1 infected branch/tree",
        "control_measures": "Lime wash tree bases, apply Hexaconazole",
        "ref": "Mango field guide part 1 page 146",
    },
    {
        "item_id": 13,
        "name": "Anthracnose",
        "category": Category.DISEASE,
        "severity": Severity.VERY_HIGH,
        "type": Type.FUNGAL,
        "season": "Wet season",
        "sci_name": "Colletotrichum gloeosporioides",
        "affected_part": f"{AffectedPart.LEAF.value}, {AffectedPart.FLOWER.value}, {AffectedPart.FRUIT.value}",
        "short_desc": "Fungus survives on infected leaves/branches; spreads via rain and wind",
        "long_desc": "The fungus Colletotrichum gloeosporioides spreads via rain-splashed spores, infecting flowers and fruits through stomata or wounds. Post-harvest, infected fruits develop soft rot under humid conditions. Leaf lesions with dark margins weaken trees by reducing photosynthesis",
        "life_cycle": "Spores germinate at >90% humidity, 25-30°C. Thrives in wet seasons",
        "symptoms": "Black lesions on leaves/flowers; post-harvest fruit rot",
        "damage": "Yield reduction, fruit spoilage",
        "monitoring": "Check leaves/flowers post-rain; use spore traps",
        "intervention": "5% infected leaves/flowers",
        "control_measures": "Copper-based fungicides, orchard sanitation",
        "ref": "Mango field guide part 1 page 134-138",
    },
    {
        "item_id": 14,
        "name": "Powdery Mildew",
        "category": Category.DISEASE,
        "severity": Severity.HIGH,
        "type": Type.FUNGAL,
        "season": "Dry season",
        "sci_name": "Oidium mangiferae",
        "affected_part": f"{AffectedPart.YOUNG_LEAF.value}, {AffectedPart.FLOWER.value}",
        "short_desc": "White powdery growth on leaf surfaces",
        "long_desc": "Oidium mangiferae forms white fungal mats on leaves and flowers, blocking sunlight and causing tissue desiccation. Nighttime humidity and daytime dryness trigger outbreaks, leading to massive flower and fruitlet drop. Thin-leaved mango varieties are most vulnerable",
        "life_cycle": "Spreads in dry, low humidity (50-70%). Active at night",
        "symptoms": "White powder on leaves/flowers; premature fruit drop",
        "damage": "Reduced fruit set",
        "monitoring": "Weekly inspection of new growth",
        "intervention": "First sign of white powder",
        "control_measures": "Sulfur sprays, resistant varieties",
        "ref": "Mango field guide part 1 page 140-142",
    },
]

# Create all objects
for item in pest_disease_data:
    print(f"Created {item['category']}: {item['name']}")

print("\nSample data creation completed!")

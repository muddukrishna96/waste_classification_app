BIN_MAPPING = {
    # Blue bin (paper/cardboard)
    "Corrugated carton": "Blue",
    "Egg carton": "Blue",
    "Magazine paper": "Blue",
    "Meal carton": "Blue",
    "Normal paper": "Blue",
    "Other carton": "Blue",
    "Paper bag": "Blue",
    "Paper cup": "Blue",
    "Paper straw": "Blue",
    "Toilet tube": "Blue",
    "Wrapping paper": "Blue",

    # Yellow bin (plastics, metals, composites)
    "Aerosol": "Yellow",
    "Aluminium blister pack": "Yellow",
    "Aluminium foil": "Yellow",
    "Carded blister pack": "Yellow",
    "Clear plastic bottle": "Yellow",
    "Crisp packet": "Yellow",
    "Disposable food container": "Yellow",
    "Disposable plastic cup": "Yellow",
    "Drink can": "Yellow",
    "Drink carton": "Yellow",
    "Foam cup": "Yellow",
    "Foam food container": "Yellow",
    "Food Can": "Yellow",
    "Metal bottle cap": "Yellow",
    "Metal lid": "Yellow",
    "Other plastic": "Yellow",
    "Other plastic bottle": "Yellow",
    "Other plastic container": "Yellow",
    "Other plastic cup": "Yellow",
    "Other plastic wrapper": "Yellow",
    "Plastic bottle cap": "Yellow",
    "Plastic film": "Yellow",
    "Plastic glooves": "Yellow",
    "Plastic lid": "Yellow",
    "Plastic straw": "Yellow",
    "Plastic utensils": "Yellow",
    "Polypropylene bag": "Yellow",
    "Pop tab": "Yellow",
    "Rope & strings": "Yellow",
    "Scrap metal": "Yellow",
    "Single-use carrier bag": "Yellow",
    "Six pack rings": "Yellow",
    "Spread tub": "Yellow",
    "Squeezable tube": "Yellow",
    "Styrofoam piece": "Yellow",
    "Tupperware": "Yellow",

    # Bio bin
    "Food waste": "Bio",
    "Tissues": "Bio",

    # Black bin
    "Battery": "Black",
    "Broken glass": "Black",  # contaminated shards
    "Cigarette": "Black",
    "Garbage bag": "Black",
    "Shoe": "Black",
    "Unlabeled litter": "Black",
    "Pizza box": "Black",  # greasy → Black

    # Glass bin
    "Glass bottle": "Glass",
    "Glass cup": "Glass",
    "Glass jar": "Glass",
}


def get_bin_info(item_class: str):
    bin_color = BIN_MAPPING.get(item_class, "Unknown")
    explanations = {
        "Blue": "🟦 Blue bin (Paper/Cardboard recycling)",
        "Yellow": "🟨 Yellow bin (Plastics, metals, composites recycling)",
        "Bio": "🟩 Bio bin (Organic waste)",
        "Black": "⬛ Black bin (Residual waste / Restmüll)",
        "Glass": "🟫 Glass bin (Glass bottles, jars, cups)"
    }
    return explanations.get(bin_color, "Not classified")
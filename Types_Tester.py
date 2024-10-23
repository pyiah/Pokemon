movetype = "Fire" # The value of type or type itself would be replaced
victims = "Ice"  # The Value of opponent or opponent itself will be replaced

# Lists every single possible reaction of moves and their damage multipliers
all_type_interactions = {"FireFire" : .5, "FireWater" : .5, "FireElectric": 1,"FireGrass": 2, "FireIce" : 2, 
"WaterFire" : 2, "WaterWater" : .5,"WaterElectric" : 1, "WaterGrass" : .5, "WaterIce" : 1, 
"ElectricFire" : 1, "ElectricWater" : 2, "ElectricElectric" : .5, "ElectricGrass" : .5, "ElectricIce" : 1,
"GrassFire" : .5, "GrassWater" : 2, "GrassElectric" : 1, "GrassGrass" : .5, "GrassIce" : 1,
"IceFire" : .5, "IceWater" : .5, "IceElectric" : 1, "IceGrass" : 2, "IceIce" : .5}

def damage_value(move_type, victims_type):
    # Returns damage multiplier
    return all_type_interactions[move_type + victims_type]

print(damage_value(movetype, victims))

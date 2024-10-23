movetype = "Fire" #The value of type or type itself would be replaced
opponent = "Ice"
all_type_interactions = {"FireFire" : .5, "FireWater" : .5, "FireElectric": 1,"FireGrass": 2, "FireIce" : 2, 
"WaterFire" : 2, "WaterWater" : .5,"WaterElectric" : 1, "WaterGrass" : .5, "WaterIce" : 1, 
"ElectricFire" : 1, "ElectricWater" : 2, "ElectricElectric" : .5, "ElectricGrass" : .5, "ElectricIce" : 1,
"GrassFire" : .5, "GrassWater" : 2, "GrassElectric" : 1, "GrassGrass" : .5, "GrassIce" : 1,
"IceFire" : .5, "IceWater" : .5, "IceElectric" : 1, "IceGrass" : 2, "IceIce" : .5} 

def damage_value(move_type, opponent_type):
    return all_type_interactions[move_type + opponent_type]

print(damage_value(movetype, opponent))
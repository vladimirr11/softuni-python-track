from project_func.medicine.salve import Salve
from project_func.medicine.painkiller import Painkiller
from project_func.supply.water_supply import WaterSupply
from project_func.supply.food_supply import FoodSupply
from project_func.medicine.medicine import Medicine
from project_func.supply.supply import Supply
from project_func.survivor import Survivor


class Bunker:
    def __init__(self) -> None:
        self.survivors = []
        self.supplies = []
        self.medicine = []
    
    @property
    def food(self):
        food_supply = [food for food in self.supplies if food.__class__.__name__ == 'FoodSupply']
        if food_supply:
            return food_supply
        
        raise IndexError('There are no food supplies left!')

    @property
    def water(self):
        water_supply = [water for water in self.supplies if water.__class__.__name__ == 'WaterSupply']
        if water_supply:
            return water_supply
        
        raise IndexError('There are no water supplies left!')

    @property
    def painkillers(self):
        painkiller_meds = [pk for pk in self.medicine if pk.__class__.__name__ == 'Painkiller']
        if painkiller_meds:
            return painkiller_meds
        
        raise IndexError('There are no painkillers left!')

    @property
    def salves(self):
        salves_meds = [s for s in self.medicine if s.__class__.__name__ == 'Salve']
        if salves_meds:
            return salves_meds
        
        raise IndexError('There are no salves left!')

    def add_survivor(self, survivor: Survivor):
        for s in self.survivors:
            if s.name == survivor.name:
                raise ValueError(f'Survivor with name {survivor.name} already exists.')
        
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        meds = [med for med in self.medicine if med.__class__.__name__ == medicine_type]
        if meds:
            last_med = meds[-1]
            self.medicine.remove(last_med)
            if survivor.needs_healing:
                last_med.apply(survivor)
                return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor: Survivor, sustenance_type: str):
        supplies = [s for s in self.supplies if s.__class__.__name__ == sustenance_type]
        if supplies:
            last_supply = supplies[-1]
            self.supplies.remove(last_supply)
            if survivor.needs_sustenance:
                last_supply.apply(survivor)
                return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for surv in self.survivors:
            surv.needs -= (surv.age * 2)
            self.sustain(surv, 'WaterSupply')
            self.sustain(surv, 'FoodSupply')

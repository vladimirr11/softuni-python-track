from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []
    
    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name=name, capacity=capacity, memory=memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name=name, capacity=capacity, memory=memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hw in System._hardware:
            if hw.name == hardware_name:
                express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hw.install(express_software)
                    System._software.append(express_software)
                except Exception as ex:
                    return str(ex)
        
        return 'Hardware does not exist'

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hw in System._hardware:
            if hw.name == hardware_name:
                express_software = LightSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hw.install(express_software)
                    System._software.append(express_software)
                except Exception as ex:
                    return str(ex)
        
        return 'Hardware does not exist'

    @staticmethod
    def release_software_component(hardware_name, software_name):
        for hw in System._hardware:
            if hw.name == hardware_name:
                for software in hw.software_components:
                    if software.name == software_name:
                        hw.uninstall(software)
        else:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        counter_hardware, counter_software = 0, 0
        total_used_memory, total_memory = 0, 0
        total_used_capacity, total_capacity = 0, 0

        for hw in System._hardware:
            counter_hardware += 1
            total_memory += hw.memory
            total_capacity += hw.capacity
            for software in hw.software_components:
                counter_software += 1
                total_used_memory += software.memory_consumption
                total_used_capacity += software.capacity_consumption

        message = f'System Analysis\n'
        message += f'Hardware Components: {counter_hardware}\n'
        message += f'Software Components: {counter_software}\n' 
        message += f'Total Operational Memory: {total_used_memory} / {total_memory}\n'
        message += f'Total Capacity Taken: {total_used_capacity} / {total_capacity}'

        return message

    @staticmethod
    def system_split():
        message = f''

        for hw in System._hardware:
            message += f'Hardware Component - {hw.name}\n'

            light_sw, express_sw = 0, 0
            memory_usage, capacity_usage = 0, 0

            for sw in hw.software_components:
                memory_usage += sw.memory_consumption
                capacity_usage += sw.capacity_consumption
                if isinstance(sw, LightSoftware):
                    light_sw += 1
                elif isinstance(sw, ExpressSoftware):
                    express_sw += 1
            
            message += f'Express Software Components: {express_sw}\n'
            message += f'Light Software Components: {light_sw}\n'

            message += f'Memory Usage: {memory_usage} / {hw.memory}\n'
            message += f'Capacity Usage: {capacity_usage} / {hw.capacity}\n'

            message += f'Type: {hw.type}\n'

            if hw.software_components:
                message += f'Software Components: {", ".join([soft_comp.name for soft_comp in hw.software_components])}\n'
            else:
                message += f'Software Components: None'
        
        return message

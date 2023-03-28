# Declare the following classes in the program:
#
# CPU - a class for describing processors;
# Memory - a class for describing memory;
# MotherBoard - a class for describing motherboards.
#
# Provide the ability to create objects of each class with the commands:
#
# cpu = CPU(name, clock speed)
# mem = Memory(name, memory size)
# mb = MotherBoard(name, processor, memory1, memory2, ..., memoryN)
# Note that when creating an object of the MotherBoard class, several objects of the Memory class can be passed, a maximum of N - the number of memory slots on the motherboard (N = 4).
#
# The class objects must have the following local properties:
#
# for the CPU class: name - name; fr - clock speed;
# for the Memory class: name - name; volume - memory size;
# for the MotherBoard class: name - name; cpu - reference to the CPU class object;
# total_mem_slots = 4 - the total number of memory slots (the attribute is assigned this value and does not change);
# mem_slots - a list of Memory class objects
# (maximum total_mem_slots = 4 pieces according to the maximum number of memory slots).
#
# The MotherBoard class must have a get_config(self)
# method to return the current configuration of components on the motherboard as the following list of four lines:
#
# ['Motherboard: <name>',
# 'Central Processor: <name>, <clock speed>',
# 'Memory Slots: <total number of memory slots>',
# 'Memory: <name_1> - <volume_1>; <name_2> - <volume_2>; ...; <name_N> - <volume_N>']
#
# Create an mb object of the MotherBoard class with one CPU (an object of the CPU class)
# and two memory slots (objects of the Memory class).
#
# P.S. No output to the screen is required, only create an object according to the specified requirements.

class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems

    def get_config(self):

        return [f'Motherboard: {self.name}',
                f'Central Processor: {self.cpu.name}, {self.cpu.fr}',
                f'Memory Slots: {self.total_mem_slots}',
                f'Memory: {";".join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))}']


mb = MotherBoard("FRPK", CPU("Intel", 2000), Memory("Kingston", 1000), Memory("Kingston", 2000))

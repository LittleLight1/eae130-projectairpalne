# Preliminary weight estimate example (A350-900)
# Template to adapt for A2

import math

#Constants: Using metric for this script
g = 9.81 
pounds2kg = 1/2.205
nm2m = 1852
min2s = 60
# 1. Mission and payload inputs
num_pilots = 4 #Staff pilot
num_att = 12 #Staff flight attendents
num_pass = 325
pilot_mass = 190*pounds2kg
att_mass = 155*pounds2kg
pass_mass = 195*pounds2kg
carry_mass = 15.72*pounds2kg
checked_mass = 28.81*pounds2kg
crew_weight = (num_pilots*pilot_mass + num_att*att_mass)*g
payload_weight = (num_pass*(pass_mass+carry_mass+checked_mass))

print("Crew weight [kg]:", crew_weight)
print("Payload weight [kg]:", payload_weight)

# 2. Fuel Fractions (Breguet equations)

def cruise_weight_fraction(R_nmi, V_ms, c_1ps, LD_cruise):
    # Convert range to meters
    # Use Breguet range equation to compute W_end/W_start
    # return W_end_over_W_start
    return math.exp(-R_nmi*nm2m*c_1ps/(V_ms*LD_cruise))


def loiter_weight_fraction(E_min, c_1ps, LD_loiter):
    # Convert endurance to seconds
    # Use Breguet endurance equation to compute W_end/W_start
    # return W_end_over_W_start
    return math.exp(-E_min*min2s*c_1ps/LD_loiter)


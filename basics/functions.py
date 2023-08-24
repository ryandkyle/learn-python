def days_to_seconds(number_of_days): 
    calculation_days_to_seconds = 24 * 60 * 60
    print(f"{str(number_of_days)} days is {number_of_days * calculation_days_to_seconds} seconds")

days_to_seconds(1)
days_to_seconds(7)
days_to_seconds(31)
days_to_seconds(365)

days_to_seconds(0)
days_to_seconds(-0)

def loop_calculation():
    i = 0
    for i in range(4):
        days_to_seconds(i)

loop_calculation()

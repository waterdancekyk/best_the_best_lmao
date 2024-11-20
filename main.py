import numpy as np

# Константы
g = 9.81  # Ускорение свободного падения, м/с^2
R = 287.05  # Газовая постоянная для воздуха, Дж/(кг·К)
#каждая функция - каждая формула
def gas_density(temperature, pressure):
    """Расчет плотности газа по уравнению состояния идеального газа."""
    return pressure / (R * temperature)

def flow_rate(rpm, displacement, density):
    """Расчет объемного и массового расхода газа."""
    volume_flow_rate = rpm * displacement / 60  # Приводим к секундам
    mass_flow_rate = volume_flow_rate * density
    return volume_flow_rate, mass_flow_rate

def bernoulli_pressure_increase(density, velocity_in, velocity_out):
    """Изменение давления по теореме Бернулли."""
    return 0.5 * density * (velocity_out**2 - velocity_in**2)

def lift_force(density, velocity, cl, area):
    """Расчет подъемной силы на лопасти."""
    return 0.5 * density * velocity**2 * cl * area
#
def calculate_fan_parameters():
    print("Введите начальные данные:")
    
    try:
        temperature = float(input("Температура воздуха (в Кельвинах): "))
        pressure_in = float(input("Давление на входе (в Па): "))
        velocity_in = float(input("Скорость на входе (в м/с): "))
        velocity_out = float(input("Скорость на выходе (в м/с): "))
        rpm = float(input("Обороты вентилятора (в об/мин): "))
        displacement = float(input("Объем вытеснения за оборот (в м³): "))
        cl = float(input("Коэффициент подъемной силы лопасти: "))
        area_blade = float(input("Площадь лопасти (в м²): "))

        # Расчеты
        density = gas_density(temperature, pressure_in)  # Плотность газа
        volume_flow_rate, mass_flow_rate = flow_rate(rpm, displacement, density)
        pressure_out = pressure_in + bernoulli_pressure_increase(density, velocity_in, velocity_out)
        lift = lift_force(density, velocity_out, cl, area_blade)

        # Вывод результатов
        print("\nРезультаты расчетов:")
        print(f"Плотность газа: {density:.2f} кг/м³")
        print(f"Объемный расход газа: {volume_flow_rate:.2f} м³/с")
        print(f"Массовый расход газа: {mass_flow_rate:.2f} кг/с")
        print(f"Давление на выходе: {pressure_out:.2f} Па")
        print(f"Подъемная сила на лопасти: {lift:.2f} Н")
    except ValueError:
        print("Ошибка ввода! Пожалуйста, вводите только числовые значения.")

#Запуск (defolt)
if __name__ == "__main__":
    while True:
        print("\n=== Расчет параметров вентилятора ===")
        print("1. Ввести данные и рассчитать")
        print("2. Выйти из программы")
        choice = input("Выберите действие (1 или 2): ")
        
        if choice == "1":
            calculate_fan_parameters()
        elif choice == "2":
            print("Спасибо за использование!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

import tkinter as tk
from tkinter import messagebox
import numpy as np

# Константы
g = 9.81  # Ускорение свободного падения, м/с²
R = 287.05  # Газовая постоянная для воздуха, Дж/(кг·К)

# Функции
def gas_density(temperature, pressure):
    """Расчет плотности газа (идеальный газ)."""
    return pressure / (R * (temperature + 273.15))

def flow_rate(rpm, blade_length, density):
    """Расчет объемного и массового расхода газа."""
    displacement = np.pi * (blade_length ** 2) / 4  # Площадь круга (лопасть)
    volume_flow_rate = rpm * displacement / 60  # Приводим к секундам
    mass_flow_rate = volume_flow_rate * density
    return volume_flow_rate, mass_flow_rate

def lift_force_coefficient(velocity, angle):
    """Пример расчета коэффициента подъемной силы в зависимости от угла атаки."""
    return 2 * np.pi * (angle / 360)

def lift_force(density, velocity, cl, area):
    """Расчет подъемной силы на лопасти."""
    return 0.5 * density * velocity ** 2 * cl * area

def bernoulli_pressure_increase(density, velocity_in, velocity_out):
    """Изменение давления по Бернулли."""
    return 0.5 * density * (velocity_out ** 2 - velocity_in ** 2)

# Основная функция для расчетов
def calculate():
    try:
        # Ввод данных
        temperature = float(entry_temperature.get())  # В C
        pressure_in = float(entry_pressure.get()) * 101325  # Атмосферы в Па
        velocity_in = float(entry_velocity_in.get())
        velocity_out = float(entry_velocity_out.get())
        rpm = float(entry_rpm.get())
        blade_length = float(entry_blade_length.get())  # В метрах
        angle = float(entry_angle.get())  # Угол атаки в градусах
        
        # Расчеты
        density = gas_density(temperature, pressure_in)
        volume_flow_rate, mass_flow_rate = flow_rate(rpm, blade_length, density)
        cl = lift_force_coefficient(velocity_out, angle)
        area_blade = np.pi * (blade_length ** 2) / 4  # Площадь лопасти
        lift = lift_force(density, velocity_out, cl, area_blade)
        pressure_out = pressure_in + bernoulli_pressure_increase(density, velocity_in, velocity_out)
        pressure_out_atm = pressure_out / 101325  # Перевод в атмосферы

        # Вывод результатов
        results_text.set(
            f"Результаты расчетов:\n"
            f"Плотность газа: {density:.2f} кг/м³\n"
            f"Объемный расход газа: {volume_flow_rate:.2f} м³/с\n"
            f"Массовый расход газа: {mass_flow_rate:.2f} кг/с\n"
            f"Давление на выходе: {pressure_out_atm:.3f} атм\n"
            f"Коэффициент подъемной силы: {cl:.3f}\n"
            f"Подъемная сила: {lift:.2f} Н"
        )
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числовые значения.")

# Создание графического интерфейса
root = tk.Tk()
root.title("Расчет параметров вентилятора")

# Ввод данных
tk.Label(root, text="Температура (°C):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_temperature = tk.Entry(root)
entry_temperature.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Давление на входе (атм):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_pressure = tk.Entry(root)
entry_pressure.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Скорость на входе (м/с):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_velocity_in = tk.Entry(root)
entry_velocity_in.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Скорость на выходе (м/с):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_velocity_out = tk.Entry(root)
entry_velocity_out.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Обороты (об/мин):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_rpm = tk.Entry(root)
entry_rpm.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Длина лопасти (м):").grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_blade_length = tk.Entry(root)
entry_blade_length.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Угол атаки (°):").grid(row=6, column=0, padx=10, pady=5, sticky="e")
entry_angle = tk.Entry(root)
entry_angle.grid(row=6, column=1, padx=10, pady=5)

# Кнопка расчета
tk.Button(root, text="Рассчитать", command=calculate).grid(row=7, column=0, columnspan=2, pady=10)

# Вывод результатов
results_text = tk.StringVar()
tk.Label(root, textvariable=results_text, justify="left").grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Запуск приложения
root.mainloop()

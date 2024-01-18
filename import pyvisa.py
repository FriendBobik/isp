import pyvisa
rm = pyvisa.ResourceManager('@py')


# Создаем объект ResourceManager
rm = pyvisa.ResourceManager()

# Печатаем список доступных портов
print(rm.list_resources())

# Выбираем ресурс, соответствующий вашему прибору (например, 'GPIB0::11::INSTR')
instrument_resource_string = 'USB0::0x2A8D::0xB318::MY58200051::INSTR'  # замените на ваш адрес прибора
multimeter = rm.open_resource(instrument_resource_string)

# Настройка параметров измерения, например, измерение напряжения
multimeter.write('CONF:VOLT:DC AUTO')

# Запрашиваем измеренное значение
reading = multimeter.query('READ?')

print("Measured Voltage: ", reading)

# Закрываем соединение
multimeter.close()

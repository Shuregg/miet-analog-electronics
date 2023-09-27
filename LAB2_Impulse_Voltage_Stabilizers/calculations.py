#1. Исходные данные:
Uin = 7 #Volt
Uout = 16 #Volt
dUout = 0.02
Rload = 120 #Om
f = 20000 #40'000 - 150'000 Hz
LIR = 0.3
R_L   = 0.2 #Om, Resistance of inductor
print("------------------------------------")
print("   INPUT  DATA    ")

print("Uin       [V]: ", Uin)
print("Uout      [V]: ", Uout)
print("dUout     [%]: ", dUout * 100)
print("Rload    [Om]: ", Rload)
print("Freq    [1/s]: ", f)
print("LIR          : ", LIR)
print("R_ind    [Om]: ", R_L)
print("------------------------------------")
print("   OUTPUT DATA    ")
#Ia = #average current
#dIout = LIR * Ia

#2. Расчет номиналов:
#2.1 Определим коэффициент заполнения импульсов
D = 1 - (Uin / Uout) #t_imp / T
print("D:              ", D)

#2.2 Ток нагрузки:
Iout = Uout / Rload
print("Iout       [A]: ", Iout)

#2.3 Период коммутации
T = 1 / f
print("T         [us]: ", T * 10**6)

#2.4 Определим минимальную индуктивность катушки
Lmin = (Uin**2 * D) / (Iout * Uout * LIR * f)
print("Lmin      [uH]: ", Lmin * 10**6) #Lmin [uH]:  2153.3203125 ~~ 2200 uH = 2.2 mU

#L >= Lmin
# !!!CKECK NEAREST VALUE FOR L IN THE E24 ROW!!!

#2.5 Ближайшее значение из ряда E24 - 2200 мкГн
L = 2.2 * 10**-3 #Henry
print("L         [uH]: ", L * 10**6)

#2.6 Абсолютная величина погрешности выходного напряжения
absdUout = dUout * Uout
print("absdUout   [V]: ", absdUout)

#t_imp - ?; Iin - ?;

#Время импульса (I-го такта)
t_imp = D * T
print("t_impulse [us]: ", t_imp * 10**6)

#Входной ток (катушки)
Iin = Uin / R_L #?????? 35 A too much
print("Iin        [A]: ", Iin)

#2.7 Минимальная ёмкость конденсатора
#Cout_min = (((Iin - Iout) * (T - t_imp)) / (absdUout))
#print("Cout_min  [uF]: ", Cout_min * 10 ** 6)
#Cout = 2400 * 10**-6
#print("Cout      [uF]: ", Cout * 10 ** 6)

print("------------------------------------")
di1 = (Uin * D * T) / (L)
di2 = ((Uin - Uout) * (1-D) * T) / (L)
print("di1        [A]:  ", di1)
print("di2        [A]: ", di2)

if (-(10**-5) <= di1+di2 <= 10**-5):
  print("\ndi1 + di2 = ", di1 + di2)
  print("The law of conservation of energy is observed!\n")

Imax = (LIR / (4 * di1)) + (di1 / 2)
Imin = Imax - di1

print("Imax       [A]:  ", Imax)
print("Imin       [A]:  ", Imin)

Cout_min2 = (((Imin + Imax) / 2) - Iload) * (T - t_imp) / (absdUout)

print("Cout_min  [uF]: ", Cout_min2 * 10 ** 6)
Cout2 = 51 * 10 **-6
print("Cout      [uF]: ", Cout2 * 10 ** 6)

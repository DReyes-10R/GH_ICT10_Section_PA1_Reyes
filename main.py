# Converting Farenheight to Celcius
from pyscript import document



def F_to_C(e):
    f_temp = document.getElementById("input1").value

    f_temp = float(f_temp)

    c_temp = (f_temp - 32) * 5 / 9
    c_temp = round(c_temp, 2)

    if c_temp > 37.8:
        result = f"{float(c_temp)} °C — Fever detected"
    else:
        result = f"{float(c_temp)} °C — Normal temperature"

    document.getElementById("output").innerHTML = result
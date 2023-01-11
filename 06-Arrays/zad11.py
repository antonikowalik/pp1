def month(n):
    months = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    print(months[n-1])

v_months = [1, 2, 11, 12]

for i in range(4):
    month(v_months[i])

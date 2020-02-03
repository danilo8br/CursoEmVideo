times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atletico",
        "botafogo", "atletico-pa", "Bahia", "Sao Paulo", "Fluminense", "Sport-recife", "Ec vitoria", "coritiba", "Avai",
        "Ponte preta", "Atleteico go")
print(f"lista de times do brasileirao: {times}")
print(20*"=")
print(f"Os 5 primeiros são: {times[0:5]}")
print(20*"=")
print(f"Os 4 ultimos são: {times[-4:]}")
print(20*"=")
print(f"Time em ordem alfabetica: {sorted(times)}")
print(20*"=")
print(f"O chapecoense está na {times.index('Chapecoense')+1}° posição")

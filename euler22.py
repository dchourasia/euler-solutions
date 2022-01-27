data = open('p022_names.txt').read().split(',')
data = [x.strip().strip('"') for x in data]

print(data[:5])
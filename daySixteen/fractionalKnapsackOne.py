
def fractKnapSack(values, weights, capacity):
    items = list(zip(values,weights))
    items.sort(key = lambda x: x[0]/x[1], reverse=True)
    total = 0
    for value, weight in items:
        if capacity >= weight:
            total += value 
            capacity -= weight
        else:
            fraction = capacity / weight 
            total += value * fraction 
            break
    return total

if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10,20,30]
    capacity = 50
    print(f'Max: {fractKnapSack(values, weights, capacity)}')
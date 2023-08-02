# data_analyzer.py
def analyze_data(data):
    average = sum(data) / len(data)
    maximum = max(data)
    minimum = min(data)
    return average, maximum, minimum

if __name__ == "__main__":
    with open("processed_data.txt", "r") as file:
        data = list(map(int, file.read().split(',')))
    average, maximum, minimum = analyze_data(data)
    print("Data analysis:")
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
# i have made my first change

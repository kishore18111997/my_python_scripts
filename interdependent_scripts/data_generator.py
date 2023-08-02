# data_generator.py
import random

def generate_data():
    data = [random.randint(1, 100) for _ in range(10)]
    return data

if __name__ == "__main__":
    data = generate_data()
    with open("data.txt", "w") as file:
        file.write(','.join(map(str, data)))
    print("Data generated and stored in data.txt.")

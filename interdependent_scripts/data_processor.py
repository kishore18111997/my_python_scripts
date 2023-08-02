# data_processor.py
def process_data(data):
    processed_data = [num * 2 for num in data]
    return processed_data

if __name__ == "__main__":
    with open("data.txt", "r") as file:
        data = list(map(int, file.read().split(',')))
    processed_data = process_data(data)
    with open("processed_data.txt", "w") as file:
        file.write(','.join(map(str, processed_data)))
    print("Data processed and stored in processed_data.txt.")

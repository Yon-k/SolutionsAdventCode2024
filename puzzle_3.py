import re

def read_data_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

if __name__ == '__main__':
    file_path = r'c:\Users\perezec2\Desktop\De Todo\SolutionsAdventCode2024\data_3.txt'
    data = read_data_file(file_path)

    if data:
        # Find all matches of the pattern mul(x,y) where x and y are integers
        pattern = r'mul\((\d+),(\d+)\)'
        matches = re.findall(pattern, data)

        total_sum = 0
        for match in matches:
            x, y = map(int, match)
            total_sum += x * y

        print("Total sum of all multiplications:", total_sum)
    else:
        print("No data read from file.")
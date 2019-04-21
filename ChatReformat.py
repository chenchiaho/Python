def read_file(filename):
    lines = []
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    date = lines[0]
    del lines[0]
    for line in lines:
        line = line.replace(line[0:5],'')
        line = line.replace(' Kevin ','Kevin: ')
        line = line.replace(' 恩彤 ', '恩彤: ')

        new.append(line)
    new.insert(0,date)
    return new

def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()


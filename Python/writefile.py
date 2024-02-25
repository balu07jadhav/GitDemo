with open('test.txt', 'r') as reader: #reader is object, this sentence included file close
    content = reader.readlines()
    print(content)
    reversed(content)
    with open('test.txt', 'w') as writer: #opened file in write mode
        for line in reversed(content):
            writer.write(line)





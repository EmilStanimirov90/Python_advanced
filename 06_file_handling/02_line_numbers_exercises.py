from string import punctuation
with open("text_v3.txt", 'r') as input_file, open("output_v2.txt", 'w') as output_file:

    for index, line in enumerate(input_file, start=1):
        punctuation_count = 0
        line_len = 0
        for c in line:
            if c.isalpha():
                line_len += 1
            elif c not in punctuation:
                punctuation_count += 1

        # with open("output_v2.txt", 'a') as output_file:
        output_file.write(f'Line {index}: {line[:-1]} ({line_len})({punctuation_count})\n')



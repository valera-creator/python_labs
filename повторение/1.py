input_string = input("строка: ").split(';')
start_string = input("слово: ")

if len(input_string) != 10:
    print('не 10 слов тут')

input_string = list(filter(lambda x: x.startswith(start_string), input_string))  # я захотел в list обернуть
print(*input_string, sep='\n')

# apple;apricot;banana;apartment;application;cherry;apricot;april;apricot;apricot
# ap

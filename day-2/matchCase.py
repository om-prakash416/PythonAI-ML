#match


color = input('enter a color: ')

match  color:
    case 'red':
        print('color is red')
    case 'blue':
        print('color is blue')
    case 'green':
        print('color is green')
    case _:
        print('wrong color')
        
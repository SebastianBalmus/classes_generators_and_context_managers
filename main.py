from time import sleep
import generators
from context_manager import *
from classes import *


if __name__ == '__main__':

    # Testing the first generator
    print('First generator: ', end='')
    for character in generators.first_generator('hello'):
        print(character, end='')

    # Testing the second generator
    print('\nSecond generator: ', end='')
    for character in generators.second_generator('hello'):
        print(character, end='')

    # Testing the third generator
    print('\nThird generator: ', end='')
    for character in generators.third_generator('hello'):
        print(character, end='')

    # Time waster 3000
    timer = int(input('\nHow many seconds do you want to waste? '))

    # Testing the timing context manager
    with StopwatchContextManager() as stopwatch:
        sleep(timer)
    print(f'{stopwatch.time_passed} seconds wasted')

    # Testing the class that uses classmethod and staticmethod decorators
    my_list = ListCreator(['water', 'eggs', 'milk'])
    print(f'List created using the constructor: {my_list.get_list()}')

    my_second_list = ListCreator.from_string('juice bacon bread')
    print(f'List created using the class method: {my_second_list.get_list()}')

    my_third_list = ListCreator.from_two_lists(my_list.get_list(), my_second_list.get_list())
    print(f'The two lists merged together: {my_third_list.get_list()}')

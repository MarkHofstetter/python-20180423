import lotto
from pprint import pprint

number_of_iterations = 10000

def collect_data(func):
    distribution = {}
    for i in range(number_of_iterations):
        numbers = func()
        check_unique = dict((k,1) for k in numbers)
        assert len(check_unique) == 6
        assert min(numbers) > 0
        assert max(numbers) < 46
        for number in numbers:
            if number not in distribution:
                distribution[number] = 1
            else:
                distribution[number] += 1
    
    assert len(distribution) == 45
    min_count = min(distribution.values())
    max_count = max(distribution.values())
    ## pprint(distribution)
    mean = number_of_iterations * 6 / 45 
    print("min count: {}, {:0.3f} max_count: {},{:0.3f}".
      format(min_count, min_count/mean, max_count, max_count/mean))
    assert min_count/mean > 0.92
    assert max_count/mean < 1.08
      
      
def test_man1():
    data = collect_data(lotto.lotto_man)
    
def test_man_bad():
    data = collect_data(lotto.lotto_man_bad)    

def test_random_sample():
    collect_data(lotto.random_sample)

def test_function(test_dict):
    test_dict['a'] = 100


test_dict_ = {'a': 10, 'b': 20}
test_function(test_dict_)
print(test_dict_)
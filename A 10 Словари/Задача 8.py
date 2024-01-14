s = '''orange strawberry barley gooseberry apple apricot barley 
currant orange melon pomegranate banana banana orange barley apricot 
plum grapefruit banana quince strawberry barley grapefruit banana grapes 
melon strawberry apricot currant currant gooseberry raspberry apricot currant 
orange lime quince grapefruit barley banana melon pomegranate barley banana orange 
barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley 
apricot currant orange melon pomegranate banana banana orange apricot barley plum banana 
grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley 
lime grapefruit pomegranate barley'''

result = {}
result_ = {}
numbers = [str(_) for _ in s.split()]

for word in numbers:
    result[word] = result.get(word, 0) + 1

mx = max(result.values())

for key, value in result.items():
    if value == mx:
        result_[key] = result_.get(key, value)
print(min(result_))

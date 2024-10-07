
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls() 
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

info1 = string_info("KAMNELOM")
print(info1)

info2 = string_info("Musik creator")
print(info2)

result1 = is_contains("urban", ["Urban", "city", "town"])
print(result1)

result2 = is_contains("Python", ["Java", "C++", "Python"])
print(result2)

print(f"Общее количество вызовов функций: {calls}")


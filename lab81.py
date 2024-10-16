def analyze_string(string):
  words = string.split()
  word_count = len(words)
  longest_word = max(words, key=len)
  return word_count, longest_word

string = input("Введіть рядок: ")
count, longest = analyze_string(string)
print("Кількість слів:", count)
print("Найдовше слово:", longest)

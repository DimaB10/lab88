def process_strings(lines):
  result = []
  for line in lines:
    if len(line) % 2 == 0:
      mid = len(line) // 2
      new_line = line[:mid-1] + line[mid-1:mid+1].upper() + line[mid+1:]
      result.append(new_line)
    else:
      print(f"Рядок '{line}' має непарну довжину і буде пропущено.")
  return result

if __name__ == "__main__":
  num_lines = int(input("Введіть кількість рядків: "))
  lines = []
  for i in range(num_lines):
    line = input(f"Введіть рядок {i+1}: ")
    lines.append(line)
  processed_lines = process_strings(lines)
  print("\nОброблені рядки:")
  for line in processed_lines:
    print(line)
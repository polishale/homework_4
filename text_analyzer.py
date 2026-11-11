from collections import Counter
import os
import re


def read_text_file(file_path: str) -> str:
  if not os.path.exists(file_path):
    raise FileNotFoundError(f"Файл за шляхом '{file_path}' не знайдено.")

  with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

  if not content.strip():
    raise ValueError("Файл порожній або містить лише пробіли.")

  return content


def analyze_text(text: str) -> dict:
  if not text or not text.strip():
    return {"total_words": 0, "frequency_dict": {}}
  words = re.findall(r"[a-zA-Zа-яА-ЯіІїЇєЄґҐ']+", text.lower())

  total_words = len(words)
  frequency_dict = dict(Counter(words))

  return {"total_words": total_words, "frequency_dict": frequency_dict}


if __name__ == "__main__":
  file_name = "sample_text.txt"

  try:
    print(f"Зчитування файлу: {file_name}...")
    raw_text = read_text_file(file_name)
    results = analyze_text(raw_text)

    print("\n Результати аналізу ")
    print(f"Загальна кількість слів: {results['total_words']}\n")
    print("Топ-15 найчастіших слів:")
    sorted_words = sorted(
        results["frequency_dict"].items(), key=lambda item: item[1], reverse=True
    )
    for word, count in sorted_words[:15]:
      print(f"  • {word}: {count}")

  except (FileNotFoundError, ValueError) as error:
    print(f"\n[Помилка обробки файлу]: {error}")
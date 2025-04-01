# Analiza Wydatków 📊

## Opis Projektu
Ten projekt to skrypt w Pythonie, który:
- Wczytuje dane z pliku CSV,
- Przetwarza i konwertuje daty,
- Generuje wykres przedstawiający wydatki miesięczne według kategorii,
- Sumuje wydatki wg kategorii i zapisuje podsumowanie do osobnego pliku CSV.

## Funkcjonalności
- **Wczytywanie danych:** wczytanie pliku `wydatki.csv` z odpowiednią obsługą wyjątków.
- **Konwersja dat:** Przetwarzanie dat i tworzenie nowej kolumny "Miesiac" dla łatwiejszej analizy.
- **Wizualizacja:** Generowanie wykresu słupkowego z użyciem bibliotek matplotlib i seaborn.
- **Podsumowanie:** Grupowanie wydatków według kategorii i eksport wyników do CSV.

## Instalacja
1. **Wymagania:**
   - Python 3.x
   - Biblioteki: `pandas`, `matplotlib`, `seaborn`, `argparse`, `logging`

2. **Instalacja bibliotek:**
   ```bash
   pip install pandas matplotlib seaborn

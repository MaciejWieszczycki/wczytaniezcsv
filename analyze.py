import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import argparse

def main():
    """
    Analiza wydatków – wczytuje dane, generuje wykres wydatków miesięcznych wg kategorii
    oraz eksportuje podsumowanie wydatków. 
    """
    # Ustawienie logowania
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    # Parser argumentów
    parser = argparse.ArgumentParser(description="Analiza wydatków")
    parser.add_argument("--input", type=str, default="wydatki.csv", help="Ścieżka do pliku CSV z danymi")
    parser.add_argument("--output_plot", type=str, default="wydatki_miesieczne_kategorie.png", help="Plik zapisu wykresu")
    parser.add_argument("--output_summary", type=str, default="podsumowanie_kategorii.csv", help="Plik zapisu podsumowania")
    args = parser.parse_args()
    
    # Wczytanie danych
    try:
        wydatki = pd.read_csv(args.input)
        logging.info("Dane wczytane pomyślnie.")
    except Exception as e:
        logging.error(f"Błąd podczas wczytywania danych: {e}")
        return
    
    # Konwersja daty i dodanie kolumny 'Miesiac'
    wydatki["Data"] = pd.to_datetime(wydatki["Data"], errors='coerce')
    wydatki.dropna(subset=["Data"], inplace=True)
    wydatki["Miesiac"] = wydatki["Data"].dt.to_period("M").astype(str)
    
    # Ustawienia stylu dla wykresów
    sns.set_style("whitegrid")
    sns.set_palette("pastel")
    
    # Tworzenie wykresu
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(data=wydatki, x="Miesiac", y="Kwota", hue="Kategoria", errorbar=None)
    ax.set_title("Wydatki miesięczne wg kategorii", fontsize=14)
    ax.set_xlabel("Miesiąc")
    ax.set_ylabel("Kwota [PLN]")
    plt.xticks(rotation=45)
    plt.legend(title="Kategoria")
    plt.tight_layout()
    
    # Zapis wykresu
    plt.savefig(args.output_plot)
    logging.info(f"Wykres zapisany jako {args.output_plot}")
    plt.show()
    
    # Sumowanie wydatków wg kategorii
    suma_kategorie = wydatki.groupby("Kategoria")["Kwota"].sum().sort_values(ascending=False)
    print("\nSUMA WYDATKÓW WG KATEGORII:")
    print(suma_kategorie)
    
    # Eksport podsumowania
    suma_kategorie.to_csv(args.output_summary)
    logging.info(f"Podsumowanie zapisane jako {args.output_summary}")

if __name__ == "__main__":
    main()

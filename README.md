# muj_projekt_6 – Automatizované testy e-shopu kancelar24.cz

## Popis projektu
Projekt obsahuje automatizované UI testy e-shopu kancelar24.cz pomocí nástrojů Playwright a pytest.

Testy ověřují základní funkčnost e-shopu z pohledu uživatele. Testy jsou rozděleny do více souborů pro lepší přehlednost a znovupoužitelnost kódu.

---

## Použité technologie
- Python
- Playwright
- Pytest

---

## Testované scénáře

### 1. Přidání produktu do košíku
- otevření detailu produktu
- přidání produktu do košíku
- ověření, že se produkt nachází v košíku

### 2. Odebrání produktu z košíku
- přidání produktu do košíku
- ověření, že je v košíku 1 produkt
- odstranění produktu
- ověření, že je košík prázdný

### 3. Filtrace produktů podle barvy
- použití filtru „černá“
- ověření změny URL
- ověření, že všechny zobrazené produkty odpovídají filtru

---

## Struktura projektu
```text
tests/
├── test_pridat_do_kosiku.py
├── test_odebrat_z_kosiku.py
├── test_filtr_barvy.py
├── conftest.py
├── helpers.py
```
- `helpers.py` – pomocné funkce (odmítnutí cookies, přidání produktu do košíku a přechod do košíku)
- `conftest.py` – sdílené fixture (vyčištění košíku)

---

## Spuštění projektu

### 1. Instalace závislostí
```bash
pip install pytest playwright pytest-playwright
```

### 2. Instalace prohlížeče
```bash
python3 -m playwright install chromium
```

### 3. Spuštění testů
```bash
python3 -m pytest tests -v
```

## Autor

Klára Chvalinová  

Projekt byl vytvořen jako studijní projekt akademie Tester s Pythonem.

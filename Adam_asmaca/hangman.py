import random
import os


KELIMELER = [
    "araba", "bilgisayar", "masa", "okul", "defter",
    "telefon", "pencere", "kitap", "yazilim", "oyun"
]


ADAM_CIZIMLERI = [
    [
        "     +---+",
        "     |   |",
        "         |",
        "         |",
        "         |",
        "         |",
        "    ========="
    ],
    [
        "     +---+",
        "     |   |",
        "     O   |",
        "         |",
        "         |",
        "         |",
        "    ========="
    ],
    [
        "     +---+",
        "     |   |",
        "     O   |",
        "     |   |",
        "         |",
        "         |",
        "    ========="
    ],
    [
        "     +---+",
        "     |   |",
        "     O   |",
        "    /|   |",
        "         |",
        "         |",
        "    ========="
    ],
    [
        "     +---+",
        "     |   |",
        "     O   |",
        "    /|\\  |",
        "         |",
        "         |",
        "    ========="
    ],
    [
        "     +---+",
        "     |   |",
        "     O   |",
        "    /|\\  |",
        "    /    |",
        "         |",
        "    ========="
    ],
    [
        "     +---+",
        "     |   |",
        "     O   |",
        "    /|\\  |",
        "    / \\  |",
        "         |",
        "    ========="
    ]
]


def ekran_temizle():
    os.system("cls" if os.name == "nt" else "clear")


def oyun_ekrani(yanlis_sayi, dogru_harfler, gizli_kelime):
    ekran_temizle()
    adam = ADAM_CIZIMLERI[yanlis_sayi]

    
    kelime_gosterim = ""
    for harf in gizli_kelime:
        if harf in dogru_harfler:
            kelime_gosterim += harf + " "
        else:
            kelime_gosterim += "_ "

 
    print("+" + "-"*35 + "+")
    print("|        ADAM ASMACA         |")
    print("|                             |")
    print(f"|   Kelime: {kelime_gosterim:<20}|")
    print(f"|   Yanlış Tahmin: {yanlis_sayi}/6       |")
    print("|                             |")
    for satir in adam:
        print(f"| {satir:<33}|")
    print("+" + "-"*35 + "+")


def adam_asmaca_oyunu():
    gizli_kelime = random.choice(KELIMELER)
    yanlis_sayi = 0
    dogru_harfler = []

    while yanlis_sayi < 6:
        oyun_ekrani(yanlis_sayi, dogru_harfler, gizli_kelime)
        tahmin = input("Harf tahmini yap: ").lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("❗ Lütfen tek bir harf gir.")
            input("Devam için Enter...")
            continue

        if tahmin in dogru_harfler:
            print("❗ Bu harfi zaten bildin.")
            input("Devam için Enter...")
            continue

        if tahmin in gizli_kelime:
            dogru_harfler.append(tahmin)
        else:
            yanlis_sayi += 1

        if all(harf in dogru_harfler for harf in gizli_kelime):
            oyun_ekrani(yanlis_sayi, dogru_harfler, gizli_kelime)
            print("🎉 Tebrikler! Kelimeyi buldun!")
            print("Kelime:", gizli_kelime)
            return

    ekran_temizle()
    
    oyun_ekrani(6, dogru_harfler, gizli_kelime)
    print("❌ Kaybettin!")
    print("Kelime:", gizli_kelime)


def oyun_baslat():
    while True:
        adam_asmaca_oyunu()
        secim = input("\nTekrar oynamak ister misin? (e/h): ").lower()

        if secim == "e":
            continue
        elif secim == "h":
            print("👋 Oyun kapatılıyor. Görüşmek üzere!")
            break
        else:
            print("❗ Geçersiz seçim. Oyun kapatılıyor.")
            break


if __name__ == "__main__":
    oyun_baslat()

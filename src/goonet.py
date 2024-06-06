from src.website import Website

class Goonet(Website):
    code = "goonet"
    name = "www.goo-net.com"
    url = "https://www.goo-net.com/cgi-bin/fsearch/goo_used_search.cgi?category=USDN"
    is_post = True
    sort_name = "sort"
    sort_value = "updated_sort:NUMD"

    makers = {
        "Toyota": "トヨタ",
        "Nissan": "日産",
        "Honda": "ホンダ",
        "Suzuki": "スズキ",
        "Daihatsu": "ダイハツ",
        "Subaru": "スバル",
        "Mitsubishi": "三菱",
        "Mazda": "マツダ",
        "Isuzu": "いすゞ",
        "Lexus": "レクサス",
        "Mitsuoka": "ミツオカ",
        "Hino": "日野",
        "Mini": "MINI",
        "Mercedes-Benz": "メルセデス・ベンツ",
        "Volkswagen": "フォルクスワーゲン",
        "BMW": "BMW",
        "Chevrolet": "シボレー",
        "Volvo": "ボルボ",
        "Audi": "アウディ",
        "Porsche": "ポルシェ",
        "Jeep": "ジープ",
        "Jaguar": "ジャガー",
        "Peugeot": "プジョー",
        "Alfa Romeo": "アルファロメオ"
    }

    body_types = {
        "Coupe": "クーペ",
        "SUV/Pickup": "SUV・ピックアップ",
        "Convertible": "オープンカー",
        "Sedan": "セダン",
        "Wagon": "ワゴン",
        "Truck": "トラック・バス"
    }


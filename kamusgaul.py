meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "AGGRO": "untuk menjadi agresif/marah",
            "ROFL": "tanggapan terhadap lelucon",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "SHEESH": "sedikit ketidaksetujuan",
            }
          
while True:
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
        break
    else:
        print('INVALID WORD')

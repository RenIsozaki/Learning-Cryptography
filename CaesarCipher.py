# シーザー暗号解読　　Unicode A〜Z = 65〜90、　a〜z = 97〜122

def character_trans(cha, i):
   moji = cha + i            # リスト内のj番目の文字をi個ずらす(A -2個ずらす-> C)
   list_1.append(chr(moji))  # ずらした文字を追加
   return 0

x = input("文字列を入力してください：")
list_0 = list(x) # 入力された文字列をlistに格納
list_1 = list()  # 空のlistの宣言

for i in range(26):                   # 25通りを表示 * 1(暗号文) + 25(その他) = 26(アルファベットの数)
    for j in range( len(list_0) ):    # 入力された文字列の数だけ複合処理を繰り返す
        cha = ord(list_0[j])
        if(65 <= cha and cha <= 90):
            if(cha + i > 90):
                d = cha - 90
                cha = 64 + d
                character_trans(cha, i)

            else:
                character_trans(cha, i)
                
        if(97 <= cha and cha <= 122):
            if(cha + i > 122):
                d = cha - 122
                cha = 96 + d
                character_trans(cha, i)
                
            else:
                character_trans(cha, i)
                
    print("No.",i + 1, "".join(list_1))
    list_1 = list()                 #リストの初期化
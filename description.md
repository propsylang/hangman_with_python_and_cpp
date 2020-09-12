# pythonでハングマンを作ろう

## <span style="color: lightgreen; ">ハングマンとは</span>

ハングマンは、相手の考えた単語を当てる2人用のゲームである。(wikipedia)  
詳しいルールは以下参照

## <span style="color: lightgreen; ">今回作るハングマンのルール</span>
1. 出題者（プログラム側）は出題する単語を選び、その単語の文字数を表す下線を引く。絞首台を描く。 
2. 解答者は、単語に入っていると思われるアルファベットを一つ答える。  
3. 出題者はアルファベットが回答の単語に含まれているか判定する。  
- アルファベットが単語に含まれているならば、下線の上のその文字が入る場所すべてにその文字を書く。  
- アルファベットが単語に含まれていないならば、絞首台につるされる人の絵を描き加える。  
4. 勝敗が決まるまで2.3.を繰り返す。以下のときに勝敗は決まる。  
- 解答者が単語を正解する。-解答者の勝利  
- 絞首台の人の絵が完成する。-出題者の勝利  
  
## <span style="color: lightgreen; ">プログラムにやらせたいこと</span>
- 単語を無作為に選ぶ
- プレイヤーの入力を受け取り、それが
    - 文字であれば正解の単語に含まれているか判定
        - 含まれていれば下線をその文字に変更し、残りの予想可能回数を１減らす
        - 含まれていなければただ残りの予想可能回数を１減らす
    - 単語であれば合っているか判定
        - 合っていればゲーム終了(プレイヤーの勝利)
        - 間違っていればゲーム続行、残りの予想可能回数を１減らす

- 予想可能回数が無くなれば出題者の勝利

<span style="color: lightblue; ">**以上を疑似コード（日本語とpython）で書いてみると以下のようになる**</span>

 ```Python
単語を決める

while クリアされてなくて試行回数が１以上:
    絞首台、文字盤を表示
    入力を受ける
    試行回数を１減らす
    if 入力が一文字:
        if 当たり:
            print("hit!")
            文字盤を更新
        else:
            print("miss!")
            
    elif:
        if 入力した単語がが正解:
            print("right word!")
            クリア
        else:
            print("wrong word!")

    else:
        print("invalid input")
        試行回数を１戻す
 ```

## <span style="color: lightgreen; ">実装の前準備</span>
```Python
def display_hangman():
    pass

def display_wordlist():
    pass

def choose_word():
    pass

def play():
    pass

def main():
    play()

if __name__ == "__main__":
    main()
```

## <span style="color: lightgreen; ">実装①～入力を受け、正解かどうか判定～</span>  
ユーザーの入力を受け付け、文字数の判定と正誤判定を行うコードを書いてみよう

変数  
 - **cleared**: クリアしたかどうか（真偽値)
 - **tries**: 試行回数（整数値）  
 - **word_ans**: 正解の単語（文字列）
 - **inp**: 入力（文字列）


 ```Python
def play():
    cleared = False
    tries = 6
    word_ans = choose_word()
    while not cleared and tries > 0:
        inp = input("Type in letter or word:")
        tries -= 1
        if len(inp) == 1:
            if inp in word_ans:
                print("hit!")
            else:
                print("miss!")

        elif len(inp) == len(word_ans):
            if inp == word_ans:
                print("right word!")
                cleared = True
            else:
                print("wrong word!")
        else:
            print("invalid input")
            tries += 1
 ```

 ## <span style="color: lightgreen; ">実装②～文字盤と絞首台の表示と更新～</span>  
既にに当てた文字は表示し、それ以外は  
今回は今までに当てた文字のリストと正解の単語を引数にとり、文字盤の文字列を返す関数を作ってみよう  

変数  
 - **wordline**: 文字盤（文字列) 
 - **letters_guessed**: 今までに当てた文字のリスト（文字列リスト）
 - **hangmanpics**: 絞首台の各段階の絵のリスト（文字列リスト）


 ```Python
def disp_wordlist(letters_guessed,word_ans):
    wordlist = ""
    for c in word_ans:#正解の単語の各文字について
        if c in letters_guessed:#すでに当てていたら
            wordlist += (c + " ")#文字を表示
        else:#まだ当てていなかったら
            wordlist += "_ "#下線を表示
    return wordlist
 ```



 


```Python
cleared = False
tries = 6
word_ans = "default"
wordline = "_" * len(word_ans)
letters_guessed = []
while not cleared and tries > 0:
    inp = input("Type in letter or word:")
    tries -= 1
    if len(inp) == 1:
        if inp in word_ans:
            print("hit!")
            letters_guessed.append(inp)#当てた文字をリストに追加
        else:
            print("miss!")
            
    elif len(inp) == len(word_ans):
        if inp == word_ans:
            print("right word!")
            cleared = True
        else:
            print("wrong word!")
    else:
        print("invalid input")
```

<details>
<summary>折りたたみ部分のタイトル</summary>
<pre>
<code>
折りたたまれる詳細情報部分
折りたたまれる詳細情報部分
折りたたまれる詳細情報部分
</code>
</pre>
</details>
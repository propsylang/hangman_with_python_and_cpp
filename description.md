# pythonでハングマンを作ろう

## <span style="color: lightgreen; ">ハングマンとは</span>

ハングマンは、相手の考えた単語を当てる2人用のゲームである。(wikipedia)  
詳しいルールは下記参照

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

- 絞首台、文字盤を表示、更新

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
実際のゲームを作る前準備として、関数を用意しておこう  
関数  
- **display_hangman**: 絞首台を表示
- **display_wordlist**: 文字盤を表示
- **choose_word**: 単語を無作為に選ぶ
- **play**: 実際にゲームを進行する
- **main**: play関数を実行する

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
※passと書かれている関数は、なにも実行しない。実際の処理を書くまでは関数だけ用意しておき、passと書いておく。  
※最後の`if __name__ == "__main__":`はこのファイルが.pyとして実行されているかを判定するものだが、気にしなくて良い（今回に関しては書かなくても良い）。詳しいことが知りたければ[参照](https://note.nkmk.me/python-if-name-main/)  
※関数を使わない、すべての処理を同じ関数に書き込む等でも同じ動きをするプログラムを書けるが、後々機能を追加しやすいように処理ごとに関数を分けて書く方が望ましい。

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
    word_ans = "default"
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
def display_wordlist(letters_guessed, word_ans):
    wordlist = ""
    for c in word_ans:
        if c in letters_guessed:
            wordlist += (c + " ")
        else:
            wordlist += "_ "
    print(wordlist)
 ```
<details>
<summary>display_hangman</summary>
<pre>
<code>

 ```Python
def display_hangman(tries):
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
    print(HANGMANPICS[6-tries],end="    ")
 ```
</code>
</pre>
</details>
  
    


```Python
def play():
    cleared = False
    tries = 6
    word_ans = "default"
    letters_guessed = []
    while not cleared and tries > 0:
        display_hangman(tries) #絞首台を表示
        display_wordlist(letters_guessed,word_ans) #文字盤を表示
        inp = input("Type in letter or word:")
        tries -= 1
        if len(inp) == 1:
            if inp in word_ans:
                print("hit!")
                letters_guessed.append(inp) #当てた文字をリストに追加
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
## <span style="color: lightgreen; ">実装③～単語を無作為に選ぶ～</span>
random.choice()関数を使って単語を無作為に選んで返す関数を作ってみよう  

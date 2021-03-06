def main():
    # 接收輸入資料，並轉成整數型別
    n = int(input())
    # 用 "int()" 創造一個空整數，再加上變數n，其實就等同於複製n的值
    # 不寫 m = n 是要避免發生指標衝突問題，很有可能這兩個變數是同一個實體
    # 意思就是，這樣 m = n 的寫法恐怕會讓 m 和 n 同時改變，就不是單純複製值了
    m = int() + n
    # 星星的中央必定有個交叉點，以此點為界，分成上下對稱的兩個部分
    # 建立兩個空串列
    top, end = list(), list()
    # range(a,b,c): 產生一個迭代序列，其值為
    # 從 a 開始數，包含 a ，每次增加 c ，直到 b 的前一個結果(無論 c>0 或是 c<0，序列都不會數到 b)
    for i in range(m, 1, -2):
        '''
            算法：
            假設你輸入5那結果應該是要長這樣(假設底線是空白，逗號是暫時加上的)
            *,_,_,_,*  --> 包含空格的寬度是5
            _,*,_,*,_  --> 包含空格的寬度是5
            _,_,*,_,_  --> 單獨的一行
            _,*,_,*,_  --> 包含空格的寬度是5
            *,_,_,_,*  --> 包含空格的寬度是5
            從以上結果可以得到以下結論：
            無論那一列有幾個星星或是星星在哪裡，寬度都一樣
            上下對稱
            中心點只有一個
            這裏range(m, 1, -2)的1就是要讓迴圈不會數到中間那一點，因為這裡是單獨印中間那個點
        '''
        # pos 是 這一列的 由左而右的 第一個 星星 在 串列中 的 位置～
        # 這是數學問題～先留給你想，拿出紙筆畫畫看就知道
        pos = int((n - i) / 2)
        # 建立一個暫時的串列來當作「現在正在填的這一列」，由於長度大家都一樣，所以，
        # 就直接預設它全部都是空白鍵，之後在對的位置再用星星替換掉空白鍵，這一列就完成了
        tmp = [" "] * (pos + i)
        # 由於pos是這一列由左而右的第一個星星在串列中的位置，所以這個動作就是把原本的空白鍵取代成星星
        tmp[pos] = "*"
        # 第二個星星的位置，會在第一個星星後面加上「中間的距離」後的那個點
        # 這是數學問題～留給你想哦！用手比比看就發現規律ㄌ
        tmp[pos + i - 1] = "*"
        # 這個時候，「現在正在填的這一列」已經填好了，就把它同時放到上下對稱的兩個串列裡面
        # 串列裡面可以有串列的，叫做「二維串列」
        # 串列.append(東西) 會把新的東西加在這個串列的最尾端
        top.append(tmp)
        # 串列.insert(位置，東西) 會把新的東西插在這個位置的後面
        end.insert(0, tmp)
    for x in top:
        # 現在就是依序地把「上部」印出，但是要把中括號和逗號去掉，所以使用"".join()
        print(''.join(x))
    if n > 0:
        # 如果他一開始輸入 0 那就不需要中間那點
        print(" " * int(n / 2) + "*")
    for y in end:
        print(''.join(y))


if __name__ == '__main__':
    # python 正規寫法
    # 如果這個檔案不是被當作模組引入，就執行 main 函式
    main()

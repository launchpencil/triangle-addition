# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('Streamlitのサンプルアプリ')
b = []

user_input = st.text_input('1段目を入力してください')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('計算する'):
    if user_input:  # 名前が入力されているかチェック
        a = list(map(int, input().split()))
        a
        for i in range(len(a)-1):
            b.append(a[i] + a[i+1])
        a = b
        b.clear()
        for i in range(len(a)-1):
            st.text(a[i])
    else:
        st.error('データを入力してください。')  # エラーメッセージを表示
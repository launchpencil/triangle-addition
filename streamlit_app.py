import streamlit as st

st.title("三角足し算リゾルバー")

b_input = st.text_input("整数のリストをスペース区切りで入力してください")
kekka = ""

# リスト入力を処理
if b_input:
    try:
        kekka += b_input + '\n'
        b = list(map(int, b_input.split()))
        # 演算処理
        st.write("計算結果:")
        for i in range(len(b)-1):
            c = []
            result = []
            for j in range(len(b)-1):
                sum_value = b[j] + b[j+1]
                c.append(sum_value)
                result.append(sum_value)
            kekka += ' '.join(map(str, result)) + '\n'
            b = c
        st.code(kekka, language="python")
    except ValueError:
        st.error("無効な入力です。整数リストを正しく入力してください。")

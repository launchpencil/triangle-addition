import streamlit as st

b_input = st.text_input("整数のリストをスペース区切りで入力してください")

# リスト入力を処理
if b_input:
    try:
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
            st.write(' '.join(map(str, result)))  # 結果を表示
            b = c  # 次のループのために b を更新
            if len(b) == 1:  # 計算が一つの要素に収束したら終了
                break
    except ValueError:
        st.error("無効な入力です。整数リストを正しく入力してください。")

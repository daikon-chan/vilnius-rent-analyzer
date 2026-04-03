import pandas as pd
import streamlit as st

st.title("Vilnius Rent Analyzer")

st.write("## このアプリについて")
st.caption("""
このアプリは、VILNIUS TECH周辺の賃貸物件を比較しやすくするためのものです。
家賃・距離・地区・部屋タイプ・家具の有無で絞り込みできます。
おすすめスコアは、家賃と大学までの距離をもとに簡易的に計算しています。
""")

# --------------------
# データ読み込みと整形
# --------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/housing_real.csv")

    # is_furnished を軽く整えてから表示用の日本語に変換
    df["is_furnished"] = df["is_furnished"].replace({
        "True": True,
        "False": False,
        "true": True,
        "false": False
    })

    df["furnished_label"] = df["is_furnished"].map({
        True: "家具あり",
        False: "家具なし"
    }).fillna("不明")

    df["room_type_label"] = df["room_type"].map({
        "studio": "ワンルーム",
        "1_room": "1LDK"
    }).fillna("不明")

    return df

# データ読み込み
df = load_data()

# 基本情報の表示
st.write("### 基本情報")

col1, col2 = st.columns(2)
with col1:
    st.metric("件数", len(df))
with col2:
    st.metric("平均家賃", f"{df['monthly_rent_eur'].mean():.1f} EUR")


# --------------------
# サイドバーの条件設定
# --------------------

st.sidebar.header("絞り込み条件")

# 家賃フィルター
max_price = st.sidebar.slider("最大家賃を選んでください", 200, 800, 450)

# 距離フィルター
max_distance = st.sidebar.slider("大学までの最大距離（km）を選んでください", 0.0, 10.0, 5.0, 0.5)

# district フィルター
districts = ["すべて"] + sorted(df["district"].unique().tolist())
selected_district = st.sidebar.selectbox("地区を選んでください", districts)

# room_type フィルター
room_types = ["すべて"] + sorted(df["room_type_label"].unique().tolist())
selected_room_type = st.sidebar.selectbox("部屋のタイプを選んでください", room_types)

# furnished フィルター
furnished_options = ["すべて", "家具あり", "家具なし"]
selected_furnished = st.sidebar.selectbox("家具の有無を選んでください", furnished_options)

# 並び替えオプション
sort_option = st.sidebar.selectbox(
    "並び順を選んでください",
    ["家賃が安い順", "家賃が高い順", "距離が近い順", "広い順"]
)

# サイドバーの説明
st.sidebar.caption("条件を選ぶと、結果・グラフ・表が自動で更新されます。")

# --------------------
# 絞り込み処理
# --------------------

# 家賃と距離でフィルタリング
filtered_df = df[df["monthly_rent_eur"] <= max_price]
filtered_df = filtered_df[filtered_df["distance_to_vilnius_tech_km"] <= max_distance]

# 地域、部屋タイプ、家具の有無でフィルタリング
if selected_district != "すべて":
    filtered_df = filtered_df[filtered_df["district"] == selected_district]

if selected_room_type != "すべて":
    filtered_df = filtered_df[filtered_df["room_type_label"] == selected_room_type]

if selected_furnished != "すべて":
    filtered_df = filtered_df[filtered_df["furnished_label"] == selected_furnished]

# 並び替え
if sort_option == "家賃が安い順":
    filtered_df = filtered_df.sort_values("monthly_rent_eur", ascending=True)
elif sort_option == "家賃が高い順":
    filtered_df = filtered_df.sort_values("monthly_rent_eur", ascending=False)
elif sort_option == "距離が近い順":
    filtered_df = filtered_df.sort_values("distance_to_vilnius_tech_km", ascending=True)
elif sort_option == "広い順":
    filtered_df = filtered_df.sort_values("size_sqm", ascending=False)


# --------------------
# 結果表示
# --------------------

# 絞り込み後の統計情報とグラフ表示
if len(filtered_df) > 0:

    # 絞り込み後の統計情報の表示
    min_price = filtered_df["monthly_rent_eur"].min()
    max_price_result = filtered_df["monthly_rent_eur"].max()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("絞り込み後件数", len(filtered_df))
    with col2:
        st.metric("絞り込み後の平均家賃", f"{filtered_df['monthly_rent_eur'].mean():.1f} EUR")
    with col3:
        st.metric("最安家賃", f"{min_price:.1f} EUR")
    with col4:
        st.metric("最高家賃", f"{max_price_result:.1f} EUR")

    # 絞り込み後のエリア別平均家賃の棒グラフ表示
    st.write("### 絞り込み後のエリア別平均家賃")
    avg_rent_by_district = (
    filtered_df.groupby("district", as_index=False)["monthly_rent_eur"]
    .mean()
    .sort_values("monthly_rent_eur", ascending=False)
    )

    st.bar_chart(
    avg_rent_by_district,
    x="district",
    y="monthly_rent_eur",
    sort=False,
    )

    # 距離と家賃の関係の散布図表示
    st.write("### 距離と家賃の関係（散布図）")

    st.scatter_chart(
        filtered_df,
        x="distance_to_vilnius_tech_km",
        y="monthly_rent_eur"
    )

    # おすすめ物件のスコアリングと表示
    df_scored = filtered_df.copy()

    df_scored["score"] = (
        df_scored["monthly_rent_eur"] +
        df_scored["distance_to_vilnius_tech_km"] * 50
    )

    top3 = df_scored.nsmallest(3, "score")

    st.write("### おすすめ物件 TOP3")
    st.dataframe(
        top3[["title", "district", "monthly_rent_eur", "distance_to_vilnius_tech_km"]],
        hide_index=True
    )

    st.caption("※ おすすめスコア = 家賃 + （距離 × 50）。小さいほどおすすめです。")

    # 絞り込み結果のデータフレームでの表示
    st.write("### 絞り込み結果")
    display_columns = [
        "title",
        "district",
        "monthly_rent_eur",
        "distance_to_vilnius_tech_km",
        "room_type_label",
        "size_sqm",
        "furnished_label",
        "deposit_eur",
        "source_name",
        "updated_at",
    ]

    display_df = filtered_df[display_columns].rename(columns={
        "title": "物件名",
        "district": "地区",
        "monthly_rent_eur": "家賃(EUR)",
        "distance_to_vilnius_tech_km": "大学までの距離(km)",
        "room_type_label": "部屋タイプ",
        "size_sqm": "広さ(㎡)",
        "furnished_label": "家具",
        "deposit_eur": "デポジット(EUR)",
        "source_name": "掲載元",
        "updated_at": "更新日",
    })

    st.dataframe(display_df, hide_index=True)

    st.write("### 物件リンク一覧")

    for _, row in filtered_df.iterrows():
        st.markdown(
            f"- [{row['title']}]({row['listing_url']}) "
            f" ({row['district']} / {row['monthly_rent_eur']} EUR) "
        )

    # 絞り込み後結果のCSVダウンロードボタン
    csv_data = display_df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label="絞り込み結果をCSVでダウンロード",
        data=csv_data,
        file_name="filtered_housing_results.csv",
        mime="text/csv",
    )

else:
    st.write("条件に合う物件がありません。家賃や距離の条件を緩めてみてください。")

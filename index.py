import streamlit as st


def run():
    st.title("Heart Stroke Prediction Using Machine Learning")
    st.markdown(
        '<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">',
        unsafe_allow_html=True)

    gen_display = ('Female', 'Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])


    age = st.text_input('Age')

    ht_display = ('No', 'Yes')
    ht = st.selectbox("Hypertension", ht_display)

    hd_display = ('No', 'Yes')
    hd = st.selectbox("Heart Disease", hd_display)

    mar_display = ('No', 'Yes')
    mar = st.selectbox("Marital Status", mar_display)

    wt_display = ('Private', 'Self-employed', 'Government Job', 'Children')
    wt = st.selectbox("Work Type", wt_display)

    rt_display = ('Urban', 'Rural')
    rt = st.selectbox("Education", rt_display)

    avg_gl = st.text_input('Average Glucose Level')

    bmi = st.text_input('BMI')

    ss_display = ('Formerly smoked', 'Never smoked', 'Smokes', 'Unknown')
    ss = st.selectbox("Employment Status", ss_display)

    submit_button = st.button('Submit')


run()

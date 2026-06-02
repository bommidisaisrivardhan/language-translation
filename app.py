import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

st.set_page_config(
    page_title="AI Language Translator",
    layout="wide"
)

st.title("🌍 AI Language Translation App")

languages={

"Arabic":"ar",
"Bengali":"bn",
"Chinese":"zh-CN",
"Dutch":"nl",
"English":"en",
"French":"fr",
"German":"de",
"Greek":"el",
"Gujarati":"gu",
"Hindi":"hi",
"Italian":"it",
"Japanese":"ja",
"Kannada":"kn",
"Korean":"ko",
"Malayalam":"ml",
"Marathi":"mr",
"Portuguese":"pt",
"Punjabi":"pa",
"Russian":"ru",
"Spanish":"es",
"Swedish":"sv",
"Tamil":"ta",
"Telugu":"te",
"Thai":"th",
"Turkish":"tr",
"Urdu":"ur",
"Vietnamese":"vi"

}

text=st.text_area(
    "Enter Text",
    height=180
)

st.write(
    "Character Count:",
    len(text)
)

col1,col2=st.columns(2)

with col1:

    source_lang=st.selectbox(
        "Translate From",
        sorted(languages.keys()),
        index=4
    )

with col2:

    target_lang=st.selectbox(
        "Translate To",
        sorted(languages.keys()),
        index=9
    )

if "history" not in st.session_state:

    st.session_state.history=[]

if st.button("Translate"):

    if text.strip()=="":

        st.warning(
            "Please Enter Text"
        )

    elif source_lang==target_lang:

        st.warning(
            "Choose Different Languages"
        )

    else:

        translated=GoogleTranslator(

            source=languages[source_lang],

            target=languages[target_lang]

        ).translate(text)

        st.success(
            "Translation Completed"
        )

        st.subheader(
            "Translated Text"
        )

        st.write(translated)

        st.session_state.history.append(
            {
                "source":source_lang,
                "target":target_lang,
                "input":text,
                "output":translated
            }
        )

        tts=gTTS(
            translated
        )

        tts.save(
            "audio.mp3"
        )

        st.audio(
            "audio.mp3"
        )

        st.download_button(
            label="Download Translation",
            data=translated,
            file_name="translation.txt"
        )

st.divider()

st.subheader(
    "Translation History"
)

if len(
    st.session_state.history
)==0:

    st.write(
        "No translations yet"
    )

else:

    for item in reversed(
        st.session_state.history
    ):

        st.write(
            f"**{item['source']} → {item['target']}**"
        )

        st.write(
            item["input"]
        )

        st.write(
            item["output"]
        )

        st.divider()

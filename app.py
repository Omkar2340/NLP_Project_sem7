import streamlit as st
import language_tool_python

# Initialize LanguageTool
tool = language_tool_python.LanguageTool('en-US')

# Autocorrect function using LanguageTool
def autocorrect_language_tool(sentence):
    matches = tool.check(sentence)
    corrected_sentence = language_tool_python.utils.correct(sentence, matches)
    return corrected_sentence

# Function to highlight misspelled words
def highlight_misspelled(text):
    matches = tool.check(text)
    highlighted_text = text
    
    for match in matches:
        # Highlight each incorrect word
        start = match.offset
        end = match.offset + match.errorLength
        highlighted_text = (
            highlighted_text[:start] +
            f'<mark style="background-color: red; color: white; padding: 0 2px;">{highlighted_text[start:end]}</mark>' +
            highlighted_text[end:]
        )
    
    return highlighted_text

# Streamlit UI
st.set_page_config(page_title="Text Correction App", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .header {
            font-size: 2em;
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }
        .subheader {
            font-size: 1.5em;
            color: #555;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .text-area {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .highlight {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">Interactive Text Correction with Streamlit</div>', unsafe_allow_html=True)

# Input text area with an empty default value
input_text = st.text_area("Enter your text:", value="", height=300, key="text_input", help="Type or paste your text here.", placeholder="Start typing...")

if input_text:
    # Display highlighted text
    highlighted_text = highlight_misspelled(input_text)
    st.markdown('<div class="subheader">Highlighted Text:</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="highlight">{highlighted_text}</div>', unsafe_allow_html=True)

    # Perform autocorrection
    corrected_sentence = autocorrect_language_tool(input_text)

    # Display corrected sentence
    st.markdown('<div class="subheader">Corrected Sentence:</div>', unsafe_allow_html=True)
    st.write(corrected_sentence)

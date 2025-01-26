import google 
import streamlit as st
st.title("**Text Style Analyzer** 🔍")
st.markdown("**Welcome!** This app analyzes the writing style of your text.")

with st.spinner("Ready to analyze your text..."):
  user_text = st.text_area("**Enter your text here:**",
                            placeholder="Paste your text here...",
                            height=200)

import google.generativeai as genai
genai.configure(api_key="AIzaSyCQcAZpBJi2ox3FZB1zXHGvYhDH8VGepL0")
model = genai.GenerativeModel(model_name="gemini-pro")




def generate_style_analysis(text):

  prompt=f"""
  You are assigned to analyze the writing style of the following text:
  text: {text}
  Specifically, consider the following aspects:
    Vocabulary and Diction:
      What is the overall tone and register of the language (formal, informal, technical, colloquial)?
      Are there any recurring words, phrases, or vocabulary choices?
      Does the writer use jargon, slang, or idioms? If so, how effectively?
      Is the vocabulary precise, descriptive, and varied?
    Sentence Structure and Syntax:
      What is the average sentence length? Are the sentences generally short, long, or a mix of both?
      Does the writer primarily use simple, compound, or complex sentences?
      How effectively does the writer use active and passive voice?
      Are there any recurring sentence patterns or stylistic devices (e.g., parallelism, repetition)?

    Figurative Language:
      Does the writer use metaphors, similes, analogies, or other figures of speech?
      If so, are these figures of speech effective and meaningful?
      Does the writer use any other literary devices, such as imagery, personification, or alliteration?
    Tone and Mood:
      What is the overall tone and mood of the text (e.g., humorous, serious, sarcastic, optimistic)?
      How does the writer convey their emotions, attitudes, and perspectives through language?
      Are there any shifts in tone or mood throughout the text?
    Organization and Structure:
      How are the ideas presented and organized within the text?
      Does the text follow a clear and logical structure (e.g., chronological, cause-and-effect, problem-solution)?
      Are there any effective transitions between ideas?
    Punctuation and Grammar:
      How effectively does the writer use punctuation (commas, semicolons, periods, etc.)?
      Are there any consistent grammatical errors or stylistic quirks?
      Does the punctuation and grammar contribute to the overall clarity and readability of the text?

    Based on your analysis, describe the writer's overall style. Is it unique and distinctive? How does the writer's style contribute to the overall message and impact of the text with help of pictorial representations such as graphs,charts etc...?






  """
  response = model.generate_content(prompt)
  return response.text









if st.button("Analyze Style 🚀"):
  if user_text:
    with st.spinner("Analyzing..."):
      style_analysis = generate_style_analysis(user_text)
      st.success("**Here's the style analysis:**")
      st.write(style_analysis)
  else:
    st.warning("**Please enter some text to analyze.**")

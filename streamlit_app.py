import streamlit as st
import textstat

def flesch_score_grade_note(ans):
    # calculate the flesch reading ease score
    score = textstat.flesch_reading_ease(ans)
    # print(f"Flesch Reading Ease Score : {score}")
    
    if score >= 90:
        grade = "5th grade"
        note = "Very easy to read. Easily understood by an average 11-year-old student."
    elif score >= 80:
        grade = "6th grade"
        note = "Easy to read. Conversational English for consumers."
    elif score >= 70:
        grade = "7th grade"
        note = "Fairly easy to read."
    elif score >= 60:
        grade = "8th & 9th grade"
        note = "Plain English. Easily understood by 13- to 15-year-old students."
    elif score >= 50:
        grade = "10th to 12th grade"
        note = "Fairly difficult to read"
    elif score >= 30:
        grade = "College"
        note = "Difficult to read."
    else:
        grade = "Professional"
        note = "Extremely difficult to read. Best understood by university graduates."
    
    # print(f"Ans-{count}")
    # print(f"Grade = {grade}")
    # print(f"Notes = {note}\n\n")
    return (score, grade, note)


st.set_page_config(page_title="Flesch Readability Score", page_icon="📖")
st.title("📖 Flesch Readability Score Checker")
st.write("Enter your text below to check its Flesch Reading Ease score and readability grade.")

ans = st.text_area("Paste your answer here:", height=200, placeholder="Ctrl + Enter")

if ans and ans.strip():
    flesch_score, flesch_grade, flesch_note = flesch_score_grade_note(ans)
    st.success(f"**Flesch Score:** {flesch_score:.2f}")
    st.info(f"**Grade Level:** {flesch_grade}")
    st.write(f"**Note:** {flesch_note}")
else:
    st.warning("Please enter some text to analyze.")
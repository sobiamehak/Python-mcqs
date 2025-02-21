
# import streamlit as st
# import json

# st.title("💡Python Multiple Choice Questions")


# # Questions Load Karna
# def load_questions():
#     with open('data/questions.json', 'r') as file:
#         questions = json.load(file)
#     return questions

# # Score Initialization
# if 'score' not in st.session_state:
#     st.session_state.score = 0

# if 'answers' not in st.session_state:
#     st.session_state.answers = {}

# # Questions Display Karna
# questions = load_questions()

# # Display the questions and collect answers
# for question in questions:
#     st.subheader(question['question'])
#     options = question['options']
    
#     # Unique key for radio button
#     user_answer = st.radio("Select your answer:", options, key=question['question'] + "_radio")

#     # Store user answers in session state
#     st.session_state.answers[question['question']] = user_answer

# # Submit Button (Only appears at the end)
# if st.button("Submit"):
#     # Reset score to 0
#     st.session_state.score = 0

#     # Loop through the questions and check answers
#     for question in questions:
#         user_answer = st.session_state.answers[question['question']]
#         correct_answer = question['answer']
        
#         # Display feedback for each question
#         if user_answer == correct_answer:
#             st.success(f"Question: {question['question']} - Correct Answer!")
#             st.session_state.score += 1
#         else:
#             st.error(f"Question: {question['question']} - Wrong Answer! The correct answer was: {correct_answer}")
    
#     # Show the total score at the end
#     st.write(f"Your total score: {st.session_state.score}")

import streamlit as st
import json

st.title("💡Python Multiple Choice Questions")

# Questions Load Karna
def load_questions():
    with open('data/questions.json', 'r') as file:
        questions = json.load(file)
    return questions

# Score Initialization
if 'score' not in st.session_state:
    st.session_state.score = 0

if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Questions Display Karna
questions = load_questions()

# Display the questions and collect answers
for question in questions:
    st.subheader(question['question'])
    options = question['options']
    
    # Unique key for radio button and no default selection
    user_answer = st.radio("Select your answer:", options, key=question['question'] + "_radio", index=None)

    # Store user answers in session state
    st.session_state.answers[question['question']] = user_answer

# Submit Button (Only appears at the end)
if st.button("Submit"):
    # Reset score to 0
    st.session_state.score = 0

    # Loop through the questions and check answers
    for question in questions:
        user_answer = st.session_state.answers[question['question']]
        correct_answer = question['answer']
        
        # Display feedback for each question
        if user_answer == correct_answer:
            st.success(f"Question: {question['question']} - Correct Answer!")
            st.session_state.score += 1
        else:
            st.error(f"Question: {question['question']} - Wrong Answer! The correct answer was: {correct_answer}")
    
    # Show the total score at the end
    st.write(f"Your total score: {st.session_state.score}")

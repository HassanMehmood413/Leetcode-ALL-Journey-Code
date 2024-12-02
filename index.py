# # # user = int(input('Enter the First number : ' ))
# # # user2 = int(input('Enter the Second Number : ' ))
# # # operator = input('Enter the operation : ')
# # # if operator == '+':
# # #     res = user + user2
# # # elif operator == '-':
# # #     res = user + user2
# # # elif operator == '/':
# # #     res = round(user/user2)
# # # elif operator == '*':
# # #     res = user*user2
# # # elif operator == "power":
# # #     res = user**user2
# # # elif operator == 'modules':
# # #     res = user%user2
# # # else:
# # #     print('Enter the operator given above')
    
# # # print(res)
# # # s = '-42'
# # # s = s.strip()
# # # print(s)

# # translations = {
# #        "hello": "hola",
# #         "dog": "perro",
# #         "cat": "gato",
# #         "well": "bien",
# #         "us": "nos",
# #         "nothing": "nada",
# #         "house": "casa",
# #         "time": "tiempo"
# #     }
# # word = 'hello'
# # print(translations[word])
# import streamlit as st
# import google.generativeai as genai

# # Configure the API key
# GOOGLE_API_KEY = "AIzaSyDma9KsEXzewUDnLTErjwVIyR3qwcRVlD8"
# genai.configure(api_key=GOOGLE_API_KEY)

# # Initialize the Generative Model
# # model = genai.GenerativeModel('gemini-pro')
# model = genai.GenerativeModel('gemini-1.5-flash')
# # Function to get response from the model
# def get_chatbot_response(user_input):
#     response = model.generate_content(user_input)
#     return response.text

# # Streamlit interface
# st.set_page_config(page_title="Simple ChatBot", layout="centered")

# st.title("✨ Simple ChatBot ✨")
# st.write("Powered by Google Generative AI")

# if "history" not in st.session_state:
#     st.session_state["history"] = []

# # Display chat history
# for user_message, bot_message in st.session_state.history:
#     st.markdown(f"""
#     <div style="
#         background-color: #d1d3e0; 
#         border-radius: 15px; 
#         padding: 10px 15px; 
#         margin: 5px 0; 
#         max-width: 70%; 
#         text-align: left; 
#         display: inline-block;
#     ">
#         <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown(f"""
#     <div style="
#         background-color: #e1ffc7; 
#         border-radius: 15px; 
#         padding: 10px 15px; 
#         margin: 5px 0; 
#         max-width: 70%; 
#         text-align: left; 
#         display: inline-block;
#     ">
#         <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
#     </div>
#     """, unsafe_allow_html=True)
    
# # user_input = input("Enter your Prompt = ")
# # output = get_chatbot_response(user_input)

# # print(output)

# with st.form(key="chat_form", clear_on_submit=True):
#     user_input = st.text_input("", max_chars=2000)
#     submit_button = st.form_submit_button("Send")

#     if submit_button:
#         if user_input:
#             response = get_chatbot_response(user_input)
#             st.session_state.history.append((user_input, response))
#         else:
#             st.warning("Please Enter A Prompt")



# adj = {{ 1, 2, 3 }, { }, { 4 }, { }, { }}
# console.log(adj[0])
# nums = [1,2,3,3,4]
# array = {}
# for i in range(len(nums)):
#     if nums[i] not in array:
#         array[i] = array.get(nums[i],0)+1
#     else:
#         array[i] = array.set(nums[i],array.get(nums[i],0)+1)
# print(array)



# print('hey I am a \'good girl\' \n and good boy ')

# print("Hey", 6, 7, sep="~", end="009')\n")


# print("hassan","haniya",'Mama',sep='%#^%^%$',end='3422')

# list = [4,5,6,7,8,9]
# print(list[2])



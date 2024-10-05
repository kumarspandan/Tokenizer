import streamlit as st #python library to build web apps

def extract_substrings(text, case_sensitive=False):
    substrings=set()
    #susbstrings={}
    words = text.split()
    for word in words:
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                if not case_sensitive:
                    substring = word[i:j].lower()  # Lowercase for case-insensitive
                else:
                    substring = word[i:j]
                substrings.add(substring)
   
    return sorted(substrings, key=len)  # Sort substrings by length

def tokenize(text):
    d = {}  # Dict to map chars to IDs
    for i in text: #for characters in text entered
        if i not in d:
            id = len(d)  # Use current dict length as ID
            d[i] = id # first element will be assigned 0, second will be assigned 1 and so on
    t_list = []
    num_list = []
    for i in text:
        token = i + ":" + str(d[i])  # Concatenate strings for tokens bca i and : both are strings
        t_list.append(token) #0:h, 1:e and so on
        num_list.append(d[i]) #0,1,2.. and so on
    return t_list, num_list


def tokenizeAgain(text):
    n = len(text)
    d = {}  # Dictionary to store tokens
    token_list = []  # List to store tokens
    count = 0  # Counter for assigning IDs
    for i in range(0, n, 2):  # Iterate over the text
        sub = text[i:i + 2]  # Extract 2-character substring
        if len(sub)==1:  # If only one character is left
            sub += "_"  # Adding an underscore
        if sub not in d:  # Check if substring already exists in dictionary
            d[sub] = count  # Assign a unique ID to the substring
            token_list.append(sub + ":" + str(count))  # Append token to the list
            count += 1
        else:
            token_list.append(sub + ":" + str(d[sub]))  # Append token to the list
    
    # Initialize an empty list
    num_list = []
    for item in token_list: # Iterate through each item in token_list
        key = item.split(":")[0] # Split the item by ":" and get the first part
        num_list.append(d[key])# Get the corresponding value from the dictionary d and append it to num_list
    return token_list, num_list
    

def main():
    st.title("Corpus Tokenizer & Substring Generator App")
    st.markdown("<style>.css-1d6feon {font-size: 18px;} .css-18e3thv {font-size: 18px;}</style>", unsafe_allow_html=True)  # Increase font size

    # Create a container with a scrollbar for better layout
    container = st.container()
    with container:
        input_text = st.text_area("Enter text:", height=200)
        case_sensitive = st.checkbox("Case-sensitive extraction")

        st.subheader("Make Substrings")
        go_button = st.button("Get Substrings")

        if go_button:
            if not input_text:
                st.error("Please enter some text:")
                return

            with st.spinner("Getting substrings..."):
                substrings = extract_substrings(input_text, case_sensitive)
                st.success("Extraction done!")

            st.write(", ".join(substrings))
            st.write(f"Total no. of substrings: {len(substrings)}")

        st.subheader("Tokenize (using Single Character)")
        tokenize_button = st.button("Get Tokens")

        if tokenize_button:
            token_list, num_list = tokenize(input_text)

            # Success message for token generation
            st.success("Tokens generated!")

            st.write(" ".join(token_list))  # Print tokens horizontally
            st.subheader("Your Tokenized Sentence is:")  # Print statement for tokenized sentence
            st.write(", ".join(map(str, num_list)))  # Print numerical list
        
        st.subheader("Tokenize (using Double Character)")
        tokenize_again_button = st.button("Get 2-Character Tokens")

        if tokenize_again_button:
            token_list, num_list = tokenizeAgain(input_text)

            # Success message for token generation
            st.success("Tokens generated!")

            st.write(" ".join(token_list))  # Print tokens horizontally
            st.subheader("Your 2-Character Tokenized Sentence is:")  # Print statement for tokenized sentence
            st.write(", ".join(map(str, num_list)))  # Print numerical list

if __name__ == "__main__":
    main()

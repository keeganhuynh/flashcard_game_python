import streamlit as st
import random

# Vocabulary flashcards split into blocks of 10 words each
flashcards = [
    {"english": "reserve", "vietnamese": "dự trữ"},
    {"english": "facility", "vietnamese": "cơ sở vật chất"},
    {"english": "promote", "vietnamese": "thăng chức"},
    {"english": "manufacture", "vietnamese": "sản xuất"},
    {"english": "exhibit", "vietnamese": "trưng bày"},
    {"english": "memo", "vietnamese": "thông báo nội bộ"},
    {"english": "enclose", "vietnamese": "đính kèm"},
    {"english": "refund", "vietnamese": "hoàn tiền"},
    {"english": "renovate", "vietnamese": "cải tạo"},
    {"english": "warranty", "vietnamese": "bảo hành"},
    {"english": "consulting", "vietnamese": "tư vấn"},
    {"english": "further", "vietnamese": "thêm nữa"},
    {"english": "insurance", "vietnamese": "bảo hiểm"},
    {"english": "potential", "vietnamese": "tiềm năng"},
    {"english": "concern", "vietnamese": "mối quan ngại"},
    {"english": "contribute", "vietnamese": "đóng góp"},
    {"english": "depart", "vietnamese": "khởi hành"},
    {"english": "subscription", "vietnamese": "sự đăng ký"},
    {"english": "supervisor", "vietnamese": "giám sát viên"},
    {"english": "chief", "vietnamese": "trưởng"},
    {"english": "maintenance", "vietnamese": "bảo trì"},
    {"english": "receipt", "vietnamese": "hóa đơn"},
    {"english": "personnel", "vietnamese": "nhân sự"},
    {"english": "expenses", "vietnamese": "chi phí"},
    {"english": "temporary", "vietnamese": "tạm thời"},
    {"english": "guarantee", "vietnamese": "bảo đảm"},
    {"english": "committee", "vietnamese": "ủy ban"},
    {"english": "regulation", "vietnamese": "quy định"},
    {"english": "complimentary", "vietnamese": "miễn phí"},
    {"english": "recruit", "vietnamese": "tuyển dụng"},
    {"english": "inspection", "vietnamese": "kiểm tra"},
    {"english": "defective", "vietnamese": "có lỗi"},
    {"english": "eligible", "vietnamese": "đủ điều kiện"},
    {"english": "council", "vietnamese": "hội đồng"},
    {"english": "inquire", "vietnamese": "hỏi"},
    {"english": "invoice", "vietnamese": "hóa đơn"},
    {"english": "procedure", "vietnamese": "thủ tục"},
    {"english": "entrance", "vietnamese": "lối vào"},
    {"english": "itinerary", "vietnamese": "hành trình"},
    {"english": "innovative", "vietnamese": "sáng tạo"},
    {"english": "inquiry", "vietnamese": "sự điều tra"},
    {"english": "merchandise", "vietnamese": "hàng hóa"},
    {"english": "extensive", "vietnamese": "rộng rãi"},
    {"english": "beverage", "vietnamese": "đồ uống"},
    {"english": "brief", "vietnamese": "ngắn gọn"},
    {"english": "exclusive", "vietnamese": "độc quyền"},
    {"english": "alternative", "vietnamese": "sự thay thế"},
    {"english": "real estate", "vietnamese": "bất động sản"},
    {"english": "mayor", "vietnamese": "thị trưởng"},
    {"english": "concerning", "vietnamese": "về việc"},
    {"english": "affordable", "vietnamese": "phải chăng"},
    {"english": "reputation", "vietnamese": "danh tiếng"},
    {"english": "negotiate", "vietnamese": "đàm phán"},
    {"english": "shuttle", "vietnamese": "xe đưa đón"},
    {"english": "postpone", "vietnamese": "hoãn lại"},
    {"english": "assess", "vietnamese": "đánh giá"},
    {"english": "promptly", "vietnamese": "ngay lập tức"},
    {"english": "exceed", "vietnamese": "vượt quá"},
    {"english": "priority", "vietnamese": "ưu tiên"},
    {"english": "assemble", "vietnamese": "lắp ráp"},
    {"english": "recipient", "vietnamese": "người nhận"},
    {"english": "acquire", "vietnamese": "thu được"},
    {"english": "willing", "vietnamese": "sẵn sàng"},
    {"english": "comprehensive", "vietnamese": "toàn diện"},
    {"english": "dessert", "vietnamese": "món tráng miệng"},
    {"english": "luggage", "vietnamese": "hành lý"},
    {"english": "hardly", "vietnamese": "hầu như không"},
    {"english": "broad", "vietnamese": "rộng"}
]

# Split flashcards into blocks of 10 words each
blocks = [flashcards[i:i + 10] for i in range(0, len(flashcards), 10)]

# Initialize session state
if 'current_block' not in st.session_state:
    st.session_state.current_block = 0
if 'current_flashcard' not in st.session_state:
    st.session_state.current_flashcard = None
if 'seen_flashcards' not in st.session_state:
    st.session_state.seen_flashcards = set()

st.title('Flashcard Game')

# Select a block
block_options = [f"Block {i + 1}" for i in range(len(blocks))]
selected_block = st.selectbox("Choose a block", block_options)

# Update the current block
block_index = block_options.index(selected_block)
st.session_state.current_block = block_index

# Display the flashcard

def next_flashcard():
    available_flashcards = [
        fc for fc in blocks[st.session_state.current_block] 
        if fc['english'] not in st.session_state.seen_flashcards
    ]
    if not available_flashcards:
        st.session_state.seen_flashcards = set()
        available_flashcards = blocks[st.session_state.current_block]
    
    st.session_state.current_flashcard = random.choice(available_flashcards)
    st.session_state.seen_flashcards.add(st.session_state.current_flashcard['english'])

def en():
    if st.session_state.current_flashcard:
        return st.session_state.current_flashcard['english']
    return ""

def vn():
    if st.session_state.current_flashcard:
        return st.session_state.current_flashcard['vietnamese']
    return ""

st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("**English**")
    st.text("")

with col2:
    st.markdown("**Vietnamese**")
    st.text("")

with col3:
    if st.button('Results'): 
        text1, text2 = en(), vn()
        with col1:
            st.markdown(f'<span style="color:white; font-size:30px">{text1}</span>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<span style="color:yellow">{text2}</span>', unsafe_allow_html=True)
    if st.button('newword'): 
        next_flashcard()
        text1, text2 = en(), ''
        with col1:
            st.markdown(f'<span style="color:white; font-size:30px">{text1}</span>', unsafe_allow_html=True)
        with col2:
            st.text(text2)
st.markdown("---")
st.markdown("### Recent results")
col1, col2, col3, col4 = st.columns(4) 
for index, element in enumerate(st.session_state.seen_flashcards):
    if index % 4 == 0:
        with col1:
            st.write(element)
    elif index % 4 == 1:
        with col2:
            st.write(element)
    elif index % 4 == 2:
        with col3:
            st.write(element)
    else:
        with col4:
            st.write(element)
    

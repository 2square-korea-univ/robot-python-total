import streamlit as st
import os
from pathlib import Path

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def get_markdown_files(directory):
    # 지정된 디렉토리에서 모든 .md 파일 찾기
    markdown_files = []
    file_paths = {}  # 표시 이름과 실제 파일 경로를 매핑
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                # 전체 경로 저장
                full_path = os.path.join(root, file)
                # 상대 경로 계산
                rel_path = os.path.relpath(full_path, directory)
                # .md 확장자를 제거한 이름 저장
                display_name = os.path.splitext(rel_path)[0]
                markdown_files.append(display_name)
                file_paths[display_name] = rel_path
    return sorted(markdown_files), file_paths

def main():
    st.title("마크다운 파일 뷰어")
    
    # 마크다운 파일이 있는 디렉토리 경로 설정
    markdown_dir = "markdown_files"  # 여기에 실제 마크다운 파일이 있는 폴더 경로를 지정하세요
    
    # 디렉토리가 없으면 생성
    os.makedirs(markdown_dir, exist_ok=True)
    
    # 파일 업로더 추가 (선택사항)
    # uploaded_files = st.file_uploader("새 마크다운 파일 업로드", 
    #                                 type="md",
    #                                 accept_multiple_files=True)
    
    # if uploaded_files:
    #     for uploaded_file in uploaded_files:
    #         # 업로드된 파일 저장
    #         file_path = os.path.join(markdown_dir, uploaded_file.name)
    #         with open(file_path, "wb") as f:
    #             f.write(uploaded_file.getbuffer())
    #         st.success(f"파일 업로드 완료: {uploaded_file.name}")
    
    # 마크다운 파일 목록 가져오기
    markdown_files, file_paths = get_markdown_files(markdown_dir)
    
    if markdown_files:
        # 드롭다운으로 파일 선택 (.md 확장자 없이 표시)
        selected_display = st.selectbox(
            "보고 싶은 문서를 선택하세요",
            markdown_files
        )
        
        if selected_display:
            # 실제 파일 경로 가져오기
            file_path = os.path.join(markdown_dir, file_paths[selected_display])
            # 마크다운 내용 읽기
            markdown_content = read_markdown_file(file_path)
            
            # 파일 이름 표시 (.md 확장자 없이)
            st.subheader(f"📄 {selected_display}")
            
            # 마크다운 내용 표시
            st.markdown(markdown_content)
    else:
        st.info("마크다운 파일이 없습니다. 파일을 업로드하거나 지정된 폴더에 .md 파일을 추가해주세요.")

if __name__ == "__main__":
    main() 